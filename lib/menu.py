class Menu:
    def __init__(self):
        self._all_items = {
            "Margherita": 7.99, 
            "Pepperoni": 9.99, 
            "Funghi": 8.99, 
            "Veggie": 8.49
        }

    def view_menu(self):
        return self._all_items
