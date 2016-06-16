# Created by colinmoore-hill at 06/06/2016
@API_BASIC_PRODUCTION @MATCH-RULE_PROD
Feature: Verify the MATCH_RULE - US & Diabetes
    To verify the the MATCH_RULE directs all US & Diabetes queries to 'MATCH'
    and the rest of the queries to 'CLASSIC'.

  @API_MATCH-RULE_basic_PROD
  Scenario: API MATCH-RULE call - Trial
    Given I am on production environment
    When  I post request a "US Diabetes" Trial
    Then I get a status code of 200
    And I am directed to "match"

  @API_MATCH-RULE_nonUS_PROD
  Scenario: API MATCH-RULE call - Trial
    Given I am on production environment
    When  I post request a "non-US Diabetes" Trial
    Then I get a status code of 200
    And I am directed to "classic"

  @API_MATCH-RULE_nonDiabetes_PROD
  Scenario: API MATCH-RULE call - Trial
    Given I am on production environment
    When  I post request a "US non-Diabetes" Trial
    Then I get a status code of 200
    And I am directed to "classic"

  @API_MATCH-RULE_nonUS_nonDiabetes_PROD
  Scenario: API MATCH-RULE call - Trial
    Given I am on production environment
    When  I post request a "non-US non-Diabetes" Trial
    Then I get a status code of 200
    And I am directed to "classic"
