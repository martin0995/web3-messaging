from flask import Flask, request, abort
from twilio.twiml.messaging_response import MessagingResponse
from twilio.request_validator import RequestValidator
from handlers import handle_balance_request, send_whatsapp_message, send_interactive_message
from twilio.rest import Client
from os import environ
import logging

TWILIO_ACCOUNT_SID = environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = environ.get('TWILIO_AUTH_TOKEN')
TWILIO_WHATSAPP_NUMBER = environ.get('TWILIO_WHATSAPP_NUMBER')
WEB3_PROVIDER_URL = environ.get('WEB3_PROVIDER_URL')
TEST_PHONE_NUMBER = environ.get('TEST_PHONE_NUMBER')

app = Flask(__name__)
app.config['SECRET_KEY'] = '' # Replace with your own secret key
app.config['WTF_CSRF_ENABLED'] = False
app.config['SERVER_NAME'] = '' # Replace with your ngrok URL

validator = RequestValidator(TWILIO_AUTH_TOKEN)

# Initialize Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Store user state (not scalable for production)
user_state = {}

@app.route('/')
def index():
    return 'Welcome to the Web3 WhatsApp Bot. Go to /test to send a test message.'

@app.route('/webhook', methods=['POST'])
def webhook():    
    incoming_msg = request.values.get('Body', '').lower()
    user_number = request.values.get('From')
    logging.debug(f"Incoming message: {incoming_msg}")
    response = MessagingResponse()
    msg = response.message()
    responded = False

    if user_number in user_state:
        state = user_state[user_number]
        if state == 'waiting_for_balance':
            if "exit" in incoming_msg:
                msg.body("Thank you for using the Web3 WhatsApp Bot. Goodbye!")
                user_state.pop(user_number)  # Clear state after handling
            else:
                balance_message = handle_balance_request(incoming_msg)
                if "Invalid Ethereum address" in balance_message:
                    send_whatsapp_message(user_number, balance_message)
                else:
                    send_whatsapp_message(user_number, balance_message)
                    user_state.pop(user_number)  # Clear state only if valid response
            responded = True
        elif state == 'waiting_for_transfer':
            msg.body("Transfer feature is under construction.")
            user_state.pop(user_number)  # Clear state after handling
            responded = True
    else:
        if '1' in incoming_msg:
            user_state[user_number] = 'waiting_for_balance'
            response_msg = send_interactive_message('1')
            send_whatsapp_message(user_number, response_msg)
            responded = True
        elif '2' in incoming_msg:
            user_state[user_number] = 'waiting_for_transfer'
            response_msg = send_interactive_message('2')
            send_whatsapp_message(user_number, response_msg)
            msg.body("Please enter the recipient's Ethereum address and the amount to transfer.")
            responded = True
        else:
            response_msg = send_interactive_message(incoming_msg)
            send_whatsapp_message(user_number, response_msg)
            responded = True

    if not responded:
        msg.body("I can help you with your wallet balance and transactions. Please send 'balance <your_ethereum_address>' to get the balance.")

    return str(response)

@app.route('/test', methods=['GET'])
def test():
    to = TEST_PHONE_NUMBER  # Replace with your phone number
    body = 'This is a test message from your WhatsApp bot!'
    message_sid = send_whatsapp_message(to, body)
    return f"Message sent with SID: {message_sid}"

if __name__ == '__main__':
    # app.run()
    app.run(host='localhost', port=5002, debug=True)
