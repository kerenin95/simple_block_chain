#Simple Python blockchain
'''unique fingerprint = transaction + previous blocks fingerprint'''

from blockbuilder import Block

genesis_block = Block('Chancellor on the brink of second bailout for banks', ['Satoshi sent 1 BTC to Ivan',
                                                                              'Satoshi sent 5 BTC to Hal Finney'])

second_block = Block(genesis_block.block_hash, ['Ivan sent 5 BTC to Liz',
                                                'John sent 5 BTC to Jenny'])
print('Block Hash Genesis block: ', end='')
print(genesis_block.block_hash)

print('Block hash Second Block: ', end='')
print(second_block.block_hash)