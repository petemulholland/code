from building import Building, BuildingEx, BuildingBlock, Torch, Stair
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3

WALL_HEIGHT = 6
WALL_DEPTH = -3 # depth below ground

# Wall turret plans:
# for moat - 3m of water 3m depp around walls => 16m diameter circle around turrets
#
#        xxxx       	       XX   x     	         x   XX       		       xxxx       		
#      xx    xx     	     xXww   x     		     x   wwxx     		     xx    xx     		
#     x        x    	    x  ww   x     		    x    ww  x    		    x        x    		
#    x          x   	   x   ww     x   		   x     ww   x   		   x          x   		
# xxx    xxxx    x  	  x    XXxx    x  		  x    xxXX    x  		  x    xxxx    xx 		
#       x    x   x  	  x   Xww  x   x  		  x   x  wwX   x  		  x   x    x      		
#      x      x   x 	 XwwwXwww   x   x 		 x   x   wwwXwwwX 		 x   x      x     		
#      x  xx  x   x 	 XwwwXwwXx  x   x 		 x   x  xXwwXwwwX 		 x   x  xx  x     		
#  XwwwXwwXx  x   x 	     x  xx  x   x 		 x   x  xx  x     		 x   x  xXwwXwwwX 		
#  XwwwXwww   x   x 	     x      x   x 		 x   x      x     		 x   x   wwwXwwwX 		
#   x   Xww  x   x  	      x    x   x  		  x   x    x      		  x   x  wwX   x  		
#   x    XXxx    x  	xxx    xxxx    x  		  x    xxxx    xx 		  x    xxXX    x  		
#    x   ww     x   	   x          x   		   x          x   		   x     ww   x   		
#     x  ww    x    	    x        x    		    x        x    		    x    ww  x    		
#      xxww   x     	     xx    xx     		     xx    xx     		     x   wwxx     		
#        XX   x     	       xxxx       		       xxxx       		     x   XX       		
#        ww         	                  		                  		                  		
#  5432109876543210		 5432109876543210		 5432109876543210		 5432109876543210		

# ###############################
# TODO: make turrets mirrorable
# ################################
class WallTurretMoat(BuildingEx):
	''' class to create 1 quater section of moat around a turret 
		default orientation is north east
		Building.NORTH => north east
		Building.WEST => north west
		Building.SOUTH => south west
		Building.EAST => south east

		7 XX      
		6 wwXX    
		5 wwwwX   
		4 wwwwwX  
		3   wwwwX 
		2    wwwX 
		1     wwwX
		0     wwwX
		  76543210
		'''
	WIDTH = 8
	def __init__(self, *args, **kwargs):
		super(WallTurretMoat, self).__init__(WallTurretMoat.WIDTH, *args, **kwargs)
		self.base_level = -3

	def _create_base(self):
		builds = []
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(0,self.base_level,0),
									block.DIRT,
									Building.SE_CORNER_POS + Vec3(-7,self.base_level,-7)))
		self._add_section("Wall turret moat - base", builds)
		 
	def _create_walls(self):
		builds = []
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(0,self.base_level,0),
									block.STONE_BRICK,
									Building.SE_CORNER_POS + Vec3(0,1,-1),
									description="moat wall"))
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-1,self.base_level,-2),
									block.STONE_BRICK,
									Building.SE_CORNER_POS + Vec3(-1,1,-3),
									description="moat wall"))

		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-2,self.base_level,-4),
									block.STONE_BRICK,
									Building.SE_CORNER_POS + Vec3(-2,1,-4),
									description="moat wall"))
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-3,self.base_level,-5),
									block.STONE_BRICK,
									Building.SE_CORNER_POS + Vec3(-3,1,-5),
									description="moat wall"))

		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-4,self.base_level,-6),
									block.STONE_BRICK,
									Building.SE_CORNER_POS + Vec3(-5,1,-6),
									description="moat wall"))
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-6,self.base_level,-7),
									block.STONE_BRICK,
									Building.SE_CORNER_POS + Vec3(-7,1,-7),
									description="moat wall"))

		self._add_section("Wall turret moat - walls", builds)

	def _create_water(self):
		builds = []
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-1,self.base_level+1,0),
									block.STONE_BRICK,
									Building.SE_CORNER_POS + Vec3(-3,0,-1),
									description="moat wall"))
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-2,self.base_level+1,-2),
									block.STONE_BRICK,
									Building.SE_CORNER_POS + Vec3(-4,0,-3),
									description="moat wall"))

		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-3,self.base_level+1,-4),
									block.STONE_BRICK,
									Building.SE_CORNER_POS + Vec3(-3,0,-5),
									description="moat wall"))

		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-4,self.base_level+1,-3),
									block.STONE_BRICK,
									Building.SE_CORNER_POS + Vec3(-5,0,-5),
									description="moat wall"))
		builds.append(BuildingBlock(Building.SE_CORNER_POS + Vec3(-6,self.base_level+1,-4),
									block.STONE_BRICK,
									Building.SE_CORNER_POS + Vec3(-7,0,-6),
									description="moat wall"))
		self._add_section("Wall turret moat - water", builds)

	def _create_structure(self):
		super(WallTurretMoat, self)._create_structure()
		self._create_base()
		self._create_walls()
		self._create_base()

class WallTurretBase(BuildingEx):
	''' base class for an 8m diameter turret with moat on an enclosure wall
		this builds a solid Stone column and moat sections to NE & NW
		& 1m wide overhang at wall height & turret top with fences around top
		derived classes should create:
			moat openings to main moat
			walkway along wall
			interior stairs in turret
			& turret access at base of inside wall
		'''
	WIDTH = 16
	def __init__(self, *args, **kwargs):
		super(WallTurretBase, self).__init__(WallTurretBase.WIDTH, *args, **kwargs)
		self.foundation_depth = WALL_DEPTH
		self.height = (WALL_HEIGHT * 2) - 1

	def _create_structure(self):
		super(WallTurretBase, self)._create_structure()
		# TODO: 
		# build a solid Stone column down to foundation level & up to 2xWall height
		# add moat sections to NE & NW
		# add 1m wide overhang at wall height 
		# add turret top (overhang) with fences around top
		# add torches around outside?

class StraightWallTurret(WallTurretBase):
	def __init__(self, *args, **kwargs):
		super(StraightWallTurret, self).__init__(*args, **kwargs)

	def _create_structure(self):
		super(StraightWallTurret, self)._create_structure()
		# TODO: 
		# moat openings to main moat
		# walkway along wall
		# interior stairs in turret
		# & turret access at base of inside wall

class CornerWallTurret(WallTurretBase):
	def __init__(self, *args, **kwargs):
		super(CornerWallTurret, self).__init__(*args, **kwargs)

	def _create_structure(self):
		super(CornerWallTurret, self)._create_structure()
		# TODO: 
		# Add extra moat secion (to SE?)
		# moat openings to main moat
		# walkway along wall
		# interior stairs in turret
		# & turret access at base of inside wall

class CastleWallAndMoat(BuildingEx):
	# TODO buttresses at intervals, walkway & fences on top, stairs at regular intervals
	pass

class CastleGate(BuildingEx):
	# TODO experiment with sticky pistons & iron bars to create portcullis in the gate
	pass

# "circular" turrets on corners?
# experiment with 3 or 4 blocks on sides?
#   ssss
#  s    s
# s      s
# s      s
# s      s
# s      s
#  s    s
#   ssss
#