from lib.customer import Customer

def test_customer_has_empty_order_history():
    customer = Customer()
    assert customer.display_orders() == []
