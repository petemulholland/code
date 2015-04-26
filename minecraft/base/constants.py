import mcpi.block as block
from building.types import PlankData

EXTERIOR_WALLS = block.STONE_BRICK
INTERIOR_WALLS = block.WOOD_PLANKS
FIREPROOF_WALLS = block.STONE_BRICK
FLOOR_WOOD = block.WOOD_PLANKS.withData(PlankData.SPRUCE)

WALL_HEIGHT = 3 # 0-3 =>4, can't be arsed doing a -1 everywhere
