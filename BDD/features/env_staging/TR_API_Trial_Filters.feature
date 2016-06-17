@API_BASIC_STAGING
Feature: Verify the filtering of responses against the Trial api
    To verify the filtering of responses is correct against the Trials API.

    Filters being used:
    ?filter[trial]=attributes.eligibility.gender:Male%20AND%20attributes.eligibility.healthy_volunteers:No
    ?filter[trial]=attributes.eligibility.gender:Male%20AND%20attributes.location_countries.country:"United States"

  @API_TRIAL_FILTER
  Scenario Outline: API Trial call - AND
    Given I am on staging environment
    When  I request to see all of <Type>
    And I filter by <Filter>
    Then I get a status code of <Expected Code>

  Examples: Request Criterion
    | Type  | Filter                                                                                                                                      | Expected Code |
    | trial |  ?filter[trial]=attributes.eligibility.gender:Male%20AND%20attributes.eligibility.healthy_volunteers:No                                     |      200      |
    | trial |  ?filter[trial]=attributes.eligibility.gender:Female%20AND%20attributes.eligibility.healthy_volunteers:No                                   |      200      |
    | trial |  ?filter[trial]=attributes.eligibility.gender:Male%20AND%20attributes.location_countries.country:"United States"                            |      200      |
    | trial |  ?filter[trial]=attributes.location_countries.country:"United States"%20AND%20attributes.location_countries.country:"Bosnia and Herzegovina"|      200      |

  @API_TRIAL_FILTER
  Scenario Outline: API Trial call - OR
    Given I am on staging environment
    When  I request to see all of <Type>
    And I filter by <Filter>
    Then I get a status code of <Expected Code>

    Examples: Request Criterion
      | Type  | Filter                                                                                                                         | Expected Code |
      | trial |  ?filter[trial]=attributes.eligibility.gender:Male OR attributes.eligibility.healthy_volunteers:No                             |      200      |
      | trial |  ?filter[trial]=attributes.location_countries.country:"United States" OR attributes.location_countries.country:"United kingdom"|      200      |


  @API_TRIAL_FILTER
  Scenario Outline: API Trial call - OR using ()
    Given I am on staging environment
    When  I request to see all of <Type>
    And I filter by <Filter>
    Then I get a status code of <Expected Code>

  Examples: Request Criterion
    | Type  | Filter                                                                                          | Expected Code |
    | trial |  ?filter[trial]=attributes.eligibility.gender:(Male Female)                                     |      200      |
    | trial |  ?filter[trial]=attributes.location_countries.country:("United States"+"United kingdom")        |      200      |
    | trial |  ?filter[trial]=attributes.location_countries.country:("United States"+"Bosnia and Herzegovina")|      200      |


  @API_TRIAL_FILTER
  Scenario Outline: API Trial call - OR with &(as AND)
    Given I am on staging environment
    When  I request to see all of <Type>
    And I filter by <Filter>
    Then I get a status code of <Expected Code>


  Examples: Request Criterion
    | Type  | Filter                                                                                                                               | Expected Code |
    | trial |  ?filter[trial]=attributes.eligibility.gender:(Male Female)&attributes.eligibility.healthy_volunteers:No                             |      200      |
    | trial |  ?filter[trial]=attributes.eligibility.gender:(Male Female)&attributes.location_countries.country:("United States"+"United kingdom") |      200      |
