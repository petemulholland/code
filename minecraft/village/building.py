from mcpi.vec3 import Vec3
import mcpi.block as block
import direction
import time

class BuildingBlock():
	def __init__(self, position=Vec3(0,0,0), block_type=block.AIR):
		self.pos = position
		self.block = block_type
	
	def __add__(self, rhs):
		c = self.clone()
		c.pos += rhs
		return c

	def __iadd__(self, rhs):
		self.pos += rhs
		return self

	def __imul__(self, k):
		self.pos *= k
		return self

	def clone(self):
		return BuildingBlock(self.pos.clone(), self.block)

	def rotateLeft(self):  
		self.pos.rotateLeft()
	
	def rotateRight(self): 
		self.pos.rotateRight()
	
	def set_level(self, y):
		self.pos.y = y

	def build(self, mc):
		mc.setBlock(self.pos.x, self.pos.y, self.pos.z, self.block)
		
	def clear(self, mc):
		mc.setBlock(self.pos.x, self.pos.y, self.pos.z, block.AIR)

class BuildingLayer():
	def __init__(self, blocks=[], level=0):
		self.blocks = []
		for block in blocks:
			new_block = block.clone()
			new_block.pos.y = level
			self.blocks.append(new_block)
		
	def clone(self):
		blocks = []
		for block in self.blocks:
			blocks.append(block.clone())
		return BuildingLayer(blocks)
		
	def set_level(self, y):
		for block in self.blocks:
			block.set_level(y)
			
	def rotateLeft(self):  
		for block in self.blocks:
			block.rotateLeft()
	
	def rotateRight(self, ct=1): 
		for block in self.blocks:
			for i in range(ct):	
				block.rotateRight()
				
	def build(self, mc):
		for block in self.blocks:
			block.build(mc)
		
	def clear(self, mc):
		for block in self.blocks:
			block.clear(mc)
	
class Building():
	def __init__(self, position=Vec3(0,0,0), direction=direction.NORTH):#, **kwargs):
		#super().__init__(**kwargs)
		self.pos = position
		self.dir = direction
		self.layers = []
		
	def _set_direction(self):
		for layer in self.layers:
			if self.dir == direction.WEST:
				layer.rotateLeft()
			elif self.dir == direction.EAST:
				layer.rotateRight()
			elif self.dir == direction.SOUTH:
				layer.rotateRight(2)
	
	def _clear_layers(self, mc):
		for i = len(self.layers) -1; i >= 0; --i:
			self.layers[i].clear(mc)
			time.sleep(5)
		
	def build(self, mc, debug=False):
		if debug == True:
			self._clear_layers(mc)
			time.sleep(5)
		
		for layer in self.layers:
			layer.build(mc)
		
			