from utils import getRequest
from config import getBaseURL
from getCampaign import getCampaign

def getAds(orgID, campaignID):
    '''
    Ads are always associated with a Campaign
    '''
    campaign = getCampaign(orgID, campaignID)
    print("\n")    
    base = getBaseURL()
    url = base+"organizations/"+str(orgID)+"/campaigns/"+str(campaignID)+'/ads?attributes_only=true'
    resp = getRequest(url)
    print("{:<12}{:<55}{:<12}{}".format("ID", "Name", "Status", "Verified"))
    for r in resp['ads']:
        print("{:<12}{:<55}{:<12}{}".format(r['id'], r['name'], r['status'], r['click_tag_verified']))
    return resp