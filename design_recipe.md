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
        # Creates a list of Meal instances
        pass # No code here yet

    def view_menu(self):
        # no parameters
        # Returns:
        #   list of meals on the menu
        # no side-effects:
        pass # No code here yet


class Meal:
    # User-facing properties:
    #   name: string
    #   price: float

    def __init__(self, name, price):
        # Parameters:
        #   name: string
        #   price: float
        # Side-effects:
        #   Sets the title and artist properties
        pass # No code here yet

    def format(self):
        # Returns:
        #   A string of the form "TITLE by ARTIST"
        pass # No code here yet

```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE

"""
Given a library
When we add two tracks
We see those tracks reflected in the tracks list
"""
library = MusicLibrary()
track_1 = Track("Carte Blanche", "Veracocha")
track_2 = Track("Synaesthesia", "The Thrillseekers")
library.add(track_1)
library.add(track_2)
library.tracks # => [track_1, track_2]
```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE

"""
Given a track with a title and an artist
We see the title reflected in the title property
"""
track = Track("Carte Blanche", "Veracocha")
track.title # => "Carte Blanche"
```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
