# Created by colinmoore-hill at 14/06/2016
@API_BASIC_PRODUCTION @CONCEPT-SUGGESTION_PROD
Feature: Verify the MATCH_RULE - US & Diabetes
    To verify the the MATCH_RULE directs all US & Diabetes queries to 'MATCH'
    and the rest of the queries to 'CLASSIC'.

    @API_CONCEPT-SUGGESTION_basic_PROD
    Scenario: API CONCEPT-SUGGESTION call -
      Given I am on production environment
      When I request a condishion "imperforate"
      Then I get a status code of 200
      And I am returned 4 options


    @API_CONCEPT-SUGGESTION_5_Max_PROD
    Scenario: API CONCEPT-SUGGESTION call - Max 5 returned for common term (i.e. cancer)
      Given I am on production environment
      When I request a condishion "cancer"
      Then I get a status code of 200
      And I am returned 5 options


    @API_CONCEPT-SUGGESTION_ERR-No_condishion_value_PROD
    Scenario: API CONCEPT-SUGGESTION call -Error - no condishion value supplied
      Given I am on production environment
      When I request a condishion ""
      Then I get a status code of 400

    @API_CONCEPT-SUGGESTION_ERR-No_condishion_added_PROD
    Scenario: API CONCEPT-SUGGESTION call -Error - no condishion added
      Given I am on production environment
      When I request a condishion just the endpoint
      Then I get a status code of 400