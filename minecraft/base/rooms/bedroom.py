from building import Building, BuildingEx, BuildingBlock, Torch, Door, Chest
from base.constants import WALL_HEIGHT, INTERIOR_WALLS
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3

class Bedroom(BuildingEx):
	WIDTH = 22
	def __init__(self, *args, **kwargs):
		super(Bedroom, self).__init__(width=Bedroom.WIDTH, *args, **kwargs)

	def _create_structure(self):
		super(Bedroom, self)._create_structure()
		builds = []

		builds.append(BuildingBlock(Building.SE_CORNER_POS,
									INTERIOR_WALLS, 
									Building.SE_CORNER_POS + Vec3(-21,WALL_HEIGHT,0),
									description="Bedroom wall"))
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-21,0,0),
									INTERIOR_WALLS, 
									Building.SE_CORNER_POS + Vec3(-21,WALL_HEIGHT,-8),
									description="Bedroom wall"))
		builds.append(BuildingBlock(Building.SE_CORNER_POS,
									INTERIOR_WALLS, 
									Building.SE_CORNER_POS + Vec3(0,WALL_HEIGHT,-8),
									description="Bedroom wall"))

		builds.append(Door(Door.HINGE_RIGHT, 
							Building.SE_CORNER_POS + Vec3(-11,0,0),
							block.DOOR_WOOD.withData(Door.SOUTH),
							description="Bedroom door"))
		builds.append(Door(Door.HINGE_LEFT, 
							Building.SE_CORNER_POS + Vec3(-12,0,0),
							block.DOOR_WOOD.withData(Door.SOUTH),
							description="Bedroom door"))
		self._add_section("Bedroom shell", builds)

