import datetime
import hashlib

#Create a 'Block' class
class Block :
  #Initialize values relating to the blockchain
  index = 0
  data = None
  h = 'Genesis'
  timestamp = datetime.datetime.now()
  previousHash = 0x0

  def __init__(self, data) :
    self.data = data

#Convert all the values to a hash using the hashlib library
  def hashBlock () :
    h = hashlib.sha256()
    h.update (
      str(Block.index).encode('utf-8') +
      str(Block.data).encode('utf-8') +
      str(Block.previousHash).encode('utf-8') +
      str(Block.timestamp).encode('utf-8') 
    )
    #Return the hash
    return h.hexdigest()


#Create a new blockchain class
class blockchain :
  block = Block("Genesis")
  #Create a new block in the blockchain
  def generateBlock (block) :
    #Set the values
    Block.previousHash =  Block.hashBlock()
    Block.index = Block.index + 1
    Block.data = block
    #Calculate the hash
    hash = Block.hashBlock()
    #--Print values for debugging purposes--#
    #print ("Previous Hash\n")
    #print (Block.previousHash)
    #print ("New hash\n")
    #print (hash)

    #Return the hash
    return hash
