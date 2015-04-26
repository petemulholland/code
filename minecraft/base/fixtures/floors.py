from building import Building, BuildingEx, BuildingBlock, Torch
from building.types import NETHER_BRICK_FENCE
from base.constants import EXTERIOR_WALLS, FLOOR_WOOD
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3

class GroundFloor(BuildingEx):
	CASTLE_SPAN = (Building.SE_CORNER_POS, 
				   Building.SE_CORNER_POS + Vec3(-27,0,-28))
	
	WIDTH = CASTLE_SPAN[0].x - (CASTLE_SPAN[1].x - 1)

	def __init__(self, *args, **kwargs):
		super(GroundFloor, self).__init__(width=GroundFloor.WIDTH, *args, **kwargs)

	def _create_structure(self):
		super(GroundFloor, self)._create_structure()
		
		builds = []
		builds.append(BuildingBlock(GroundFloor.CASTLE_SPAN[0] + Vec3(0,-2,0),
									EXTERIOR_WALLS,
									GroundFloor.CASTLE_SPAN[1] + Vec3(0,-1,0),
									description="Castle floor"))
		self._add_section("Ground floor", builds)

class UpperFloor(GroundFloor):

	def __init__(self, *args, **kwargs):
		super(UpperFloor, self).__init__(*args, **kwargs)

	def _create_structure(self):
		super(GroundFloor, self)._create_structure()
		builds = []
		builds.append(BuildingBlock(GroundFloor.CASTLE_SPAN[0] + Vec3(-1,0,-1),
									EXTERIOR_WALLS,
									GroundFloor.CASTLE_SPAN[1] + Vec3(1,1,1),
									description="Castle floor"))

		builds.append(BuildingBlock(GroundFloor.CASTLE_SPAN[0] + Vec3(-1,0,-1),
									FLOOR_WOOD,
									GroundFloor.CASTLE_SPAN[1] + Vec3(1,1,1),
									description="Castle floor"))
		# TODO: Add embedded beams
		self._add_section("Upper floor", builds)

