from building import Building, BuildingLayer, BuildingBlock
from oriented_blocks import Torch
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3



class Farm(Building):
	BOUNDARY_SPAN = (Vec3(-3,0,-1), Vec3(3,0,-9))
	LAND_SPAN = (Vec3(-2,0,-2), Vec3(2,0,-8))
	WATER_SPAN = (Vec3(0,0,-2), Vec3(0,0,-8))
	CROPS_LEFT_SPAN = (Vec3(-2,0,-2), Vec3(-1,0,-8))
	CROPS_RIGHT_SPAN = (Vec3(1,0,-2), Vec3(2,0,-8))

	def __init__(self, *args, **kwargs):
		super(Farm, self).__init__(*args, **kwargs)

		offset = self.build_pos
		layer_blocks = []
		layer_blocks.append(BuildingBlock(offset, Farm.BOUNDARY_SPAN[0], 
									block.WOOD, Farm.BOUNDARY_SPAN[1],
									description="Farm boundary"))
		layer_blocks.append(BuildingBlock(offset, Farm.LAND_SPAN[0], 
									block.DIRT, Farm.LAND_SPAN[1],
									description="Farm land"))
		layer_blocks.append(BuildingBlock(offset, Farm.WATER_SPAN[0], 
									block.WATER, Farm.WATER_SPAN[1],
									description="Farm irrigation"))

		self.layers.append(BuildingLayer(layer_blocks, 0))
		del layer_blocks[:]


		# TODO try placing crop types to get data
		layer_blocks.append(BuildingBlock(offset, Farm.CROPS_LEFT_SPAN[0], 
									block.FARMLAND, Farm.CROPS_LEFT_SPAN[1],
									description="Farm crops west"))
		layer_blocks.append(BuildingBlock(offset, Farm.CROPS_RIGHT_SPAN[0], 
									block.FARMLAND, Farm.CROPS_RIGHT_SPAN[1],
									description="Farm crops east"))

		self.layers.append(BuildingLayer(layer_blocks, 1))
		del layer_blocks[:]

		self._set_orientation()


	def build(self, mc):
		super(Farm, self).build(mc)
	
