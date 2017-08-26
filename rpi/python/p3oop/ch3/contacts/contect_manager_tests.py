from contact_manager import Contact, ContactList

class ContactTests():
	def run_contact_tests(self):
		pass

	def run_contact_list_tests(self):
		c1 = Contact(John A", johna@example.net")
		c2 = Contact(John B", johnb@example.net")
		c3 = Contact(Jenna C", jennac@example.net")
		
		[c.name for c in Contact.all_contacts.search('John')]
		
		
if __name__ == "__main__":
	ct = ContactTests()
	ct.run_contact_list_tests()