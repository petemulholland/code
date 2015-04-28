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

		# windows:
		builds.append(BuildingBlock(Bedroom.WALLS_CORNER_POS['North East'] + Vec3(-3,1,0),
									block.GLASS_PANE, 
									Bedroom.WALLS_CORNER_POS['North East'] + Vec3(-4,2,0),
									description="window"))
		builds.append(BuildingBlock(Bedroom.WALLS_CORNER_POS['North East'] + Vec3(-7,1,0),
									block.GLASS_PANE, 
									Bedroom.WALLS_CORNER_POS['North East'] + Vec3(-8,2,0),
									description="window"))
		builds.append(BuildingBlock(Bedroom.WALLS_CORNER_POS['North East'] + Vec3(-13,1,0),
									block.GLASS_PANE, 
									Bedroom.WALLS_CORNER_POS['North East'] + Vec3(-14,2,0),
									description="window"))
		builds.append(BuildingBlock(Bedroom.WALLS_CORNER_POS['North East'] + Vec3(-17,1,0),
									block.GLASS_PANE, 
									Bedroom.WALLS_CORNER_POS['North East'] + Vec3(-18,2,0),
									description="window"))
		self._add_section("Bedroom windows", builds)

		# torches
		self._add_section("Bedroom torches", builds)
		builds.append(Torch(Bedroom.WALLS_CORNER_POS['South East'] + Vec3(-6,2,-8),
							block.TORCH.withData(Torch.SOUTH)))
		builds.append(Torch(Bedroom.WALLS_CORNER_POS['South West'] + Vec3(-15,2,-8),
							block.TORCH.withData(Torch.SOUTH)))

		builds.append(Torch(Bedroom.WALLS_CORNER_POS['South East'] + Vec3(-6,2,-1),
							block.TORCH.withData(Torch.SOUTH)))
		builds.append(Torch(Bedroom.WALLS_CORNER_POS['South West'] + Vec3(-15,2,-1),
							block.TORCH.withData(Torch.SOUTH)))

		builds.append(Torch(Bedroom.WALLS_CORNER_POS['South East'] + Vec3(-1,2,-4),
							block.TORCH.withData(Torch.SOUTH)))
		builds.append(Torch(Bedroom.WALLS_CORNER_POS['South West'] + Vec3(-20,2,-4),
							block.TORCH.withData(Torch.SOUTH)))
