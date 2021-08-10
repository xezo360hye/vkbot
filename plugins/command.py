from utils.plugins.base import PluginBase

from utils.methods.perms import PermissionManager
from os import listdir
from os.path import isfile, join
class Main(PluginBase):
	name = "Commander"
	def __init__(self, main):
		names = [join("plugins", "commands", f).replace('/', '.')[:-3] for f in listdir(join("plugins", "commands")) if isfile(join("plugins", "commands", f))]
		self.commands = []
		for p in names:
			try:
				self.commands.append(__import__(p, fromlist=[None]).Main(main))
			except Exception as e:
				print(f"Could not load command {p}:\n> {e}")

		self.pm = PermissionManager()

		super().__init__(main)

	# This is not a bug, idk why $event is 2 args instead of 1, but the first one (type) is useless in this prog, so this solution is good enough
	rmtext = lambda a, x: x if x.object.message.update({'text': ' '.join(x.object.message['text'].split()[1:])}) else x
	def message_new(self, event):
		if event.object.message['text'].startswith('!'):
			try:
				res = []
				p = [p for p in self.commands if event.object.message['text'].split()[0][1:] in p.cmd]
				for i in p:
					if self.pm.hasPerm(event.object.message['from_id'], i.perm):
						res.append(i.run(self.rmtext(event)))
					else: self.noPerm(event)
				return -1 if -1 in res\
					else 1 if 1 in res\
					else 0
			except Exception as e:
				print(e)
				return -1

	def noPerm(self, event):
		self.main.vk_api.messages.send(
			user_ids = event.object.message['from_id'],
			peer_id = event.object.message['peer_id'],
			random_id = self.main.randid(),
			message = 'У вас недостаточно прав!')