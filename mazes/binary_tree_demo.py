from mazes.grid import Grid
from mazes.binary_tree import BinaryTree

if __name__ == "__main__":
	grid = Grid(8, 8)
	print(grid)
	bt = BinaryTree()
	grid = bt.on(grid)
	print(grid)
	

