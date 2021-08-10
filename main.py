from bot import Bot
import config

bot = Bot(config.GROUP_ID, config.TOKEN)
bot.start()
