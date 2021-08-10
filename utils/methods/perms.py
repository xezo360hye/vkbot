from utils.methods.config import Config, getMainDataFolder
class PermissionManager:
	def __init__(self):
		self.perms = Config(getMainDataFolder('perms'), {})

	def hasPerm(self, user_id, perm):
		if perm == 0: return True
		return perm in self.getPerms(user_id)

	def getPerms(self, user_id):
		return self.perms.getAll().get(user_id, [])

	def addPerm(self, user_id, perm):
		self.perms.data[user_id].append(perm)
		self.perms.save()
		return self

	def rmPerm(self, user_id, perm):
		try:
			self.perms.get(user_id, []).remove(perm)
			self.perms.save()
		except: pass
		return self
	def resetPerms(self, user_id):
		for p in self.perms.get(user_id, []):
			self.rmPerm(user_id, p)
		return self