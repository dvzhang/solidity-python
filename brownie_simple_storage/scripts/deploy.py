from brownie import accounts, config, SimpleStorage, network
import os

def get_account():
    if (network.show_active() == "development"):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_simple_storage():
    # account = accounts[0]
    # account = accounts.load('gorAccount')
    # account = accounts.add(os.getenv('PRIVATE_KEY'))
    # account = accounts.add(config["wallets"]["from_key"])
    account = get_account()

    simple_storage = SimpleStorage.deploy({"from":account})
    stored_value = simple_storage.retrieve()
    transaction = simple_storage.store(15, {"from":account})
    transaction.wait(1)
    stored_value = simple_storage.retrieve()

    print(stored_value)


def main():
    deploy_simple_storage()
