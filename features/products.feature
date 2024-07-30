# features/products.feature

Feature: Product management
  As a Product manager
  I need a RESTful catalog service
  So that I can keep track of my products

  Scenario: Create a Product
    Given the following products
      | name    | description | price | available | category |
      | Product1 | Desc1       | 10.0  | True      | TOYS     |
    When I visit the "home page"
    And I set the "name" field to "Product1"
    And I set the "description" field to "Desc1"
    And I set the "price" field to "10.0"
    And I set the "available" field to "True"
    And I set the "category" field to "TOYS"
    And I press the "Create" button
    Then I should see "Success"

  Scenario: Read a Product
    Given the following products
      | name    | description | price | available | category |
      | Product1 | Desc1       | 10.0  | True      | TOYS     |
    When I visit the "home page"
    And I set the "product id" field to "1"
    And I press the "Retrieve" button
    Then I should see "Product1"

  Scenario: Update a Product
    Given the following products
      | name    | description | price | available | category |
      | Product1 | Desc1       | 10.0  | True      | TOYS     |
    When I visit the "home page"
    And I set the "product id" field to "1"
    And I set the "name" field to "UpdatedProduct"
    And I press the "Update" button
    Then I should see "Success"

  Scenario: Delete a Product
    Given the following products
      | name    | description | price | available | category |
      | Product1 | Desc1       | 10.0  | True      | TOYS     |
    When I visit the "home page"
    And I set the "product id" field to "1"
    And I press the "Delete" button
    Then I should see "Success"

  Scenario: List All Products
    Given the following products
      | name    | description | price | available | category |
      | Product1 | Desc1       | 10.0  | True      | TOYS     |
      | Product2 | Desc2       | 20.0  | False     | FOOD     |
    When I visit the "home page"
    And I press the "List" button
    Then I should see "Product1"
    And I should see "Product2"

  Scenario: Search by Name
    Given the following products
      | name    | description | price | available | category |
      | Product1 | Desc1       | 10.0  | True      | TOYS     |
    When I visit the "home page"
    And I set the "name" field to "Product1"
    And I press the "Search" button
    Then I should see "Product1"

  Scenario: Search by Category
    Given the following products
      | name    | description | price | available | category |
      | Product1 | Desc1       | 10.0  | True      | TOYS     |
      | Product2 | Desc2       | 20.0  | False     | FOOD     |
    When I visit the "home page"
    And I set the "category" field to "TOYS"
    And I press the "Search" button
    Then I should see "Product1"
    And I should not see "Product2"

  Scenario: Search by Availability
    Given the following products
      | name    | description | price | available | category |
      | Product1 | Desc1       | 10.0  | True      | TOYS     |
      | Product2 | Desc2       | 20.0  | False     | FOOD     |
    When I visit the "home page"
    And I set the "available" field to "True"
    And I press the "Search" button
    Then I should see "Product1"
    And I should not see "Product2"
