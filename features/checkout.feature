Feature: Checkout
  As a user
  In order to purchase products
  I should be presented an option to checkout after adding products to cart

  Scenario Outline:
    Given I have added <product> to cart
    When I choose to checkout
    Then I should be provided the option to checkout with my purchase

    Examples:
      | product     |
      | Capping Kit |