from utils.methods.config import Config, getMainDataFolder
from utils.methods.usr import getID
def isBanned(event):
	banlist = Config(getMainDataFolder() + "banlist.yml")
	user = getID(event)
	try:
		return user in banlist.getAll()
	except: return False