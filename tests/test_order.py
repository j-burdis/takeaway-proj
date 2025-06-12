from unittest.mock import Mock
from lib.order import Order

def test_order_is_initially_empty_dict():
    menu = Mock()
    order = Order(menu)
    assert order._order_items == {}
