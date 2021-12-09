# Created by Svetlana at 4/4/19
Feature: Test Scenarios for Search functionality in Help

  Scenario: User can search for Cancel Orders in Help
    Given Open Amazon Help page
    When Input Cancel Orders into help search field
    And Click on search button
    Then Confirm for Cancel Orders are shown
