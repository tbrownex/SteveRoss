import requests
import json

import config

def createAddressableTarget(orgID):
    hdr = config.getHeader()
    base = config.getBaseURL()
    url = base + "organizations/"+str(orgID)+"/addresses"
    return url
    resp = requests.post(url, data=None, headers=hdr)
    newCampaign = resp.json()
    return newCampaign
    ID = newCampaign['campaigns'][0]['id']
    print("Campaign {} created".format(ID))
    return ID