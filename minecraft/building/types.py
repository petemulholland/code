import mcpi.block as block

PAINTING = block.Block(321)

class PlankData:
	OAK = 0
	SPRUCE = 1
	BIRCH = 2
	JUNGLE = 3
	ACACIA = 4 
	DARK_OAK = 5

TORCH_REDSTONE_INACTIVE = block.Block(75)
TORCH_REDSTONE_ACTIVE = block.Block(76)

STAIRS_BRICK =		block.Block(108)
STAIRS_STONE_BRICK = block.Block(109)
STAIRS_NETHER_BRICK = block.Block(114)
STAIRS_SANDSTONE =	block.Block(128)
STAIRS_SPRUCE =		block.Block(134)
STAIRS_BIRCH =		block.Block(135)
STAIRS_JUNGLE =		block.Block(136)
STAIRS_QUARTZ =		block.Block(156)

# TODO: other oriented blocks to be defined: ??
# http://minecraft.gamepedia.com/Data_values#Block_IDs
#	- redstone repeater
#	- piston (& sticky piston)
#	- button
#	- lever
#	- hopper
#	- sign
#	- painting?
#	- dispenser
#	- fence gate?
#	- bookshelf - no orientation data
#	- wood

# TODO: implement hopper
''' Hopper
0x1, 0x2, 0x4:
A three-bit field storing a value from 0 to 5:

	0: Output facing down
	1: (unused)
	2: Output facing north
	3: Output facing south
	4: Output facing west
	5: Output facing east
0x8 	Set if activated/disabled.
'''
HOPPER = block.Block(154)

# no orientation data for bookshelves, self orienting?
BOOK_SHELF = block.Block(47)
NETHER_BRICK_FENCE = block.Block(113)
ENCHANTING_TABLE = block.Block(116)
CAULDRON = block.Block(118)
ANVIL = block.Block(145)
