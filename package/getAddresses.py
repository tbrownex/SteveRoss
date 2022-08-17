import getArgs
from utils import getRequest
from config import getBaseURL

def main(orgID):
    # Show all the addresses for an Organization
    assert orgID is not None, "Need an Organization ID"
    base = getBaseURL()
    url = base+"organizations/"+str(orgID)+"/addresses"
    IDs, names = getAll(url)
    return zip(IDs, names)

def getAll(url):
    # No printing, just get the ID and Name of all Addresses
    IDs = []
    names = []
    resp = getRequest(url)
    numPages = resp['paging']['total']
    for page in range(2, numPages+2):
        for a in resp['addresses']:
            IDs.append(a['id'])
            names.append(a['name'])
        resp = getRequest(url+"?page="+str(page))
    return IDs, names

def printAddress(resp):
    print("{:<15}{:<40}".format("Campaign ID", "Address ID"))
    for address in resp['campaign_addresses']:
        print("{:<15}{}".format(address['campaign_id'], address['address_id']))

if __name__ == "__main__":
    args = getArgs.main()
    print(args)
    main(args)