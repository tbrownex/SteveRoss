from config import getBaseURL
from getCampaign import getCampaign
from utils import delRequest

def deleteCampaign(orgID, campaignID):
    campaign = getCampaign(orgID, campaignID)
    print("\n")    
    base = getBaseURL()
    url = base+"organizations/"+str(orgID)+"/campaigns/"+str(campaignID)
    delRequest(url)
    return