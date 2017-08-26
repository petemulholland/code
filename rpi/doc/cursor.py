class Cursor:
	def __init__(self, document):
		self.document = document
		self.position = 0
		
	def forward(self):
		if self.position < len(self.document.characters):
			self.position += 1
		
	def back(self):
		if self.position > 0:
			self.position -= 1
		
	def home(self):
		if self.position > 0:
			while self.document.characters[self.position - 1].character != '\n':
				self.back()
				if self.position == 0:
					# got to beginning of file before newline
					break
				
	def end(self):
		if len(self.document.characters) > 0:
			while self.position < len(self.document.characters) and \
					self.document.characters[self.position].character != '\n':
				self.forward()
	
	