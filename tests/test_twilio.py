from lib.menu import Menu
from lib.customer import Customer
from lib.order import Order
import os
from twilio.rest import Client
from dotenv import load_dotenv, dotenv_values
load_dotenv()


account_sid = os.getenv("TWILIO_SID")
auth_token  = os.getenv("TWILIO_AUTH_TOKEN")

client = Client(account_sid, auth_token)

# message = client.messages.create(
#     to="+18777804236",
#     from_="+447956504846",
#     body="Hello from Python!")

# print(message.body)

# def test_confirmation_message_sent_when_order_places():
#     pizza_menu = Menu()
#     customer = Customer()
#     order = Order(pizza_menu)
#     order.add_to_order("Margherita", 2)
#     order.complete_order(customer)
#     assert order.send_confirmation() == "Thank you! Your order was placed and will be delivered before 18:52 after I have ordered."