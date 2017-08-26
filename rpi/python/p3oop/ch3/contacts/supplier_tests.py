from contect_manager import Contact
from supplier import Supplier

class SupplierTests():
	def run_supplier_tests(self):
		c = Contact("Some Body", "somebody@example.net")
		s = Supplier("Sup Plier", "supplier@example.net")
		print(c.name, c.email, s.name, s.email)
		
		c.all_contacts
		
		try:
			c.order("Ineed pliers") # expect error here
		except AttributeError as e: 
			print("Exception for c.order()")
			print("exception args: ", e.args)
		
		s.order("I need pliers")
	
if __name__ == "__main__":
	st = SupplierTests()
	st.run_supplier_tests()