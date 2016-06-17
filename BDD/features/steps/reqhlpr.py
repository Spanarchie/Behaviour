import requests


def rqstr(url):
    auth = ("qEZxd3bC707QtFLCrBLP6DhDvHVALcJP", "BtMPHHrOrAqFReGz")
    print ("URL : {}".format(url))
    r = requests.get(url, auth=auth)
    statusCode = r.status_code
    jsonData = r.json()
    return ([statusCode, jsonData])
