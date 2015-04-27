from building import Building, BuildingEx, BuildingBlock, Stair
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3

# xxwwxx 5
# xxwwxx 4
#   xx   3
#   xx   2
#   xx   1
#   xx   0
# 543210
class MainStairs(BuildingEx):
	# TODO: implement 
	# - up 4 centrally (2 wide)+ up 2 to each side
	# use inverted stairs for "support" underneath each stair, except where upper floor supports the stair (last 1 at top)
	# need to embed inverted stairs into floor above central stair part (maybe?).
	# create air space in upper floor for stairs to travel through
	# - fences bordering all stairs & balcony above.
	WIDTH = 6
	def __init__(self, *args, **kwargs):
		super(MainStairs, self).__init__(width=MainStairs.WIDTH, *args, **kwargs)

	def _create_structure(self):
		super(MainStairs, self)._create_structure()
		
		builds = []

		# clear floor above stairs
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(0,4,0),
									block.AIR,
									Building.SE_CORNER_POS + Vec3(-5,5,-3),
									description="Clear floor above main staircase"))
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-2,4,-4),
									block.AIR,
									Building.SE_CORNER_POS + Vec3(-3,5,-5),
									description="Clear floor above landing"))
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-1,5,-4),
									block.AIR,
									Building.SE_CORNER_POS + Vec3(-4,5,-5),
									description="Clear floor above side stairs"))
		self._add_section("Clear floor area for stairs", builds)

		# add the central staircase
		for z in range(0,5):
			builds.append(Stair(Building.SE_CORNER_POS + Vec3(-2,z,-z), 
								block.STAIRS_WOOD.withData(Stair.NORTH), 
								Building.SE_CORNER_POS + Vec3(-3,z,-z), 
								description="Stair"))
			support = Stair(Building.SE_CORNER_POS + Vec3(-2,z,-(z+1)), 
							block.STAIRS_WOOD.withData(Stair.SOUTH), 
							Building.SE_CORNER_POS + Vec3(-3,z,-(z+1)), 
							description="Stair support")
			support.invert()
			builds.append(support)

		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-2,3,-4),
									block.WOOD_PLANKS,
									Building.SE_CORNER_POS + Vec3(-3,3,-5),
									description="Landing"))


		support = Stair(Building.SE_CORNER_POS + Vec3(-1,3,-4), 
						block.STAIRS_WOOD.withData(Stair.WEST), 
						Building.SE_CORNER_POS + Vec3(-1,3,-5), 
						description="Stair support")
		support.invert()
		builds.append(support)
		support = Stair(Building.SE_CORNER_POS + Vec3(-4,3,-4), 
						block.STAIRS_WOOD.withData(Stair.EAST), 
						Building.SE_CORNER_POS + Vec3(-4,3,-5), 
						description="Stair support")
		support.invert()
		builds.append(support)

		builds.append(Stair(Building.SE_CORNER_POS + Vec3(-1,4,-4), 
							block.STAIRS_WOOD.withData(Stair.EAST), 
							Building.SE_CORNER_POS + Vec3(-1,4,-5), 
							description="Stair"))
		builds.append(Stair(Building.SE_CORNER_POS + Vec3(-4,4,-4), 
							block.STAIRS_WOOD.withData(Stair.WEST), 
							Building.SE_CORNER_POS + Vec3(-4,4,-5), 
							description="Stair"))

		builds.append(Stair(Building.SE_CORNER_POS + Vec3(0,5,-4), 
							block.STAIRS_WOOD.withData(Stair.EAST), 
							Building.SE_CORNER_POS + Vec3(0,5,-5), 
							description="Stair"))
		builds.append(Stair(Building.SE_CORNER_POS + Vec3(-5,5,-4), 
							block.STAIRS_WOOD.withData(Stair.WEST), 
							Building.SE_CORNER_POS + Vec3(-5,5,-5), 
							description="Stair"))
		
		self._add_section("Staircase", builds)

		# TODO: add railings on upper floor

	def build_at(self, mc, pos):
		super(MainStairs, self).build_at(mc, pos)
