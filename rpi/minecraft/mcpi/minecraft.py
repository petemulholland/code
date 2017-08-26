from mcpi.vec3 import Vec3
import random
from  mcpi.block import *

#MOCK_PLAYER_POS = Vec3(20,8,-20)
MOCK_PLAYER_POS = Vec3(0,0,0)

#class Player:
#	def getPos(self):
#		return MOCK_PLAYER_POS
		
#	def getTilePos(self):
#		return MOCK_PLAYER_POS
		
#	def setPos(self, x, y, z):
#		pass
		
#	def setTilePos(self, x, y, z):
#		pass

class Player():
	"""Methods for the host (Raspberry Pi) player"""
	def __init__(self):
		self.pos = MOCK_PLAYER_POS

	def getPos(self):
		return self.pos

	def setPos(self, *args):
		print "Setting player position: " + str(args[0])
		self.pos = args[0]

	def getTilePos(self):
		return self.pos

	def setTilePos(self, *args):
		print "Setting player tile position" + str(args[0])
		self.pos = args[0]

	def getDirection(self):
		"Get unit vector of x,y,z for the player's direction => [Vec3]"
		return Vec3(0,0,-1) # default to north, need to debug this in game


class Camera:
	def setNormal(self, *args):
		"""Set camera mode to normal Minecraft view ([entityId])"""
		print "Setting camera mode to normal"

	def setFixed(self):
		"""Set camera mode to fixed view"""
		print "Setting camera mode to fixed"

	def setFollow(self, *args):
		"""Set camera mode to follow an entity ([entityId])"""
		print "Setting camera mode to follow"

	def setPos(self, *args):
		"""Set camera entity position (x,y,z)"""
		print "Setting camera position"

class Event:
	def pollBlockHits(self):
		pass
		#"Block Hits (Only triggered by sword) => [BlockEvent]"
		#Available on Minecraft: Pi EditionAvailable on RaspberryJuice
		##get block event hits that have occured since the last time the function was run
		#blockEvents = mc.events.pollBlockHits()
		#for blockEvent in blockEvents:
		#	print blockEvent
		return list(Vec3(0,0,0))

	def clearAll(self):
		pass

class Minecraft:
	def __init__(self):
		self.player = Player()
		self.camera = Camera()
		self.events = Event()

	@classmethod
	def create(cls):
		print
		print
		print "!*!*!*!*!*!*!*!*!*!*!!*!*!*!*!*!*!*!*!*!"
		print "!*!*!*! Using Mock minecraft API !*!*!*!"
		print "!*!*!*!*!*!*!*!*!*!*!!*!*!*!*!*!*!*!*!*!"
		print
		return Minecraft()
	
		
	def setBlock(self, *args):
		pass

	def setBlocks(self, *args):
		pass

	def postToChat(self, message):
		print message

	def getHeight(self, x,z):
		return 65


	random_block_ids = [STONE.id, DIRT.id, GRASS.id, GRAVEL.id, AIR.id, LEAVES.id]
	interesting_block_ids = [SAND.id, DOOR_WOOD.id, DOOR_IRON.id] 
	def getBlock(self, x,y,z):
		return random.choice(Minecraft.random_block_ids)

	random_blocks = [STONE, DIRT, GRASS, GRAVEL, AIR, LEAVES]
	interesting_blocks = [SAND, DOOR_WOOD, DOOR_IRON] 
	def getBlockWithData(self, x,y,z):
		return random.choice(Minecraft.random_blocks)


	
	#def getBlock(self, *args):
	#	pass

	#def getBlockWithData(self, *args):
	#	return Block(0,0)

	#def getBlocks(self, *args):
	#	pass
	