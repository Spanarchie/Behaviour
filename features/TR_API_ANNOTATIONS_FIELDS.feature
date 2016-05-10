@API_ANNOTATIONS @API_ANNOTATIONS_FIELDS

Feature: Verify the filtering of responses against the annotation api
    To verify the filtering of responses is correct against the annotation API.


#   There are no list objecting the Annotations at this point in time.
#  Scenario Outline: API List Fields - Country
#    Given I am on staging environment
#    When  I request to see all of <Type>
#    And I filter by <field>
#    Then I get a status code of <Expected Code>
#
#  Examples: Request Criterion
#    | Type       | field                                                     | Expected Code |
#    | annotation |  ?field[annotation]=attributes.location_countries.country |      200      |
#    | annotation |  ?field[annotation]=attributes.keywords                   |      200      |
#

  Scenario Outline: API Single field - String
    Given I am on staging environment
    When  I request to see all of <Type>
    And I filter by <field>
    Then I get a status code of <Expected Code>

    Examples: Request Criterion
      | Type       | field                                  | Expected Code |
      | annotation | ?field[annotation]=type                |      200      |
      | annotation | ?field[annotation]=attributes.type_ns  |      200      |

 Scenario Outline: API annotations with trials included - Single field - String
  Given I am on staging environment
  When  I request to see all of <Type>
  And I filter by <Field>
  And I include the <Include>
  Then I get a status code of <Expected Code>
  And the type_ns is in the type_ns_list

  Examples: Request Criterion
    | Type       | Field                                  | Include  | Expected Code |
    | annotation | ?field[annotation]=type                | trial    |      200      |
    | annotation | ?field[annotation]=attributes.type_ns  | trial    |      200      |

  Scenario Outline: API annotations with trials included - Single field - String invalid include
    Given I am on staging environment
    When  I request to see all of <Type>
    And I filter by <Field>
    And I include the <Include>
    Then I get a status code of <Expected Code>
    And I see the Error title is <Er-message>

    Examples: Request Criterion
      | Type       | Field                                  | Include  | Expected Code | Er-message        |
      | annotation | ?field[annotation]=type                | protocol |      400      | Invalid parameter |
      | annotation | ?field[annotation]=attributes.type_ns  | protocol |      400      | Invalid parameter |