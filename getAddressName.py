from utils import getRequest
from config import getBaseURL

def getAddressName(addressID):
    base = getBaseURL()
    url = base+"addresses/"+str(addressID)
    resp = getRequest(url)
    return resp['addresses'][0]['name']