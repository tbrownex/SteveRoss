import json

from utils import putRequest
from config import getBaseURL

def updateDeviceTypes(campaignID, deviceTypes):
    base = getBaseURL()
    url = base +"/campaigns/"+str(campaignID)+"/device_types"
    payload = {"device_type_ids": deviceTypes}
    payload=json.dumps(payload)
    return putRequest(url, payload)