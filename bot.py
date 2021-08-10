import vk_api.vk_api

from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.bot_longpoll import VkBotEventType

from os import listdir
from os.path import isfile, join

from time import time

from utils.methods.isbl import isBanned
class Bot:
	blacklist = ['message_typing_state', 'message_reply']

	def __init__(self, group_id, token):
		vk = vk_api.VkApi(token = token)
		self.long_poll = VkBotLongPoll(vk, group_id, wait = 30)
		self.vk_api = vk.get_api()

		names = [join("plugins", f).replace('/', '.')[:-3] for f in listdir("plugins") if isfile(join("plugins", f)) and f[-3:] == ".py"]
		self.plugins = {}
		for p in names:
			try:
				self.plugins[__import__(p, fromlist=[None]).Main.name] = __import__(p, fromlist=[None]).Main(self)
				print(f"'{p}.py' loaded..")
			except Exception as e:
				print(f"Could not load plugin {p}:\n> {e}")
		if len(self.plugins) == 0:
			print("""Bot created, but no plugins was loaded
				Bot will be stopped now""")
			exit()
		print("Bot created")

	def start(self):
		while True:
			try:
				for event in self.long_poll.listen():
					# print(event)
					if isBanned(event): 
						print("User blocked, event passed")
						continue
					c = []
					for plugin in self.plugins.values():
						c.append(plugin.run(event))
					if event.type.value not in self.blacklist: 
						self.info(c, event.type.value)
			except KeyboardInterrupt:
				exit('')
			except: pass

	def info(self, c, name):
		if len(c) - len(i for i in c if i == None) == 0:
			print('No response')
			return
		print(f"| Plugins response info ({name})")
		print(f"| Succesful: {len([i for i in c if i == 1])}")
		print(f"| Errors: {len([i for i in c if i == 0])}")
		print(f"| Criticals: {len([i for i in c if i == -1])}")
		print(f"| No response: {len([i for i in c if i == None])}")
		print( "----------------")

	def randid(self):
		return time() * 10**7 % 10**12 // 10**4