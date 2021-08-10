import yaml
class Config:
	config = []
	def __init__(self, path, default=None):
		self.path = path
		try:
			with open(self.path, 'r') as f:
				self.data = yaml.safe_load(f)
		except (yaml.YAMLError, FileNotFoundError):
			print(f"{path}: file not found and will be created")
			with open(self.path, 'x') as f:
				self.data = default
				f.write(yaml.dump(default))

	def get(self, key, default=False):
		try:
			return self.data[key]
		except (KeyError, IndexError):
			return default

	def getAll(self):
		return self.data

	def unset(self, *args):
		for k in args:
			try:
				remove(self.data[k])
			except: pass
		self.save()

	def set(self, **kwargs):
		for k, v in kwargs:
			self.data[k] = v
		self.save()

	def save(self):
		try:
			with open(self.path, 'w') as f:
				f.write(yaml.dump(self.data, allow_unicode=True))
			return 1
		except (yaml.YAMLError, FileNotFoundError):
			return -1

def getDataFolder(path=''):
	return f"plugins_data/{path}{'.yml' if path != '' else ''}"
def getMainDataFolder(path=''):
	return f"data/{path}{'.yml' if path != '' else ''}"