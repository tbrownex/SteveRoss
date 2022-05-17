import json

from config import getBaseURL
from getCampaign import getCampaign
from createCampaign import createCampaign
from updateCampaign import update
from getGeoFences import getGeoFences
from utils import postRequest

def copyCampaign(orgID, campaignID, numCopies):
    # Get a campaign to copy, then create a campaign, then update it with values from the copied
    # First get the campaign to copy
    master = getCampaign(orgID, campaignID)
    name = master['name']
    payload = formatPayload(master)
    # Now create new campaigns
    newIDs = createCampaigns(orgID, payload, numCopies, name)
    # Update the GeoFences
    addGeoFences(orgID, campaignID, newIDs)
    
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
    newIDs = []
    for n in range(1, numCopies+1):
        payload['campaign']['name'] = name+' - copy '+str(n)
        newID = createCampaign(orgID)
        payloadString = json.dumps(payload)
        resp = update(orgID, newID, payloadString)
        newIDs.append(newID)
    return newIDs
    
def addGeoFences(orgID, campaignID, newIDs):
    # Get the GeoFence data from the master campaign
    payload = formatGeoPayload(orgID, campaignID)
    base = getBaseURL()
    for newID in newIDs:
        url = base+'organizations/'+str(orgID)+'/campaigns/'+str(newID)+'/geo_fences'
        resp = postRequest(url, payload)

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