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
#	- wood
#	- anvil
#   - bed

from common_oriented_blocks import Ladder, Chest, Furnace
from torch import Torch
from stair import Stair
from door import Door
from wood import Wood

#Wood NOTE: Acacia & Dark oak were added in 1.7
#Block 17
#	DV 	Description
#	0 	0000 Oak wood facing up/down
#	1 	0001 Spruce wood facing up/down
#	2 	0010 Birch wood facing up/down
#	3 	0011 Jungle wood facing up/down
#	4 	0100 Oak wood facing East/West
#	5 	0101 Spruce wood facing East/West
#	6 	0110 Birch wood facing East/West
#	7 	0111 Jungle wood facing East/West
#	8 	1000 Oak wood facing North/South
#	9 	1001 Spruce wood facing North/South
#	10 	1010 Birch wood facing North/South
#	11 	1011 Jungle wood facing North/South
#	12 	1100 Oak wood with only bark
#	13 	1101 Spruce wood with only bark
#	14 	1110 Birch wood with only bark
#	15 	1111 Jungle wood with only bark

#Block 162
#	DV 	Description
#	0 	Acacia wood facing up/down
#	1 	Dark Oak wood facing up/down
#	4 	Acacia wood facing East/West
#	5 	Dark Oak wood facing East/West
#	8 	Acacia wood facing North/South
#	9 	Dark Oak wood facing North/South
#	12 	Acacia wood with only bark
#	13 	Dark Oak wood with only bark