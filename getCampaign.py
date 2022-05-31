from utils import getRequest
from config import getBaseURL
from getOrganization import getOrg

def getCampaign(orgID, campaignID=None):
    getOrg(orgID)
    print("\n")    
    base = getBaseURL()
    if campaignID:
        url = base+"organizations/"+str(orgID)+"/campaigns/"+str(campaignID)
        resp = singleCampaign(url)
    else:
        url = base+"organizations/"+str(orgID)+"/campaigns/"
        resp = allCampaigns(url)
    return resp
    
def singleCampaign(url):
    resp = getRequest(url)
    payload = resp['campaigns'][0]
    return payload
    '''keys=['id', 'name', 'custom_id', 'status', 'start_date', 'end_date']
    for k in keys:
        print("{:<20}{}".format(k, payload[k]))
    return resp'''

def allCampaigns(url):
    resp = getRequest(url)
    print("{:<10}{}".format("ID", "Name"))
    for c in resp['campaigns']:
        print("{:<10}{}".format(c['id'], c['name']))
    return resp