from utils import postRequest
from config import getBaseURL

def activateCampaign(orgID, campaignID):
    base = getBaseURL()
    url = base+'organizations/'+str(orgID)+'/campaigns/'+str(campaignID)+'/activate'
    resp = postRequest(url, data=None)
    return resp