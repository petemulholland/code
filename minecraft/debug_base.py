from base.utils import *
from base.rooms import *
from base.castle import Castle
from base.debug.debug_base import mc, pl, debug_building
from base.debug.debug_wall_turrets import debug_enclosure_walls, create_walls, create_corner_turrets, create_straight_turrets
from utils import setup_test_area

if __name__ == "__main__":
	#search_result = search_chunk_for(DOOR_WOOD, 0, 0, search_at, abortive_block_ids)
	# TODO: debug fireplace builds, coords don't look right
	#global mc
	#setup_test_area(mc)
	
	#debug_dining_hall()
	#debug_building(Kitchen)
	#debug_building(Pantry)
	#debug_building(EnchantingRoom)
	#debug_building(Smithy)
	#debug_building(DiningHall)
	#debug_building(MainStairs)

	# TODO: debug this in game, brekaing before start of each room build so I can watch the result.
	#debug_building(Castle)
	setup_test_area(mc)
	debug_enclosure_walls()

