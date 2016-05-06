@API_BASIC
Feature: Verify the filtering of responses against the Trial api
    To verify the filtering of responses is correct against the Trials API.

  @API_TRIAL_FILTER
  Scenario Outline: API Trial call - AND
    Given I am on staging environment
    When  I request to see all of <Type>
    And I add <filter>
    Then I get a status code of <Expected Code>

  Examples: Request Criterion
    | Type  | filter                                                                                                    | Expected Code |
    | trial |  ?filter[trial]=attributes.eligibility.gender:Male%20AND%20attributes.eligibility.healthy_volunteers:No   |      200      |
    | trial |  ?filter[trial]=attributes.eligibility.gender:Female%20AND%20attributes.eligibility.healthy_volunteers:No |      200      |
    | trial |  ?filter[trial]=attributes.eligibility.gender:Male%20AND%20attributes.location_countries.country:"United States"   |      200      |
    | trial |  ?filter[trial]=attributes.location_countries.country:"United States"%20AND%20attributes.location_countries.country:"Bosnia and Herzegovina"   |      200      |


  @API_TRIAL_FILTER
  Scenario Outline: API Trial call - OR
    Given I am on staging environment
    When  I request to see all of <Type>
    And I add <filter>
    Then I get a status code of <Expected Code>

  Examples: Request Criterion
    | Type  | filter                                                                                                  | Expected Code |
    | trial |  ?filter[trial]=attributes.eligibility.gender:Male%20OR%20attributes.eligibility.healthy_volunteers:No  |      200      |
    | trial |  ?filter[trial]=attributes.eligibility.gender:(Male Female)                                             |      200      |
    | trial |  ?filter[trial]=attributes.location_countries.country:("United States"+"United kingdom")                |      200      |
    | trial |  ?filter[trial]=attributes.location_countries.country:("United States"+"Bosnia and Herzegovina")        |      200      |
    | trial |  ?filter[trial]=attributes.location_countries.country:(United States+Australia)                         |      200      |

  @API_TRIAL_FILTER
  Scenario Outline: API Trial call - OR with AND
    Given I am on staging environment
    When  I request to see all of <Type>
    And I add <filter>
    Then I get a status code of <Expected Code>

  Examples: Request Criterion
    | Type  | filter                                                                                                  | Expected Code |
    | trial |  ?filter[trial]=attributes.eligibility.gender:(Male Female)&attributes.eligibility.healthy_volunteers:No|      200      |
