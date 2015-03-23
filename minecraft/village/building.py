from mcpi.vec3 import Vec3
import mcpi.block as block
import direction
import time

class BuildingBlock():
	def __init__(self, offset, pos, block_type=block.AIR, pos2=Vec3(0,0,0)):
		self.offset = offset
		self.pos = pos
		self.block = block_type
		self.pos2 = pos2
	
	def clone(self):
		return BuildingBlock(self.offset.clone(), self.pos.clone(), 
							 self.block, self.pos2.clone())

	def rotateLeft(self):  
		self.pos.rotateLeft()
		self.pos2.rotateLeft()
	
	def rotateRight(self, ct=1): 
		for i in range(ct):	
			self.pos.rotateRight()
			self.pos2.rotateRight()
	
	def set_level(self, y):
		self.pos.y = y
		if self.pos2 != Vec3(0, 0, 0):
			self.pos2.y = y

	def _build(self, mc, blockType):
		p1 = self.offset + self.pos
		if self.pos2 == Vec3(0, 0, 0):
			mc.setBlock(p1.x, p1.y, p1.z, blockType)
		else:
			p2 = self.offset + self.pos2
			mc.setBlocks(p1.x, p1.y, p1.z, 
						 p2.x, p2.y, p2.z, blockType)

	def build(self, mc):
		self._build(mc, self.block)
		
	def clear(self, mc, fill=block.AIR):
		self._build(mc, fill)

class BuildingLayer():
	def __init__(self, blocks=[], level=0):
		self.blocks = []
		self._level = level
		for block in blocks:
			new_block = block.clone()
			new_block.set_level(level)
			self.blocks.append(new_block)
		
	def clone(self):
		blocks = []
		for block in self.blocks:
			blocks.append(block.clone())
		return BuildingLayer(blocks)

	@property 
	def level(self): 
		'''level attribute accessor'''
		return self._level 
	
	@level.setter 
	def level(self, y): 
		self.level = y
		for block in self.blocks:
			block.set_level(y)
			
	def rotateLeft(self):  
		for block in self.blocks:
			block.rotateLeft()
	
	def rotateRight(self, ct=1): 
		for block in self.blocks:
			block.rotateRight(ct)
				
	def build(self, mc):
		for block in self.blocks:
			block.build(mc)
		
	def clear(self, mc, fill=block.AIR):
		for block in self.blocks:
			block.clear(mc, fill)
	
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
	
	def clear(self, ground_fill=block.DIRT):
		for i in xrange(len(self.layers), 0, -1):
			if self.layers[i].level < 0:
				self.layers[i].clear(mc, ground_fill)
			else:
				self.layers[i].clear(mc) # default to AIR
			time.sleep(5)
		
	def build(self, mc, debug=False):
		if debug == True:
			self._clear_layers(mc)
			time.sleep(5)
		
		for layer in self.layers:
			layer.build(mc)
		
			