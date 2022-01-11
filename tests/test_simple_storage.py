from brownie import accounts, SimpleStorage


def test_deploy():
    # arrange
    account = accounts[0]
    # act
    simple_storage = SimpleStorage.deploy({'from': account})
    starting_value = simple_storage.retrieve()
    expected = 0
    # assert
    assert starting_value == expected

def test_updating_storage():
    # arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({'from': account})
    # act
    expected = 15
    simple_storage.store(expected, {'from': account})
    retrieved = simple_storage.retrieve()
    # assert
    assert expected == retrieved

