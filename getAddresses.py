from utils import getRequest
from config import getBaseURL

def getAddresses(campaignID, orgID=None):
    # If orgID passed, get the addresses for an Organization otherwise it's addresses for a Campaign
    base = getBaseURL()
    if orgID is not None:
        url = base+"organizations/"+str(orgID)+"/addresses"
        resp = getRequest(url)
        printOrg(resp)
    else:
        url = base+"campaigns/"+str(campaignID)+'/campaign_addresses'
        resp = getRequest(url)
        printCampaign(resp)
    return resp

def printOrg(resp):
    print("{:<10}{:<40}{}".format("ID", "Name", "Active"))
    for address in resp['addresses']:
        print("{:<10}{:<40}{}".format(address['id'], address['name'], address['active']))

def printCampaign(resp):
    print("{:<10}{:<40}".format("ID", "Address ID"))
    for address in resp['campaign_addresses']:
        print("{:<10}{}".format(address['id'], address['address_id']))