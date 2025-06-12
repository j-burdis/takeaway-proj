from lib.menu import Menu
from lib.customer import Customer
from lib.order import Order

def test_order_menu_returns_same_menu():
    pizza_menu = Menu()
    order = Order(pizza_menu)
    assert order._menu._all_items == {
        "Margherita": 7.99, 
        "Pepperoni": 9.99, 
        "Funghi": 8.99, 
        "Veggie": 8.49
    }

def test_add_method_adds_menu_item_to_order():
    pizza_menu = Menu()
    order = Order(pizza_menu)
    order.add_to_order("Veggie", 1)
    assert order._order_items == {
        "Veggie": {"price": 8.49, "quantity": 1}
    }

def test_add_method_adds_multiple_items_to_order():
    pizza_menu = Menu()
    order = Order(pizza_menu)
    order.add_to_order("Veggie", 1)
    order.add_to_order("Margherita", 2)
    assert order._order_items == {
        "Veggie": {"price": 8.49, "quantity": 1},
        "Margherita": {"price": 7.99, "quantity": 2}
    }

def test_view_order_method_returns_order_items():
    pizza_menu = Menu()
    order = Order(pizza_menu)
    order.add_to_order("Veggie", 3)
    assert order.view_order() == {
        "Veggie": {"price": 8.49, "quantity": 3}
    }

def test_calculate_total_cost_correctly():
    pizza_menu = Menu()
    order = Order(pizza_menu)
    order.add_to_order("Veggie", 1)
    order.add_to_order("Margherita", 2)
    assert order.calculate_total() == 24.47

def test_order_appended_to_customer_orders_when_completed():
    pizza_menu = Menu()
    customer = Customer()
    order = Order(pizza_menu)
    order.add_to_order("Margherita", 2)
    order.complete_order(customer)
    assert customer._order_history == [order]
