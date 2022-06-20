import csv
import secrets
import json
from eth_account import Account
from web3 import Web3

# The amount of accounts you would like to create
NUMBER_OF_ACCOUNTS = 50 # Type the number of accounts you want

# The amount of tokens you would like to send per account
AMOUNT_OF_TOKENS = 0.001  # Type the number of tokens you want, where 1 = 1 Token that has 18 decimals = 1 BEP20 token

# The address of the token you would like to send to each address
TOKEN_ADDRESS = '' # Paste the BSC address of whatever token you want to send, in between the two quotation marks

# The address of the wallet sending tokens
YOUR_ADDRESS = '' # Paste your wallet's address in between the two quotation marks

# The private key of your account from which you are sending tokens
YOUR_KEY = '' # Paste your private key in between the two quotation marks

# The EIP20 Application Binary Interface
EIP20_ABI = json.loads('[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":true,"inputs":[{"internalType":"address","name":"_owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getOwner","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"}]')
# The BSC RPC url to use the Binance Smart Chain (BSC) Mainnet
# Change this url to 'https://data-seed-prebsc-1-s1.binance.org:8545' if you want to use the BSC Testnet
binance_url = 'https://bsc-dataseed.binance.org/' 
w3 = Web3(Web3.HTTPProvider(binance_url))
# Connect to the desired token's contract
token = w3.eth.contract(address=TOKEN_ADDRESS, abi=EIP20_ABI)
# Get your wallet's nonce 
nonce = w3.eth.get_transaction_count(YOUR_ADDRESS) 


# Create a new .csv file called "accounts.csv"
with open('accounts.csv', 'w') as file:
    # Initialize the header
    writer = csv.writer(file, delimiter=',')
    # Write the header row on the csv
    writer.writerow(['Address', 'Private Key'])
    # Write a row containing a randomly generated address and private key for the specified number of times
    for i in range(NUMBER_OF_ACCOUNTS):
        print('Sent transaction number ', i)
        # First we create an account with a secure key
        acc = Account.create(secrets.randbits(256))
        # Write a row containing the generated key + address
        writer.writerow([acc.address, acc.privateKey.hex()[2:]])
        # Create a transaction
        transaction = token.functions.transfer(
            acc.address, # The address to which we send tokens to
            w3.toWei(AMOUNT_OF_TOKENS, 'ether'), # The amount of tokens being sent 1 = 1 Token that has 18 decimals = 1 BNB
        ).buildTransaction({
            'chainId': 56,  # If you change this to 97 it sets it to the Testnet. 56 is the Mainnet.
            'gas' : 2000000,
            'gasPrice' : 10000000000, 
            'nonce': nonce,
        })
        # Send tokens from your account to the newly generated address
        signed = w3.eth.account.signTransaction(transaction, YOUR_KEY)
        w3.eth.send_raw_transaction(signed.rawTransaction)
        nonce += 1