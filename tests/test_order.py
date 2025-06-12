from unittest.mock import Mock
from lib.order import Order

def test_order_is_initially_empty_dict():
    menu = Mock()
    order = Order(menu)
    assert order._order_items == {}

def test_order_mock_menu_returns_same_menu():
    pizza_menu = Mock()
    pizza_menu._all_items = {
        "Margherita": 7.99, 
        "Pepperoni": 9.99, 
        "Funghi": 8.99, 
        "Veggie": 8.49
    }
    order = Order(pizza_menu)
    assert order._menu._all_items == {
        "Margherita": 7.99, 
        "Pepperoni": 9.99, 
        "Funghi": 8.99, 
        "Veggie": 8.49
    }

def test_add_method_adds_multiple_mock_menu_items_to_order():
    pizza_menu = Mock()
    pizza_menu._all_items = {
        "Margherita": 7.99, 
        "Pepperoni": 9.99, 
        "Funghi": 8.99, 
        "Veggie": 8.49
    }
    order = Order(pizza_menu)
    order.add_to_order("Veggie", 1)
    order.add_to_order("Margherita", 2)
    assert order._order_items == {
        "Veggie": {"price": 8.49, "quantity": 1},
        "Margherita": {"price": 7.99, "quantity": 2}
    }

def test_mock_view_order_method_returns_order_items():
    pizza_menu = Mock()
    pizza_menu._all_items = {
        "Margherita": 7.99, 
        "Pepperoni": 9.99, 
        "Funghi": 8.99, 
        "Veggie": 8.49
    }
    order = Order(pizza_menu)
    order.add_to_order("Veggie", 3)
    assert order.view_order() == {
        "Veggie": {"price": 8.49, "quantity": 3}
    }

def test_calculate_total_cost_correctly_from_mock_menu():
    pizza_menu = Mock()
    pizza_menu._all_items = {
        "Margherita": 7.99, 
        "Pepperoni": 9.99, 
        "Funghi": 8.99, 
        "Veggie": 8.49
    }
    order = Order(pizza_menu)
    order.add_to_order("Veggie", 1)
    order.add_to_order("Margherita", 2)
    assert order.calculate_total() == 24.47

def test_order_appended_to_customer_orders_when_completed():
    pizza_menu = Mock()
    pizza_menu._all_items = {
        "Margherita": 7.99, 
        "Pepperoni": 9.99, 
        "Funghi": 8.99, 
        "Veggie": 8.49
    }
    customer = Mock()
    customer._order_history = []
    order = Order(pizza_menu)
    order.add_to_order("Margherita", 2)
    order.complete_order(customer)
    assert customer._order_history == [order]
