# Ethereum Wallet/Private Key/Address Generator
This script generates a .csv file called *accounts.csv* containing a given number of ECDSA private keys and their associated Ethereum addresses. The private keys are generated using a cryptographically-secure pseudo random generator. Simultaneously, a given wallet address also sends a given amount of tokens to each generated new address.

## How to use this generator
In order to use it, there are three steps. Firstly, download this repository. 

Second, open the generator.py file and at the top of the file you will find five variables which require you to enter the number of accounts (NUMBER_OF_ACCOUNTS) you wish to create, the number of tokens (AMOUNT_OF_TOKENS) (for a 18-decimal token) that you wish to send per account, your token's address (TOKEN_ADDRESS), your wallet's address (YOUR_ADDRESS) and your private key (YOUR_KEY). 

Once you have filled these five strings of information, you must open terminal, navigate to this folder and install dependencies:
```
pip install -r requirements.txt
```
Then simply open your terminal,  containing generator.py and type the command:
```
python generator.py
```

# How to only create accounts and not send tokens
You can turn off the token sending feature by setting SEND_TOKENS to False.