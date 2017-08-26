import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3

from building import Building, BuildingEx, BuildingBlock, SubBuilding, Torch, Stair, Door
from building.types import STAIRS_STONE_BRICK
from base.enclosure.walls.constants import *

################################################################
# class CastleGate
################################################################
class CastleGate(BuildingEx):
	# TODO experiment with sticky pistons & iron bars to create portcullis in the gate
	# TODO: how will the moat extensions around flanking turrets meet & affect span of bridge?
	#		gap of 8m between turrets should provide a 2m long section of moat 3m wide
	#       have space to set turret accessbeside gate, (doesn't need to be far side of turrets)
	#       
	# TODO: with wall base & moat water level at 0
	#if 0 is the block above ground level, walls sit on ground level (extend below, but gate will be on 0
	# water level in moats at 0 would be above ground level, -1 would be level with ground, -2 would be 1m drop
	# with moat foundation at -4 this gives 2m deep moat, - would prefer 3m deep.
	#        xxxx            xxxx      1
	#      xx    xx        xx    xx    01
	#     x        x      x        x   9
	#    x          x    x          x  8
	#   x    xxxx    xxxx    xxxx    x 7
	#       X    X    bb    X    X     6
	#      X      X   bb   X      X    5  = create walk spaces here with arrow slits with view on bridge
	#      X      X   bb   X      X    4  - current stair setup will interfere with this, 
	#   wwwXwwwwwwXwww  wwwXwwwwwwXwww 3
	#   wwwXwwwwwwXwww  wwwXwwwwwwXwww 2
	#       X     d        d     X     1
	#        XXXXXX        XXXXXX      0
	#   987654321098765432109876543210
	#            2         1
	#
	''' mirrored flanking turrets 
	    & double doors for gate
		& bridge over moat''' 
	WIDTH = 32
	def __init__(self, wall_length, *args, **kwargs):
		super(CastleGate, self).__init__(width=CastleGate.WIDTH, *args, **kwargs)

	def _create_structure(self):
		super(CastleGate, self)._create_structure()

