from mcpi.vec3 import Vec3

#MOCK_PLAYER_POS = Vec3(20,8,-20)
MOCK_PLAYER_POS = Vec3(0,0,0)

class Player:
	def getPos(self):
		return MOCK_PLAYER_POS
		
	def getTilePos(self):
		return MOCK_PLAYER_POS
		
	def setPos(self, x, y, z):
		pass
		
	def setTilePos(self, x, y, z):
		pass

class Minecraft:
	def __init__(self):
		self.player = Player()
	
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

	
	#def getBlock(self, *args):
	#	pass

	#def getBlockWithData(self, *args):
	#	return Block(0,0)

	#def getBlocks(self, *args):
	#	pass
	