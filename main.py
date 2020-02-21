import datetime
import hashlib
from termcolor import colored


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

        #Store in txt file
        file = open('mineHistory.txt', 'a')
        file.write("Hash: " + Block.hashBlock() + "\nNonce: " + str(Block.nonce) + "\n")
        break
      else :
        #Increase the nonce
        Block.nonce = Block.nonce + 1

blockchain = Blockchain()

value = 0
#Repeat forever
while True:
  response = input(colored("Enter m to mine a new block\n Press t to view all hashes generated\nPress v to see the simulated value of each block: ", "green")) 
  if response == 't' :
    file = open('mineHistory.txt', 'r')
    print (colored("Reading responses: ", "green"))
    print (colored(file.read(), "red"))
  elif response == 'm' :
    block = input("What data do you want the block to hold? ")
    times = int(input("How many times do you want to mine? "))
    for n in range(times) :
      blockchain.mine(block)
      print ("Block mined")
      value = Block.nonce/2
  elif response == 'v' :
    print ("Relative value of blocks: " + str(value) + "\nThe value is based on the difficulty to mine")
  else :
    print(colored("Sorry, please type that again", "red"))
