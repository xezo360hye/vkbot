from utils.plugin.command import Command
from random import randint as rnd
class Main(Command):
	cmd = ["say"]
	def run(self, event):
		self.main.vk_api.messages.send(
			user_ids = event.object.message['from_id'],
			peer_id = event.object.message['peer_id'],
			random_id = rnd(0, 1023),
			message = event.object.message['text'])
		return 1