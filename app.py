from pyrogram import Client, filters
from flask import Flask, request
from plugins import var


app = Flask(__name__)


@app.route("/", methods = ["GET", "POST"])
def call_back():
	content = request.json

	try:
		# get info
		# user = int(content["telegram"])
		plan = content["reference"]["link"]
		print("cant")
	except:
		return

	# days = int(var.ref[plan])


	client = Client("session/api")
	client.start()
	client.send_message(956473054, plan)
	client.stop()

    # try:
    #     result = client.get_chat_member(var.private_channel, user)
    #     invite_link = client.create_chat_invite_link(var.private_channel, member_limit = 1)
    # except Exception as e:
    #     # client.send_message(uid, f'Please join in my channel: @{var.public_channel}')
    #     invite_link = False




        


    