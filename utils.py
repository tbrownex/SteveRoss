import requests
import json

from config import getHeader

def getRequest(url, data=None):
    hdr = getHeader()
    resp = requests.get(url, data=data, headers=hdr)
    return resp.json()

def putRequest(url, data):
    hdr = getHeader()
    resp = requests.put(url, data=data, headers=hdr)
    if resp.status_code == 200:
        print("success")
    else:
        print(resp.status_code)
    return resp

def postRequest(url, data, files=None):
    hdr = getHeader()
    if files:
        # The POST with files parameter, for posting an Ad, can't specify content-type for some reason
        hdr.pop('Content-Type', None)
        resp = requests.post(url, data=data, headers=hdr, files=files)
    else:
        resp = requests.post(url, data=data, headers=hdr)
    return resp.json()