import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("ewfghjyeufuyegfyueguyfgew6", "uyewghoijoi33iurg6781huk")
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:R!tv!k%4014@localhost:3306/eduverse_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    NETWORKS = {
        "development": {
            "url": "http://127.0.0.1:8545",  # Local network (e.g., Ganache)
            "network_id": 1337,  # Network ID for Ganache or custom network
            "contract_address": "0x4622C6282F974c5eeb94A90d615BafBe446C7E12",  # Deployed contract address
        },
        "ropsten": {
            "url": "https://ropsten.infura.io/v3/YOUR_INFURA_PROJECT_ID",  # Infura or other provider URL
            "network_id": 3,  # Ropsten testnet network ID
            "contract_address": "0xYourContractAddressHere",
        },
        "mainnet": {
            "url": "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID",  # Mainnet URL
            "network_id": 1,  # Mainnet network ID
            "contract_address": "0xYourContractAddressHere",
        }
    }


