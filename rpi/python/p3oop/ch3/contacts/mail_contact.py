from contact_manager import Contact

class MailSender:
	def send_mail(self, message):
		print ("Sending mail to " + self.email)
		# add email logic here
		
		
class EmailableContact(Contact, MailSender):
	pass
	