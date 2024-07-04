from web3 import Web3
import logging
from config.settings import WEB3_PROVIDER_URL

logging.basicConfig(level=logging.DEBUG, format="|%(levelname)s| %(asctime)s - %(message)s")
web3 = Web3(Web3.HTTPProvider(WEB3_PROVIDER_URL))

def test_connection():
    if web3.is_connected():
        print("Connected to Ethereum network")
    else:
        print("Failed to connect to Ethereum network")

def get_balance(address):
    balance = web3.eth.get_balance(address)
    logging.info(f"Balance of {address}: {balance}")
    return web3.from_wei(balance, 'ether')

if __name__ == "__main__":
    test_connection()
    # Replace with an actual Ethereum address for testing
    address = "0xB9D7934878B5FB9610B3fE8A5e441e8fad7E293f"
    balance = get_balance(address)
    print(f"The balance of {address} is {balance} ETH")
