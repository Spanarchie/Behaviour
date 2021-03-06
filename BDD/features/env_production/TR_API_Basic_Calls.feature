# Created by colinmoore-hill at 06/05/2016

@API_BASIC_PRODUCTION
Feature: Verify the basic api call
    To verify the basic api to collect all Trials, Protocols and Annotations

  @API_BASIC_TRIAL_PROD
  Scenario: API basic call - Trial
    Given I am on production environment
    When  I request to see all Trials
    Then I get a status code of 200

  @API_BASIC_PROTCOL_PROD
  Scenario: API basic call - Protocol
    Given I am on production environment
    When  I request to see all Protocol
    Then I get a status code of 200

  @API_BASIC_ANNOTATION_PROD
  Scenario: API basic call - Annotation
    Given I am on production environment
    When  I request to see all Annotation
    Then I get a status code of 200
