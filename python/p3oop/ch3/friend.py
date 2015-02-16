from contact_manager import Contact
from address_holder import AddressHolder

class Friend(Contact, AddressHolder):
	def __init__(self, phone='', **kwargs)
		super().__init__(**kwargs)
		self.phone = phone

