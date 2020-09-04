class User:
	uuid = ''
	tag = ''

class UserManager:
	_users = {}


	def register(self, user:User) -> bool:
		if user.tag in self._users:
			return False
		else:
			self._users[user.tag] = user
			return True


	def unregiser(self, tag:str) -> bool:
		return self._users.pop(tag) != None 


