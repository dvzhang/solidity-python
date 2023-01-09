from brownie import accounts, config, SimpleStorage


def read_contract():
    simple_storage = SimpleStorage[-1]
    # go take the index thats one less than the length
    # ABI
    # Address
    print(simple_storage.retrieve())


def main():
    read_contract()