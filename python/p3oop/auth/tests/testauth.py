import auth

if __name__ == "__main__":
	
# Set up a test user and permission 
auth.authenticator.add_user("joe", "joepassword") 
auth.authorizor.add_permission("test program") 
auth.authorizor.add_permission("change program") 
auth.authorizor.permit_user("test program", "joe")

# TODO implement Editor class
