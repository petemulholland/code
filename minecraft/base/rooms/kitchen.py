from building import Building, BuildingEx, BuildingBlock, SubBuilding, Torch, Furnace, Chest
from base_room import RoomBase
from base.fixtures import OpenDoorway
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3

class Kitchen(RoomBase):
	# TODO: implement 
	 # -Kitchen (5x5 ?) + well space
	 #	stone slab counter tops - pressure plate is not as high.
	 #	furnaces
	 #	cauldron
	 #	wood slab counter tops
	 #	well

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

		builds = []
		builds.append(SubBuilding(OpenDoorway(Building.NORTH), Building.SE_CORNER_POS + Vec3(-3,0,0)))
		builds.append(SubBuilding(OpenDoorway(Building.EAST), RoomBase.WALLS_CORNER_POS['South West'] + Vec3(0,0,-2)))

		self._add_section("Doorways", builds)
		# TODO: add fittings, torches, windows & door to dining hall
		builds.append(Torch(RoomBase.WALLS_CORNER_POS['South East'] + Vec3(-2,2,-1),
							block.TORCH.withData(Torch.NORTH)))

		builds.append(Torch(RoomBase.WALLS_CORNER_POS['North East'] + Vec3(-2,2,1),
							block.TORCH.withData(Torch.SOUTH)))
		builds.append(Torch(RoomBase.WALLS_CORNER_POS['North East'] + Vec3(-1,2,2),
							block.TORCH.withData(Torch.WEST)))

		builds.append(Torch(RoomBase.WALLS_CORNER_POS['North West'] + Vec3(2,2,1),
							block.TORCH.withData(Torch.SOUTH)))
		builds.append(Torch(RoomBase.WALLS_CORNER_POS['North West'] + Vec3(1,2,2),
							block.TORCH.withData(Torch.EAST)))

		builds.append(Torch(RoomBase.WALLS_CORNER_POS['South West'] + Vec3(2,2,-1),
							block.TORCH.withData(Torch.NORTH)))
		self._add_section("Torches", builds)

		self._set_orientation()

