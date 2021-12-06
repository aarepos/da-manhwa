from pyrogram import Client
from plugins import var
import sys

try:

	user = int(sys.argv[1])
	plan = sys.argv[2]
	client = Client("session/api")
	client.start()
	client.send_message(user, "Your plan is " + plan)
	client.stop()

except Exception as e:
	print(e)