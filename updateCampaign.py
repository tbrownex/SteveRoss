from utils import putRequest
from config import getBaseURL

def updateCampaign(orgID, campaignID, payload):
    base = getBaseURL()
    url = base + "organizations/"+str(orgID)+"/campaigns/"+str(campaignID)
    return putRequest(url, payload)