@API_BASIC_PRODUCTION @API_TRIAL_SHOW_FIELDS_PROD
Feature: Verify the filtering of responses against the Protocol api
    To verify the filtering of responses is correct against the protocol API.

#   There are curremntly no list fields in the Protocol at the moment.
#  @API_TRIAL_SHOW_FIELDS
#  Scenario Outline: API-protocol List Fields - Country
#    Given I am on production environment
#    When  I request to see all of <Type>
#    And I filter by <field>
#    Then I get a status code of <Expected Code>
#
#  Examples: Request Criterion
#    | Type     | field                                                          | Expected Code |
#    | protocol |  ?field[protocol]=attributes.eligibility.drug_administered_by  |      200      |

  @API_TRIAL_SHOW_FIELDS_PROD
  Scenario Outline: API-protocol Single field - String
    Given I am on production environment
    When  I request to see all of <Type>
    And I filter by <field>
    Then I get a status code of <Expected Code>

    Examples: Request Criterion
      | Type     |  field                                      | Expected Code |
      | protocol | ?field[protocol]=type                       |      200      |
      | protocol | ?field[protocol]=attributes.eligibility.who |      200      |

