from mcpi.vec3 import Vec3

class Player:
	def getPos(self):
		return Vec3(0,0,0)
		
	def getTilePos(self):
		return Vec3(0,0,0)
		
	def setPos(self, x, y, z):
		pass
		
	def setTilePos(self, x, y, z):
		pass

class Minecraft:
	def __init__(self):
		self.player = Player()
	
	@classmethod
	def create(cls):
		print "!*!*!*!*!*!*!*!*!*!*!!*!*!*!*!*!*!*!*!*!"
		print "!*!*!*! Using Mock minecraft API !*!*!*!"
		print "!*!*!*!*!*!*!*!*!*!*!!*!*!*!*!*!*!*!*!*!"
		return Minecraft()
	
	#create = classmethod(create)
		
	def setBlocks(self, x0,y0,z0, x1,y1,z1, id, data=0):
		pass
	
	def setBlock(self, x,y,z, id, data=0):
		pass
	
	def postToChat(self, message):
		print message
	
	