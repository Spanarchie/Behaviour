#
#
#
import requests

def rqstr(url):
    auth = ("qEZxd3bC707QtFLCrBLP6DhDvHVALcJP", "BtMPHHrOrAqFReGz")
    print ("URL : {}".format(url))
    r = requests.get(url, auth=auth)
    statusCode = r.status_code
    return statusCode


@Given('I am on staging environment')
def step_impl1(context):
    context.trgt = "api.staging.trialreach.com/"

@When('I request to see all Trials')
def step_impl2(context):
    context.trgt = context.trgt+"trial"

@When('I request to see all of {type}')
def step_impl3(context, type):
    context.trgt = context.trgt + type

@When('I request to see all Protocol')
def step_impl3(context):
    context.trgt = context.trgt + "protocol"


@When('I request to see all Annotation')
def step_impl4(context):
    context.trgt = context.trgt + "annotation"

@when(u'I Include Protocols and Annotations')
def step_impl(context):
    context.trgt = context.trgt + "?include=protocol,annotation"

@when(u'I Include protocols')
def step_impl(context):
    context.trgt = context.trgt + "?include=protocol"

@when(u'I Include annotations')
def step_impl(context):
    context.trgt = context.trgt + "?include=annotation"

@when(u'I Include trials')
def step_impl(context):
    context.trgt = context.trgt + "?include=trial"

@when(u'I Include Protocols and trials')
def step_impl(context):
    context.trgt = context.trgt + "?include=protocol,trial"


####                    ####
####    USING FILTERS   ####
####                    ####

@when(u'I filter by {filter}')
def step_impl(context, filter):
    context.trgt = context.trgt + filter


#          @THEN
####                    ####
####  Validate Results  ####
####                    ####

@Then('I get a status code of 200')
def step_impl5(context):
    url = "https://"+context.trgt
    context.actual = rqstr( url )
    exp = 200
    assert exp == context.actual

@Then('I get a status code of 400')
def step_impl5(context):
    url = "https://"+context.trgt
    context.actual = rqstr( url )
    exp = 400
    assert exp == context.actual
