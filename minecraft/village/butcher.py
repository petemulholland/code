from building import Building, BuildingLayer, BuildingBlock
from oriented_blocks import Torch, Stair, Ladder
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3

class Butcher(Building):
	"""description of class"""
	
	def __init__(self, *args, **kwargs):
		super(Butcher, self).__init__(*args, **kwargs)

		offset = self.build_pos

		self._set_orientation()
		
	def build(self, mc):
		super(Butcher, self).build(mc)

