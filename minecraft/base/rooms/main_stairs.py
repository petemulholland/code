from building import Building, BuildingEx, BuildingBlock, Stair
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3

class MainStairs(BuildingEx):
	# TODO: implement 
	# - up 4 centrally (2 wide)+ up 2 to each side
	# use inverted stairs for "support" underneath each stair, except where upper floor supports the stair (last 1 at top)
	# need to embed inverted stairs into floor above central stair part (maybe?).
	# create air space in upper floor for stairs to travel through
	# - fences bordering all stairs & balcony above.
	WIDTH = 6
	def __init__(self, *args, **kwargs):
		super(MainStairs, self).__init__(width=MainStairs.WIDTH, *args, **kwargs)

		self._set_orientation()
