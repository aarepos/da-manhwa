from tinydb import TinyDB, Query
from pyrogram import Client
from plugins import var
import time
import sys



def main(user, plan):

	try:

		q = Query()
		db = TinyDB("database/db.json")
		expi = int(time.time()) + (int(var.ref[plan]) * 86400)


		# start client
		client = Client("session/api")
		client.start()

		# create invite_link
		link = client.create_chat_invite_link(var.private_channel, member_limit=1)
		invite_link = link.invite_link


		# cal expire
		search_for_user = db.search(q.id == user)
		if len(search_for_user) == 0:
			return

		ziro = search_for_user[0]["expire"]
		if ziro != None:
			expi += int(ziro * 86400)
		else:
			pass


		# edit_database
		db.update({
			"type": "vip",
			"expire": expi,
			"alert": True
		}, q.id == user)


		# send_for_user
		days = int(expire / 86400)
		client.send_message(
			chat_id = user,
			text = f"Your plan is {days}\nYour link: {invite_link}"
		)
		
		# end client
		client.stop()

	except Exception as e:
		print(e)



if True:
	user = int(sys.argv[1])
	plan = sys.argv[2]

	plan = plan.split("/")[-1]

	main(user, plan)
