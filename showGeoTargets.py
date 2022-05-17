from utils import getRequest
from config import getBaseURL
from getOrganization import getOrg

def showGeoTargets(orgID, campaignID):
    getOrg(orgID)
    print("\n")
    base = getBaseURL()
    url = base+'organizations/'+str(orgID)+'/campaigns/'+str(campaignID)+'/geo_targets'
    print(url)
    resp = getRequest(url)
    return resp