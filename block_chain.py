import hashlib
import json
from time import time



#Blockchain class
class Blockchain(object):
    """ 
    Very simple example of how  a crypto block chain works!
    """


    def __init__(self):
        # this list will act as the chain, which we will add blocks to
        self.chain = []
        # pending transactions will be a list of transactions not yet approved. If approved, they will be added to a new block
        self.pending_transactions = []

        self.new_block(previous_hash="test hash 5/2/2021",proof=100)
    
    def new_block(self,proof,previous_hash=None):
        block = {
            'index' :len(self.chain) +1,
            'timestamp': time(),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }
        self.pending_transactions = []
        self.chain.append(block)

        return block

    
    @property
    def last_block(self):
        return self.chain[-1]


    def new_transaction(self,sender,recipient,amount):
        #define a function for a new transaction with sender, recepient, and amount
        transaction = {
            'sender' :sender,
            'recipient': recipient,
            'amount': amount


        }

        self.pending_transactions.append(transaction)
        return self.last_block['index'] + 1

    def hash(self,block):
        #hashing function.. this is where the cryptography comes in..
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash

#use below if you want it to only run when using the command line.. otherwise it will run if you import it
if __name__ == "__main__":
    blockchain = Blockchain()
    t1 = blockchain.new_transaction("Kevin",'Charles','5 coins')
    t2 = blockchain.new_transaction("James",'Rob','2.5 coins')
    t3 = blockchain.new_transaction("Nigel",'Aliza','10 coins')
    blockchain.new_block(124345)

    t4 = blockchain.new_transaction("Aliza",'Nigel','5 coins')
    t5 = blockchain.new_transaction("Rob",'James','2.5 coins')
    t6 = blockchain.new_transaction("Charles",'Kevin','10 coins')
    blockchain.new_block(6789)

    print( "Blochain: :", blockchain.chain)
