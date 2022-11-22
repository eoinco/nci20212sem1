# we're going to do some deterministic wallet stuff here

# requirements
# pip install hdwallet
# https://github.com/meherett/python-hdwallet
from hdwallet import BIP44HDWallet
from hdwallet.cryptocurrencies import EthereumMainnet
from hdwallet.derivations import BIP44Derivation
from hdwallet.utils import generate_mnemonic
from typing import Optional
from decouple import config

def getPrivateKey(accountNumber):
    mnemonic = config('SEED_PHRASE')
    myWallet: BIP44HDWallet = BIP44HDWallet(cryptocurrency=EthereumMainnet)
    myWallet.from_mnemonic(
        mnemonic=mnemonic, language="english", passphrase=""
    )
    
    myWallet.clean_derivation()
    path = "m/44'/60'/0'/0/" + str(accountNumber)
    # path = "m/44'/60'/0'/0/1" Account 2 in metamask
    myWallet.from_path(path=path)

    print("wallet address = " + myWallet.address())
    print("private key:  " + myWallet.private_key())
    pk = myWallet.private_key()
    myWallet.clean_derivation()
    return pk

# wallet address should be 0xa52e2884F0E8cd3f74A141087bFc05505aF8CB30

#  account 2 is 0xac4FafdA6A3A6B48b4cDC2a896acf8D104C81d6C



