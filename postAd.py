from utils import postRequest
from config import getBaseURL

import requests

def postAd(orgID, campaignID, adDetails):
    '''
    Associates an image to a campaign
    "adDetails" is a dictionary for naming the Ad and the location of the image
    '''
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