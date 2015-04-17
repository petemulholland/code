from mcpi.vec3 import Vec3
import random
import mcpi.block

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


class Minecraft:
	def __init__(self):
		self.player = Player()
		self.camera = Camera()

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

	random_blocks = [STONE, DIRT, GRASS, AIR, LEAVES, DOOR_WOOD, DOOR_IRON] 
	def getBlockWithData(self, x,y,z):
		return random.choice(random_blocks)


	
	#def getBlock(self, *args):
	#	pass

	#def getBlockWithData(self, *args):
	#	return Block(0,0)

	#def getBlocks(self, *args):
	#	pass
	