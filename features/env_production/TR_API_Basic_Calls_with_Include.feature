# Created by colinmoore-hill at 06/05/2016
@API_BASIC_PRODUCTION
Feature: Verify the basic api call
    To verify the basic api to collect all Trials, Protocols and Annotations

  Scenario: API basic Trial call - with BOTH  Protocols and Annotations
    Given I am on production environment
    When  I request to see all Trials
    And I Include protocols and annotations
    Then I get a status code of 200

 Scenario: API basic Trial call - with Protocols
    Given I am on production environment
    When  I request to see all Trials
    And I Include protocols
    Then I get a status code of 200

   Scenario: API basic Trial call - with Annotations
    Given I am on production environment
    When  I request to see all Trials
    And I Include annotations
    Then I get a status code of 200

   Scenario: API basic Protocol call -  with trials
    Given I am on production environment
    When  I request to see all Protocol
    And I Include trials
    Then I get a status code of 200

  Scenario: API basic Annotation call - with Trials
    Given I am on production environment
    When  I request to see all Annotation
    And I Include trials
    Then I get a status code of 200




   Scenario: API basic Protocol call - with Annotations And Trials(INVALID)
    Given I am on production environment
    When  I request to see all Protocol
    And I Include annotations
    Then I get a status code of 400
    And I see the Error title is "Invalid parameter"

  Scenario: API basic Protocol call - with Annotations(INVALID)
    Given I am on production environment
    When  I request to see all Protocol
    And I Include annotations
    Then I get a status code of 400
    And I see the Error title is "Invalid parameter"

  Scenario: API basic Annotation call - BOTH  Protocols and Trials(INVALID)
    Given I am on production environment
    When  I request to see all Annotation
    And I Include protocols and trials
    Then I get a status code of 400
    And I see the Error title is "Invalid parameter"

  Scenario: API basic Annotation call - with Protocols(INVALID)
    Given I am on production environment
    When  I request to see all Annotation
    And I Include protocols
    Then I get a status code of 400
    And I see the Error title is "Invalid parameter"

