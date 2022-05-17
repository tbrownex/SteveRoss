from utils import postRequest
from config import getBaseURL
from getCampaign import getCampaign

import requests

def postAd(orgID, campaignID, adDetails):
    campaign = getCampaign(orgID, campaignID)
    print("\n")
    base = getBaseURL()
    url = base+"organizations/"+str(orgID)+"/campaigns/"+str(campaignID)+'/ads'
    payload = {
        'ad[name]': adDetails['name'],
        'ad[target_url]': 'http://simpli.fi'
    }
    imagePath = adDetails['path']
    imageName = adDetails['fileName']
    files = [
        ('ad[primary_creative]', (imageName, open(f'{imagePath}/{imageName}', 'rb'), 'image/jpeg'))
    ]
    resp = postRequest(url, payload, files)
    return resp