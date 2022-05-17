from utils import getRequest
from config import getBaseURL

def getGeoFences(orgID, campaignID, fenceID=None, prt=True):
    '''
    Get either:
        a) all the geoFences for a campaign 
        b) all the coordinates for a geoFence
    "prt" parameter indicates whether to print or not
    '''
    base = getBaseURL()
    url = base+'organizations/'+str(orgID)+'/campaigns/'+str(campaignID)+'/geo_fences'
    resp = getRequest(url)
    if prt:
        if fenceID:
            getCoordinates(resp, fenceID)
        else:
            getFences(resp)
    return resp

def getFences(resp):
    # Get the ID and Name for all the Fences associated with a campaign
    print("{:<12}{:<15}{}".format('ID', 'Type', 'Name'))
    for r in resp['geo_fences']:
        print("{:<12}{:<15}{}".format(r['id'], r['geo_fence_type_name'], r['name']))

def getCoordinates(resp, fenceID):
    # Get the lat/long for the provided Fence ID
    print("{:<15}{}".format("Type", "Name"))
    for r in resp['geo_fences']:
        if r['id'] == fenceID:
            print("{:<15}{}\n".format(r['geo_fence_type_name'], r['name']))
            print("{:<14}{}".format('Longitude', 'Latitude'))
            for point in r['bid_area']['coordinates'][0]:
                print("{:<14}{}".format(point[0], point[1]))