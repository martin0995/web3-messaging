import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from blockchain.wallet import get_balance
from twilio.rest import Client
from config.settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_WHATSAPP_NUMBER

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_whatsapp_message(to, body):
    message = client.messages.create(
        from_=TWILIO_WHATSAPP_NUMBER,
        body=body,
        to=to
    )
    return message.sid

def handle_balance_request(address):
    try:
        balance = get_balance(address)
        return f"The balance of {address} is {balance} ETH."
    except ValueError as e:
        return f"Invalid Ethereum address: {address}. Please provide a valid address OR type 'exit' to cancel."

def send_interactive_message(body):
    if body == '1':
        return "Please enter your Ethereum address to check the balance."
    elif body == '2':
        return "Please enter the recipient's Ethereum address and the amount to transfer."
    else:
        return "Hi! please select the option you want to perform:\n1. Check balance\n2. Transfer funds\n"
