import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3

from building import Building, BuildingEx, BuildingBlock, SubBuilding, Torch, Stair, Door
from building.types import STAIRS_STONE_BRICK
from base.enclosure.walls.constants import *

# Wall turret plans:
# for moat - 3m of water 3m depp around walls => 16m diameter circle around turrets
#
#        xxxx       6	       XX   x     	     x   XX       	       xxxx       
#      xx    xx     5	     xXww   x     	     x   wwxx     	     xx    xx     
#     x        x    4	    x  ww    x    	    x    ww  x    	    x        x    
#    x          x   3	   x   ww     x   	   x     ww   x   	   x          x   
#  xx    xxxx    x  2	  x    XXxx    x  	  x  O xxXX    x  	  x    xxxx O  xx 
#       x    x   x  1	  x   Xww  x   x  	  x   x  wwX   x  	  x   x    x      
#      x      x   x 01	 XwwwXwww   x   x 	 x   x   wwwXwwwX 	 x   x      x     
#      x  xx  x   x 9	 XwwwXwwXx  x   x 	 x   x  xXwwXwwwX 	 x   x  xx  x     
#  XwwwXwwXx  x   x 8	     x  xx  x   x 	 x   x  xx  x     	 x   x  xXwwXwwwX 
#  XwwwXwww   x   x 7	     x      x   x 	 x   x      x     	 x   x   wwwXwwwX 
#   x   Xww  x   x  6	      x    x   x  	  x   x    x      	  x   x  wwX   x  
#   x    XXxx O  x  5	 xx  O xxxx    x  	  x    xxxx    xx 	  x    xxXX    x  
#    x   ww     x   4	   x          x   	   x          x   	   x     ww   x   
#     x  ww    x    3	    x        x    	    x        x    	    x    ww  x    
#      xxww   x     2	     xx    xx     	     xx    xx     	     x   wwxx     
#        XX   x     1	       xxxx       	       xxxx       	     x   XX       
#        ww         0	                  	                  	                  
#  5432109876543210		 5432109876543210	 5432109876543210	 5432109876543210	



################################################################
# class WallTurretBase
################################################################
class WallTurretBase(BuildingEx):
	''' base class for an 8m diameter turret with moat on an enclosure wall
		this builds a solid Stone column and moat sections to NE & NW
		& 1m wide overhang at wall height & turret top with fences around top
		derived classes should create:
			moat openings to main moat
			walkway along wall
			interior stairs in turret
			& turret access at base of inside wall

		#    x m       1
		#    w o       01
		#    w a       9 
		#    w t       8
		#   xxxx       7  
		#  x    x moat 6  
		# x      x     5 
		# x  xx  xwwwx 4 
		# x  xx  x     3 
		# x      x     2 
		#  x    x      1 
		#   xxxx       0 
		# 
		# 765432101234          
		'''
	WIDTH = 8 # including the moat will screw with the mirroring of stairs & access points
	
	def __init__(self, *args, **kwargs):
		super(WallTurretBase, self).__init__(width=WallTurretBase.WIDTH, *args, **kwargs)
		self.foundation_depth = WALL_DEPTH
		self.height = (WALL_HEIGHT * 2) - 1
		self.column_se_corner = Vec3(0,0,0) # TODO: need to figure out how to positions this, but build column relative to this 

	def _create_column(self):
		builds = []
		# create 4x8 rectangle
		builds.append(BuildingBlock(self.column_se_corner + Vec3(-2,self.foundation_depth,0),
									block.STONE_BRICK,
									self.column_se_corner + Vec3(-5,self.height,-7),
									description="turret column, n-s section"))
		# create 8x4 rectangle
		builds.append(BuildingBlock(self.column_se_corner + Vec3(0,self.foundation_depth,-2),
									block.STONE_BRICK,
									self.column_se_corner + Vec3(-7,self.height,-5),
									description="turret column, e-w section"))
		# create 6x6 square
		builds.append(BuildingBlock(self.column_se_corner + Vec3(-1,self.foundation_depth,-1),
									block.STONE_BRICK,
									self.column_se_corner + Vec3(-6,self.height,-6),
									description="turret column, central square"))
		self._add_section("Turret - main column", builds)

	def _add_torches(self):
		builds = []
		heights = [3, WALL_HEIGHT+3]
		for height in heights:
			builds.append(Torch(self.column_se_corner + Vec3(-8,height,-4),
								block.TORCH.withData(Torch.WEST),
								description="main column torch"))
			builds.append(Torch(self.column_se_corner + Vec3(-4,height,-8),
								block.TORCH.withData(Torch.NORTH),
								description="main column torch"))
			builds.append(Torch(self.column_se_corner + Vec3(1,height,-4),
								block.TORCH.withData(Torch.EAST),
								description="main column torch"))
			builds.append(Torch(self.column_se_corner + Vec3(3,height,1),
								block.TORCH.withData(Torch.SOUTH),
								description="main column torch"))

		self._add_section("Turret - main column torches", builds)

	def _create_overhangs(self):
		'''
		#    bbbb    8 b => overhang
		#   bxxxxb   7  
		#  bx    xb  6  
		# bx      xb 5 
		# bx  xx  xb 4 
		# bx  xx  xb 3 
		# bx      xb 2 
		#  bx    xb  1 
		#   bxxxxb   0 
		#    bbbb      
		#987654321012          
		'''
		heights = [self.height, WALL_HEIGHT - 1]
		builds = []
		for height in heights:		
			# create 4x10 rectangle
			builds.append(BuildingBlock(self.column_se_corner + Vec3(-2,height,1),
										block.STONE_BRICK,
										self.column_se_corner + Vec3(-5,height,-8),
										description="turret overhang, n-s extreme"))
			# create 10x4 rectangle
			builds.append(BuildingBlock(self.column_se_corner + Vec3(1,height,-2),
										block.STONE_BRICK,
										self.column_se_corner + Vec3(-8,height,-5),
										description="turret overhang, e-w extreme"))
			# create 6x8 rectangle
			builds.append(BuildingBlock(self.column_se_corner + Vec3(-1,height,0),
										block.STONE_BRICK,
										self.column_se_corner + Vec3(-6,height,-7),
										description="turret overhang, n-s center"))
			# create 8x6 rectangle
			builds.append(BuildingBlock(self.column_se_corner + Vec3(0,height,-1),
										block.STONE_BRICK,
										self.column_se_corner + Vec3(-7,height,-6),
										description="turret overhang, e-w center"))
		self._add_section("Turret - overhangs", builds)

	def _create_battlements(self):
		# TODO add torches with up orientation to fences
		# temporary - build column & add a torch on each side
		'''
		#    ffffff    9
		#   ffbbbbff   8 b => overhang
		#  ffbxxxxbff  7  
		# ffbx    xbff 6  
		# fbx      xbf 5 
		# fbx  xx  xbf 4 
		# fbx  xx  xbf 3 
		# fbx      xbf 2 
		# ffbx    xbff 1 
		#  ffbxxxxbff  0 
		#   ffbbbbff   1
		#    ffffff    2
		# 987654321012          
		'''
		builds = []
		# south length
		builds.append(BuildingBlock(self.column_se_corner + Vec3(-1,self.height,2),
									block.FENCE,
									self.column_se_corner + Vec3(-6,self.height+1,2),
									description="battlements"))

		# SW indents
		builds.append(BuildingBlock(self.column_se_corner + Vec3(-6,self.height,1),
									block.FENCE,
									self.column_se_corner + Vec3(-7,self.height+1,1),
									description="battlements"))
		builds.append(BuildingBlock(self.column_se_corner + Vec3(-7,self.height,0),
									block.FENCE,
									self.column_se_corner + Vec3(-8,self.height+1,0),
									description="battlements"))
		builds.append(BuildingBlock(self.column_se_corner + Vec3(-8,self.height,-1),
									block.FENCE,
									self.column_se_corner + Vec3(-9,self.height+1,-1),
									description="battlements"))

		# SE indents
		builds.append(BuildingBlock(self.column_se_corner + Vec3(-1,self.height,1),
									block.FENCE,
									self.column_se_corner + Vec3(0,self.height+1,1),
									description="battlements"))
		builds.append(BuildingBlock(self.column_se_corner + Vec3(0,self.height,0),
									block.FENCE,
									self.column_se_corner + Vec3(1,self.height+1,0),
									description="battlements"))
		builds.append(BuildingBlock(self.column_se_corner + Vec3(1,self.height,-1),
									block.FENCE,
									self.column_se_corner + Vec3(2,self.height+1,-1),
									description="battlements"))

		# West length
		builds.append(BuildingBlock(self.column_se_corner + Vec3(-9,self.height,-2),
									block.FENCE,
									self.column_se_corner + Vec3(-9,self.height+1,-5),
									description="battlements"))

		# East length
		builds.append(BuildingBlock(self.column_se_corner + Vec3(2,self.height,-2),
									block.FENCE,
									self.column_se_corner + Vec3(2,self.height+1,-5),
									description="battlements"))

		# NW indents
		builds.append(BuildingBlock(self.column_se_corner + Vec3(-6,self.height,-8),
									block.FENCE,
									self.column_se_corner + Vec3(-7,self.height+1,-8),
									description="battlements"))
		builds.append(BuildingBlock(self.column_se_corner + Vec3(-7,self.height,-7),
									block.FENCE,
									self.column_se_corner + Vec3(-8,self.height+1,-7),
									description="battlements"))
		builds.append(BuildingBlock(self.column_se_corner + Vec3(-8,self.height,-6),
									block.FENCE,
									self.column_se_corner + Vec3(-9,self.height+1,-6),
									description="battlements"))

		# NE indents
		builds.append(BuildingBlock(self.column_se_corner + Vec3(-1,self.height,-8),
									block.FENCE,
									self.column_se_corner + Vec3(0,self.height+1,-8),
									description="battlements"))
		builds.append(BuildingBlock(self.column_se_corner + Vec3(0,self.height,-7),
									block.FENCE,
									self.column_se_corner + Vec3(1,self.height+1,-7),
									description="battlements"))
		builds.append(BuildingBlock(self.column_se_corner + Vec3(1,self.height,-6),
									block.FENCE,
									self.column_se_corner + Vec3(2,self.height+1,-6),
									description="battlements"))

		# North length
		builds.append(BuildingBlock(self.column_se_corner + Vec3(-1,self.height,-9),
									block.FENCE,
									self.column_se_corner + Vec3(-6,self.height+1,-9),
									description="battlements"))

		self._add_section("Turret - battelements/fences", builds)
		
	def _create_structure(self):
		''' Section names:
			Turret - main column
			Turret - main column torches
			Turret - overhangs
			Turret - battelements/fences
		'''
		super(WallTurretBase, self)._create_structure()
		# TODO: 
		# add battlement torches


		# build a solid Stone column down to foundation level & up to 2xWall height
		self._create_column()
		self._add_torches()
		# add 1m wide overhang at wall height  & turret top
		self._create_overhangs()
		# add fences around top
		self._create_battlements()

################################################################
# class StraightWallTurret
################################################################
class StraightWallTurret(WallTurretBase):
	'''
	#        xxxx       1	
	#      xx    xx     01	
	#     x        x    9	
	#    x          x   8	
	#  xx    xxxx    xx 7	
	#   c   x    x   c  6	c => needs to be cleared
	#  c   x      x   c 5	
	#  c   x  xx  x   c 4	
	#  XwwwXwwXXwwXwwwX 3	
	#  XwwwXwwwwwwXwwwX 2	
	#       X   x d     1	
	#        XXxxxx     0	
	#                   
	#  1098765432101234
	#   1		
	'''
	def __init__(self, *args, **kwargs):
		super(StraightWallTurret, self).__init__(*args, **kwargs)

	def _create_moat(self):
		builds = []

		ne_moat = WallTurretMoat(Building.NORTH)
		ne_moat.open_se_wall()
		builds.append(SubBuilding(ne_moat, self.column_se_corner + Vec3(4,0,-4)))

		nw_moat = WallTurretMoat(Building.WEST)
		nw_moat.open_nw_wall()
		builds.append(SubBuilding(nw_moat, self.column_se_corner + Vec3(-4,0,-11)))

		self._add_section("Straight Turret - moat", builds)

	def _clear_wall_walkway(self):
		builds = []
		builds.append(BuildingBlock(self.column_se_corner + Vec3(-7,WALL_HEIGHT,-2),
									block.AIR,
									self.column_se_corner + Vec3(0,WALL_HEIGHT+2,-3),
									description="clear turret moat end- air bove water"))

		self._add_section("Straight Turret - clear wall walkway", builds)

	def _create_stairs(self):
		builds = []
		heights = [0, WALL_HEIGHT] # starting height for staircases
		for height in heights:		

			# north facing stairs & head clearance
			builds.append(BuildingBlock(self.column_se_corner + Vec3(self._get_x(-1),height,-4), 
										block.AIR, 
										self.column_se_corner + Vec3(self._get_x(-2),height+3,-4), 
										description="Stair clearance"))

			builds.append(Stair(self.column_se_corner + Vec3(self._get_x(-1),height,-4), 
								STAIRS_STONE_BRICK.withData(Stair.NORTH), 
								self.column_se_corner + Vec3(self._get_x(-2),height,-4), 
								description="Stair"))

			builds.append(BuildingBlock(self.column_se_corner + Vec3(self._get_x(-1),height+1,-5), 
										block.AIR, 
										self.column_se_corner + Vec3(self._get_x(-2),height+4,-5), 
										description="Stair clearance"))

			builds.append(Stair(self.column_se_corner + Vec3(self._get_x(-1),height+1,-5), 
								STAIRS_STONE_BRICK.withData(Stair.NORTH), 
								self.column_se_corner + Vec3(self._get_x(-2),height+1,-5), 
								description="Stair"))

			# clear landing & space for next stair
			builds.append(BuildingBlock(self.column_se_corner + Vec3(self._get_x(-2),height+2,-5), 
										block.AIR, 
										self.column_se_corner + Vec3(self._get_x(-3),height+5,-6), 
										description="Stair clearance"))

			stair_direction = Stair.WEST
			if self.mirrored:
				stair_direction = Stair.EAST


			builds.append(Stair(self.column_se_corner + Vec3(self._get_x(-3),height+2,-5), 
								STAIRS_STONE_BRICK.withData(stair_direction), 
								self.column_se_corner + Vec3(self._get_x(-3),height+2,-6), 
								description="Stair"))

			builds.append(BuildingBlock(self.column_se_corner + Vec3(self._get_x(-4),height+3,-5), 
										block.AIR, 
										self.column_se_corner + Vec3(self._get_x(-4),height+6,-6), 
										description="Stair clearance"))

			builds.append(Stair(self.column_se_corner + Vec3(self._get_x(-4),height+3,-5), 
								STAIRS_STONE_BRICK.withData(stair_direction), 
								self.column_se_corner + Vec3(self._get_x(-4),height+3,-6), 
								description="Stair"))

			# clear landing & space for next stair
			builds.append(BuildingBlock(self.column_se_corner + Vec3(self._get_x(-5),height+4,-6), 
										block.AIR, 
										self.column_se_corner + Vec3(self._get_x(-5),height+7,-6), 
										description="landing clearance"))

			builds.append(BuildingBlock(self.column_se_corner + Vec3(self._get_x(-5),height+4,-5), 
										block.AIR, 
										self.column_se_corner + Vec3(self._get_x(-6),height+7,-5), 
										description="Stair clearance"))

			builds.append(Stair(self.column_se_corner + Vec3(self._get_x(-5),height+4,-5), 
								STAIRS_STONE_BRICK.withData(Stair.SOUTH), 
								self.column_se_corner + Vec3(self._get_x(-6),height+4,-5), 
								description="Stair"))

			builds.append(BuildingBlock(self.column_se_corner + Vec3(self._get_x(-5),height+5,-4), 
										block.AIR, 
										self.column_se_corner + Vec3(self._get_x(-6),height+8,-4), 
										description="Stair clearance"))

			builds.append(Stair(self.column_se_corner + Vec3(self._get_x(-5),height+5,-4), 
								STAIRS_STONE_BRICK.withData(Stair.SOUTH), 
								self.column_se_corner + Vec3(self._get_x(-6),height+5,-4), 
								description="Stair"))

		self._add_section("Straight Turret stairs", builds)

	def _create_turret_access(self):
		builds = []
		builds.append(BuildingBlock(self.column_se_corner + Vec3(self._get_x(0),0,0),
									block.STONE_BRICK,
									self.column_se_corner + Vec3(self._get_x(-1),3,-1),
									description="turret access point"))
		builds.append(BuildingBlock(self.column_se_corner + Vec3(self._get_x(-1),0,-1),
									block.AIR,
									self.column_se_corner + Vec3(self._get_x(-2),2,-3),
									description="turret acces clearance"))
		hinge_type = Door.HINGE_LEFT
		door_orientation = Door.EAST
		if self.mirrored:
			hinge_type = Door.HINGE_RIGHT
			door_orientation = Door.WEST

		# Place door on east wall of access point, so doorways either side of gate face each other
		# this will probably be usefull if i have to leave assess between animal pens on east wall
		builds.append(Door(Door.hinge_type, 
							self.column_se_corner + Vec3(self._get_x(0),0,-1),
							block.DOOR_WOOD.withData(door_orientation),
							description="Turret access door"))

		self._add_section("Straight Turret access", builds)

	def add_gate_access(self):
		# TODO: remove current access point,
		#		add access point  at opposite side from stair base
		#		create wall space with arrow slits
		pass

	def _create_structure(self):
		''' Section names: 
			Straight Turret - clear moat openings
			Straight Turret - clear wall walkway
			Straight Turret stairs
			Straight Turret access
		'''
		super(StraightWallTurret, self)._create_structure()
		self._create_moat()
		self._clear_wall_walkway()
		#self._create_stairs()
		#self._create_turret_access()

################################################################
# class CornerWallTurret
################################################################
class CornerWallTurret(WallTurretBase):
	'''
	#        xxxx       1	
	#      xx    xx     01	
	#     x        x    9	
	#    x          x   8	
	#  xx    xxxx    x  7	
	#   c   x    x   x  6	
	#  c   x      x   x 5	
	#  c   x  xx  x   x 4	
	#  XwwwXwwXx  x   x 3	
	#  XwwwXwww   x   x 2	
	#      dXww  x   x  1	
	#      xxXXxx O  x  0	=> se corner pos of turret	
	#        ww     x   1	
	#        ww    x    2	
	#        ww  cx     3	
	#        XXcc x     4	
	#                 	
	#  1098765432101234
	#   1		
	'''
	def __init__(self, *args, **kwargs):
		super(CornerWallTurret, self).__init__(*args, **kwargs)

	def _create_moat(self):
		builds = []

		if not self.mirrored:
			builds.append(SubBuilding(WallTurretMoat(Building.NORTH), self.column_se_corner + Vec3(4,0,-4)))

			nw_moat = WallTurretMoat(Building.WEST)
			nw_moat.open_nw_wall()
			builds.append(SubBuilding(nw_moat, self.column_se_corner + Vec3(-4,0,-11)))

			se_moat = WallTurretMoat(Building.EAST)
			se_moat.open_se_wall()
			builds.append(SubBuilding(se_moat, self.column_se_corner + Vec3(-3,0,4)))
		else:
			builds.append(SubBuilding(WallTurretMoat(Building.WEST), self.column_se_corner + Vec3(-4,0,-11)))

			ne_moat = WallTurretMoat(Building.NORTH)
			ne_moat.open_se_wall()
			builds.append(SubBuilding(ne_moat, self.column_se_corner + Vec3(4,0,-4)))

			sw_moat = WallTurretMoat(Building.SOUTH)
			sw_moat.open_nw_wall()
			builds.append(SubBuilding(sw_moat, self.column_se_corner + Vec3(-11,0,-3)))


		self._add_section("Corner Turret - moat", builds)

	def _clear_wall_walkway(self):
		builds = []
		builds.append(BuildingBlock(self.column_se_corner + Vec3(self._get_x(-7),WALL_HEIGHT,-2),
									block.AIR,
									self.column_se_corner + Vec3(self._get_x(-4),WALL_HEIGHT+2,-3),
									description="clear corner turret wall walkway"))
		builds.append(BuildingBlock(self.column_se_corner + Vec3(self._get_x(-5),WALL_HEIGHT,-3),
									block.AIR,
									self.column_se_corner + Vec3(self._get_x(-4),WALL_HEIGHT+2,0),
									description="clear corner turret wall walkway"))

		builds.append(Torch(self.column_se_corner + Vec3(self._get_x(-6),WALL_HEIGHT+2,-2),
							block.TORCH.withData(Torch.NORTH),
							description="walkway torch"))
		torch_orientation = Torch.EAST
		if self.mirrored:
			torch_orientation = Torch.WEST

		builds.append(Torch(self.column_se_corner + Vec3(self._get_x(-5),WALL_HEIGHT+2,-1),
							block.TORCH.withData(torch_orientation),
							description="walkway torch"))
		self._add_section("Turret - clear wall walkway", builds)

	def _create_stairs(self):
		builds = []
		heights = [0, WALL_HEIGHT] # starting height for staircases
		for height in heights:		
			# north facing stairs & head clearance
			stair_direction = Stair.EAST
			if self.mirrored:
				stair_direction = Stair.WEST

			builds.append(BuildingBlock(self.column_se_corner + Vec3(self._get_x(-3),height,-1), 
										block.AIR, 
										self.column_se_corner + Vec3(self._get_x(-3),height+3,-2), 
										description="Stair clearance"))

			builds.append(Stair(self.column_se_corner + Vec3(self._get_x(-3),height,-1), 
								STAIRS_STONE_BRICK.withData(stair_direction), 
								self.column_se_corner + Vec3(self._get_x(-3),height,-2), 
								description="Stair"))

			builds.append(BuildingBlock(self.column_se_corner + Vec3(self._get_x(-2),height+1,-1), 
										block.AIR, 
										self.column_se_corner + Vec3(self._get_x(-2),height+4,-2), 
										description="Stair clearance"))

			builds.append(Stair(self.column_se_corner + Vec3(self._get_x(-2),height+1,-1), 
								STAIRS_STONE_BRICK.withData(stair_direction), 
								self.column_se_corner + Vec3(self._get_x(-2),height+1,-2), 
								description="Stair"))

			# clear landing & space for next stair
			builds.append(BuildingBlock(self.column_se_corner + Vec3(self._get_x(-1),height+2,-2), 
										block.AIR, 
										self.column_se_corner + Vec3(self._get_x(-2),height+5,-3), 
										description="Stair clearance"))


			builds.append(Stair(self.column_se_corner + Vec3(self._get_x(-1),height+2,-3), 
								STAIRS_STONE_BRICK.withData(Stair.NORTH), 
								self.column_se_corner + Vec3(self._get_x(-2),height+2,-3), 
								description="Stair"))

			builds.append(BuildingBlock(self.column_se_corner + Vec3(self._get_x(-1),height+3,-4), 
										block.AIR,
										self.column_se_corner + Vec3(self._get_x(-2),height+6,-4), 
										description="Stair clearance"))

			builds.append(Stair(self.column_se_corner + Vec3(self._get_x(-1),height+3,-4), 
								STAIRS_STONE_BRICK.withData(Stair.NORTH), 
								self.column_se_corner + Vec3(self._get_x(-2),height+3,-4), 
								description="Stair"))

			torch_orientation = Torch.WEST
			if self.mirrored:
				torch_orientation = Torch.EAST
			builds.append(Torch(self.column_se_corner + Vec3(self._get_x(-1),height+5,-4),
								block.TORCH.withData(Torch.WEST),
								description="Torch"))

			# clear landing & space for next stair
			builds.append(BuildingBlock(self.column_se_corner + Vec3(self._get_x(-1),height+4,-5), 
										block.AIR, 
										self.column_se_corner + Vec3(self._get_x(-1),height+7,-5), 
										description="landing clearance"))

			builds.append(BuildingBlock(self.column_se_corner + Vec3(self._get_x(-2),height+4,-5), 
										block.AIR, 
										self.column_se_corner + Vec3(self._get_x(-2),height+7,-6), 
										description="Stair clearance"))

			stair_direction = Stair.WEST
			if self.mirrored:
				stair_direction = Stair.EAST
			builds.append(Stair(self.column_se_corner + Vec3(self._get_x(-2),height+4,-5), 
								STAIRS_STONE_BRICK.withData(stair_direction), 
								self.column_se_corner + Vec3(self._get_x(-2),height+4,-6), 
								description="Stair"))

			builds.append(BuildingBlock(self.column_se_corner + Vec3(self._get_x(-3),height+5,-5), 
										block.AIR, 
										self.column_se_corner + Vec3(self._get_x(-3),height+8,-6), 
										description="Stair clearance"))

			builds.append(Stair(self.column_se_corner + Vec3(self._get_x(-3),height+5,-5), 
								STAIRS_STONE_BRICK.withData(stair_direction), 
								self.column_se_corner + Vec3(self._get_x(-3),height+5,-6), 
								description="Stair"))

		# clear walk space to wall
		builds.append(BuildingBlock(self.column_se_corner + Vec3(self._get_x(-4),WALL_HEIGHT,-4), 
									block.AIR, 
									self.column_se_corner + Vec3(self._get_x(-5),WALL_HEIGHT+2,-6), 
									description="Walk space clearance to wall top"))
		builds.append(Torch(self.column_se_corner + Vec3(self._get_x(-5),WALL_HEIGHT+2,-6),
							block.TORCH.withData(Torch.SOUTH),
							description="Torch"))

		self._add_section("Corner Turret stairs", builds)

	def _create_turret_access(self):
		builds = []
		builds.append(BuildingBlock(self.column_se_corner + Vec3(self._get_x(-6),-2,0),
									block.STONE_BRICK,
									self.column_se_corner + Vec3(self._get_x(-7),3,-1),
									description="turret access point"))
		builds.append(BuildingBlock(self.column_se_corner + Vec3(self._get_x(-4),0,-1),
									block.AIR,
									self.column_se_corner + Vec3(self._get_x(-6),2,-1),
									description="turret acces clearance"))
		builds.append(BuildingBlock(self.column_se_corner + Vec3(self._get_x(-4),0,-2),
									block.AIR,
									self.column_se_corner + Vec3(self._get_x(-4),2,-2),
									description="turret acces clearance"))
		hinge_type = Door.HINGE_RIGHT
		door_orientation = Door.WEST
		inside_torch = Torch.EAST
		outside_torch = Torch.WEST
		if self.mirrored:
			hinge_type = Door.HINGE_LEFT
			door_orientation = Door.EAST
			inside_torch = Torch.WEST
			outside_torch = Torch.EAST

		builds.append(Door(hinge_type, 
						   self.column_se_corner + Vec3(self._get_x(-7),0,-1),
						   block.DOOR_WOOD.withData(door_orientation),
						   description="Turret access door"))
		builds.append(Torch(self.column_se_corner + Vec3(-6,2,-1),
							block.TORCH.withData(inside_torch),
							description="main column torch"))
		builds.append(Torch(self.column_se_corner + Vec3(-8,2,-1),
							block.TORCH.withData(outside_torch),
							description="main column torch"))

		self._add_section("Corner Turret access", builds)

	def _create_structure(self):
		super(CornerWallTurret, self)._create_structure()
		self._create_moat()
		self._clear_wall_walkway()
		self._create_stairs()
		self._create_turret_access()

