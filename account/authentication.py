from django.contrib.auth.models import User

class EmailAuth(object):
	"""
		Authenticate users using email
	"""
	def authenticate(self, request, username=None, password=None):
		try:
			user = User.objects.get(email=username)
			if user.check_password(password) == True:
				return user
			else:
				return None
		except User.DoesNotExist:
			return None
			
	def get_user(self, user_id):
		try:
			return User.objects.get(pk=user_id)
		except User.DoesNotExist:
			return None
			