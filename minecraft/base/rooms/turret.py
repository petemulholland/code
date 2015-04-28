from building import Building, BuildingEx, BuildingBlock, SubBuilding, Torch, Door, Stair
from base.constants import EXTERIOR_WALLS, INTERIOR_WALLS, WALL_HEIGHT
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3

# TODOs:
# with layout of upper floor want to be able to mirror the turrets East-west 
# for back turrets, & rotate for front turrets
# Also want to be able to specify access enclosure building material, to use stone on roof & wood inside.
class Turret(BuildingEx):
	#    XXX     6
	#   XsswX    5
	#  XwssssX   4
	#  XssXssXWW 3
	#  Xssw  w   2
	#   Xww  w   1
	#    XXwdw   0
	#     W
	#
	#  6543210

	WIDTH = 7
	def __init__(self, *args, **kwargs):
		super(Turret, self).__init__(width=Turret.WIDTH, *args, **kwargs)
		self.access_enclosure = block.WOOD_PLANKS

	def set_access_enclosure_material(self, block_type):
		self.access_enclosure = block_type

	def _create_wall_clearances(self):
		builds = []

		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(self._get_x(-3),0,-1),
									block.AIR,
									Building.SE_CORNER_POS + Vec3(self._get_x(-3),WALL_HEIGHT,-2),
									description="turret wall clearance"))
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(self._get_x(-1),0,-3),
									block.AIR,
									Building.SE_CORNER_POS + Vec3(self._get_x(-2),WALL_HEIGHT,-3),
									description="turret wall clearance"))
		self._add_section("Wall clearances for turret", builds)

	# TODO: enable mirroring turrets along both NS and EW axes
	def _create_walls(self):
		builds = []
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(self._get_x(-4),0,0),
									EXTERIOR_WALLS,
									Building.SE_CORNER_POS + Vec3(self._get_x(-4),WALL_HEIGHT+2,0),
									description="turret wall"))
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(self._get_x(-5),0,-1),
									EXTERIOR_WALLS,
									Building.SE_CORNER_POS + Vec3(self._get_x(-5),WALL_HEIGHT+2,-1),
									description="turret wall"))
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(self._get_x(-6),0,-2),
									EXTERIOR_WALLS,
									Building.SE_CORNER_POS + Vec3(self._get_x(-6),WALL_HEIGHT+2,-4),
									description="turret wall"))
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(self._get_x(-5),0,-5),
									EXTERIOR_WALLS,
									Building.SE_CORNER_POS + Vec3(self._get_x(-5),WALL_HEIGHT+2,-5),
									description="turret wall"))
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(self._get_x(-4),0,-6),
									EXTERIOR_WALLS,
									Building.SE_CORNER_POS + Vec3(self._get_x(-2),WALL_HEIGHT+2,-6),
									description="turret wall"))
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(self._get_x(-1),0,-5),
									EXTERIOR_WALLS,
									Building.SE_CORNER_POS + Vec3(self._get_x(-1),WALL_HEIGHT+2,-5),
									description="turret wall"))
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(self._get_x(0),0,-4),
									EXTERIOR_WALLS,
									Building.SE_CORNER_POS + Vec3(self._get_x(0),WALL_HEIGHT+2,-4),
									description="turret wall"))

		self._add_section("Turret walls", builds)
		
	def _create_stairs(self):
		builds = []

		# north facing stairs, supports & landing
		builds.append(Stair(Building.SE_CORNER_POS + Vec3(self._get_x(-1),0,-3), 
							block.STAIRS_WOOD.withData(Stair.NORTH), 
							Building.SE_CORNER_POS + Vec3(self._get_x(-2),0,-3), 
							description="Stair"))

		support = Stair(Building.SE_CORNER_POS + Vec3(self._get_x(-1),0,-4), 
							block.STAIRS_WOOD.withData(Stair.SOUTH), 
							Building.SE_CORNER_POS + Vec3(self._get_x(-2),0,-4), 
							description="Support")
		support.invert()
		builds.append(support)
		builds.append(Stair(Building.SE_CORNER_POS + Vec3(self._get_x(-1),1,-4), 
							block.STAIRS_WOOD.withData(Stair.NORTH), 
							Building.SE_CORNER_POS + Vec3(self._get_x(-2),1,-4), 
							description="Stair"))

		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(self._get_x(-2),1,-5),
									block.WOOD_PLANKS,
									description="landing"))

		# east facing stairs, supports & landing
		stair_direction = Stair.WEST
		support_direction = Stair.EAST
		if self.mirrored:
			stair_direction = Stair.EAST
			support_direction = Stair.WEST


		support = Stair(Building.SE_CORNER_POS + Vec3(self._get_x(-3),1,-4), 
							block.STAIRS_WOOD.withData(support_direction), 
							Building.SE_CORNER_POS + Vec3(self._get_x(-3),1,-5), 
							description="Support")
		support.invert()
		builds.append(support)
		builds.append(Stair(Building.SE_CORNER_POS + Vec3(self._get_x(-3),2,-4), 
							block.STAIRS_WOOD.withData(stair_direction), 
							Building.SE_CORNER_POS + Vec3(self._get_x(-3),2,-5), 
							description="Stair"))

		support = Stair(Building.SE_CORNER_POS + Vec3(self._get_x(-4),2,-4), 
							block.STAIRS_WOOD.withData(support_direction), 
							Building.SE_CORNER_POS + Vec3(self._get_x(-4),2,-5), 
							description="Support")
		support.invert()
		builds.append(support)
		builds.append(Stair(Building.SE_CORNER_POS + Vec3(self._get_x(-4),3,-4), 
							block.STAIRS_WOOD.withData(stair_direction), 
							Building.SE_CORNER_POS + Vec3(self._get_x(-4),3,-5), 
							description="Stair"))

		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(self._get_x(-5),3,-4),
									block.WOOD_PLANKS,
									description="landing"))


		# south facing stairs, supports & landing
		support = Stair(Building.SE_CORNER_POS + Vec3(self._get_x(-4),3,-3), 
							block.STAIRS_WOOD.withData(Stair.NORTH), 
							Building.SE_CORNER_POS + Vec3(self._get_x(-5),3,-3), 
							description="Support")
		support.invert()
		builds.append(support)
		builds.append(Stair(Building.SE_CORNER_POS + Vec3(self._get_x(-4),4,-3), 
							block.STAIRS_WOOD.withData(Stair.SOUTH), 
							Building.SE_CORNER_POS + Vec3(self._get_x(-5),4,-3), 
							description="Stair"))

		support = Stair(Building.SE_CORNER_POS + Vec3(self._get_x(-4),4,-2), 
							block.STAIRS_WOOD.withData(Stair.NORTH), 
							Building.SE_CORNER_POS + Vec3(self._get_x(-5),4,-2), 
							description="Support")
		support.invert()
		builds.append(support)
		builds.append(Stair(Building.SE_CORNER_POS + Vec3(self._get_x(-4),5,-2), 
							block.STAIRS_WOOD.withData(Stair.SOUTH), 
							Building.SE_CORNER_POS + Vec3(self._get_x(-5),5,-2), 
							description="Stair"))

		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(self._get_x(-4),5,-1),
									block.WOOD_PLANKS,
									description="landing"))

		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(self._get_x(-3),5,-1),
									block.WOOD_PLANKS,
									Building.SE_CORNER_POS + Vec3(self._get_x(-3),5,-2),
									description="landing extension"))

		self._add_section("Turret stairs", builds)

	# TODO: add torches & Windows

	def _create_interior_enclosure(self):
		builds = []
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(self._get_x(0),0,0),
									self.access_enclosure,
									Building.SE_CORNER_POS + Vec3(self._get_x(-2),WALL_HEIGHT,0),
									description="turret interior wall"))
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(self._get_x(0),0,0),
									self.access_enclosure,
									Building.SE_CORNER_POS + Vec3(self._get_x(0),WALL_HEIGHT,-2),
									description="turret interior wall"))
		hinge_type = Door.HINGE_LEFT
		if self.mirrored:
			hinge_type = Door.HINGE_RIGHT

		builds.append(Door(Door.HINGE_LEFT, 
							Building.SE_CORNER_POS + Vec3(self._get_x(-1),0,0),
							block.DOOR_WOOD.withData(Door.SOUTH),
							description="Turret access door"))

		self._add_section("Turret interior enclosure", builds)

	def _create_structure(self):
		super(Turret, self)._create_structure()
		self._create_wall_clearances()
		self._create_walls()
		self._create_stairs()
		self._create_interior_enclosure()

class TurretTaper(BuildingEx):
	# TODO: implement
	# turret base l-1
	#            6
	#    XXX     5
	#   XXXXX    4
	#   XX       3
	#   XX       2
	#    X       1
	#            0
	#  6543210

	# turret base l-2
	#            6
	#            5
	#     XX     4
	#    X       3
	#    X       2
	#            1
	#            0
	#  6543210
	WIDTH = 7
	def __init__(self, *args, **kwargs):
		super(TurretTaper, self).__init__(width=TurretTaper.WIDTH, *args, **kwargs)

	def _create_structure(self):
		super(TurretTaper, self)._create_structure()
		builds = []
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-2,WALL_HEIGHT+2,-4),
									EXTERIOR_WALLS,
									Building.SE_CORNER_POS + Vec3(-4,WALL_HEIGHT+2,-5)))

		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-4,WALL_HEIGHT+2,-4),
									EXTERIOR_WALLS,
									Building.SE_CORNER_POS + Vec3(-5,WALL_HEIGHT+2,-2)))

		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-1,WALL_HEIGHT+2,-4),
									EXTERIOR_WALLS))
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-4,WALL_HEIGHT+2,-1),
									EXTERIOR_WALLS))

		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-2,WALL_HEIGHT+1,-4),
									EXTERIOR_WALLS,
									Building.SE_CORNER_POS + Vec3(-3,WALL_HEIGHT+1,-4)))

		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-4,WALL_HEIGHT+1,-3),
									EXTERIOR_WALLS,
									Building.SE_CORNER_POS + Vec3(-4,WALL_HEIGHT+1,-2)))

		self._add_section("Turret base", builds)
