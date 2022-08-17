import math

from utils import getRequest
from config import getBaseURL
from getOrganization import getOrg

def getCampaign(orgID, campaignID=None):
    '''
    Either show the details of a singe campaign or get all the campaigns for an Organization
    '''
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
    keys=['id', 'name', 'custom_id', 'status', 'start_date', 'end_date']
    for k in keys:
        print("{:<20}{}".format(k, payload[k]))
    return resp

def allCampaigns(url):
    # Get the ID and Name of all campaigns
    IDs = []
    names = []
    resp = getRequest(url)
    numPages = math.ceil(resp['paging']['total'] / resp['paging']['size'])
    for page in range(2, numPages+2):
        for c in resp['campaigns']:
            IDs.append(c['id'])
            names.append(c['name'])
        resp = getRequest(url+"?page="+str(page))
    return IDs, names