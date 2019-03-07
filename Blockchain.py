"""
Blockchain

Credit: Gaurav Jain - accessed March 4, 2019
    https://www.pyscoop.com/building-a-simple-blockchain-in-python/
    https://github.com/gjain0/blockchain-python
"""
from Block import Block


class BlockChain(object):
    """
    Blockchain object
    """
    def __init__(self):
        self.chain = []
        self.current_node_transactions = []
        self.nodes = set()
        self.create_genesis_block()

    @property
    def get_serialized_chain(self):
        """
        Get serialized chain
        :return:
        :rtype:
        """
        return [vars(block) for block in self.chain]

    def create_genesis_block(self):
        """
        Create the genesis block
        :return:
        :rtype:
        """
        self.create_new_block(proof=0, previous_hash=0)

    def create_new_block(self, proof, previous_hash):
        """
        Create new block
        :param proof:
        :type proof:
        :param previous_hash:
        :type previous_hash:
        :return:
        :rtype:
        """
        block = Block(
            index=len(self.chain),
            proof=proof,
            previous_hash=previous_hash,
            transactions=self.current_node_transactions
        )
        self.current_node_transactions = []  # Reset the transaction list

        self.chain.append(block)
        return block

    @staticmethod
    def is_valid_block(block, previous_block):
        """
        Checks if block is valid
        :param block:
        :type block:
        :param previous_block:
        :type previous_block:
        :return:
        :rtype:
        """
        if previous_block.index + 1 != block.index:
            return False

        elif previous_block.get_block_hash != block.previous_hash:
            return False

        elif not BlockChain.is_valid_proof(block.proof, previous_block.proof):
            return False

        elif block.timestamp <= previous_block.timestamp:
            return False

        return True

    def create_new_transaction(self, sender, recipient, data):
        """
        Create new transaction
        :param sender:
        :type sender:
        :param recipient:
        :type recipient:
        :param data:
        :type data:
        :return:
        :rtype:
        """
        self.current_node_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'message': data
        })
        return True

    @staticmethod
    def is_valid_transaction():
        """
        Checks if transaction is valid
        :return:
        :rtype:
        """
        # Not Implemented
        pass

    @staticmethod
    def create_proof_of_work(previous_proof):
        """
        Generate "Proof Of Work"
        A very simple `Proof of Work` Algorithm -
            - Find a number such that, sum of the number and previous POW number is divisible by 7
        """
        proof = previous_proof + 1
        while not BlockChain.is_valid_proof(proof, previous_proof):
            proof += 1

        return proof

    @staticmethod
    def is_valid_proof(proof, previous_proof):
        """
        Checks if proof is valid
        :param proof:
        :type proof:
        :param previous_proof:
        :type previous_proof:
        :return:
        :rtype:
        """
        return (proof + previous_proof) % 7 == 0

    @property
    def get_last_block(self):
        """
        Gets the last block in the chain
        :return:
        :rtype:
        """
        return self.chain[-1]
