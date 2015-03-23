from building import Building, BuildingLayer, BuildingBlock
from oriented_blocks import Torch
import mcpi.block as block
from mcpi.vec3 import Vec3



class LampPost(Building):
	BLACK_WOOL = 15
	
	def __init__(self, **kwargs):
		super(LampPost, self).__init__(**kwargs)

		offset = self.pos
		post = BuildingBlock(offset, Vec3(0,0,0), block.FENCE)
		self.layers.append(BuildingLayer(post, 0))
		self.layers.append(BuildingLayer(post, 1))
		self.layers.append(BuildingLayer(post, 2))

		west1 = Vec3(-1,0,0)
		north1 = Vec3(0,0,1)
		east1 = Vec3(1,0,0)
		south1 = Vec3(0,0,-1)
		
		lamp_blocks = []
		lamp_blocks.append(BuildingBlock(offset, Vec3(0,0,0), block.WOOL, None, BLACK_WOOL))
		lamp_blocks.append(Torch(offset, west1, block.TORCH, None, Torch.WEST))
		lamp_blocks.append(Torch(offset, east1, block.TORCH, None, Torch.EAST))
		lamp_blocks.append(Torch(offset, south1, block.TORCH, None, Torch.SOUTH)) 
		lamp_blocks.append(Torch(offset, north1, block.TORCH, None, Torch.NORTH)) 
		self.layers.append(BuildingLayer(lamp_blocks, 3))
		
		self._set_direction()

	def build(self, mc):
		super(LampPost, self).build(mc)
	
