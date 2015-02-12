class Cell:
	def __init__(self, row, column):
		self._row = row
		self._column = column
		self._links = {} # dictionary?
		
	@property 
	def row(self): 
		'''Read-only row attribute'''
		return self._row 
		
	@property 
	def column(self): 
		'''Read-only column attribute'''
		return self._column 
		
	@property 
	def links(self): 
		'''Read-only links attribute'''
		return self._links 
		
	@property 
	def north(self): 
		'''north attribute accessor'''
		return self._north 
		
	@north.setter 
	def north(self, value): 
		self._north = value
			
	@property 
	def south(self): 
		'''south attribute accessor'''
		return self._south 
		
	@south.setter 
	def south(self, value): 
		self._south = value
			
	@property 
	def east(self): 
		'''east attribute accessor'''
		return self._east 
		
	@east.setter 
	def east(self, value): 
		self._east = value
			
	@property 
	def west(self): 
		'''west attribute accessor'''
		return self._west 
		
	@west.setter 
	def west(self, value): 
		self._west = value
						
							
	def link(self, cell, bidi=True):
		'''link 'cell' to this cell'''
		self._links[cell] = True
		if bidi:
			cell.link(self, False)
	
	def unlink(self, cell, bidi=True):
		'''unlink 'cell' from this cell'''
		del _links[cell]
		if bidi:
			cell.unlink(self, False)
			
	def is_linked(self, cell):
		'''Returns True if the given cell is linked to this cell'''
		return cell in self._links
		
	def neighbors(self):
		'''TODO figure out what the ruby code is doing here?'''
		neighbors = []
		if self.north != None:
			neighbors.append(self.north)
		if self.south != None:
			neighbors.append(self.south)
		if self.east != None:
			neighbors.append(self.east)
		if self.west != None:
			neighbors.append(self.west)
		return neighbors
		