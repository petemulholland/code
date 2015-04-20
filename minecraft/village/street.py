from building import Building, BuildingLayer, BuildingBlock
import mcpi.block as block
from mcpi.vec3 import Vec3

class Street(Building):
	WIDTH = 3
	def __init__(self, *args, **kwargs):
		super(Street, self).__init__(width=Street.WIDTH, *args, **kwargs)
		
		path = BuildingBlock(Building.SE_CORNER_POS, block.COBBLESTONE, 
								Building.SE_CORNER_POS + Vec3(-2,0,-2))
		self.add_layer(BuildingLayer([path], -2))

		path = BuildingBlock(Building.SE_CORNER_POS, block.GRAVEL, 
								Building.SE_CORNER_POS + Vec3(-2,0,-2))
		self.add_layer(BuildingLayer([path], -1))
		
		self._set_orientation()

	def build(self, mc):
		super(Street, self).build(mc)
	
