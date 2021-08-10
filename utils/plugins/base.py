class PluginBase(object):
	name = "Plugin"
	def __init__(self, main, *args):
		self.main = main

	def getName(self):
		return self.name

	def run(self, event):
		try:
			return getattr(self, event.type.value)(event)
		except AttributeError:
			try:
				return getattr(self, event.type)(event)
			except Exception as e:
				print(f"Critical error in {self.getName()}:\n{e}")
				return -1
		except Exception as e:
			print(f"Critical error in {self.getName()}:\n{e}")
			return -1

	def message_new(self, event): pass
	def message_reply(self, event): pass
	def message_edit(self, event): pass
	def message_event(self, event): pass
	def message_typing_state(self, event): pass
	def message_allow(self, event): pass
	def message_deny(self, event): pass

	def photo_new(self, event): pass
	def photo_comment_new(self, event): pass
	def photo_comment_edit(self, event): pass
	def photo_comment_restore(self, event): pass
	def photo_comment_delete(self, event): pass

	def audio_new(self, event): pass
	def video_new(self, event): pass
	def video_comment_new(self, event): pass
	def video_comment_edit(self, event): pass
	def video_comment_restore(self, event): pass
	def video_comment_delete(self, event): pass

	def wall_post_new(self, event): pass
	def wall_repost(self, event): pass
	def wall_reply_new(self, event): pass
	def wall_reply_edit(self, event): pass
	def wall_reply_restore(self, event): pass
	def wall_reply_delete(self, event): pass

	# Likes for posts, photos e.g.
	def like_add(self, event): pass
	def like_remove(self, event): pass

	def board_post_new(self, event): pass
	def board_post_edit(self, event): pass
	def board_post_restore(self, event): pass
	def board_post_delete(self, event): pass

	# For shops
	def market_comment_new(self, event): pass
	def market_comment_edit(self, event): pass
	def market_comment_restore(self, event): pass
	def market_comment_delete(self, event): pass

	def market_order_new(self, event): pass
	def market_order_edit(self, event): pass

	def group_leave(self, event): pass
	def group_join(self, event): pass

	def user_unblock(self, event): pass
	def user_block(self, event): pass

	def poll_vote_new(self, event): pass

	# Changing group's staff, settings and avatar
	def group_officers_edit(self, event): pass
	def group_change_settings(self, event): pass
	def group_change_photo(self, event): pass

	# Event in mini-app
	def app_payload(self, event): pass

	def donut_subscription_create(self, event): pass
	def donut_subscription_prolonged(self, event): pass
	def donut_subscription_expired(self, event): pass
	def donut_subscription_cancelld(self, event): pass
	def donut_subscription_price_change(self, event): pass
	def donut_money_withdraw(self, event): pass
	def donut_money_withdraw_error(self, event): pass