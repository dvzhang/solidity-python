from scripts.helpful_scripts import get_account, get_contract
from brownie import GLDToken


def deploy():
    account = get_account()
    NFT = GLDToken.deploy(
        get_contract("eth_usd_price_feed").address,
        {"from": account}
    )
    print("Deployed")
    return NFT


def main():
    deploy()
    