from lib.menu import Menu

def test_view_menu_when_class_initialised():
    menu = Menu()
    assert menu.view_menu() == {
        "Margherita": 7.99, 
        "Pepperoni": 9.99, 
        "Funghi": 8.99, 
        "Veggie": 8.49
    }
