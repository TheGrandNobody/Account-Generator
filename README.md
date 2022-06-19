# Ethereum Wallet Generator
This script generates a .csv file called *accounts.csv* containing a given number of ECDSA private keys and their associated Ethereum addresses. The private keys are generated using a cryptographically-secure pseudo random generator. 

## How to use this generator
In order to use it, you simply need to open your terminal, navigate to the folder containing the script and run the script with the number of accounts you wish to create as an argument. For example, an individual wanting to generate 10 accounts would type this in their terminal:
```
python generator.py 10
```