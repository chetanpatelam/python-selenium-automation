# Created by Svetlana at 4/4/19
Feature: Test Scenarios to verify Amazon Cart

  Scenario: User can confirm that the cart is empty
    Given Open Amazon Home page
    When Press on Cart icon
    Then Confirm that the cart is empty
