from building import Building, BuildingLayer, BuildingBlock
import mcpi.block as block
from mcpi.vec3 import Vec3
import copy

class Street(Building):
	WIDTH = 3
	def __init__(self, multiplier=1, *args, **kwargs):
		super(Street, self).__init__(width=Street.WIDTH, *args, **kwargs)
		self.multiplier = multiplier
				
		z_extent = (-3 * multiplier) + 1
		path = BuildingBlock(Building.SE_CORNER_POS, block.COBBLESTONE, 
								Building.SE_CORNER_POS + Vec3(-2,0,z_extent))
		self.add_layer(BuildingLayer([path], -2))

		path = BuildingBlock(Building.SE_CORNER_POS, block.GRAVEL, 
								Building.SE_CORNER_POS + Vec3(-2,0,z_extent))
		self.add_layer(BuildingLayer([path], -1))
		
		self._set_orientation()

	def clone(self):
		return type(self)(copy.copy(self.multiplier), copy.copy(self.dir))


