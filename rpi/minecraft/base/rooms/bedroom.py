from building import Building, BuildingEx, BuildingBlock, Torch, Door, Chest
from base.constants import WALL_HEIGHT, INTERIOR_WALLS
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3

class Bedroom(BuildingEx):
	WALLS_CORNER_POS = {'South East' : Building.SE_CORNER_POS + Vec3(0,0,0), 
						'South West' : Building.SE_CORNER_POS + Vec3(-21,0,0),
						'North West' : Building.SE_CORNER_POS + Vec3(-21,0,-9),
						'North East' : Building.SE_CORNER_POS + Vec3(0,0,-9) }

	WIDTH = WALLS_CORNER_POS['South East'].x - (WALLS_CORNER_POS['South West'].x - 1)

	def __init__(self, *args, **kwargs):
		super(Bedroom, self).__init__(width=Bedroom.WIDTH, *args, **kwargs)

	def _create_walls_and_doors(self):
		builds = []
		builds.append(BuildingBlock(Bedroom.WALLS_CORNER_POS['South East'],
									INTERIOR_WALLS, 
									Bedroom.WALLS_CORNER_POS['South West'] + Vec3(0,WALL_HEIGHT,0),
									description="Bedroom south wall"))
		builds.append(BuildingBlock(Bedroom.WALLS_CORNER_POS['South West'],
									INTERIOR_WALLS, 
									Bedroom.WALLS_CORNER_POS['North West'] + Vec3(0,WALL_HEIGHT,1),
									description="Bedroom west wall"))
		builds.append(BuildingBlock(Bedroom.WALLS_CORNER_POS['South East'],
									INTERIOR_WALLS, 
									Bedroom.WALLS_CORNER_POS['North East'] + Vec3(0,WALL_HEIGHT,1),
									description="Bedroom east wall"))

		builds.append(Door(Door.HINGE_RIGHT, 
							Bedroom.WALLS_CORNER_POS['South East'] + Vec3(-6,0,0),
							block.DOOR_WOOD.withData(Door.SOUTH),
							description="Bedroom door"))
		builds.append(Door(Door.HINGE_LEFT, 
							Bedroom.WALLS_CORNER_POS['South East'] + Vec3(-7,0,0),
							block.DOOR_WOOD.withData(Door.SOUTH),
							description="Bedroom door"))
		
		builds.append(Door(Door.HINGE_RIGHT, 
							Bedroom.WALLS_CORNER_POS['South East'] + Vec3(-14,0,0),
							block.DOOR_WOOD.withData(Door.SOUTH),
							description="Bedroom door"))
		builds.append(Door(Door.HINGE_LEFT, 
							Bedroom.WALLS_CORNER_POS['South East'] + Vec3(-15,0,0),
							block.DOOR_WOOD.withData(Door.SOUTH),
							description="Bedroom door"))
		self._add_section("Bedroom shell", builds)

	def _create_windows(self):
		builds = []
		# windows:
		builds.append(BuildingBlock(Bedroom.WALLS_CORNER_POS['North East'] + Vec3(-3,1,0),
									block.GLASS_PANE, 
									Bedroom.WALLS_CORNER_POS['North East'] + Vec3(-4,2,0),
									description="window"))
		builds.append(BuildingBlock(Bedroom.WALLS_CORNER_POS['North East'] + Vec3(-7,1,0),
									block.GLASS_PANE, 
									Bedroom.WALLS_CORNER_POS['North East'] + Vec3(-8,2,0),
									description="window"))
		builds.append(BuildingBlock(Bedroom.WALLS_CORNER_POS['North East'] + Vec3(-13,1,0),
									block.GLASS_PANE, 
									Bedroom.WALLS_CORNER_POS['North East'] + Vec3(-14,2,0),
									description="window"))
		builds.append(BuildingBlock(Bedroom.WALLS_CORNER_POS['North East'] + Vec3(-17,1,0),
									block.GLASS_PANE, 
									Bedroom.WALLS_CORNER_POS['North East'] + Vec3(-18,2,0),
									description="window"))
		self._add_section("Bedroom windows", builds)

	def _create_torches(self):
		builds = []
		# torches
		builds.append(Torch(Bedroom.WALLS_CORNER_POS['South East'] + Vec3(-5,2,-8),
							block.TORCH.withData(Torch.SOUTH)))
		builds.append(Torch(Bedroom.WALLS_CORNER_POS['South East'] + Vec3(-16,2,-8),
							block.TORCH.withData(Torch.SOUTH)))

		builds.append(Torch(Bedroom.WALLS_CORNER_POS['South East'] + Vec3(-5,2,-1),
							block.TORCH.withData(Torch.WEST)))
		builds.append(Torch(Bedroom.WALLS_CORNER_POS['South East'] + Vec3(-16,2,-1),
							block.TORCH.withData(Torch.EAST)))
							
		builds.append(Torch(Bedroom.WALLS_CORNER_POS['South East'] + Vec3(-1,2,-4),
							block.TORCH.withData(Torch.NORTH)))
		builds.append(Torch(Bedroom.WALLS_CORNER_POS['South East'] + Vec3(-20,2,-4),
							block.TORCH.withData(Torch.NORTH)))

		self._add_section("Bedroom torches", builds)


	def _create_structure(self):
		#   sssggssggssssggssggsss 9
		#   wb   T   ffff   T   bw 8 
		#   wb       ffff       bw 7 side walls lined with book shelves
		#   wb    c  ffff  c    bw 6 c  => chair
		#   wb                  bw 5
		#   wT       fccf       Tw 4  fences posts 3 high around bed, wood slabs on top?
		#   wt        bb        cw 3  t=> table, c=> chair
		#   wtc       bb        cw 2	desk & chairs one side, sofa on the other?
		#   wt   T   f  f   T    w 1
		#   wwwwwwddwwwwwwddwwwwww 0 TODO: move doors
		#           t    t          
		#   1098765432109876543210
		#    2         1          
		super(Bedroom, self)._create_structure()
		self._create_walls_and_doors()
		self._create_windows()
		self._create_torches()

		builds = []

		# bookshelves
		builds.append(BuildingBlock(Bedroom.WALLS_CORNER_POS['North East'] + Vec3(-1,0,1),
									block.BOOKSHELF,
									Bedroom.WALLS_CORNER_POS['North East'] + Vec3(-1,3,4),
									description="East bookshelves"))
		builds.append(BuildingBlock(Bedroom.WALLS_CORNER_POS['North West'] + Vec3(1,0,1),
									block.BOOKSHELF,
									Bedroom.WALLS_CORNER_POS['North West'] + Vec3(1,3,4),
									description="West bookshelves"))
		self._add_section("Bedroom bookshelves", builds)
							
		# TODO: fireplace, bed & chest, desk & chairs & sofa