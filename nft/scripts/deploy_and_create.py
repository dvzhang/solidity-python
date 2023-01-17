from brownie import SimpleCollectible
from scripts.helpful_scripts import OPENSEA_FORMAT, get_account

sample_token_uri = "ipfs://Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"


def main():
    account = get_account()
    simple_collectible = SimpleCollectible.deploy({"from": account})
    tx = simple_collectible.createCollectible(
        sample_token_uri, {"from": account})
    tx.wait(1)
    print(
        f"You can view your NFT at {OPENSEA_FORMAT.format(simple_collectible.address, simple_collectible.tokenCounter()-1)}")
