import json
import os
import random
import datetime
import logging

from getCampaign import getCampaign
from createCampaign import createCampaign
from updateCampaign import updateCampaign
from getDeviceTypes import getDeviceTypes
from updateDeviceTypes import updateDeviceTypes
from getGeoFences import getGeoFences
from postAd import postAd
from config import getBaseURL
from utils import postRequest
from activateCampaign import activateCampaign
from addAddressableTargetToCampaign import addAddressableTargetToCampaign

ADDRESSIDS = [727840, 727841, 727842, 728054, 728055, 728056, 728057, 728058, 728059]

logLoc = "/home/tbrownex/"
logFile = "LoadTest.log"
logDefault = "info"
logLevel = getattr(logging, logDefault.upper(), None)
logging.basicConfig(filename=logLoc+logFile,\
                        level=logLevel,\
                        format='%(levelname)s:%(message)s')
    
logger = logging.getLogger('tcpserver')

def copyCampaign(orgID, masterIDs, numCopies):
    d = {}     # This is for tracking purposes in case of error
    #assert numCopies == len(ADDRESSIDS), "number of copies does not match number of Address IDs"
    # Get a campaign to copy, then create a campaign, then update it with values from the copied
    # First get the campaign to copy
    master = getCampaign(orgID, campaignID)
    master = master['campaigns'][0]
    name = 'LoadTest'
    payload = formatPayload(master)
    # Now create new campaigns for new Org (LoadTest)
    orgID = 386279
    #newIDs = createCampaigns(orgID, payload, numCopies, name)
    #addDeviceTypes(campaignID, newIDs)
    #addGeoFences(orgID, campaignID, newIDs)
    #logger.warning('Posting Ads starting: '+ str(datetime.datetime.now()))
    #processAds(orgID, newIDs)
    #logger.warning('Dayparting starting: '+ str(datetime.datetime.now()))
    #processDayParting(orgID, newIDs)
    #logger.warning('Addresses starting: '+ str(datetime.datetime.now()))
    #processAddresses(orgID, newIDs)
    logger.warning('Activation starting: '+ str(datetime.datetime.now()))
    activate(orgID, newIDs)
    logger.warning('Activation ended: '+ str(datetime.datetime.now()))
    return newIDs
    
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
    characters = 4
    newIDs = []
    for n in range(1, numCopies+1):
        payload['campaign']['name'] = name + ' ' + str(n).zfill(characters)
        newID = createCampaign(orgID)
        payloadString = json.dumps(payload)
        resp = updateCampaign(orgID, newID, payloadString)
        newIDs.append(newID)
    return newIDs

def addDeviceTypes(campaignID, newIDs):
    # Get the Device Types from the master campaign
    print("Updating Device Types")
    deviceTypes = getDeviceTypes(campaignID)
    for newID in newIDs:
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

def processDayParting(orgID, newIDs):
    print("Day-parting")
    payload = {
      'campaign': {"week_dayparting": [
        [7,8,9,10,11,12,13,14,15,16,17,18,19,20],
        [7,8,9,10,11,12,13,14,15,16,17,18,19,20],
        [7,8,9,10,11,12,13,14,15,16,17,18,19,20],
        [7,8,9,10,11,12,13,14,15,16,17,18,19,20],
        [7,8,9,10,11,12,13,14,15,16,17,18,19,20],
        [7,8,9,10,11,12,13,14,15,16,17,18,19,20],
        [7,8,9,10,11,12,13,14,15,16,17,18,19,20]
      ]}
    }
    payload = json.dumps(payload)
    count=0
    for key in newIDs:
        resp = updateCampaign(orgID, key, payload)
        count +=1
        if count % 500 == 0:
            logger.warning(str(key) + ' -- ' + str(datetime.datetime.now()))

def processAds(orgID, newIDs):
    path = '/home/tbrownex/repos/SteveRoss/August 2022/images'
    files = os.listdir(path)
    for key in newIDs:
        for file in files:
            adDetails = {
                'name': file.split('.')[0],
                'path': path,
                'fileName': file,
                'targetURL': 'https://LoadTest.com'
            }
            resp = postAd(orgID, key, adDetails)

def processAddresses(orgID, newIDs):
    print("Associating Addressable Targets")
    count=0
    for campaign in newIDs:
        addressID = random.choice(ADDRESSIDS)
        addAddressableTargetToCampaign(orgID, campaign, addressID)
        count +=1
        if count % 500 == 0:
            logger.warning(str(campaign) + ' -- ' + str(datetime.datetime.now()))

def activate(orgID, newIDs):
    print("Activating")
    count=0
    for key in newIDs:
        activateCampaign(orgID, key)
        count +=1
        if count % 500 == 0:
            logger.warning(str(key) + ' -- ' + str(datetime.datetime.now()))

def setLogging():
    logLoc = "/home/tbrownex/"
    logFile = "LoadTest.log"
    logDefault = "info"
    logLevel = getattr(logging, logDefault.upper(), None)

    logging.basicConfig(filename=logLoc+logFile,\
                        level=logLevel,\
                        format='%(levelname)s:%(message)s')
    