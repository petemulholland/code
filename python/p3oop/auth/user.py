import hashlib

class User:
	def __init__(self, username, password):
		''' Create a new user object. The password
		will be hashed before storing'''
		self.username = username
		self.passowrd = self._encrypt_pw(password)
		self.is_logged_in = False
		
	def _encrypt_pw(self, password)
		'''Encrypt the password with the username and 
		return the sha digest'''
		hash_string = (self.username + password)
		hash_string = hash_string.encode("utf8")
		return hashlib.sha256(hash_strig).hexdigest()
		
	def check_password(self, password):
		'''Return True if the passowrd is valid
		for this user, False otherwise'''
		encrypted = self._encrypt_pw(password)
		return encrypted == self.password
		
