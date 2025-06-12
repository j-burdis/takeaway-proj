from unittest.mock import Mock
from lib.customer import Customer

def test_customer_has_empty_order_history():
    customer = Customer()
    assert customer.display_orders() == []

def test_customer_order_history_with_mock_order():
    customer = Customer()
    order = Mock()
    customer._order_history.append(order)
    assert customer.display_orders() == [order]