import csv
import secrets
from eth_account import Account
import sys

with open('accounts.csv', 'w') as file:
    # Initialize the header
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(['Address', 'Private Key'])

    for i in range(int(sys.argv[1])):
        acc = Account.create(secrets.randbits(256))
        writer.writerow([acc.address, acc.privateKey.hex()[2:]])