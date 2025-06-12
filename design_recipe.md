# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

As a customer
So that I can check if I want to order something
I would like to see a list of dishes with prices.

As a customer
So that I can order the meal I want
I would like to be able to select some number of several available dishes.

As a customer
So that I can verify that my order is correct
I would like to see an itemised receipt with a grand total.

<!-- Use the twilio-python package to implement, with Mocks -->
As a customer
So that I am reassured that my order will be delivered on time
I would like to receive a text such as "Thank you! Your order was placed and will be delivered before 18:52" after I have ordered.

## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
                ┌─────────────┐    ┌───────────────────┐    
                │  Menu       │    │  Customer         │    
                │  - meals    │    │  - orders         │    
Nouns           │             │    │                   │    
meal            └───┬─────────┘    └────┬──────────────┘    
price               │ has a             │ has a list        
order               │ list of           ▼ of orders         
receipt             │ meals        ┌───────────────────┐    
total               ▼              │  Order            │    
                ┌─────────────┐    │  - order-items    │    
Verbs           │  Meal       │    │  - total-cost     │    
order           │  - name     │    └────┬──────────────┘    
select          │  - price    │         │ has a list of     
see list        │             │         ▼ order items       
see receipt     └─────────────┘    ┌───────────────────┐    
                                   │  Order item       │    
                                   │  - name           │    
                                   │  - price          │    
                                   │  - quantity       │    
                                   │                   │    
                                   │  - takes menu as  │    
                                   │    a parameter?   │    
                                   │                   │    
                                   └───────────────────┘    
```

_Also design the interface of each class in more detail._

```python
class Menu:
    # User-facing properties:
    #   meals: list of instances of Meal

    def __init__(self):
        # No parameters
        # Creates a dictionary of meals and prices
        # names as keys, prices as values
        pass # No code here yet

    def view_menu(self):
        # no parameters
        # Returns:
        #   dictionary of meals on the menu
        # no side-effects
        pass # No code here yet

class Customer:
    # user facing properties:
    #   order history (orders): list of order instances

    def __init__(self):
        # side effects:
        #   creates an empty list which will be 
        #   populated by the customer's orders
        pass

    def display_orders(self)
        # returns:
        #   the list of order instances for this customer

class Order:
    def __init__(self):
        #   menu as a parameter?
        # side effects:
        #   creates an empty dictionary 
        #   where order items can be added
        pass

    def calculate_total(self):
        # returns:
        #   float: total cost of the items 
        #           in the order dictionary
        pass

    def add_to_order(self, name, quantity)
        # params:
        #   name: string of item from the menu
        #   quantity: integer
        # side effects: appends item to the order dictionary 
        #               so it has name, price and quantity
        pass

    def view_order(self)
        # returns:
        #   dictionary of items in the current 
        #   order with names, prices and 
        #   quantities as well as a grand total
        pass

    def complete_order(self):
        # side effects:
        #   appends order to order list of customer
        #   clears the order of all items - necessary?
        #   triggers order_confirmation() method
        pass

    def order_confirmation(self):
        # returns:
        #   confirmation message with delivery time
        pass
```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE
"""
Given an item is added to an order
We can check that the add method works
"""
order = Order()
order.add_to_order("Pizza", 2)
order.order_items # => {"Pizza": {"price": 9.99, "quantity": 2}

"""
Given an item is added to an order
We can see this item added to the order dictionary
"""
order = Order()
order.add_to_order("Pizza", 2)
order.view_order() # => {"Pizza": {"price": 9.99, "quantity": 2}

"""
Given an order contains menu items
I can calculate the total order cost
"""
order = Order()
order.add_to_order("Pizza", 2)
order.calculate_total() # => 19.98

"""
Given an order is completed
It is appended to the list of orders for that customer
"""
customer = Customer()
order = Order()
order.add_to_order("Pizza", 2)
order.complete_order()
customer.orders.append(order)
customer.display_orders() # => [order]

"""
Given an order is completed
I recieve a confirmation text with the delivery time
"""
customer = Customer()
order = Order()
order.add_to_order("Pizza", 2)
order.complete_order() # receives text from twilio

```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE

"""
Given a menu
I can return the list of names 
and prices of all the items
"""
menu = Menu()
menu.view_menu() # => {dict of all items}

"""
Given a customer
Initially an empty list of orders is returned
"""
customer = Customer()
customer.display_orders() # => []

"""
Given an order is created
Initially it returns an empty dictionary
"""
order = Order()
order.order_items # => {}
```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
