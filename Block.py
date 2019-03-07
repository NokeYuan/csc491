"""
Block

Credit: Gaurav Jain - accessed March 4, 2019
    https://www.pyscoop.com/building-a-simple-blockchain-in-python/
    https://github.com/gjain0/blockchain-python
"""
import time
import hashlib


class Block(object):
    """
    Block object
    """
    def __init__(self, index, proof, previous_hash, transactions, timestamp=None):
        self.index = index
        self.proof = proof
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = timestamp or time.time()

    @property
    def get_block_hash(self):
        """
        Gets the block hash
        :return:
        :rtype:
        """
        block_string = "{}{}{}{}{}".format(
            self.index,
            self.proof,
            self.previous_hash,
            self.transactions,
            self.timestamp)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def __repr__(self):
        return "Index: {} - Proof: {} - Previous Hash: {} - Transactions: {} - Timestamp: {}".format(
            self.index, self.proof, self.previous_hash, self.transactions, self.timestamp)
