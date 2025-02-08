from flask import Blueprint, jsonify, request
from .blockchain import web3, edu_token, edu_certificate, scholarship

routes = Blueprint("routes", __name__)

@routes.route("/balance/<address>", methods=["GET"])
def get_balance(address):
    """ Get EduToken balance of an address """
    balance = edu_token.functions.balanceOf(web3.to_checksum_address(address)).call()
    return jsonify({"balance": balance})

@routes.route("/mint-token", methods=["POST"])
def mint_token():
    """ Mint EduTokens to an address """
    data = request.json
    address = web3.to_checksum_address(data["address"])
    amount = int(data["amount"])

    txn = edu_token.functions.mint(address, amount).transact({"from": web3.eth.accounts[0]})
    web3.eth.wait_for_transaction_receipt(txn)

    return jsonify({"message": f"Minted {amount} EduTokens to {address}", "txn": txn.hex()})

@routes.route("/mint-certificate", methods=["POST"])
def mint_certificate():
    """ Mint an education certificate NFT """
    data = request.json
    recipient = web3.to_checksum_address(data["recipient"])

    txn = edu_certificate.functions.safeMint(recipient).transact({"from": web3.eth.accounts[0]})
    web3.eth.wait_for_transaction_receipt(txn)

    return jsonify({"message": f"Certificate minted for {recipient}", "txn": txn.hex()})
