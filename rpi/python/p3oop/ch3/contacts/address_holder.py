class AddressHolder:
	def __init__(self, street='', city='', state='', code='', **kwargs):
		super().__init__(**kwargs)
		self.street = street
		self.city = city
		self.state = state
		self.code = code

