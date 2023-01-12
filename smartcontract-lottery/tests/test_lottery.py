# # 50/1333.44 = 0.0374970002399808
# from scripts.helpful_scripts import (
#     get_account,
#     # fund_with_link,
#     # get_contract,
#     # LOCAL_BLOCKCHAIN_ENVIRONMENTS,
# )
# from brownie import Lottery, config, exceptions, network
# from web3 import Web3
# import pytest


# def test_get_entrance_fee():
#     account = get_account()
#     lottery = Lottery.deploy(
#         config["networks"][network.show_active()]["eth_usd_price_feed"],
#         {"from": account}
#     )

#     assert lottery.getEntranceFee() > Web3.toWei(0.035, "ether")
#     assert lottery.getEntranceFee() < Web3.toWei(0.039, "ether")
