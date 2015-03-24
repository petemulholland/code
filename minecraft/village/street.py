from building import Building, BuildingLayer, BuildingBlock
import mcpi.block as block
from mcpi.vec3 import Vec3

class Street(Building):
	def __init__(self, *args, **kwargs):
		super(Street, self).__init__(*args, **kwargs)
		
		offset = Vec3(0,0,1)
		gravel = BuildingBlock(offset, Vec3(-1,0,-1), block.GRAVEL, Vec3(1,0,1))
		self.layers.append(BuildingLayer(gravel, -1))
		
		self._set_orientation()

	def build(self, mc):
		super(Street, self).build(mc)
	
