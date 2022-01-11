from brownie import accounts, config, network, SimpleStorage


def deploy_simple_storage():
    account = get_Account()   # use local accounts
    #account = accounts.load('my-account')   # load account created with brownie accounts create my-account (password encrypted)
    #account = accounts.add(config['wallets']['from_key'])  # get account from e.g. metamask private key set in config and .env file
    simple_storage = SimpleStorage.deploy({'from': account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {'from': account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)

def get_Account():
    if network.show_active() == 'development': return accounts[0]
    return accounts.add(config['wallets']['from_key'])

def main():
    deploy_simple_storage()


if __name__ == '__main__':
    main()