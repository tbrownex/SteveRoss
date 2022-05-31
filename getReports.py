from utils import getRequest
from config import getBaseURL

def getReports(orgID):
    base = getBaseURL()
    url = base+"organizations/"+str(orgID)+"/report_center/reports?page=2&size=20"
    resp = getRequest(url)
    print("{:<12}{}".format('Rpt ID', 'Name'))
    for r in resp['reports']:
        print("{:<12}{}".format(r['id'], r['title']))
    return resp