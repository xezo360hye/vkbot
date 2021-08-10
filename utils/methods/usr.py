# compare = {
# 	"message_new": lambda event: event.object.message['from_id'],
# 	"message_reply": lambda event: event.object['from_id'],
# 	"message_edit": lambda event: event.object['from_id'],
# 	"message_typing_state": lambda event: event.object['from_id'],
# 	"message_event": lambda event: event.object['user_id'],
# 	"message_allow": lambda event: event.object['user_id'],
# 	"message_deny": lambda event: event.object['user_id'],
# 	"photo_new": lambda event: event.object['owner_id'],
# 	"photo_comment_new": lambda event: event.object['from_id'],
# 	"photo_comment_edit": lambda event: event.object['from_id'] ,
# 	"photo_comment_restore": lambda event: event.object['from_id'] ,
# 	"photo_comment_delete": lambda event: event.object['deleter_id'] ,
# 	"audio_new": lambda event: event.object['owner_id'],
# 	"video_new": lambda event: event.object['owner_id'],
# 	"video_comment_new": lambda event: event.object['from_id'],
# 	"video_comment_edit": lambda event: event.object['from_id'],
# 	"video_comment_restore": lambda event: event.object['from_id'],
# 	"video_comment_delete": lambda event: event.object['deleter_id'],
# 	"wall_post_new": lambda event: event.object['from_id'],
# 	"wall_repost": lambda event: event.object['from_id'],
# 	"wall_reply_new": lambda event: event.object['from_id'],
# 	"wall_reply_edit": lambda event: event.object['from_id'],
# 	"wall_reply_restore": lambda event: event.object['from_id'],
# 	"wall_reply_delete": lambda event: event.object['deleter_id'],
# 	"like_add": lambda event: ,
# 	"like_remove": lambda event: ,
# 	"board_post_new": lambda event: ,
# 	"board_post_edit": lambda event: ,
# 	"board_post_restore": lambda event: ,
# 	"board_post_delete": lambda event: ,
# 	"market_comment_new": lambda event: ,
# 	"market_comment_edit": lambda event: ,
# 	"market_comment_restore": lambda event: ,
# 	"market_comment_delete": lambda event: ,
# 	"market_order_new": lambda event: ,
# 	"market_order_edit": lambda event: ,
# 	"group_leave": lambda event: ,
# 	"group_join": lambda event: ,
# 	"user_unblock": lambda event: ,
# 	"user_block": lambda event: ,
# 	"poll_vote_new": lambda event: ,
# 	"group_officers_edit": lambda event: ,
# 	"group_change_settings": lambda event: ,
# 	"group_change_photo": lambda event: ,
# 	"vkpay_transaction": lambda event:
# }

def getID(event):
	ways = ['from_id', 'owner_id', 'deleter_id']
	for w in ways:
		try:
			return event.object[w]
		except: pass
	# If no ways are correct, try another one or return 0 (False):
	try:
		return event.object.message['from_id']
	except: return 0

def getUser(event):
	return vk_api.users.get(user_ids = getID(event))