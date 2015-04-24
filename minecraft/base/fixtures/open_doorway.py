from building import Building, BuildingEx, BuildingBlock, Stair
from building.types import STAIRS_STONE_BRICK
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3

class OpenDoorway(BuildingEx):
	''' 2 wide open space (apply air blocks)
		+ 2 upside down stairs on 3rd level 
		TODO: add depth & arch block type'''
	WIDTH = 2
	def __init__(self, *args, **kwargs):
		super(OpenDoorway, self).__init__(width=OpenDoorway.WIDTH, *args, **kwargs)

		# TODO: add depth & stair type params to this.
		builds = []
		builds.append(BuildingBlock(Building.SE_CORNER_POS,
									block.AIR, 
									Building.SE_CORNER_POS + Vec3(-1, 1, 0),
									description="clear door space"))
		
		# TODO: figure out a better way of inverting stairs
		stair = Stair(Building.SE_CORNER_POS + Vec3(0, 2, 0), 
					  STAIRS_STONE_BRICK.withData(Stair.WEST), 
					  description="door arch")
		stair.invert()
		builds.append(stair)
		stair = Stair(Building.SE_CORNER_POS + Vec3(-1, 2, 0), 
					  STAIRS_STONE_BRICK.withData(Stair.EAST), 
					  description="door arch")
		stair.invert()
		builds.append(stair)

		self._add_section("Arched open doorway", builds)
		self._set_orientation()
