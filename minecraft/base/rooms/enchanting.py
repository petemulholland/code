from building import Building, BuildingEx, BuildingBlock, SubBuilding, Torch, Chest
from base_room import RoomBase
from base.fixtures import OpenDoorway
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3

class EnchantingRoom(RoomBase):
	# TODO: implement 
	# - enchanting room - close to smithy (4x4 will do for books, + 1 or 2 for storage chests)
	# ssssssss
	# sbbbbb s
	# sb     s
	# sb     s
	# sb     s
	#        s
	#        s
	# ss  ssss
	def __init__(self, *args, **kwargs):
		super(EnchantingRoom, self).__init__(*args, **kwargs)

		builds = []
		builds.append(SubBuilding(OpenDoorway(Building.NORTH), Building.SE_CORNER_POS + Vec3(-1,0,0)))
		builds.append(SubBuilding(OpenDoorway(Building.EAST), EnchantingRoom.WALLS_CORNER_POS['South East'] + Vec3(0,0,-2)))

		builds.append(BuildingBlock(EnchantingRoom.WALLS_CORNER_POS['North East'] + Vec3(-2,1,0),
									block.GLASS_PANE,
									EnchantingRoom.WALLS_CORNER_POS['North East'] + Vec3(-5,1,0),
									description="Window"))
		self._add_section("Doorways", builds)

		############################################################################
		# TODO: add fittings

		############################################################################
		#torches, 
		# south wall torches either side of arched doorway
		builds.append(Torch(EnchantingRoom.WALLS_CORNER_POS['South East'] + Vec3(-3,2,-1),
							block.TORCH.withData(Torch.NORTH)))
		builds.append(Torch(EnchantingRoom.WALLS_CORNER_POS['South West'] + Vec3(2,2,-1),
							block.TORCH.withData(Torch.NORTH)))
		# torch on west wall sw corner
		builds.append(Torch(EnchantingRoom.WALLS_CORNER_POS['South West'] + Vec3(1,2,-2),
							block.TORCH.withData(Torch.EAST)))
		
		# torches in north east corner on north & east walls
		builds.append(Torch(EnchantingRoom.WALLS_CORNER_POS['North East'] + Vec3(-2,2,1),
							block.TORCH.withData(Torch.SOUTH)))
		# this is only torch on west wall, move closer to center
		builds.append(Torch(EnchantingRoom.WALLS_CORNER_POS['North East'] + Vec3(-1,2,3),
							block.TORCH.withData(Torch.WEST)))

		# torches in north west corner on north & west walls.
		builds.append(Torch(EnchantingRoom.WALLS_CORNER_POS['North West'] + Vec3(2,2,1),
							block.TORCH.withData(Torch.SOUTH)))
		builds.append(Torch(EnchantingRoom.WALLS_CORNER_POS['North West'] + Vec3(1,2,2),
							block.TORCH.withData(Torch.EAST)))

		self._add_section("Torches", builds)

		self._set_orientation()
