from lib.order import Order

def test_order_is_initially_empty_dict():
    order = Order()
    assert order.order_items == {}
