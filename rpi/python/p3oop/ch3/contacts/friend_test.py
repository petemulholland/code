from friend import Friend

class FriendTests():
	def run_friend_tests(self):
		# think friend needs named params now.
		friend = Friend(name="Jaoh Smith", email="jsmith@example.net", phone="1234-555-1234", street="some st.", city="Some City")
		print("friend.name: ", friend.name)
		print("friend.email: ", friend.email)
		print("friend.phone: ", friend.phone)
		print("friend.street: ", friend.street)
		print("friend.city: ", friend.city)
		print("friend.state: ", friend.state)
		print("friend.code: ", friend.code)
		
if __name__ == "__main__":
	ft = FriendTests()
	ft.run_friend_tests()