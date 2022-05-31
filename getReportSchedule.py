from utils import getRequest
from config import getBaseURL

def getReportSchedule(orgID, reportID):
    base = getBaseURL()
    url = base+"organizations/"+str(orgID)+"/report_center/reports/"+str(reportID)+"/schedules?children=true"
    print(url)
    resp = getRequest(url)
    '''print("{:<12}{}".format('Rpt ID', 'Name'))
    for r in resp['reports']:
        print("{:<12}{}".format(r['id'], r['title']))'''
    return resp