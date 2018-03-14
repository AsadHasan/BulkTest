Feature: Add product to shopping cart
  As a user
  In order to purchase a product
  I should be able to add products to my shopping cart

  Scenario Outline:
    Given I select a <product>
    When I add it to shopping cart
    Then it is successfully added to the shopping cart

    Examples:
      | product                  |
      | Ultra Fine Scottish Oats |