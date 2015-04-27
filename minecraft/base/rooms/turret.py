from building import Building, BuildingEx, BuildingBlock, SubBuilding, Torch, Door
from base.constants import EXTERIOR_WALLS, INTERIOR_WALLS, WALL_HEIGHT
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3

class Turret(BuildingEx):
	# TODO: implement 
	#    XXX     6
	#   XsswX    5
	#  XwssssX   4
	#  XssXssXXX 3
	#  Xssw  w   2
	#   Xww  w   1
	#    XXwdw   0
	#     X
	#
	#  6543210

	WIDTH = 7
	def __init__(self, *args, **kwargs):
		super(Turret, self).__init__(width=Turret.WIDTH, *args, **kwargs)

	def _create_wall_clearances(self):
		builds = []
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-3,0,-1),
									block.AIR,
									Building.SE_CORNER_POS + Vec3(-3,WALL_HEIGHT,-2),
									description="turret wall clearance"))
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-1,0,-3),
									block.AIR,
									Building.SE_CORNER_POS + Vec3(-2,WALL_HEIGHT,-3),
									description="turret wall clearance"))
		self._add_section("Wall clearances for turret", builds)

	def _create_walls(self):
		builds = []
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-4,0,0),
									EXTERIOR_WALLS,
									Building.SE_CORNER_POS + Vec3(-4,WALL_HEIGHT+2,0),
									description="turret wall"))
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-5,0,-1),
									EXTERIOR_WALLS,
									Building.SE_CORNER_POS + Vec3(-5,WALL_HEIGHT+2,-1),
									description="turret wall"))
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-6,0,-2),
									EXTERIOR_WALLS,
									Building.SE_CORNER_POS + Vec3(-6,WALL_HEIGHT+2,-4),
									description="turret wall"))
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-5,0,-5),
									EXTERIOR_WALLS,
									Building.SE_CORNER_POS + Vec3(-5,WALL_HEIGHT+2,-5),
									description="turret wall"))
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-4,0,-6),
									EXTERIOR_WALLS,
									Building.SE_CORNER_POS + Vec3(-2,WALL_HEIGHT+2,-6),
									description="turret wall"))
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-1,0,-5),
									EXTERIOR_WALLS,
									Building.SE_CORNER_POS + Vec3(-1,WALL_HEIGHT+2,-5),
									description="turret wall"))
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(0,0,-4),
									EXTERIOR_WALLS,
									Building.SE_CORNER_POS + Vec3(0,WALL_HEIGHT+2,-4),
									description="turret wall"))

		self._add_section("Turret walls", builds)

	def _create_stairs(self):
		builds = []
		self._add_section("Turret stairs", builds)

	def _create_interior_enclosure(self):
		builds = []
		builds.append(BuildingBlock(Building.SE_CORNER_POS,
									INTERIOR_WALLS,
									Building.SE_CORNER_POS + Vec3(-2,WALL_HEIGHT,0),
									description="turret interior wall"))
		builds.append(BuildingBlock(Building.SE_CORNER_POS,
									INTERIOR_WALLS,
									Building.SE_CORNER_POS + Vec3(0,WALL_HEIGHT,-2),
									description="turret interior wall"))
		builds.append(Door(Door.HINGE_LEFT, 
							Building.SE_CORNER_POS + Vec3(-1,0,0),
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
