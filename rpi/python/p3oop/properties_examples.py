# examples of "restricting" access to attributes using properties
# see loc 2611 in Python 3 OOP
class Foo: 
	@property 
	def foo(self): 
		return self._foo 
		
	@foo.setter 
	def foo(self, value): 
		self._foo = value


class Silly: 
	# property picks up doc string from inital getter method.
	@property 
	def silly(self): 
		"This is a silly property" 
		print("You are getting silly") 
		return self._silly 
		
	@silly.setter 
	def silly(self, value): 
		print("You are making silly {}".format( value)) 
		self._silly = value 
	

