from utils import getRequest
from config import getBaseURL

def getDeviceTypes(campaignID):
    # The "device_types" request will return all the device type IDs for this campaign
    base = getBaseURL()
    url = base+"/campaigns/"+str(campaignID)+"/device_types"
    resp = getRequest(url)
    # Could be more than 1 device type so need to loop
    l = []
    for d in resp['device_types']:
        l.append(d['id'])
    return l