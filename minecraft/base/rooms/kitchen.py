from building import Building, BuildingEx, BuildingBlock, SubBuilding, Torch, Furnace, Chest, Door
from base_room import GroundRoomBase
from building.types import CAULDRON
from base.fixtures import OpenDoorway
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3

class Kitchen(GroundRoomBase):
	# sssssdss
	# swwws cs	  c => chest, w = water
	# wssss cs	  w => window, c => chest
	# wp         w => window, p => wood planks, space => open doorway
	# wc         w => window, c => cauldron
	# wt    cs   w => window, t => crafting table, c => chest
	# spff  cs   p => wood planks, f => furnace
	# ssss  ss

	def __init__(self, *args, **kwargs):
		super(Kitchen, self).__init__(*args, **kwargs)

	def _create_structure(self):
		super(Kitchen, self)._create_structure()
		builds = []
		############################################################################
		# Open arched doorways
		builds.append(SubBuilding(OpenDoorway(Building.NORTH), Building.SE_CORNER_POS + Vec3(-3,0,0)))
		builds.append(SubBuilding(OpenDoorway(Building.EAST), Kitchen.WALLS_CORNER_POS['South West'] + Vec3(0,0,-2)))

		# window & door across corridor to dining hall
		builds.append(BuildingBlock(Kitchen.WALLS_CORNER_POS['North East'] + Vec3(-2,1,0),
									block.GLASS_PANE,
									Kitchen.WALLS_CORNER_POS['North East'] + Vec3(-5,1,0),
									description="Window"))
		builds.append(Door(Door.HINGE_RIGHT, 
							Kitchen.WALLS_CORNER_POS['South East'] + Vec3(0,0,-2), 
							block.DOOR_WOOD.withData(Door.EAST),
							description="Door"))

		self._add_section("Doorways", builds)
		
		############################################################################
		# TODO: add fittings
		builds.append(BuildingBlock(Kitchen.WALLS_CORNER_POS['North East'] + Vec3(-2,0,1),
									block.STONE_BRICK,
									Kitchen.WALLS_CORNER_POS['North East'] + Vec3(-1,0,4),
									description="Well wall"))
		builds.append(BuildingBlock(Kitchen.WALLS_CORNER_POS['North East'] + Vec3(-1,0,1),
									block.WATER,
									Kitchen.WALLS_CORNER_POS['North East'] + Vec3(-1,0,3),
									description="Well water"))

		builds.append(BuildingBlock(Kitchen.WALLS_CORNER_POS['North East'] + Vec3(-3,0,1),
									block.WOOD_PLANKS,
									description="counter"))
		builds.append(BuildingBlock(Kitchen.WALLS_CORNER_POS['North East'] + Vec3(-4,0,1),
									CAULDRON,
									description="sink"))
		builds.append(BuildingBlock(Kitchen.WALLS_CORNER_POS['North East'] + Vec3(-5,0,1),
									block.CRAFTING_TABLE,
									description="crafting table"))
		builds.append(BuildingBlock(Kitchen.WALLS_CORNER_POS['North East'] + Vec3(-6,0,1),
									block.WOOD_PLANKS,
									description="counter"))

		builds.append(Furnace(Kitchen.WALLS_CORNER_POS['North West'] + Vec3(1,0,2),
							  block.FURNACE_INACTIVE.withData(Furnace.EAST),
							  description="range"))
		builds.append(Furnace(Kitchen.WALLS_CORNER_POS['North West'] + Vec3(1,0,3),
							  block.FURNACE_INACTIVE.withData(Furnace.EAST),
							  description="range"))

		builds.append(Chest(Kitchen.WALLS_CORNER_POS['South East'] + Vec3(-1,0,-1), 
							block.CHEST.withData(Chest.EAST), 
							Kitchen.WALLS_CORNER_POS['South East'] + Vec3(-2,1,-1), 
							description="Chest"))
		builds.append(Chest(Kitchen.WALLS_CORNER_POS['South West'] + Vec3(1,0,-1), 
							block.CHEST.withData(Chest.EAST), 
							Kitchen.WALLS_CORNER_POS['South West'] + Vec3(2,1,-1), 
							description="Chest"))

		self._add_section("Fittings", builds)

		############################################################################
		#torches, 
		# south wall torches either side of arched doorway
		builds.append(Torch(Kitchen.WALLS_CORNER_POS['South East'] + Vec3(-2,2,-1),
							block.TORCH.withData(Torch.NORTH)))
		builds.append(Torch(Kitchen.WALLS_CORNER_POS['South West'] + Vec3(2,2,-1),
							block.TORCH.withData(Torch.NORTH)))
		
		# torches in north east corner on north & east walls
		builds.append(Torch(Kitchen.WALLS_CORNER_POS['North East'] + Vec3(-2,2,1),
							block.TORCH.withData(Torch.SOUTH)))
		builds.append(Torch(Kitchen.WALLS_CORNER_POS['North East'] + Vec3(-1,2,2),
							block.TORCH.withData(Torch.WEST)))

		# torches in north west corner on north & west walls.
		builds.append(Torch(Kitchen.WALLS_CORNER_POS['North West'] + Vec3(2,2,1),
							block.TORCH.withData(Torch.SOUTH)))
		# this is only torch on west wall, move closer to center
		builds.append(Torch(Kitchen.WALLS_CORNER_POS['North West'] + Vec3(1,2,3),
							block.TORCH.withData(Torch.EAST)))

		# torch over doorway to corridor
		builds.append(Torch(Kitchen.WALLS_CORNER_POS['South East'] + Vec3(-1,2,-2),
							block.TORCH.withData(Torch.WEST)))

		self._add_section("Torches", builds)

