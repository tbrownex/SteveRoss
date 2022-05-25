import json
import os

from config import getBaseURL
from getCampaign import getCampaign
from createCampaign import createCampaign
from updateCampaign import updateCampaign
from getGeoFences import getGeoFences
from utils import postRequest
from postAd import postAd
from createAddressableTargets import createAddressableTargets
from getDeviceTypes import getDeviceTypes
from updateDeviceTypes import updateDeviceTypes
from addAddressableTargetToCampaign import addAddressableTargetToCampaign

ADDRESSIDS = [678604, 678605, 678606, 678607, 678608, 678609, 678610, 678611, 678612]

def copyCampaign(orgID, campaignID, orgName, numCopies):
    assert numCopies == len(ADDRESSIDS), "number of copies does not match number of Address IDs"
    # Get a campaign to copy, then create a campaign, then update it with values from the copied
    # First get the campaign to copy
    master = getCampaign(orgID, campaignID)
    master = master['campaigns'][0]
    name = master['name']
    payload = formatPayload(master)
    # Now create new campaigns
    newIDs = createCampaigns(orgID, payload, numCopies, name)
    # Update the Device Types
    addDeviceTypes(campaignID, newIDs)
    # Update the GeoFences
    addGeoFences(orgID, campaignID, newIDs)
    # Add the Ads (JPEG or PNGs)
    processAds(orgID, newIDs, orgName)
    print("Associating Addressable Targets")
    for x, campaignID in enumerate(newIDs):
        addressID = ADDRESSIDS[x]
        addAddressableTargetToCampaign(orgID, campaignID, addressID)
    return
    
def formatPayload(campaign):
    # These attributes have different names when updating than when "getting"
    campaign['oba_provider'] = campaign['oba_provider']['id']
    campaign['campaign_type_id'] = campaign['campaign_type']['id']
    campaign['bid_type_id'] = campaign['bid_type']['id']
        
    keys = ['resource', 'id', 'oba_provider', 'campaign_type', 'bid_type',
            'current_win_rate', 'status', 'viewability', 'resources', 'actions']
    for key in keys:
        campaign.pop(key)
        d = {}
        d['campaign'] = campaign
    return d

def createCampaigns(orgID, payload, numCopies, name):
    # Each campaign created is just a stub
    print("Creating Campaigns")
    characters = 2 if numCopies < 100 else 3
    newIDs = []
    for n in range(2, numCopies+2):
        payload['campaign']['name'] = name + ' ' + str(n).zfill(characters)
        newID = createCampaign(orgID)
        payloadString = json.dumps(payload)
        resp = updateCampaign(orgID, newID, payloadString)
        newIDs.append(newID)
        print("-- {}".format(newID))
    return newIDs

def addDeviceTypes(campaignID, newIDs):
    # Get the Device Types from the master campaign
    print("Updating Device Types")
    deviceTypes = getDeviceTypes(campaignID)
    for newID in newIDs:
        print("-- {}".format(newID))
        updateDeviceTypes(newID, deviceTypes)

def addGeoFences(orgID, campaignID, newIDs):
    # Get the GeoFence data from the master campaign
    print("Updating GeoFences")
    payload = formatGeoPayload(orgID, campaignID)
    base = getBaseURL()
    for newID in newIDs:
        print("-- {}".format(newID))
        url = base+'organizations/'+str(orgID)+'/campaigns/'+str(newID)+'/geo_fences'
        postRequest(url, payload)

def formatGeoPayload(orgID, campaignID):
    # Get the GeoFence data from the master, then create the payload for all the copies
    resp = getGeoFences(orgID, campaignID, None, False) 
    l = []
    payload = resp['geo_fences']
    for n in payload:
        n.pop('id')
        n.pop('campaign_id')
        l.append(n)
    payload = {}
    payload['geo_fences'] = l
    return json.dumps(payload)

def processAds(orgID, newIDs, orgName):
    path = '/home/tbrownex/repos/SteveRoss/'+orgName+'/images'
    files = os.listdir(path)
    for key in newIDs:
        for file in files:
            adDetails = {
                'name': file.split('.')[0],
                'path': path,
                'fileName': file
            }
            resp = postAd(orgID, key, adDetails)