from django.conf import settings
from web3 import Web3

def print_default_account():
    # Connect to Ethereum node
    w3 = Web3(Web3.HTTPProvider(settings.ETH_NODE_URL))

    # Derive sender address from private key for debugging
    account = w3.eth.account.from_key(settings.PRIVATE_KEY)
    sender_address = account.address
    print(f"Sender Address: {sender_address}")

    # Get the default account from settings
    default_account = settings.DEFAULT_ACCOUNT  # Ensure you set this in your settings
    print(f"Default account: {default_account}")  # Print the default account

# Call the function to see the output
print_default_account()