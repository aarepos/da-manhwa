from apscheduler.schedulers.asyncio import AsyncIOScheduler
from tinydb import TinyDB, Query
from pyrogram import Client
from pyromod import listen
from plugins import var
import time


api = Client("session/api")


def event_loop():

	q = Query()
	db = TinyDB("database/db.json").all()
	now = int(time.time())

	for user in db:
		user_id = user["id"]
		expire  = user["expire"]

		if expire == None:
			continue

		neg = expire - now
		if neg < 0:
			db.update({"type": "free", "expire": None, "alert": False}, q.id == user_id)
			try:
				api.start()
				api.kick_chat_member(var.private_channel, user_id)
				api.send_message(user_id, var.you_kicked)
				api.stop()
			except:
				pass




scheduler = AsyncIOScheduler()
scheduler.add_job(event_loop, "interval", seconds = 21600)
scheduler.start()




if __name__ == "__main__":
	api.run()