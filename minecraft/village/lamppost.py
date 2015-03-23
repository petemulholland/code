from building import Building, BuildingLayer, BuildingBlock
from oriented_blocks import Torch
import mcpi.block as block
from mcpi.vec3 import Vec3



class LampPost(Building):
	BLACK_WOOL = 15
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		offset = Vec3(0,0,1)
		post = BuildingBlock(offset, Vec3(0,0,0), block.FENCE)
		self.layers.append(BuildingLayer(post, 0)
		self.layers.append(BuildingLayer(post, 1)
		self.layers.append(BuildingLayer(post, 2)

		# todo: need to fix torch direction on rotation
		lamp_blocks = []
		lamp_blocks.append(BuildingBlock(offset, Vec3(0,0,0), block.WOOL, Vec3(0,0,0), BLACK_WOOL)
		lamp_blocks.append(Torch(offset, Vec3(-1,0,0), block.TORCH, Vec3(0,0,0), Torch.WEST))
		lamp_blocks.append(Torch(offset, Vec3(1,0,0), block.TORCH, Vec3(0,0,0), Torch.EAST))
		lamp_blocks.append(Torch(offset, Vec3(0,0,-1), block.TORCH, Vec3(0,0,0), Torch.SOUTH)) 
		lamp_blocks.append(Torch(offset, Vec3(0,0,1), block.TORCH, Vec3(0,0,0), Torch.NORTH)) 
		self.layers.append(BuildingLayer(lamp_blocks, 3)
		
		self._set_direction()

	def build(self, mc):
		super().build(mc)
	
