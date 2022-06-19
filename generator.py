import csv
import secrets
from eth_account import Account
import sys

# Create a new .csv file called "accounts.csv"
with open('accounts.csv', 'w') as file:
    # Initialize the header
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(['Address', 'Private Key'])
    # Write a row containing a randomly generated address and private key for the specified number of times
    for i in range(int(sys.argv[1])):
        acc = Account.create(secrets.randbits(256))
        writer.writerow([acc.address, acc.privateKey.hex()[2:]])