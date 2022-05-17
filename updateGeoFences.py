from utils import postRequest
from config import getBaseURL
from getOrganization import getOrg

def updateGeoFences(orgID, campaignID, payload):
    base = getBaseURL()
    url = base+'organizations/'+str(orgID)+'/campaigns/'+str(campaignID)+'/geo_fences'
    resp = postRequest(url, payload)
    return resp