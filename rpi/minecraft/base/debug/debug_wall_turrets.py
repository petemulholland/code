from base.enclosure.walls import CastleWallAndMoat, StraightWallTurret, CornerWallTurret
from debug_base import mc, pl
from building import Building
from mcpi.vec3 import Vec3

# TODO: add tests to create:
#		1. wall with moat (CastleWallAndMoat)
#			- in 4 directions making a square		
#			- need (8*2) + 16 = 32 & some space - 40
#		2. Corner turret on each corner
#		3. 1 straight wall turret on each wall, mirror 2 of them (east & south).

build_offset = Vec3(-1,0,-1)
global mc, ps
ps = mc.player.getTilePos()
ps += build_offset

# build rotated towers on wall corners at:
# (-10,-10), (-30,-10), (-30,-30), (-10,-30)
# build mirrored towers at: 
# (10,-10), (30,-10), (30,-30), (10,-30)

#        xxxx       8	       XX   x     	     x   XX       	       xxxx       
#      xx    xx     7	     xXww   x     	     x   wwxx     	     xx    xx     
#     x        x    6	    x  ww    x    	    x    ww  x    	    x        x    
#    x          x   5	   x   ww     x   	   x     ww   x   	   x          x   
#  xx    xxxx    x  4	  x    XXxx    x  	  x  O xxXX    x  	  x    xxxx O  xx 
#       x    x   x  3	  x   Xww  x   x  	  x   x  wwX   x  	  x   x    x      
#      x      x   x 2 	 XwwwXwww   x   x 	 x   x   wwwXwwwX 	 x   x      x     
#      x  xx  x   x 1	 XwwwXwwXx  x   x 	 x   x  xXwwXwwwX 	 x   x  xx  x     
#  XwwwXwwOx  x   x 0	     x  xx  x   x 	 x   x  xx  x     	 x   x  xXwwXwwwX 
#  XwwwXwww   x   x 1	     x      x   x 	 x   x      x     	 x   x   wwwXwwwX 
#   x   Xww  x   x  2	      x    x   x  	  x   x    x      	  x   x  wwX   x  
#   x    XXxx O  x  3	 xx  O xxxx    x  	  x    xxxx    xx 	  x    xxXX    x  
#    x   ww     x   4	   x          x   	   x          x   	   x     ww   x   
#     x  ww    x    5	    x        x    	    x        x    	    x    ww  x    
#      xxww   x     6	     xx    xx     	     xx    xx     	     x   wwxx     
#        XX   x     7	       xxxx       	       xxxx       	     x   XX       
#        ww         8	                  	                  	                  
#  7654321012345678		 6543210987654321	 5432109876543210	 5432109876543210	
#                              1                  1                   1

walls = [(Vec3(-10,0,-9), 21, Building.EAST),
		 (Vec3(-9,0,-28), 21, Building.NORTH),
		 (Vec3(-28,0,-29), 21, Building.WEST),
		 (Vec3(-29,0,-10), 21, Building.SOUTH),
		 (Vec3(28,0,-9), 21, Building.EAST),
		 (Vec3(29,0,-28), 21, Building.NORTH),
		 (Vec3(10,0,-29), 21, Building.WEST),
		 (Vec3(9,0,-10), 21, Building.SOUTH),
		 ]
towers = [(Vec3(-12,0,-5), False, Building.EAST),
 		  (Vec3(-5,0,-26), False, Building.NORTH),
		  (Vec3(-25,0,-33), False, Building.WEST),
		  (Vec3(-33,0,-12), False, Building.SOUTH),
		  (Vec3(26,0,-12), True, Building.SOUTH),
 		  (Vec3(26,0,-26), True, Building.EAST),
		  (Vec3(12,0,-26), True, Building.NORTH),
		  (Vec3(12,0,-12), True, Building.WEST),
		  ]

def create_walls():
	for pos, len, dir in walls:
		wall = CastleWallAndMoat(len, dir)
		wall.build_to_left(mc, ps + pos)

	#wall = CastleWallAndMoat(40, Building.EAST)
	#wall.build_to_left(mc, ps + Vec3(-1,0,0))

	#wall = CastleWallAndMoat(40, Building.NORTH)
	#wall.build_to_left(mc, ps + Vec3(0,0,-38))

	#wall = CastleWallAndMoat(40, Building.WEST)
	#wall.build_to_left(mc, ps + Vec3(-38,0,-39))

	#wall = CastleWallAndMoat(40, Building.SOUTH)
	#wall.build_to_left(mc, ps + Vec3(-39,0,-1))

def create_corner_turrets():
	for pos, mirrored, dir in towers:
		turret = CornerWallTurret(dir)
		if mirrored:
			turret.mirror()
		turret.build_to_left(mc, ps + pos)

	## north turrret on NE corner
	#turret = CornerWallTurret(Building.NORTH)
	#turret.build_to_left(mc, ps + Vec3(4,0,-36))
	## mirrored North turret on NW corner (give WEST with stairs in opposite direction)
	#turret = CornerWallTurret(Building.NORTH)
	#turret.mirror()
	#turret.build_to_left(mc, ps + Vec3(-36,0,-36))
	## East turret on SE corner
	#turret = CornerWallTurret(Building.EAST)
	#turret.build_to_left(mc, ps + Vec3(-4,0,4))
	## mirrored EAST on SW corner?
	#turret = CornerWallTurret(Building.EAST)
	#turret.mirror()
	#turret.build_to_left(mc, ps + Vec3(-35,0,-3))

def create_straight_turrets():
	pass

def debug_corner_turret():
	turret = CornerWallTurret(Building.NORTH)
	turret.build_to_left(mc, ps + Vec3(-8,0,-8))

def debug_enclosure_walls():
	create_walls()
	create_corner_turrets()
	#create_straight_turrets()
