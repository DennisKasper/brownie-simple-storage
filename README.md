# Simple Storage - Smart Contract Example

Playing around with [Smart Contracts](https://ethereum.org/en/developers/docs/smart-contracts/) on the [Ethereum Blockchain](https://ethereum.org/en/) with the help of [Brownie](https://eth-brownie.readthedocs.io/en/stable/toctree.html) framework.

This projects follows the free tutorial [Solidity, Blockchain, and Smart Contract Course – Beginner to Expert Python Tutorial](https://www.youtube.com/watch?v=M576WGiDBdQ&t=16200s) (starting from 4:30:00) from freeCodeCamp.org.

It mainly serves as private notes.

## Prerequisites

- [MetaMask](https://metamask.io/)
- [Infura](https://infura.io/)
- [Ganache](https://trufflesuite.com/ganache/)

## Setup Local Development Environment

Manjaro Linux 21.2.1, Python 3.10.1, Node.js 17.3.0.

Clone the repository and set the environment variables in .env.

```bash
git clone https://github.com/DennisKasper/brownie-simple-storage.git
cd brownie-simple-storage
cp .env.dev .env
```

### Setup with virtualenv

Setup a virtual environment and pip install `eth-brownie`

```bash
python -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip wheel setuptools
pip install eth-brownie
```

Test the installation with

```bash
$ brownie --version
Brownie v1.16.4 - Python development framework for Ethereum
```

In case of `ImportError: .../site-packages/cytoolz/functoolz.cpython-310-x86_64-linux-gnu.so: undefined symbol: _PyGen_Send` update the cytoolz package

```bash
pip install --upgrade cytoolz
```

### Setup with pipx

Refer to the [help](https://eth-brownie.readthedocs.io/en/stable/install.html) for installation.

## Resources/Links

- [smartcontractkit/chainlink-brownie-contracts](https://github.com/smartcontractkit/chainlink-brownie-contracts)