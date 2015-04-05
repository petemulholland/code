from building import Building, BuildingLayer, BuildingBlock, TABLE_TOP
from oriented_blocks import Torch, Stair, Ladder, Door
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3

class Library(Building):
	"""description of class"""
	WALLS_CORNER_POS = {'South East' : Building.SE_CORNER_POS + Vec3(0,0,-1), 
						'South West' : Building.SE_CORNER_POS + Vec3(-8,0,-1),
						'North West' : Building.SE_CORNER_POS + Vec3(-8,0,-6),
						'North East' : Building.SE_CORNER_POS + Vec3(0,0,-6) }

	NORTH_WIN_SPANS = {'North West' : (WALLS_CORNER_POS['North East'] + Vec3(-5,0,0), 
										WALLS_CORNER_POS['North East'] + Vec3(-6,0,0)),
						'North East' : (WALLS_CORNER_POS['North East'] + Vec3(-2,0,0), 
										WALLS_CORNER_POS['North East'] + Vec3(-3,0,0)) }

	OTHER_WIN_SPANS = {'West' : (WALLS_CORNER_POS['South West'] + Vec3(0,0,-2), 
									WALLS_CORNER_POS['South West'] + Vec3(0,0,-3)),
						'East' : (WALLS_CORNER_POS['South East'] + Vec3(0,0,-2), 
									WALLS_CORNER_POS['South East'] + Vec3(0,0,-3)),
						'South' : (WALLS_CORNER_POS['South East'] + Vec3(-4,0,0), 
									WALLS_CORNER_POS['South East'] + Vec3(-6,0,0)) }

	DOOR_POS = WALLS_CORNER_POS['South East'] + Vec3(-1,0,0)
	
	WIDTH = 9
	def __init__(self, *args, **kwargs):
		super(Library, self).__init__(width=Library.WIDTH, *args, **kwargs)

		layer_blocks = []
		########################################################################
		# level 1
		layer_blocks.append(BuildingBlock(Library.WALLS_CORNER_POS['South West'], 
										block.COBBLESTONE, Library.WALLS_CORNER_POS['North East'],
										description="Floor"))

		layer_blocks.append(Stair(Library.DOOR_POS + Vec3(0,0,1), 
								block.STAIRS_COBBLESTONE.withData(Stair.NORTH), 
								description="Front door step"))

		self.add_layer(BuildingLayer(layer_blocks, 0))
		del layer_blocks[:]

		########################################################################
		# level 2
		layer_blocks.append(BuildingBlock(Library.WALLS_CORNER_POS['South West'], 
										block.COBBLESTONE, Library.WALLS_CORNER_POS['North West'],
										description="West wall"))
		layer_blocks.append(BuildingBlock(Library.WALLS_CORNER_POS['North West'], 
										block.COBBLESTONE, Library.WALLS_CORNER_POS['North East'],
										description="North wall"))
		layer_blocks.append(BuildingBlock(Library.WALLS_CORNER_POS['North East'], 
										block.COBBLESTONE, Library.WALLS_CORNER_POS['South East'],
										description="East wall"))
		layer_blocks.append(BuildingBlock(Library.WALLS_CORNER_POS['South East'], 
										block.COBBLESTONE, Library.WALLS_CORNER_POS['South West'],
										description="South wall"))
		# Clear door space
		layer_blocks.append(BuildingBlock(Library.DOOR_POS, 
										block.AIR, description="Clear door"))
		# seats corner
		layer_blocks.append(BuildingBlock(Library.WALLS_CORNER_POS['North West'] + Vec3(1,0,1),
										block.WOOD_PLANKS, description="seat corner"))
		# seats
		layer_blocks.append(Stair(Library.WALLS_CORNER_POS['North West'] + Vec3(1,0,2),
								block.STAIRS_WOOD.withData(Stair.WEST), 
								description="west seat"))
		layer_blocks.append(Stair(Library.WALLS_CORNER_POS['North West'] + Vec3(2,0,1),
								block.STAIRS_WOOD.withData(Stair.NORTH), 
								Library.WALLS_CORNER_POS['North West'] + Vec3(5,0,1),
								description="north seats"))
		# table bases 
		layer_blocks.append(BuildingBlock(Library.WALLS_CORNER_POS['South West'] + Vec3(2,0,-3),
										block.FENCE, description="table base"))
		layer_blocks.append(BuildingBlock(Library.WALLS_CORNER_POS['South West'] + Vec3(4,0,-3),
										block.FENCE, description="table base"))

		layer_blocks.append(BuildingBlock(Library.WALLS_CORNER_POS['South West'] + Vec3(1,0,-1),
								block.CRAFTING_TABLE, description="crafting table"))

		self.add_layer(BuildingLayer(layer_blocks, 1))
		del layer_blocks[:]

		########################################################################
		# Common sets of blocks
		corners = []
		for key, pos in Library.WALLS_CORNER_POS.items():
			corners.append(BuildingBlock(pos, block.COBBLESTONE,
										description=key + " corner"))
		# north windows are only used on 1 layer,
		# east, south & west are used on 2 levels
		other_windows = []
		for key, span in Library.OTHER_WIN_SPANS.items():
			other_windows.append(BuildingBlock(span[0], block.GLASS_PANE, span[1],
									  description= key + " window"))
		
		# these walls are used on 3 levels	
		walls = []
		walls.append(BuildingBlock(Library.WALLS_CORNER_POS['South West'] + Vec3(0,0,-1), 
										block.WOOD_PLANKS, Library.WALLS_CORNER_POS['North West'] + Vec3(0,0,1),
										description="West wall"))
		walls.append(BuildingBlock(Library.WALLS_CORNER_POS['North West'] + Vec3(1,0,0), 
										block.WOOD_PLANKS, Library.WALLS_CORNER_POS['North East'] + Vec3(-1,0,0),
										description="North wall"))
		walls.append(BuildingBlock(Library.WALLS_CORNER_POS['North East'] + Vec3(0,0,1), 
										block.WOOD_PLANKS, Library.WALLS_CORNER_POS['South East'] + Vec3(0,0,-1),
										description="East wall"))
		walls.append(BuildingBlock(Library.WALLS_CORNER_POS['South East'] + Vec3(-1,0,0), 
										block.WOOD_PLANKS, Library.WALLS_CORNER_POS['South West'] + Vec3(1,0,0),
										description="South wall"))
			
		########################################################################
		# level 3
		# corners & walls
		layer_blocks.extend(corners)
		layer_blocks.extend(walls)

		# north windows
		for key, span in Library.NORTH_WIN_SPANS.items():
			layer_blocks.append(BuildingBlock(span[0], block.GLASS_PANE, span[1],
									  description= key + " window"))
		# other windows
		layer_blocks.extend(other_windows)

		# Clear door space
		layer_blocks.append(BuildingBlock(Library.DOOR_POS, 
										block.AIR, description="clear door"))

		# table bases 
		layer_blocks.append(BuildingBlock(Library.WALLS_CORNER_POS['South West'] + Vec3(2,0,-3),
										TABLE_TOP, description="table top"))
		layer_blocks.append(BuildingBlock(Library.WALLS_CORNER_POS['South West'] + Vec3(4,0,-3),
										TABLE_TOP, description="table top"))


		self.add_layer(BuildingLayer(layer_blocks, 2))
		del layer_blocks[:]

		########################################################################
		# level 4
		# corners & walls
		layer_blocks.extend(corners)
		layer_blocks.extend(walls)

		# books
		layer_blocks.append(BuildingBlock(Library.WALLS_CORNER_POS['North West'] + Vec3(1,0,1), 
											block.BOOKSHELF, 
											Library.WALLS_CORNER_POS['North East'] + Vec3(-1,0,1),
											description="Book shelves"))

		# other windows
		layer_blocks.extend(other_windows)

		self.add_layer(BuildingLayer(layer_blocks, 3))
		del layer_blocks[:]

		########################################################################
		# level 5
		# corners & walls
		layer_blocks.extend(corners)
		layer_blocks.extend(walls)

		layer_blocks.append(BuildingBlock(Library.WALLS_CORNER_POS['North West'] + Vec3(0,0,1), 
										block.WOOD_PLANKS, Library.WALLS_CORNER_POS['North East'] + Vec3(0,0,1),
										description="North rafters"))
		layer_blocks.append(BuildingBlock(Library.WALLS_CORNER_POS['South East'] + Vec3(0,0,-1), 
										block.WOOD_PLANKS, Library.WALLS_CORNER_POS['South West'] + Vec3(0,0,-1),
										description="South rafters"))

		self.add_layer(BuildingLayer(layer_blocks, 4))
		del layer_blocks[:]

		########################################################################
		# level 6
		layer_blocks.append(BuildingBlock(Library.WALLS_CORNER_POS['South West'], 
										block.COBBLESTONE, Library.WALLS_CORNER_POS['North East'],
										description="Ceiling"))
		# north and south roof eaves
		layer_blocks.append(Stair(Library.WALLS_CORNER_POS['North West'] + Vec3(0,0,-1), 
										block.STAIRS_WOOD.withData(Stair.SOUTH), 
										Library.WALLS_CORNER_POS['North East'] + Vec3(0,0,-1),
										description="North roof eaves"))
		layer_blocks.append(Stair(Library.WALLS_CORNER_POS['South East'] + Vec3(0,0,1), 
										block.STAIRS_WOOD.withData(Stair.NORTH), 
										Library.WALLS_CORNER_POS['South West'] + Vec3(0,0,1),
										description="South roof eaves"))

		self.add_layer(BuildingLayer(layer_blocks, 5))
		del layer_blocks[:]

		########################################################################
		# level 7
		layer_blocks.append(BuildingBlock(Library.WALLS_CORNER_POS['South West'] + Vec3(0,0,-1), 
										block.COBBLESTONE, Library.WALLS_CORNER_POS['North East'] + Vec3(0,0,1),
										description="Ceiling"))
		# north and south roof eaves
		layer_blocks.append(Stair(Library.WALLS_CORNER_POS['North West'], 
										block.STAIRS_WOOD.withData(Stair.SOUTH), 
										Library.WALLS_CORNER_POS['North East'],
										description="North roof eaves"))
		layer_blocks.append(Stair(Library.WALLS_CORNER_POS['South East'], 
										block.STAIRS_WOOD.withData(Stair.NORTH), 
										Library.WALLS_CORNER_POS['South West'],
										description="South roof eaves"))

		self.add_layer(BuildingLayer(layer_blocks, 6))
		del layer_blocks[:]

		########################################################################
		# level 8
		# TODO: adjust positsions
		layer_blocks.append(BuildingBlock(Library.WALLS_CORNER_POS['South West'] + Vec3(0,0,-2), 
										block.COBBLESTONE, Library.WALLS_CORNER_POS['North East'] + Vec3(0,0,2),
										description="Ceiling"))
		# north and south roof eaves
		layer_blocks.append(Stair(Library.WALLS_CORNER_POS['North West'] + Vec3(0,0,1), 
										block.STAIRS_WOOD.withData(Stair.SOUTH), 
										Library.WALLS_CORNER_POS['North East'] + Vec3(0,0,1),
										description="North roof eaves"))
		layer_blocks.append(Stair(Library.WALLS_CORNER_POS['South East'] + Vec3(0,0,-1), 
										block.STAIRS_WOOD.withData(Stair.NORTH), 
										Library.WALLS_CORNER_POS['South West'] + Vec3(0,0,-1),
										description="South roof eaves"))

		self.add_layer(BuildingLayer(layer_blocks, 7))
		del layer_blocks[:]

		########################################################################
		# level 9
		# TODO: adjust positsions
		# north and south roof eaves
		layer_blocks.append(Stair(Library.WALLS_CORNER_POS['North West'] + Vec3(0,0,2), 
										block.STAIRS_WOOD.withData(Stair.SOUTH), 
										Library.WALLS_CORNER_POS['North East'] + Vec3(0,0,2),
										description="North roof eaves"))
		layer_blocks.append(Stair(Library.WALLS_CORNER_POS['South East'] + Vec3(0,0,-2), 
										block.STAIRS_WOOD.withData(Stair.NORTH), 
										Library.WALLS_CORNER_POS['South West'] + Vec3(0,0,-2),
										description="South roof eaves"))

		self.add_layer(BuildingLayer(layer_blocks, 8))
		del layer_blocks[:]

		########################################################################
		# add the door
		self.add_block(Door(Door.HINGE_LEFT, 
							Vec3(Library.DOOR_POS.x, 1, Library.DOOR_POS.z), 
							block.DOOR_WOOD.withData(Door.SOUTH)))

		self._set_orientation()
		
	def build(self, mc):
		super(Library, self).build(mc)

