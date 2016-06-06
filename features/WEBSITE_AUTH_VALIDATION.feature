# Created by colinmoore-hill at 11/05/2016
@WEB_AUTH_SANITY
Feature: Verify the main web pages for Trialreach are behaving as expected
    This will do a very basic check to verify that pages are accessible and with auth
    where required - Demo01,  Staging, Production

         Landing Pages - trialreach.com, trialreach.com/bridge,
         Classic Pages - Team, Jobs and a special trial(TM511)
         Single API Page - /trial

    Basic auth (TR_AUTH) has been applied to certain pages to prevent bpts crawling demo/test pages.
         : Staging & Demo environments - web need to be logged into
         : Bridge is a log on screen, therefore not required.



  @DEMO_00_LANDING_PAGES  @DEMO_WEB_SANITY
  Scenario Outline: DEMO_00 Web site landing pages & auth access
    Given I have promoted code
    When  I request to see <webpage> with <auth>
    Then I EXPECT a status code of <Expected Code>

  Examples: Request Criterion
    | webpage                                                          | Expected Code | auth   |
    |  http://demo-demo00.trialreach.com/                              |      401      | empty  |
    |  http://demo-demo00.trialreach.com/bridge                        |      200      | empty  |


  @DEMO_01_LANDING_PAGES  @DEMO_WEB_SANITY
  Scenario Outline: DEMO_01 Web site landing pages & auth access
    Given I have promoted code
    When  I request to see <webpage> with <auth>
    Then I EXPECT a status code of <Expected Code>

    Examples: Request Criterion
    | webpage                                                          | Expected Code | auth   |
    |  http://demo-demo01.trialreach.com/                              |      401      | empty  |
    |  http://demo-demo01.trialreach.com/bridge                        |      401      | empty  |
    |  https://api.demo.trialreach.com/trial                           |      200      | apigee |



  @STAGING_LANDING_PAGES @STAGING_WEB_SANITY
  Scenario Outline: STAGING Web site landing pages & auth access
    Given I have promoted code
    When  I request to see <webpage> with <auth>
    Then I EXPECT a status code of <Expected Code>

    Examples: Request Criterion
    | webpage                                                          | Expected Code | auth   |
    #Without auth
    |  http://staging.trialreach.com/                                  |      401      | empty  |
    |  http://staging.trialreach.com/bridge                            |      401      | empty  |
    #With auth applied
    |  http://staging.trialreach.com/                                  |      200      |  tr    |
    |  http://staging.trialreach.com/bridge                            |      200      |  tr    |
    |  https://api.staging.trialreach.com/trial                        |      200      | apigee |
    # Classic Pages
    |  http://staging.trialreach.com/about/jobs.html?let_me_in         |      200      |  tr    |
    |  http://staging.trialreach.com/about/team.html?let_me_in         |      200      |  tr    |
    |  http://staging.trialreach.com/find_global_trials.html?let_me_in |      200      |  tr    |
    |  http://staging.trialreach.com/s/TM511?let_me_in                 |      200      |  tr    |


  @PRODUCTION_LANDING_PAGES  @PRODUCTION_WEB_SANITY
  Scenario Outline: STAGING Web site landing pages & auth access
    Given I have promoted code
    When  I request to see <webpage> with <auth>
    Then I EXPECT a status code of <Expected Code>

    Examples: Request Criterion
    | webpage                                                          | Expected Code | auth   |
    # Live Site Pages
    |  http://trialreach.com/                                          |      200      | empty  |
    |  http://trialreach.com/bridge                                    |      200      | empty  |
    |  https://api.trialreach.com/trial                                |      200      | apigee |
    #   Live Classic Pages
    |  http://trialreach.com/about/jobs.html                           |      200      | empty  |
    |  http://trialreach.com/about/team.html                           |      200      | empty  |
    |  http://trialreach.com/find_global_trials.html                   |      200      | empty  |
    |  https://trialreach.com/s/TM511                                  |      200      | empty  |
