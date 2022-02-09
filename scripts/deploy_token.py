from brownie import OurToken
from scripts.general_scripts import get_account

initial_supply = 10_000 * (10**18)

def main():
    account = get_account()
    our_token = OurToken.deploy(initial_supply, {'from': account})
    print(our_token.name())