# blockchain.py
import json
from web3 import Web3
from flask import current_app
from config import Config

# Connect to the selected network (e.g., development, ropsten, mainnet)
network = "development"  # Change this to the desired network
network_config = Config.NETWORKS[network]

# Initialize Web3
web3 = Web3(Web3.HTTPProvider(network_config["url"]))

# Ensure connection
if web3.is_connected():
    print(f"Connected to {network} network")
else:
    print(f"Failed to connect to {network} network")

# Load contract ABI and address
def load_contract(contract_name):
    path = f"./blockchain/build/{contract_name}.json"

    with open(path) as f:
        contract_json = json.load(f)

    address = network_config["contract_address"]  # Use the contract address from the config
    abi = contract_json["abi"]
    
    contract = web3.eth.contract(address=address, abi=abi)
    return contract

# Load contracts
edu_token = load_contract("EduToken")
edu_certificate = load_contract("EduCertificate")
scholarship = load_contract("Scholarship")
