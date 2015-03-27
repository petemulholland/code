from mcpi.vec3 import Vec3
import mcpi.block as block
import time

SLEEP_SECS = 0

DEBUG_BLOCK_WRITES = True
DEBUG_BLOCK_CTOR = False
DEBUG_BLOCK_ROTATION = False
DEBUG_BUILD_CLEAR = False
DEBUG_LAYERS = True

class BuildingBlock(object):
	def __init__(self, offset, pos, block_type=block.AIR, pos2=None, description=None):
		self.offset = offset
		self.pos = pos
		self.block = block_type
		self.pos2 = pos2
		self.description = description
		if DEBUG_BLOCK_CTOR:
			print str(self)
			
	def __str__(self):
		ret = "Block: offset: {0}, pos:{1}".format(str(self.offset),
													str(self.pos))
		ret += ", type:{0}".format(str(self.block))
		if self.pos2 is not None:
			ret += ", pos2:{0}".format(str(self.pos2))
		return ret
		
	def clone(self):
		if DEBUG_BLOCK_CTOR:
			print "Cloning ", str(self) 
		new_pos2 = None
		if self.pos2 is not None:
			new_pos2 = self.pos2.clone()
		return BuildingBlock(self.offset.clone(), self.pos.clone(), 
							 self.block.clone(), new_pos2, self.description)

	def applyRelativeOffset(self, offset):
		if offset is not None:
			if DEBUG_BLOCK_ROTATION:
				print "Applying offset to ", str(self)
			self.pos += offset
			if self.pos2 is not None:
				self.pos2 += offset

			if DEBUG_BLOCK_ROTATION:
				print "Offset applied to ", str(self)

	def rotateLeft(self):  
		if DEBUG_BLOCK_ROTATION:
			print "Rotating left", str(self)
		self.pos.rotateLeft()
		if self.pos2 is not None:
			self.pos2.rotateLeft()
		if DEBUG_BLOCK_ROTATION:
			print "Rotated left", str(self)
	
	def rotateRight(self, ct=1): 
		if DEBUG_BLOCK_ROTATION:
			print "Rotating right ", str(self)
		for i in range(ct):	
			self.pos.rotateRight()
			if self.pos2 is not None:
				self.pos2.rotateRight()
		if DEBUG_BLOCK_ROTATION:
			print "Rotated right", str(self)
	
	def set_level(self, y):
		self.pos.y = y
		if self.pos2 is not None:
			self.pos2.y = y

	def _build(self, mc, block_type):
		p1 = self.offset + self.pos
		if self.pos2 is None:
			if DEBUG_BLOCK_WRITES:
				out = "setBlock(%s,%s)"%(str(p1), str(block_type))
				if self.description is not None:
					out += " # " + self.description
				print out
			mc.setBlock(p1, block_type)
		else:
			p2 = self.offset + self.pos2
			if DEBUG_BLOCK_WRITES:
				out = "setBlocks(%s,%s,%s)"%(str(p1), str(p2), str(block_type))
				if self.description is not None:
					out += " # " + self.description
				print out
			mc.setBlocks(p1, p2, block_type)

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
		self._level = y
		for block in self.blocks:
			block.set_level(y)
			
	def applyRelativeOffset(self, offset):
		if offset is not None:
			for block in self.blocks:
				block.applyRelativeOffset(offset)
		
	def offsetAndRotateLeft(self, offset):
		for block in self.blocks:
			block.applyRelativeOffset(offset)
			block.rotateLeft()
			
	def rotateLeft(self):  
		for block in self.blocks:
			block.rotateLeft()
	
	def offsetAndRotateRight(self, offset, ct=1): 
		for block in self.blocks:
			block.applyRelativeOffset(offset)
			block.rotateRight(ct)

	def rotateRight(self, ct=1): 
		for block in self.blocks:
			block.rotateRight(ct)
				
	def build(self, mc):
		for block in self.blocks:
			block.build(mc)
		
	def clear(self, mc, fill=block.AIR):
		for i in xrange(len(self.blocks) - 1, -1, -1):
			self.blocks[i].clear(mc, fill)
	
class Building(object):
	NORTH = 0
	SOUTH = 2
	EAST  = 1
	WEST  = -1

	def __init__(self, build_pos, orientation, build_offset=None):
		self.build_pos = build_pos
		self.dir = orientation
		self.build_offset = build_offset
		self.layers = []

	def _set_orientation(self):
		for layer in self.layers:
			if self.dir == Building.WEST:
				layer.offsetAndRotateLeft(self.build_offset)
			elif self.dir == Building.EAST:
				layer.offsetAndRotateRight(self.build_offset)
			elif self.dir == Building.SOUTH:
				layer.offsetAndRotateRight(self.build_offset, 2)
			else:
				layer.applyRelativeOffset(self.build_offset)

	def clear(self, mc, ground_fill=block.DIRT, debug=DEBUG_BUILD_CLEAR):
		if debug:
			self._clear_layers_down(mc)
			
		print "clearing down building layers"
		for i in xrange(len(self.layers) - 1, -1, -1):
			if self.layers[i].level < 0:
				self.layers[i].clear(mc, ground_fill)
				if debug:
					time.sleep(SLEEP_SECS)
			else:
				self.layers[i].clear(mc) # default to AIR
			time.sleep(SLEEP_SECS)
	
	def _clear_layers_down(self, mc):
		print "clearing building layers down first"
		for i in xrange(len(self.layers) - 1, -1, -1):
			self.layers[i].clear(mc)
			time.sleep(SLEEP_SECS)
		
	def build(self, mc, debug=DEBUG_BUILD_CLEAR):
		if debug:
			self._clear_layers_down(mc)

		print "building up building layers"
		for layer in self.layers:
			if DEBUG_LAYERS:
				print
				print "building layer: %s"%(layer.level)
			layer.build(mc)
			if debug:
				time.sleep(SLEEP_SECS)

