class Order:
    def __init__(self, menu):
        self._order_items = {}
        self._menu = menu

    def add_to_order(self, item, quantity):
        item_details = {}
        item_details["price"] = self._menu._all_items[item]
        item_details["quantity"] = quantity
        self._order_items[item] = item_details

    def view_order(self):
        return self._order_items

    def calculate_total(self):
        return sum([
                  (item[1]["price"] * item[1]["quantity"]) 
                    for item in self._order_items.items()
                ])

    def complete_order(self, customer):
        self._order_items["total"] = self.calculate_total()
        customer._order_history.append(self)
        # customer.send_confirmation()