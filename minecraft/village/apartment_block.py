from building import Building, BuildingLayer, BuildingBlock
from oriented_blocks import Stair, Torch, Door
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3

# TODO: building base classes aren't going to work for apartment block composted of small apartments.
#		need to layout apartment block as whole building
#		add surrounding farms in the build method (or just add to bluepritn layers in init?)
#       6 apartments per floor with window beside front door, end apts can have side windows too.
#		add stone walkway (1x block wide) on ground floor
#		add wooden plank walkway around top with stairs down at front
class Apartment(Building):
	
	WALLS_CORNER_POS = {'South East' : Building.SE_CORNER_POS,
						'South West' : Building.SE_CORNER_POS + Vec3(-6,0,0),
						'North West' : Building.SE_CORNER_POS + Vec3(-6,0,-4),
						'North East' : Building.SE_CORNER_POS + Vec3(0,0,-4)}

	WALL_SPANS = [(WALLS_CORNER_POS['South West'] + Vec3(0,0,-1), 
						WALLS_CORNER_POS['North West'] + Vec3(0,0,1), "West Wall"),
					(WALLS_CORNER_POS['North West'] + Vec3(1,0,0), 
						WALLS_CORNER_POS['North East'] + Vec3(-1,0,0), "North Wall"),
					(WALLS_CORNER_POS['North East'] + Vec3(0,0,1), 
						WALLS_CORNER_POS['South East'] + Vec3(0,0,-1), "East Wall"),
					(WALLS_CORNER_POS['South East'] + Vec3(-1,0,0), 
						WALLS_CORNER_POS['South West'] + Vec3(1,0,0), "South Wall")]

	DOOR_POS = WALLS_CORNER_POS['South East'] + Vec3(-2,0,0)
	STEP_POS = DOOR_POS + Vec3(0,0,1)
	TORCH_POS = DOOR_POS + Vec3(0,0,-1)

	WIN_POS = WALLS_CORNER_POS['South East'] + Vec3(-4,0,0)

	WIDTH = 7
	def __init__(self, *args, **kwargs):
		super(Apartment, self).__init__(width=Apartment.WIDTH, *args, **kwargs)

		#######################################################################
		# Level 1:
		layer_blocks = []
		layer_blocks.append(BuildingBlock(Apartment.WALLS_CORNER_POS['South West'], 
							  block.COBBLESTONE, Apartment.WALLS_CORNER_POS['North East'],
							  description="House base"))
		layer_blocks.append(Stair(Apartment.STEP_POS, 
								block.STAIRS_COBBLESTONE.withData(Stair.NORTH),
								description="Front step"))

		self.add_layer(BuildingLayer(layer_blocks, 0))
		del layer_blocks [:]

		#######################################################################
		# Common blocks:
		walls = []
		
		# cobblestone corners
		for key, pos in Apartment.WALLS_CORNER_POS.items():
			walls.append(BuildingBlock(pos, block.COBBLESTONE, description="Corner stone"))
		
		# wood plank walls 
		for pos1, pos2, desc in Apartment.WALL_SPANS:
			walls.append(BuildingBlock(pos1, block.WOOD_PLANKS, pos2, desc))

		#######################################################################
		# Level 2:
		# add walls as above & clear door	
		layer_blocks.extend(walls)
		
		layer_blocks.append(BuildingBlock(Apartment.DOOR_POS, block.AIR, description="Clear door"))
		self.add_layer(BuildingLayer(layer_blocks, 1))
		del layer_blocks [:]

		#######################################################################
		# Level 3:
		# add walls, clear door	& add windows
		layer_blocks.extend(walls)
			
		layer_blocks.append(BuildingBlock(Apartment.DOOR_POS, block.AIR, description="Clear door"))

		for pos in Apartment.WIN_POS:
			layer_blocks.append(BuildingBlock(pos, block.GLASS_PANE, description="Window"))

		self.add_layer(BuildingLayer(layer_blocks, 2))
		del layer_blocks [:]

		#######################################################################
		# Level 4:
		# add walls & torch over door	
		layer_blocks.extend(walls)
			
		layer_blocks.append(Torch(Apartment.TORCH_POS, block.TORCH.withData(Torch.NORTH), 
									description="Torch over door"))
		self.add_layer(BuildingLayer(layer_blocks, 3))
		del layer_blocks [:]

		#######################################################################
		# build the roof
		layer_blocks.append(BuildingBlock(Apartment.WALLS_CORNER_POS['South East'], 
							block.WOOD, Apartment.WALLS_CORNER_POS['North West'],
							description="Roof wood span"))
		layer_blocks.append(BuildingBlock(Apartment.WALLS_CORNER_POS['South East'] + Vec3(-1,0,-1), 
							block.WOOD_PLANKS, Apartment.WALLS_CORNER_POS['North West'] + Vec3(1,0,1),
							description="Roof wood plank span"))

		layer_blocks.append(BuildingBlock(Apartment.LADDER_POS, block.AIR, description="Clear ladder space"))
		
		layer_blocks.append(ladder)

		self.add_layer(BuildingLayer(layer_blocks, 4))
		del layer_blocks [:]

		#######################################################################
		# add the fences to the roof
		layer_blocks.append(BuildingBlock(Apartment.WALLS_CORNER_POS['South East'], 
							block.FENCE, Apartment.WALLS_CORNER_POS['North West'],
							description="Cover roof with fences"))
		layer_blocks.append(BuildingBlock(Apartment.WALLS_CORNER_POS['South East'] + Vec3(-1,0,-1), 
							block.AIR, Apartment.WALLS_CORNER_POS['North West'] + Vec3(1,0,1),
							description="Clear fences from inner roof"))

		self.add_layer(BuildingLayer(layer_blocks, 5))
		del layer_blocks [:]

		#######################################################################
		# add the door
		self.add_block(Door(Door.HINGE_RIGHT, 
							Vec3(Apartment.DOOR_POS.x, 1, Apartment.DOOR_POS.z), 
							block.DOOR_WOOD.withData(Door.SOUTH)))

		self._set_orientation()

		
	def build(self, mc):
		super(Apartment, self).build(mc)

class ApartmentBlock(Building):
	WIDTH = 7

	def build(self, mc):
		super(ApartmentBlock, self).build(mc)

