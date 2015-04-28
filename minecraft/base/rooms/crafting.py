from building import Building, BuildingEx, BuildingBlock, Torch, Chest, Door
from base_room import UpperRoomBase
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3

class CraftingRoom(UpperRoomBase):
	def __init__(self, *args, **kwargs):
		super(CraftingRoom, self).__init__(*args, **kwargs)

	def _create_structure(self):
		super(CraftingRoom, self)._create_structure()
		builds = []
		builds.append(Door(Door.HINGE_RIGHT, 
							UpperRoomBase.WALLS_CORNER_POS['South East'] + Vec3(-3,0,0),
							block.DOOR_WOOD.withData(Door.SOUTH),
							description="Crafting room door"))
		builds.append(Door(Door.HINGE_LEFT, 
							UpperRoomBase.WALLS_CORNER_POS['South East'] + Vec3(-4,0,0),
							block.DOOR_WOOD.withData(Door.SOUTH),
							description="Crafting room door"))
		self._add_section("Crafting room doors", builds)
