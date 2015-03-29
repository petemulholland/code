from building import Building, BuildingLayer, BuildingBlock
from oriented_blocks import Torch
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3



class Farm(Building):
	BOUNDARY_SPAN = (Vec3(0,0,0), Vec3(-6,0,-8))
	LAND_SPAN = (BOUNDARY_SPAN[0] + Vec3(-1,0,-1), 
					BOUNDARY_SPAN[1] + Vec3(1,0,1))
	WATER_SPAN = (BOUNDARY_SPAN[0] + Vec3(-3,0,-1), 
					BOUNDARY_SPAN[0] + Vec3(-3,0,-7))
	#CROPS_LEFT_SPAN = (Vec3(-2,0,-2), Vec3(-1,0,-8))
	#CROPS_RIGHT_SPAN = (Vec3(1,0,-2), Vec3(2,0,-8))

	WIDTH = 7
	def __init__(self, *args, **kwargs):
		super(Farm, self).__init__(width=Farm.WIDTH, *args, **kwargs)

		layer_blocks = []
		layer_blocks.append(BuildingBlock(Farm.BOUNDARY_SPAN[0], 
									block.WOOD, Farm.BOUNDARY_SPAN[1],
									description="Farm boundary"))
		layer_blocks.append(BuildingBlock(Farm.LAND_SPAN[0], 
									block.DIRT, Farm.LAND_SPAN[1],
									description="Farm land"))
		layer_blocks.append(BuildingBlock(Farm.WATER_SPAN[0], 
									block.WATER, Farm.WATER_SPAN[1],
									description="Farm irrigation"))

		self.layers.append(BuildingLayer(layer_blocks, 0))
		del layer_blocks[:]

		for i in range(7):
			layer_blocks.append(BuildingBlock(Farm.LAND_SPAN[0] + Vec3(0,0,-i), 
										Block(59, i), Farm.LAND_SPAN[1] + Vec3(0,0,-i),
										description="Farm land"))

		self.layers.append(BuildingLayer(layer_blocks, 1))
		self._set_orientation()


	def build(self, mc):
		super(Farm, self).build(mc)
	
