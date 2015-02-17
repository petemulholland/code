from auth.authenticator import Authenticator
from auth.authorizer import Authorizer

authenticator = Authenticator()
authorizer = Authorizer(authenticator)
