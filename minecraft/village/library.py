from building import Building, BuildingLayer, BuildingBlock
from oriented_blocks import Torch, Stair, Ladder
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3

class Library(Building):
	"""description of class"""
	WALLS_CORNER_POS = {'South West' : Vec3(-7,0,-2),
						'North West' : Vec3(-7,0,-7),
						'North East' : Vec3(1,0,-7),
						'South East' : Vec3(1,0,-2) }

	NORTH_WIN_SPANS = {'North West' : (Vec3(-4,0,-7), Vec3(-5,0,-7)),
						'North East' : (Vec3(-1,0,-7), Vec3(-2,0,-7)) }

	OTHER_WIN_SPANS = {'West' : (Vec3(-7,0,-4), Vec3(-7,0,-5)),
						'East' : (Vec3(1,0,-5), Vec3(1,0,-4)),
						'South' : (Vec3(-2,0,3), Vec3(-2,0,5)), }

	DOOR_POS = Vec3(0,0,-2)
	
	def __init__(self, *args, **kwargs):
		super(Library, self).__init__(*args, **kwargs)

		offset = self.build_pos
		layer_blocks = []

		########################################################################
		# level 1
		layer_blocks.append(BuildingBlock(offset, Library.WALLS_CORNER_POS['South West'], 
										block.COBBLESTONE, Library.WALLS_CORNER_POS['North East'],
										description="Floor"))

		layer_blocks.append(Stair(offset, Library.DOOR_POS + Vec3(0,0,1), 
								block.STAIRS_COBBLESTONE.withData(Stair.NORTH), 
								description="Front door step"))

		self.layers.append(BuildingLayer(layer_blocks, 0))
		del layer_blocks[:]

		# level 2
		layer_blocks.append(BuildingBlock(offset, Library.WALLS_CORNER_POS['South West'], 
										block.COBBLESTONE, Library.WALLS_CORNER_POS['North West'],
										description="West wall"))
		layer_blocks.append(BuildingBlock(offset, Library.WALLS_CORNER_POS['North West'], 
										block.COBBLESTONE, Library.WALLS_CORNER_POS['North East'],
										description="North wall"))
		layer_blocks.append(BuildingBlock(offset, Library.WALLS_CORNER_POS['North East'], 
										block.COBBLESTONE, Library.WALLS_CORNER_POS['South East'],
										description="East wall"))
		layer_blocks.append(BuildingBlock(offset, Library.WALLS_CORNER_POS['South East'], 
										block.COBBLESTONE, Library.WALLS_CORNER_POS['South West'],
										description="South wall"))
		# Clear door space
		layer_blocks.append(BuildingBlock(offset, Library.DOOR_POS, 
										block.AIR, description="Clear door"))
		# seats corner
		layer_blocks.append(BuildingBlock(offset, Library.WALLS_CORNER_POS['North West'] + Vec3(1,0,1),
										block.WOOD_PLANKS, description="seat corner"))
		# seats
		layer_blocks.append(Stair(offset, Library.WALLS_CORNER_POS['North West'] + Vec3(1,0,2),
								block.STAIRS_WOOD.withData(Stair.WEST), 
								description="west seat"))
		layer_blocks.append(Stair(offset, Library.WALLS_CORNER_POS['North West'] + Vec3(2,0,1),
								block.STAIRS_WOOD.withData(Stair.NORTH), 
								Library.WALLS_CORNER_POS['North West'] + Vec3(5,0,1),
								description="north seats"))
		# table bases 
		layer_blocks.append(BuildingBlock(offset, Vec3(-3,0,-5),
										block.FENCE, description="table base"))
		layer_blocks.append(BuildingBlock(offset, Vec3(-5,0,-5),
										block.FENCE, description="table base"))

		layer_blocks.append(BuildingBlock(offset, Library.WALLS_CORNER_POS['South West'] + Vec3(1,0,-1),
								block.CRAFTING_TABLE, description="crafting table"))

		# TODO: seats tables & crafting table
		self.layers.append(BuildingLayer(layer_blocks, 1))
		del layer_blocks[:]

		########################################################################
		# Common sets of blocks
		corners = []
		for key, pos in Library.WALLS_CORNER_POS.items():
			corners.append(BuildingBlock(offset, pos, block.COBBLESTONE,
										description=key + " corner"))
		# north windows are only used on 1 layer,
		# east, south & west are used on 2 levels
		other_windows = []
		for key, span in Library.OTHER_WIN_SPANS.items():
			other_windows.append(BuildingBlock(offset, span[0], block.AIR, span[1],
									  description= "Clearing " + key + " window"))
			other_windows.append(BuildingBlock(offset, span[0], block.GLASS_PANE, span[1],
									  description= key + " window"))
		
		# these walls are used on 3 levels	
		walls = []
		walls.append(BuildingBlock(offset, Library.WALLS_CORNER_POS['South West'] + Vec3(0,0,-1), 
										block.WOOD_PLANKS, Library.WALLS_CORNER_POS['North West'] + Vec3(0,0,1),
										description="West wall"))
		walls.append(BuildingBlock(offset, Library.WALLS_CORNER_POS['North West'] + Vec3(1,0,0), 
										block.WOOD_PLANKS, Library.WALLS_CORNER_POS['North East'] + Vec3(-1,0,0),
										description="North wall"))
		walls.append(BuildingBlock(offset, Library.WALLS_CORNER_POS['North East'] + Vec3(0,0,1), 
										block.WOOD_PLANKS, Library.WALLS_CORNER_POS['South East'] + Vec3(0,0,-1),
										description="East wall"))
		walls.append(BuildingBlock(offset, Library.WALLS_CORNER_POS['South East'] + Vec3(-1,0,0), 
										block.WOOD_PLANKS, Library.WALLS_CORNER_POS['South West'] + Vec3(1,0,0),
										description="South wall"))
			
		########################################################################
		# level 3
		# corners & walls
		layer_blocks.extend(corners)
		layer_blocks.extend(walls)

		# walls 
		# north windows
		for key, span in Library.NORTH_WIN_SPANS.items():
			layer_blocks.append(BuildingBlock(offset, span[0], block.AIR, span[1],
									  description= "Clearing " + key + " window"))
			layer_blocks.append(BuildingBlock(offset, span[0], block.GLASS_PANE, span[1],
									  description= key + " window"))
		# other windows
		layer_blocks.extend(other_windows)

		# Clear door space
		layer_blocks.append(BuildingBlock(offset, Library.DOOR_POS, 
										block.AIR, description="clear door"))

		# TODO: add table tops
		# table bases 
		#layer_blocks.append(BuildingBlock(offset, Vec(-3,0,-5),
		#								block.FENCE, description="table base"))
		#layer_blocks.append(BuildingBlock(offset, Vec(-5,0,-5),
		#								block.FENCE, description="table base"))

		self.layers.append(BuildingLayer(layer_blocks, 2))
		del layer_blocks[:]

		########################################################################
		# level 4
		# corners & walls
		layer_blocks.extend(corners)
		layer_blocks.extend(walls)

		# books
		walls.append(BuildingBlock(offset, Library.WALLS_CORNER_POS['North West'] + Vec3(1,0,1), 
										block.BOOKSHELF, Library.WALLS_CORNER_POS['North East'] + Vec3(-1,0,1),
										description="North wall"))

		# other windows
		layer_blocks.extend(other_windows)

		self.layers.append(BuildingLayer(layer_blocks, 3))
		del layer_blocks[:]

		########################################################################
		# level 5
		# corners & walls
		layer_blocks.extend(corners)
		layer_blocks.extend(walls)

		layer_blocks.append(BuildingBlock(offset, Library.WALLS_CORNER_POS['North West'] + Vec3(0,0,1), 
										block.WOOD_PLANKS, Library.WALLS_CORNER_POS['North East'] + Vec3(0,0,1),
										description="North rafters"))
		layer_blocks.append(BuildingBlock(offset, Library.WALLS_CORNER_POS['South East'] + Vec3(0,0,-1), 
										block.WOOD_PLANKS, Library.WALLS_CORNER_POS['South West'] + Vec3(0,0,-1),
										description="South rafters"))

		self.layers.append(BuildingLayer(layer_blocks, 4))
		del layer_blocks[:]

		########################################################################
		# level 6
		layer_blocks.append(BuildingBlock(offset, Library.WALLS_CORNER_POS['South West'], 
										block.COBBLESTONE, Library.WALLS_CORNER_POS['North East'],
										description="Ceiling"))
		# north and south roof eaves
		layer_blocks.append(Stair(offset, Library.WALLS_CORNER_POS['North West'] + Vec3(0,0,-1), 
										block.STAIRS_WOOD.withData(Stair.SOUTH), 
										Library.WALLS_CORNER_POS['North East'] + Vec3(0,0,-1),
										description="North roof eaves"))
		layer_blocks.append(Stair(offset, Library.WALLS_CORNER_POS['South East'] + Vec3(0,0,1), 
										block.STAIRS_WOOD.withData(Stair.NORTH), 
										Library.WALLS_CORNER_POS['South West'] + Vec3(0,0,1),
										description="South roof eaves"))

		self.layers.append(BuildingLayer(layer_blocks, 5))
		del layer_blocks[:]

		########################################################################
		# level 7
		layer_blocks.append(BuildingBlock(offset, Library.WALLS_CORNER_POS['South West'] + Vec3(0,0,-1), 
										block.COBBLESTONE, Library.WALLS_CORNER_POS['North East'] + Vec3(0,0,1),
										description="Ceiling"))
		# north and south roof eaves
		layer_blocks.append(Stair(offset, Library.WALLS_CORNER_POS['North West'], 
										block.STAIRS_WOOD.withData(Stair.SOUTH), 
										Library.WALLS_CORNER_POS['North East'],
										description="North roof eaves"))
		layer_blocks.append(Stair(offset, Library.WALLS_CORNER_POS['South East'], 
										block.STAIRS_WOOD.withData(Stair.NORTH), 
										Library.WALLS_CORNER_POS['South West'],
										description="South roof eaves"))

		self.layers.append(BuildingLayer(layer_blocks, 6))
		del layer_blocks[:]

		########################################################################
		# level 8
		# TODO: adjust positsions
		layer_blocks.append(BuildingBlock(offset, Library.WALLS_CORNER_POS['South West'] + Vec3(0,0,-2), 
										block.COBBLESTONE, Library.WALLS_CORNER_POS['North East'] + Vec3(0,0,2),
										description="Ceiling"))
		# north and south roof eaves
		layer_blocks.append(Stair(offset, Library.WALLS_CORNER_POS['North West'] + Vec3(0,0,1), 
										block.STAIRS_WOOD.withData(Stair.SOUTH), 
										Library.WALLS_CORNER_POS['North East'] + Vec3(0,0,1),
										description="North roof eaves"))
		layer_blocks.append(Stair(offset, Library.WALLS_CORNER_POS['South East'] + Vec3(0,0,-1), 
										block.STAIRS_WOOD.withData(Stair.NORTH), 
										Library.WALLS_CORNER_POS['South West'] + Vec3(0,0,-1),
										description="South roof eaves"))

		self.layers.append(BuildingLayer(layer_blocks, 7))
		del layer_blocks[:]

		########################################################################
		# level 9
		# TODO: adjust positsions
		# north and south roof eaves
		layer_blocks.append(Stair(offset, Library.WALLS_CORNER_POS['North West'] + Vec3(0,0,2), 
										block.STAIRS_WOOD.withData(Stair.SOUTH), 
										Library.WALLS_CORNER_POS['North East'] + Vec3(0,0,2),
										description="North roof eaves"))
		layer_blocks.append(Stair(offset, Library.WALLS_CORNER_POS['South East'] + Vec3(0,0,-2), 
										block.STAIRS_WOOD.withData(Stair.NORTH), 
										Library.WALLS_CORNER_POS['South West'] + Vec3(0,0,-2),
										description="South roof eaves"))

		self.layers.append(BuildingLayer(layer_blocks, 8))
		del layer_blocks[:]

		########################################################################
		self._set_orientation()
		
	def build(self, mc):
		super(Library, self).build(mc)

