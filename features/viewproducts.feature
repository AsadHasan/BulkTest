Feature: View products
  In order to get information about products
  As a user
  I want to be able to view product details

  Scenario Outline:
    Given I am presented search results for <term>
    When I select a <product>
    Then I can view the product details

    Examples:
      | term   | product                   |
      | shaker | SHAKER BOTTLE BLACK 700ML |