from building import Building, BuildingEx, BuildingBlock, CompositeBuilding, Torch
from building.types import NETHER_BRICK_FENCE
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3

# TODO fireplace need to go down 1 level to contain lava,
#		If I want grill at floor level then this would protrude into lower floor
#		unless i make floors 2 blocks deep (inthis case i could embed beams in floors)
class Fireplace(BuildingEx):
	AREA_SPAN = (Vec3(0,-1,0), Vec3(-3,3,-3))
	OPEN_FRONT_SPAN = (Vec3(0,1,0), Vec3(-3,3,0))
	GRATE_SPAN = (Vec3(-1,1,-1), Vec3(-2,2,-2))
	GRILL_SPAN = (Vec3(0,1,0), Vec3(-3,1,0))
	LAVAL_SPAN = (Vec3(-1,0,-2), Vec3(-2,0,-2))
	TORCH_POS = (Vec3(0,3,0), Vec3(-3,3,0))

	GRILL_TYPE = NETHER_BRICK_FENCE

	WIDTH = (AREA_SPAN[0].x - AREA_SPAN[1].x) + 1

	def __init__(self, *args, **kwargs):
		super(Fireplace, self).__init__(width=Fireplace.WIDTH, *args, **kwargs)

		# create walls
		builds = []
		builds.append(BuildingBlock(Fireplace.AREA_SPAN[0],
									block.STONE_BRICK, 
									Fireplace.AREA_SPAN[1],
									description="Stone fill"))

		builds.append(BuildingBlock(Fireplace.OPEN_FRONT_SPAN[0],
									block.AIR, 
									Fireplace.OPEN_FRONT_SPAN[1],
									description="Clear Front"))
		builds.append(BuildingBlock(Fireplace.GRATE_SPAN[0],
									block.AIR, 
									Fireplace.GRATE_SPAN[1],
									description="Clear grate"))
		builds.append(BuildingBlock(Fireplace.GRILL_SPAN[0],
									Fireplace.GRILL_TYPE, 
									Fireplace.GRILL_SPAN[1],
									description="Stone fill"))
		builds.append(BuildingBlock(Fireplace.LAVAL_SPAN[0],
									block.LAVA, 
									Fireplace.LAVAL_SPAN[1],
									description="Stone fill"))

		builds.append(Torch(Fireplace.TORCH_POS[0], block.TORCH.withData(Torch.SOUTH), 
							description="torch"))
		builds.append(Torch(Fireplace.TORCH_POS[1], block.TORCH.withData(Torch.SOUTH), 
							description="torch"))
		self._add_section("Fireplace", builds)

		self._set_orientation()
