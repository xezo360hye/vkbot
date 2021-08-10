class Command(object):
	cmd = ["cmd"]
	perm = 0
	def __init__(self, main, *args):
		self.main = main

	def getName(self):
		return self.name

	def run(self, event): pass