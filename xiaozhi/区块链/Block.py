import datetime
import hashlib


class Block:
    def __init__(self, index, data, timestamp, previous_hash):
        self.index = index
        self.data = data
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        hash = hashlib.sha256()
        data = str(self.index)+str(self.data)+str(self.timestamp)+str(self.previous_hash)
        hash.update(data.encode("utf-8"))
        return hash.hexdigest()

# 创造创世区块
def create_genesis_block():
    return Block(0, "Initival block", datetime.datetime.now(), "0")


# 关联区块链(核心)
def next_block(last_block):
    this_index = last_block.index + 1
    this_data = "xiaozhi"+str(this_index)
    this_timestamp = datetime.datetime.now()
    this_hash = last_block.hash # 这里记录上次的hash值,做关联
    return Block(this_index, this_data, this_timestamp, this_hash)


blockchain = [create_genesis_block()]
previous_block = blockchain[0]

num_of_blocks_to_add = 50

for i in range(0, num_of_blocks_to_add):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    print("Block #{} has been added to the blcokchain!".format(block_to_add.index))
    print("Hash:{}n".format(block_to_add.hash))
