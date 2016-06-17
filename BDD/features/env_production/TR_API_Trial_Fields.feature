@API_BASIC_PRODUCTION @API_TRIAL_SHOW_FIELDS_PROD
Feature: Verify the filtering of responses against the Trial api
    To verify the filtering of responses is correct against the Trials API.

    Filters being used:
    ?filter[trial]=attributes.eligibility.gender:Male%20AND%20attributes.eligibility.healthy_volunteers:No
    ?filter[trial]=attributes.eligibility.gender:Male%20AND%20attributes.location_countries.country:"United States"

  @API_TRIAL_SHOW_FIELDS_PROD
  Scenario Outline: API List Fields - Country
    Given I am on production environment
    When  I request to see all of <Type>
    And I filter by <field>
    Then I get a status code of <Expected Code>

  Examples: Request Criterion
    | Type  | field                                               | Expected Code |
    | trial |  ?field[trial]=attributes.location_countries.country |      200      |
    | trial |  ?field[trial]=attributes.keywords                   |      200      |

  @API_TRIAL_SHOW_FIELDS_PROD
  Scenario Outline: API Single field - String
    Given I am on production environment
    When  I request to see all of <Type>
    And I filter by <field>
    Then I get a status code of <Expected Code>

    Examples: Request Criterion
      | Type  | field                                                | Expected Code |
      | trial |  ?field[trial]=attributes.location_countries.country |      200      |
      | trial |  ?field[trial]=attributes.keywords                   |      200      |

