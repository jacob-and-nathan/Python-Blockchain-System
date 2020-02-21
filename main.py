import datetime
import hashlib

#Create a 'Block' class
class Block :
  #Initialize values relating to the blockchain
  index = 0
  data = None
  hash = None
  timestamp = datetime.datetime.now()
  previousHash = 0x0
  next = None
  #Number only sored once, or as I like to call it, 'incrementing variable'
  nonce = 0

  def __init__(self, data) :
    self.data = data

#Convert all the values to a hash using the hashlib library
  def hashBlock () :
    hash = hashlib.sha256()
    hash.update (
      str(Block.nonce).encode('utf-8') +
      str(Block.index).encode('utf-8') +
      str(Block.data).encode('utf-8') +
      str(Block.previousHash).encode('utf-8') +
      str(Block.timestamp).encode('utf-8') 
    )
    #Return the hash
    return hash.hexdigest()


#Create a new blockchain class
class Blockchain :
  #The maximum nonce
  maxNonce = 2**32

  #mining difficulty variable
  diff = 14

  #Target hash
  target = 2**(256-diff)

  #This is the Genesis block
  block = Block("Genesis")

  #Stores the newest addition to the block
  head = block

  #Create a new block in the blockchain
  def generateBlock (block) :
    #Change some values
    Block.previousHash =  Block.hashBlock()
    Block.index = Block.index + 1
    Block.next = block
    Blockchain.block = Block.next

  def mine (self, block) :
    #Repeat maxNonce times
    for n in range(blockchain.maxNonce) :
      #Check if the proposed block is to be accepted
      if int(Block.hashBlock(), 16) <= blockchain.target :
        Blockchain.generateBlock(block)
        break
      else :
        #Increase the nonce
        Block.nonce = Block.nonce + 1

blockchain = Blockchain()
