import json

from utils import putRequest
from config import getBaseURL

def addAddressableTargetToCampaign(orgID, campaignID, addressID):
    '''
    Addressable targets are defined at the Org level
    This will assign one of them to a Campaign
    '''
    base = getBaseURL()
    url = base + "campaigns/"+str(campaignID)+'/campaign_addresses/change'
    d = {'add': [
        {"address_id": addressID,
         "segment_target_type_id": 2
        }]
        }
    payload = {'campaign_first_party_segments': d}
    payload = json.dumps(payload)
    return putRequest(url, payload)