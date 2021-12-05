from pyrogram import Client, filters
from tinydb import TinyDB, Query
from . import var

from .keyboards import (
	non_vip_start_kb,
	vip_start_kb
)


# block
@Client.on_message(filters.all, -2)
async def check_for_message_in_block(client, message):

	q = Query()
	db = TinyDB("database/db.json")
	uid = message.from_user.id

	search_for_user = db.search(q.id == uid)

	if len(search_for_user) == 0: return

	user_type = search_for_user[0]["status"]

	if user_type == "block":
		await message.stop_propagation()

@Client.on_callback_query(filters.all, -2)
async def check_for_call_in_block(client, data):

	q = Query()
	db = TinyDB("database/db.json")
	uid = data.from_user.id

	search_for_user = db.search(q.id == uid)

	if len(search_for_user) == 0: return

	user_type = search_for_user[0]["status"]

	if user_type == "block":
		await data.message.stop_propagation()



# channel lock
@Client.on_message(filters.text, -1)
async def channel_lock(client, message):
    
    uid = message.from_user.id

    try:

        result = await client.get_chat_member(var.public_channel, uid)
        return

    except Exception as e:
        await client.send_message(uid, f'Please join in my channel: @{var.public_channel}')
        await message.stop_propagation()



# add new user in database
async def new_user(client, message):

	q = Query()
	db = TinyDB("database/db.json")
	uid = message.from_user.id

	db.insert({
		"id": uid,
		"type": "free",
		"expire": None,
		"alert": False,
		"status": None
	})



# start command handler
@Client.on_message(filters.command("start"))
async def start(client, message):

	q = Query()
	db = TinyDB("database/db.json")
	uid = message.from_user.id


	search_for_user = db.search(q.id == uid)
	if len(search_for_user) == 0:
		await new_user(client, message)
		inline_kb = non_vip_start_kb
		text      = var.non_vip_start_txt
	else:
		user_type = search_for_user[0]["type"]

		if user_type == "vip":
			inline_kb = vip_start_kb
			text      = var.vip_start_txt
		else:
			inline_kb = non_vip_start_kb
			text      = var.non_vip_start_txt

	await message.reply_text(text, reply_markup = inline_kb)




@Client.on_callback_query(filters.regex("home_page"))
async def return_to_home_page(client, data):

	q = Query()
	db = TinyDB("database/db.json")
	uid = data.from_user.id

	search_for_user = db.search(q.id == uid)
	user_type = search_for_user[0]["type"]

	if user_type == "vip":
		inline_kb = vip_start_kb
		text      = var.vip_start_txt
	else:
		inline_kb = non_vip_start_kb
		text      = var.non_vip_start_txt
	
	await data.answer("", show_alert = False)
	await data.message.edit(
		text,
		reply_markup = inline_kb
	)