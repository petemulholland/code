from cell import Cell

class Grid:
	def __init__(self, rows, columns):
		self._rows = rows
		self._columns = columns
		self._grid = self._prepare_grid
		self._configure_cells()
		
	def _prepare_grid(self):
		# TODO: think this should work, list comprehension
		return [[Cell(r, c) for c in range(self.columns)] for r in range(self.rows)] 
		
	def _configure_cells(self):
		for row in range(self.rows):
			for col in range(self.columns):
				cell = self._grid[row][col]
				cell.north = self._get_cell(row - 1, col)
				cell.south = self._get_cell(row + 1, col)
				cell.east = self._get_cell(row, col - 1)
				cell.west = self._get_cell(row, col + 1)
				
	# TODO: figure out if this can be done with a custom accessor method?
	def _get_cell(self, row, col):
		if row < 0 or row >= self.rows:
			return None
		if col < 0 or col >= self.columns:
			return None
			
		return self._grid[row][col]
		
	@property 
	def rows(self): 
		'''Read-only rows attribute'''
		return self._rows
		
	@property 
	def columns(self): 
		'''Read-only columns attribute'''
		return self._columns
		
	
	def random_cell(self):
		# TODO: import random & pick random row & column.
		pass
	
	def size(self):
		return self.rows * self.columns
