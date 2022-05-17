from utils import postRequest
import config

def createCampaign(orgID):
    base = config.getBaseURL()
    url = base + "organizations/"+str(orgID)+"/campaigns"
    newCampaign = postRequest(url, data=None)
    ID = newCampaign['campaigns'][0]['id']
    print("Campaign {} created".format(ID))
    return ID