from brownie import SimpleStorage


def read_contract():
    simple_storage = SimpleStorage[-1]  # most recent deployment
    print(simple_storage.retrieve())
    
def main():
    read_contract()


if __name__ == '__main__':
    main()