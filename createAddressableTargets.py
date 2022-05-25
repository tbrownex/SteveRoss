import json
import os

from utils import postRequest, putRequest
import config

def createAddressableTargets(orgID, path):
    '''
    For each CSV in "path", create an Addressable Target at the Org level
    Each Addressable Target has a unique ID which needs to be saved and returned
    '''
    csvList = getFiles(path)
    addressIDs = []
    for csv in csvList:
        print('--  ', csv)
        addressID = processAddressList(orgID, path, csv)
        addressIDs.append(addressID)
    return addressIDs

def processAddressList(orgID, path, csv):
    # For each CSV create a Target (basically a stub) then add the addresses
    # "create" returns a URL that is used to upload the CSV
    resp = createTarget(orgID, csv)
    addressID = resp['addresses'][0]['id']
    url = resp['upload_url']
    uploadCSV(url, path, csv)
    return addressID
    
def createTarget(orgID, csv):
    # segment_score of "2" means "Frequent"
    base = config.getBaseURL()
    url = base + "organizations/"+str(orgID)+"/addresses"
    d = {'name': csv.split('.')[0],
         "first_party_segment_score_filter_attributes": {"segment_score_filter_id": 2}
        }
    payload = {"address": d}
    payload = json.dumps(payload)
    return postRequest(url, data=payload)

def getFiles(path):
    # This folder should hold all the CSVs with addesses (and only the addresses)
    return sorted(os.listdir(path))

def uploadCSV(url, path, csv):
    fullPath = path+"/"+csv
    with open(fullPath, "rb") as f:
        resp = putRequest(url, f)