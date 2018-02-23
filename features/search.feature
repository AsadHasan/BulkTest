Feature: Search for products
  In order to find relevant products
  As a user
  I want to be able to search for products and apply required filters

  Background:
    Given I am on the homepage

  Scenario Outline: Search for products and filter results
    When I search for <products>
    And apply <filter> on the results
    Then only products with filter <label> are shown

    Examples:
      | products      | filter |
      | multivitamins | vegan  |

