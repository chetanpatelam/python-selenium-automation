# Created by chait at 12/1/2021
Feature: Test scenarios for search functionality in Google
  # Enter feature description here

  Scenario: User can search for a product
    Given Open Google page
    When Input watch into search field
    And Click on search icon
    Then Product results for watch are shown