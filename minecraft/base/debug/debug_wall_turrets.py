from base.enclosure.walls import CastleWallAndMoat, StraightWallTurret, CornerWallTurret

# currently using 7m diameter for castle turrets - these don't work well on 2m wide wall
#										
# 7m diameter:		# 9m diameter		# 10 m diameter
#										#				
#    xxx			#    xxxxx			#     xxxx
#   x   x			#   xx   xx			#    x    x
#  x     x			#  xx     xx		#   x      x
#  x  x--x			#  x       x		#  x        x
#  x     x			#  x   x---x		#  x   xx---x
#   x   x			#  x       x		#  x   xx   x
#    xxx			#  xx     xx		#  x        x
#					#   xx   xx			#   x      x
#					#    xxxxx			#    x    x
#										#     xxxx
#										
#	8m diameter corner
#	
#	    xxxx   
#	   x ss x
#	  xs    sx
#	  xs xx sx		=> this might be a good fit for 2m wide walls
#	xxxxxxx--x		=> steps would come out onto wall, 
#	xxxxxx   x		=> 
#	   dxx  x
#	   xxxxx
#	    xx
#	    xx
#
#	8m diameter straight wall
#	
#	    xxxx   
#	   x ss x
#	  xs    sx
#	  xs xx sx		=> this might be a good fit for 2m wide walls
#	xxxxxxxxxxxx	=> steps would come out onto wall, 
#	xxxxxxxxxxxx	=> 
#	   d    d
#	   xxxxxx
#	    

# TODO: add tests to create:
#		1. wall with moat (CastleWallAndMoat)
#			- in 4 directions making a square		
#			- need (8*2) + 16 = 32 & some space - 40
#		2. Corner turret on each corner
#		3. 1 straight wall turret on each wall, mirror 2 of them (east & south).

def debug_enclosure_walls():
	pass
	