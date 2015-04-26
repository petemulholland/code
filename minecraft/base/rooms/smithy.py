from building import Building, BuildingEx, BuildingBlock, SubBuilding, Torch, Chest
from building.types import ANVIL
from base_room import GroundRoomBase
from base.fixtures import OpenDoorway
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3

class Smithy(GroundRoomBase):
	# - smithy (anvil, crafting table & chests
	# ss  ssss
	# s   at s
	# s      s
	#       cs
	#       cs
	# s      s
	# scc  ccs
	# ssssssss
	def __init__(self, *args, **kwargs):
		super(Smithy, self).__init__(*args, **kwargs)

	def _create_structure(self):
		super(Smithy, self)._create_structure()
		builds = []
		builds.append(SubBuilding(OpenDoorway(Building.NORTH), Building.SE_CORNER_POS + Vec3(-3,0,0)))
		builds.append(SubBuilding(OpenDoorway(Building.EAST), Smithy.WALLS_CORNER_POS['South West'] + Vec3(0,0,-2)))

		builds.append(BuildingBlock(Smithy.WALLS_CORNER_POS['North East'] + Vec3(-2,1,0),
									block.GLASS_PANE,
									Smithy.WALLS_CORNER_POS['North East'] + Vec3(-5,1,0),
									description="Window"))
		self._add_section("Doorways", builds)
		
		############################################################################
		# TODO: add fittings

		builds.append(BuildingBlock(Smithy.WALLS_CORNER_POS['North West'] + Vec3(1,0,2),
									ANVIL,
									description="Anvil"))
		builds.append(BuildingBlock(Smithy.WALLS_CORNER_POS['North West'] + Vec3(1,0,1),
									block.CRAFTING_TABLE,
									description="crafting table"))

		builds.append(Chest(Smithy.WALLS_CORNER_POS['South East'] + Vec3(-1,0,-1), 
							block.CHEST.withData(Chest.EAST), 
							Smithy.WALLS_CORNER_POS['South East'] + Vec3(-2,1,-1), 
							description="South wall chests"))
		builds.append(Chest(Smithy.WALLS_CORNER_POS['South West'] + Vec3(1,0,-1), 
							block.CHEST.withData(Chest.EAST), 
							Smithy.WALLS_CORNER_POS['South West'] + Vec3(2,1,-1), 
							description="South wall chests"))

		builds.append(Chest(Smithy.WALLS_CORNER_POS['North East'] + Vec3(-1,0,1), 
							block.CHEST.withData(Chest.EAST), 
							Smithy.WALLS_CORNER_POS['North East'] + Vec3(-2,1,1), 
							description="South wall chests"))

		builds.append(Chest(Smithy.WALLS_CORNER_POS['South East'] + Vec3(-1,0,-3), 
							block.CHEST.withData(Chest.EAST), 
							Smithy.WALLS_CORNER_POS['South East'] + Vec3(-1,1,-4), 
							description="South wall chests"))


		self._add_section("Fittings", builds)

		############################################################################
		#torches, 
		# south wall torches either side of arched doorway
		builds.append(Torch(Smithy.WALLS_CORNER_POS['South East'] + Vec3(-2,2,-1),
							block.TORCH.withData(Torch.NORTH)))
		builds.append(Torch(Smithy.WALLS_CORNER_POS['South West'] + Vec3(2,2,-1),
							block.TORCH.withData(Torch.NORTH)))
		
		# torches in north east corner on north & east walls
		builds.append(Torch(Smithy.WALLS_CORNER_POS['North East'] + Vec3(-2,2,1),
							block.TORCH.withData(Torch.SOUTH)))
		builds.append(Torch(Smithy.WALLS_CORNER_POS['North East'] + Vec3(-1,2,2),
							block.TORCH.withData(Torch.WEST)))

		# torches in north west corner on north & west walls.
		builds.append(Torch(Smithy.WALLS_CORNER_POS['North West'] + Vec3(2,2,1),
							block.TORCH.withData(Torch.SOUTH)))
		# this is only torch on west wall, move closer to center
		builds.append(Torch(Smithy.WALLS_CORNER_POS['North West'] + Vec3(1,2,3),
							block.TORCH.withData(Torch.EAST)))

		# torch over doorway to corridor
		builds.append(Torch(Smithy.WALLS_CORNER_POS['South East'] + Vec3(-1,2,-2),
							block.TORCH.withData(Torch.WEST)))

		self._add_section("Torches", builds)
