#
#
#
import requests
import pytest

type_ns_list = ["pfizer.irb_approved","pfizer.document","pfizer.logo","pfizer.brochure", "pfizer.image"]
auth_dict = {
'auth_apigee' : ("qEZxd3bC707QtFLCrBLP6DhDvHVALcJP", "BtMPHHrOrAqFReGz"),
'auth_tr' : ("pablo", "emeraldcity"),
'auth_empty' : ("","")
}

json_Payloads = {
    "US Diabetes" : {
        "age": 55,
        "country_code": "US",
        "concept_id": "mesh:M0447381",
        "distance": 10,
        "geo": {
            "latitude": 40.7128,
            "longitude": 74.0059
        },
        "location": "New York, New York, United States",
        "gender": "Both",
        "containing_term": "Type 2 Diabetes"
    },

    "non-US Diabetes": {
        "age": 55,
        "country_code": "IE",
        "concept_id": "mesh:M0447381",
        "distance": 10,
        "geo": {
            "latitude": 40.7128,
            "longitude": 74.0059
        },
        "location": "New York, New York, United States",
        "gender": "Both",
        "containing_term": "Type 2 Diabetes"
    },

    "US non-Diabetes": {
        "age": 55,
        "country_code": "US",
        "concept_id": "mesh:M0447384",
        "distance": 10,
        "geo": {
            "latitude": 40.7128,
            "longitude": 74.0059
        },
        "location": "New York, New York, United States",
        "gender": "Both",
        "containing_term": "Type 2 Diabetes"
    },

    "non-US non-Diabetes": {
        "age": 55,
        "country_code": "GB",
        "concept_id": "mesh:M0447384",
        "distance": 10,
        "geo": {
            "latitude": 40.7128,
            "longitude": 74.0059
        },
        "location": "New York, New York, United States",
        "gender": "Both",
        "containing_term": "Type 2 Diabetes"
    }
};


def postReq(url, payload):
    auth = ("qEZxd3bC707QtFLCrBLP6DhDvHVALcJP", "BtMPHHrOrAqFReGz")
    buildHeader = {'Content-Type':'application/json'}
    r = requests.post(url, auth=auth, json=payload, headers=buildHeader)
    data = r.json()
    print("Data = {}".format(data))
    route = data['data']['attributes']['redirect_type']
    print("route = {}".format(route))
    statusCode = r.status_code
    statusHeaders = r.headers
    if statusCode == 200:
        statusData = r.json()['data']
    else:
        statusData = r.json()['errors']
    print(" Status Code = {}".format(statusCode))
    return [statusCode, statusData, statusHeaders, route]


def rqstr(context, url):
    auth = ("qEZxd3bC707QtFLCrBLP6DhDvHVALcJP", "BtMPHHrOrAqFReGz")
    r = requests.get(url, auth=auth)
    statusCode = r.status_code
    statusHeaders = r.headers
    if (context.web == 0):
        if statusCode == 200:
            statusData = r.json()['data']
            context.optCount = len(statusData)
            print("statusData : {}".format(statusData))
        else:
            statusData = r.json()['errors']
    else:
        statusData = ""
    return [statusCode, statusData, statusHeaders]

def QuickCheck(context, url):
    auth = auth_dict[context.auth]
    print("AUTH = {}".format(auth))
    r = requests.get(url, auth=auth)
    data = r.status_code
    print ("DATA : {}".format(data))
    statusCode = r.status_code
    return statusCode


@Given('I am on staging environment')
def step_impl1(context):
    context.web = 0
    context.trgt = "api.staging.trialreach.com/"


@Given(u'I have promoted code')
def step_impl1(context):
    context.web = 1
    context.trgt = ""

@When('I request to see all Trials')
def step_impl2(context):
    context.trgt = context.trgt+"trial"
    url = "https://"+context.trgt
    context.actual = rqstr(context, url )

@When('I request to see all of {type}')
def step_impl3(context, type):
    context.trgt = context.trgt + type
    url = "https://"+context.trgt
    context.actual = rqstr(context, url )

@When('I request to see all Protocol')
def step_impl3(context):
    context.trgt = context.trgt + "protocol"
    url = "https://"+context.trgt
    context.actual = rqstr(context, url )


@When('I request to see all Annotation')
def step_impl4(context):
    context.trgt = context.trgt + "annotation"
    url = "https://"+context.trgt
    context.actual = rqstr(context, url )

@when(u'I Include Protocols and Annotations')
def step_impl(context):
    context.trgt = context.trgt + "?include=protocol,annotation"
    url = "https://"+context.trgt
    context.actual = rqstr(context, url )

@when(u'I Include protocols')
def step_impl(context):
    context.trgt = context.trgt + "?include=protocol"
    url = "https://"+context.trgt
    context.actual = rqstr(context, url )

@when(u'I Include annotations')
def step_impl(context):
    context.trgt = context.trgt + "?include=annotation"
    url = "https://"+context.trgt
    context.actual = rqstr(context, url )

@when(u'I Include trials')
def step_impl(context):
    context.trgt = context.trgt + "?include=trial"
    url = "https://"+context.trgt
    context.actual = rqstr(context, url )

@when(u'I Include Protocols and trials')
def step_impl(context):
    context.trgt = context.trgt + "?include=protocol,trial"
    url = "https://"+context.trgt
    context.actual = rqstr(context, url )


####                    ####
####    USING FILTERS   ####
####                    ####

@when(u'I filter by {filter}')
def step_impl(context, filter):
    context.trgt = context.trgt + filter
    url = "https://"+context.trgt
    context.actual = rqstr(context, url )

# To include protocol & annotations to trials and vice versa
@when(u'I include the {filter}')
def step_impl(context, filter):
    context.trgt = context.trgt + "&include="+filter
    url = "https://"+context.trgt
    context.actual = rqstr(context, url )


@When(u'I request to see {webpage} with {auth}')
def step_VerifyWebpage(context, webpage, auth):
    context.trgt = webpage
    context.auth = "auth_"+auth
    url = context.trgt
    context.actual = rqstr(context, url )

@When(u'I post request a "{payload}" Trial')
def step_postReq(context, payload):
    uri = "https://api.staging.trialreach.com/match-rule/redirect"
    payloadr = json_Payloads[payload]
    print("payload - {}".format(payloadr))
    context.actual = postReq( uri, payloadr)


@when(u'I request a condishion ""')
def step_concept_No_suggestion_value(context):
    url = "https://api.build.trialreach.com/concept/suggestion?condition="
    context.actual = rqstr(context, url )

@when(u'I request a condishion "{term}"')
def step_concept_suggestion(context, term):
    url = "https://api.build.trialreach.com/concept/suggestion?condition="+term
    context.actual = rqstr(context, url )

@when(u'I request a condishion just the endpoint')
def step_concept_No_suggestion(context):
    url = "https://api.build.trialreach.com/concept/suggestion"
    context.actual = rqstr(context, url )


#          @THEN
####                    ####
####  Validate Results  ####
####                    ####

@Then('I get a status code of 200')
def step_impl5(context):
    exp = 200
    assert exp == context.actual[0]


@Then('I get a status code of 400')
def step_impl5(context, exp=400):
    # url = "https://"+context.trgt
    # context.actual = rqstr( url )
    assert exp == context.actual[0]


@Then ('the type_ns is in the type_ns_list')
def step_CheckResultInList(context):
    print(context.actual[1])
    for item in context.actual[1]:
        assert item['attributes']['type_ns'] in type_ns_list

@Then('I see the Error title is {message}')
@Then('I see the Error title is "{message}"')
def step_VerifyErrorMessage(context, message):
    print ("Message : {}".format(message))
    print ("Actual : {}".format(context.actual[1][0]['title']))
    assert message == context.actual[1][0]['title']

@Then('I EXPECT a status code of {exp}')
def step_AuthStatusCheck(context, exp):
    url = context.trgt
    context.actual = QuickCheck(context, url)
    print("Expected : {} = Actual : {}".format(exp, context.actual))
    context.web = 0
    assert exp == str(context.actual)


@Then('I am directed to {message}')
@Then('I am directed to "{message}"')
def step_VerifyReDirect(context, message):
    print ("Message : {}".format(message))
    print ("Actual : {}".format(context.actual[3]))
    assert message == context.actual[3]


@Then('I am returned {cnt} options')
def step_VerifyOptionsReturned(context, cnt):
    count = str(context.optCount)
    print("Count : {}".format(count))
    print("Cnt : {}".format(cnt))
    assert cnt == count


