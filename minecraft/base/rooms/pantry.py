from building import Building, BuildingEx, BuildingBlock, SubBuilding, Torch, Chest
from base_room import GroundRoomBase
from base.fixtures import OpenDoorway
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3

class Pantry(GroundRoomBase):
	# - pantry (chests for raw & cooked food)

	"""description of class"""
	def __init__(self, *args, **kwargs):
		super(Pantry, self).__init__(*args, **kwargs)

	def _create_structure(self):
		super(Pantry, self)._create_structure()
		builds = []
		builds.append(SubBuilding(OpenDoorway(Building.NORTH), Building.SE_CORNER_POS + Vec3(-3,0,0)))
		builds.append(SubBuilding(OpenDoorway(Building.EAST), Pantry.WALLS_CORNER_POS['South East'] + Vec3(0,0,-2)))

		self._add_section("Pantry Doorways", builds)

		############################################################################
		# add chests
		# on south wall 
		builds.append(Chest(Pantry.WALLS_CORNER_POS['South East'] + Vec3(-1,0,-1), 
							block.CHEST.withData(Chest.EAST), 
							Pantry.WALLS_CORNER_POS['South East'] + Vec3(-2,1,-1), 
							description="South wall chests"))
		builds.append(Chest(Pantry.WALLS_CORNER_POS['South West'] + Vec3(1,0,-1), 
							block.CHEST.withData(Chest.EAST), 
							Pantry.WALLS_CORNER_POS['South West'] + Vec3(2,1,-1), 
							description="South wall chests"))

		# on north wall
		builds.append(Chest(Pantry.WALLS_CORNER_POS['North East'] + Vec3(-2,0,1), 
							block.CHEST.withData(Chest.EAST), 
							Pantry.WALLS_CORNER_POS['North East'] + Vec3(-3,1,1), 
							description="South wall chests"))
		builds.append(Chest(Pantry.WALLS_CORNER_POS['North West'] + Vec3(1,0,1), 
							block.CHEST.withData(Chest.EAST), 
							Pantry.WALLS_CORNER_POS['North West'] + Vec3(2,1,1), 
							description="South wall chests"))

		# on west wall
		builds.append(Chest(Pantry.WALLS_CORNER_POS['South West'] + Vec3(1,0,-3), 
							block.CHEST.withData(Chest.EAST), 
							Pantry.WALLS_CORNER_POS['South West'] + Vec3(1,1,-4), 
							description="South wall chests"))

		# on east wall 
		builds.append(Chest(Pantry.WALLS_CORNER_POS['North East'] + Vec3(-1,0,2), 
							block.CHEST.withData(Chest.EAST), 
							Pantry.WALLS_CORNER_POS['North East'] + Vec3(-1,1,3), 
							description="South wall chests"))

		self._add_section("Pantry Chests", builds)

		############################################################################
		#torches, 
		# south wall torches either side of arched doorway
		builds.append(Torch(Pantry.WALLS_CORNER_POS['South East'] + Vec3(-2,2,-1),
							block.TORCH.withData(Torch.NORTH)))
		builds.append(Torch(Pantry.WALLS_CORNER_POS['South West'] + Vec3(2,2,-1),
							block.TORCH.withData(Torch.NORTH)))
		# torch on west wall sw corner
		builds.append(Torch(Pantry.WALLS_CORNER_POS['South West'] + Vec3(1,2,-2),
							block.TORCH.withData(Torch.EAST)))
		
		# torches in north east corner on north & east walls
		builds.append(Torch(Pantry.WALLS_CORNER_POS['North East'] + Vec3(-2,2,1),
							block.TORCH.withData(Torch.SOUTH)))
		# this is only torch on west wall, move closer to center
		builds.append(Torch(Pantry.WALLS_CORNER_POS['North East'] + Vec3(-1,2,3),
							block.TORCH.withData(Torch.WEST)))

		# torches in north west corner on north & west walls.
		builds.append(Torch(Pantry.WALLS_CORNER_POS['North West'] + Vec3(2,2,1),
							block.TORCH.withData(Torch.SOUTH)))
		builds.append(Torch(Pantry.WALLS_CORNER_POS['North West'] + Vec3(1,2,2),
							block.TORCH.withData(Torch.EAST)))

		self._add_section("Pantry Torches", builds)



