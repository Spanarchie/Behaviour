# Created by colinmoore-hill at 06/06/2016
@MATCH-RULE
Feature: Verify the MATCH_RULE - US & Diabetes
    To verify the the MATCH_RULE directs all US & Diabetes queries to 'MATCH'
    and the rest of the queries to 'CLASSIC'.

  @API_MATCH-RULE_basic
  Scenario: API MATCH-RULE call - Trial
    Given I am on staging environment
    When  I post request a "US Diabetes" Trial
    Then I get a status code of 200
    And I am directed to "match"

  @API_MATCH-RULE_nonUS
  Scenario: API MATCH-RULE call - Trial
    Given I am on staging environment
    When  I post request a "non-US Diabetes" Trial
    Then I get a status code of 200
    And I am directed to "classic"

  @API_MATCH-RULE_nonDiabetes
  Scenario: API MATCH-RULE call - Trial
    Given I am on staging environment
    When  I post request a "US non-Diabetes" Trial
    Then I get a status code of 200
    And I am directed to "classic"

  @API_MATCH-RULE_nonUS_nonDiabetes
  Scenario: API MATCH-RULE call - Trial
    Given I am on staging environment
    When  I post request a "non-US non-Diabetes" Trial
    Then I get a status code of 200
    And I am directed to "classic"
