# Web3 WhatsApp Bot
This project is a WhatsApp bot that allows users to interact with their Ethereum wallets. The bot can check wallet balances and eventually handle transfers. It uses Flask for the web framework, Twilio for WhatsApp messaging, and web3.py for interacting with the Ethereum blockchain.

## Features
- Check Ethereum wallet balance.
- Interactive messaging with quick reply buttons.

## Prerequisites
- Python 3.6 or higher
- Twilio account
- ngrok
- Infura account (or another Ethereum node provider)

## Installation
1. Clone the repository:

```bash
git clone https://github.com/your-repo/web3-whatsapp-bot.git
cd web3-whatsapp-bot
```

2. Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Create a .env file:

```env
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886
WEB3_PROVIDER_URL=https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID
TEST_PHONE_NUMBER = your_test_phone_number
```

## Setup
### ngrok
1. Download and install ngrok:

```bash
brew install ngrok
```

2. Start ngrok on port 5002:

```bash
ngrok http 5002
```

### Twilio
1. Configure the Twilio Sandbox:
- Go to your Twilio console.
- Navigate to Programmable Messaging > Try it Out > WhatsApp Sandbox.
- Update the "WHEN A MESSAGE COMES IN" URL to your ngrok forwarding URL (e.g., https://5fa6-85-76-103-138.ngrok-free.app/webhook).

### Flask Application
1. Update `app.config` and `app.run`:

In your `bot.py` file, set the `SERVER_NAME` and update the `app.run` parameters:

```python
app.config['SERVER_NAME'] = '5fa6-85-76-103-138.ngrok-free.app'
app.run(host='localhost', port=5002, debug=True)
```

## Running the Bot
1. Start the Flask application:

```bash
python3 bot/bot.py
```

2. Test the bot:

- Send a WhatsApp message to your Twilio sandbox number.
- Use commands like balance <your_ethereum_address> to interact with the bot.

## Code Overview
### Directory Structure

```
web3_whatsapp_bot/
│
├── bot/
│   ├── __init__.py
│   ├── bot.py
│   └── handlers.py
│
├── blockchain/
│   ├── __init__.py
│   ├── wallet.py
│   └── transactions.py
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   └── secrets.py
│
├── tests/
│   ├── __init__.py
│   ├── test_bot.py
│   └── test_blockchain.py
│
├── main.py
├── requirements.txt
└── README.md
```

### `bot/bot.py`
The main Flask application file. Handles incoming WhatsApp messages and routes them to the appropriate handlers.

### `bot/handlers.py`
Contains functions to handle specific commands, such as checking the balance of an Ethereum address.

### `blockchain/wallet.py`
Contains functions to interact with the Ethereum blockchain using web3.py.

### `config/settings.py`
Loads environment variables and sets up configuration for the application.

## Example Usage
### Check Balance
1. Send a message to the bot:

```
Hi
```
2. The bot responds with an interactive menu to guide you through the options.

```
Hi! please select the option you want to perform:
1.⁠ ⁠Check balance
2.⁠ ⁠Transfer funds
```

3. Send desired option:

```
1
```

4. Bot will respond to selected option savind the history of your answers:

```
Please enter your Ethereum address to check the balance.
```

5. Provide X Ethreum address:

```
XX
```

6. Bot will respond accordingly:

```
The balance of XX is 315.104171236 ETH.
```

In case that the address does not exists:

```
Invalid Ethereum address: XX. Please provide a valid address OR type 'exit' to cancel.
```

## Troubleshooting
- Ensure ngrok is running and the forwarding URL is correctly configured in Twilio.
- Check the Flask logs for any error messages.
- Make sure all environment variables are correctly set in the .env file.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.
