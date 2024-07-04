from web3 import Web3
from os import environ
from config.settings import WEB3_PROVIDER_URL

# Connect to a blockchain node (Infura, local node, etc.)
web3 = Web3(Web3.HTTPProvider(WEB3_PROVIDER_URL))

def get_balance(address):
    checksum_address = web3.to_checksum_address(address)
    balance = web3.eth.get_balance(checksum_address)
    return web3.from_wei(balance, 'ether')
