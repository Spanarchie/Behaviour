# -*- coding: utf-8 -*-
import json
import requests
import os, sys
import time
import logging
import pygal

buildHeader = {}
targetENV = "staging"
# targetURL = "api.staging.trialreach.com"

from py2neo import Graph
# gdb = Graph()

# -- Set Env & targets -- #
if len(sys.argv) == 2 :
    targetENV= sys.argv[1]

if (targetENV == "staging") :
    targetURL = "api.staging.trialreach.com"
    buildHeader = {'ENV-NODE': ''}

elif targetENV == "rnd" :
    targetURL = "api.build.trialreach.com"
    buildHeader = {'ENV-NODE': 'rnd'}

else:
    targetURL = "api.build.trialreach.com"
    buildHeader = {'ENV-NODE': ''}


# -- LOGGING -- #
logger = logging.getLogger('API Load Test '+targetENV)
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
timestr = time.strftime("%Y%m%d-%H%M%S")
filename = "logs/{}API_Test-{}-{}.log".format("CMH_LOG-", buildHeader["ENV-NODE"],timestr)
print("Filename : {}".format(filename))
fh = logging.FileHandler(filename)
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)
# add the handlers to logger
logger.addHandler(ch)
logger.addHandler(fh)


# -- Set targets -- #
base_trial = """https://{}/trial""".format(targetURL)
base_protocol = """https://{}/protocol""".format(targetURL)
base_annotation = """https://{}/annotation""".format(targetURL)

req_include_P_A = """https://{}/trial?include=protocol,annotation""".format(targetURL)
req_include_P = """https://{}/trial?include=protocol""".format(targetURL)
req_include_A = """https://{}/trial?include=annotation""".format(targetURL)

req_include_P_A_with_lstChange_Range = """http://{}/trial\
?include=protocol,annotation&fields[trial]=attributes.lastchanged_date\
&filter[trial]=attributes.lastchanged_date.value:[2016-04-14T20:34:36.034865+00:00+TO+2016-04-14T20:31:59.047674+00:00]""".format(targetURL)

req_include_P_A_with_lstChange_Range = """http://{}/trial\
?include=annotation\
&fields[trial]=attributes.lastchanged_date\
&filter[trial]=attributes.lastchanged_date.value:[2016-04-14T20:34:36.034865+00:00+TO+2016-04-14T20:31:59.047674+00:00]""".format(targetURL)
req_include_P_with_lstChange_Range = """http://{}/trial\
?include=protocol\
&fields[trial]=attributes.lastchanged_date\
&filter[trial]=attributes.lastchanged_date.value:[2016-04-14T20:34:36.034865+00:00+TO+2016-04-14T20:31:59.047674+00:00]""".format(targetURL)

trial_req_LT_Date = """http://{}/trial\
?include=protocol,annotation\
&fields[trial]=attributes.lastchanged_date\
&filter[trial]=attributes.lastchanged_date.value:[LT+2016-04-14T20:34:36.034865+00:00]""".format(targetURL)

protocol_req_LT_Date = """http://{}/protocol\
?fields[protocol]=attributes.lastchanged_date\
&filter[protocol]=attributes.lastchanged_date.value:[LT+2016-04-14T20:34:36.034865+00:00]""".format(targetURL)

annotation_req_LT_Date = """http://{}/annotation\
?fields[annotation]=attributes.lastchanged_date\
&filter[annotation]=attributes.lastchanged_date.value:[LT+2016-04-14T20:34:36.034865+00:00]""".format(targetURL)

req_LE_Date = """http://{}/trial\
?include=protocol,annotation\
&fields[trial]=attributes.lastchanged_date\
&filter[trial]=attributes.lastchanged_date.value:[LE+2016-04-14T20:34:36.034865+00:00]""".format(targetURL)


req_GT_Date = """http://{}/trial\
?include=protocol,annotation\
&fields[trial]=attributes.lastchanged_date\
&filter[trial]=attributes.lastchanged_date.value:[GT+2016-04-14T20:34:36.034865+00:00]""".format(targetURL)

req_GE_Date = """http://{}/trial\
?include=protocol,annotation\
&fields[trial]=attributes.lastchanged_date\
&filter[trial]=attributes.lastchanged_date.value:[GE+2016-04-14T20:34:36.034865+00:00]""".format(targetURL)

req_OR_with_Ampersand = """http://{}/trial\
?fields[trial]=attributes.eligibility.gender\
&filter[trial]=attributes.eligibility.gender:(Male Female)&attributes.eligibility.healthy_volunteers:No""".format(targetURL)

req_OR_same_fields = """https://{}/trial\
?fields[trial]=attributes.eligibility.gender\
&filter[trial]=attributes.eligibility.gender:Male OR attributes.eligibility.gender:Female""".format(targetURL)

OR_country_List_fields = """https://{}/trial\
?filter[trial]=attributes.location_countries.country:(United States+Australia)\
&fields[trial]=attributes.location_countries.country""".format(targetURL)

OR_keyword_List_fields = """https://{}/trial\
?filter[trial]=attributes.keyword:(psoriasis meta-analyses)\
&fields[trial]=attributes.keyword""".format(targetURL)

req_OR_diff_fields = """https://{}/trial\
?filter[trial]=attributes.eligibility.gender:Male%20OR%20attributes.eligibility.healthy_volunteers:No\
&fields[trial]=attributes.eligibility.gender,attributes.eligibility.healthy_volunteers""".format(targetURL)

req_AND_diff_fields = """https://{}/trial\
?filter[trial]=attributes.eligibility.gender:Male%20AND%20attributes.eligibility.healthy_volunteers:No\
&fields[trial]=attributes.eligibility.gender,attributes.eligibility.healthy_volunteers""".format(targetURL)




def dataCapture(trg = "", req = "", clt ="", pos = "", dur = "", resp = ""):
    qry  = 'merge (r :REQUEST {name: "'+str(req)+'", target: "'+str(trg)+'", clt: "'+str(clt)+'", pos: "'+str(pos)+'", dur: "'+str(dur)+'", resp: "'+str(resp)+'" })'
    # qry1  = 'merge (r :REQUEST { name: "{}", target: "{}", clt: "{}", pos: "{}", dur: {}  })'.format(req, trg, clt, pos, dur)
    print (qry )


def generatePerfChart(data, title, date, root="svg/"):
    maxLen = 0
    bar_chart = pygal.Line()
    bar_chart.title = '{} - {} API page requests durations (in ms)'.format(date, targetENV)
    bar_chart.x_title='Initial & Page number'
    bar_chart.y_title='Duration in ms'
    for x in data['results']:
        bar_chart.add(x[0],x[1])
        curLen = len(x[1])
        if maxLen < curLen:
            maxLen = len(x[1])
    bar_chart.x_labels = map(str, range(0, maxLen))
    if title =="Combined":
        if root == "svg/":
            bar_chart.render_to_file('svg/{}-{}{}_chart2.svg'.format(date, title, targetENV))
        else:
            bar_chart.render_to_file('{}{}{}.svg'.format(root, title, targetENV))
    else:
            bar_chart.render_to_file('{}{}-{}{}_chart2.svg'.format(root, date, title, targetENV))


def generateActualPerfChart(data, title, date, root="svg/"):
    maxLen = 0
    dataset=[]
    bar_chart = pygal.Line()
    bar_chart.title = '{} - {} API sequential page request durations (in ms)'.format(date, targetENV)
    bar_chart.x_title='Initial & Page number'
    bar_chart.y_title='Duration in ms'
    for x in data['results']:
        dataset = dataset+x[1]
        curLen = len(x[1])
        if maxLen < curLen:
            maxLen = len(x[1])
    bar_chart.add("Actual", dataset)
    bar_chart.x_labels = map(str, range(0, len(dataset)))
    if root == "svg/":
        bar_chart.render_to_file('{}{}-{}_chart2.svg'.format(root, date, title))
    else:
        bar_chart.render_to_file('{}{}.svg'.format(root, title))



def reportingFunc(jsonObj, timestr):
    src = "reports/svgImg/latest/"
    dest = "reports/svgImg/previous/"
    files = ["Combined.svg", "Actual.svg"]
    for file in files:
        src1 = src+file
        print(src1)
        dest1 = dest+file
        print(dest1)
        os.rename( src1, dest1 )
    generatePerfChart(jsonObj, "Combined", timestr, "reports/svgImg/latest/")
    generateActualPerfChart(jsonObj, "Actual", timestr, "reports/svgImg/latest/")


def loadr(trgt):
    current_milli_time = lambda: int(round(time.time() * 1000))
    result = []

    with open('API_Perf_Rec.dat') as data_file:
        data = json.load(data_file)


    timestr = time.strftime("%Y%m%d-%H%M%S")
    jsonObj= {}
    jsonObj["date"] = timestr
    jsonObj["results"] = []


    for indx, reqst in enumerate(trgt):
        resList = [] # To record the request durations

        strtTime = current_milli_time()
        r = requests.get(trgt[1], auth=('qEZxd3bC707QtFLCrBLP6DhDvHVALcJP', 'BtMPHHrOrAqFReGz'), headers=buildHeader)
        endTime = current_milli_time()
        durTime = endTime - strtTime
        resList.append(durTime)
        clt = os.uname()[1]
        respCode = r.status_code
        print("resp : {}".format(respCode))
        print ("{} : {} took {}ms".format(trgt[0], "Initial request", durTime))
        logger.info(
            "ENV {} - init request - {} - client {} - Start {} - end {} - Duration {} - status {}".format(targetENV,
                                                                                                           trgt[0],
                                                                                                           clt,
                                                                                                           strtTime,
                                                                                                           endTime,
                                                                                                           durTime,
                                                                                                           respCode))

        dataCapture(targetURL, trgt[0], clt, "init", durTime, respCode)

        resp = r.json()
        pgs = resp['meta']['total-pages']
        lstPg = pgs+1

        # Make a request for each page & measure the duration.
        for p in range(1, lstPg):
            if trgt[0][:5] == "base_":
                req = "{}?page[number]={}".format(trgt[1], str(p))
            else:
                req = "{}&page[number]={}".format(trgt[1], str(p))
            print ("Requested : {}".format(req))
            strtTime = current_milli_time()
            r = requests.get(req, auth=('qEZxd3bC707QtFLCrBLP6DhDvHVALcJP', 'BtMPHHrOrAqFReGz'), headers=buildHeader)
            endTime = current_milli_time()
            durTime = endTime - strtTime
            respCode = r.status_code
            print ("{} : pg{} took {}ms".format(trgt[0], str(p), durTime))
            logger.info("ENV {} - page request - {} - client {} - Start {} - end {} - Duration {} - status {}".format(targetENV, trgt[0], clt, strtTime, endTime, durTime, respCode))
            dataCapture(targetURL, trgt[0], clt, "p"+str(p), durTime, respCode)
            resList.append(durTime)
        jsonObj["results"].append([trgt[0], resList])
        generatePerfChart(jsonObj, trgt[0], timestr)

    data.append(jsonObj)

    reportingFunc(jsonObj, timestr)


    with open('API_Perf_Rec.dat', 'w') as outfile:
        json.dump(data, outfile)
    return



import multiprocessing

if __name__ == '__main__':
    jobs = []
    trgts = [
                ["base_trial", base_trial], ["base_protocol", base_protocol],
                ["base_annotation", base_annotation],['req_OR_same_fields', req_OR_same_fields],
                ['req_OR_diff_fields', req_OR_diff_fields], ['req_AND_diff_fields', req_AND_diff_fields],
                ['req_include_P_A', req_include_P_A], ['req_include_P', req_include_P],
                ['req_include_A', req_include_A]
            ]
    for i in trgts:
        p = multiprocessing.Process(target=loadr, args=(i,))
        print ("trgt = {}".format(p))
        jobs.append(p)
        p.start()
