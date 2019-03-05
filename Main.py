"""
Main app

Credit: Gaurav Jain - accessed March 4, 2019
    https://www.pyscoop.com/building-a-simple-blockchain-in-python/
    https://github.com/gjain0/blockchain-python
"""
from Blockchain import BlockChain
import json

blockchain = BlockChain()

print(">>>>> Before Mining...")
print(blockchain.chain)

last_block = blockchain.get_last_block
last_proof = last_block.proof
proof = blockchain.create_proof_of_work(last_proof)

# Sender "0" means that this node has mined a new block
# For mining the Block(or finding the proof), we must be awarded with some amount(in our case this is 1)

# blockchain.create_new_transaction(
#     sender="0",
#     recipient="address_x",
#     amount=1,
# )
#
# last_hash = last_block.get_block_hash
# block = blockchain.create_new_block(proof, last_hash)

blocks = []
proofs = []

for i in range(5):
    last_block = blockchain.get_last_block
    last_proof = last_block.proof
    proofs.append(blockchain.create_proof_of_work(last_proof))
    blockchain.create_new_transaction(
        sender="0",
        recipient="address_x" + str(i),
        amount=1+i,
    )
    last_hash = last_block.get_block_hash
    blocks.append(blockchain.create_new_block(proofs[i], last_hash))


print(">>>>> After Mining...")
# print(blockchain.chain)


def get_block():
    """
    Get block
    :return:
    :rtype:
    """
    json_chain = []
    for block in blockchain.chain:
        json_chain.append(json.dumps(block.__dict__))
    return json_chain


print(get_block())
