from brownie import config, network, interface
from scripts.helpful_scripts import get_account


def get_weth(gas_strategy):
    """
    Mints WETH by depositing ETH
    """
    # ABI
    # Address
    account = get_account()
    weth = interface.IWeth(config["networks"][network.show_active()]["weth_token"])
    tx = weth.deposit({"from": account, "value": 0.1 * 10 ** 18, "gas_price": gas_strategy})
    tx.wait(1)
    print("Received 0.1 WETH")


def main():
    get_weth()
