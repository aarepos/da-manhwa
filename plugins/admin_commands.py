from pyrogram import Client, filters
from tinydb import TinyDB, Query
from . import var
import time

from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton
)


@Client.on_message(filters.user(var.admin) & filters.command("block"))
async def block_user(client, message):

	uid = message.from_user.id
	q   = Query()
	db  = TinyDB("database/db.json")

	try:
		target = int(message.command[1])
	except:
		return


	search_for_user = db.search(q.id == target)
	if len(search_for_user) == 0:
		await message.reply_text("User not found.")
		return 0

	db.update({"status": "block"}, q.id == target)
	await message.reply_text("OK, blocked.")


@Client.on_message(filters.user(var.admin) & filters.command("unblock"))
async def unblock_user(client, message):

	uid = message.from_user.id
	q   = Query()
	db  = TinyDB("database/db.json")

	try:
		target = int(message.command[1])
	except:
		return


	search_for_user = db.search(q.id == target)
	if len(search_for_user) == 0:
		await message.reply_text("User not found.")
		return 0

	db.update({"status": None}, q.id == target)
	await message.reply_text("OK, unblocked.")



@Client.on_message(filters.user(var.admin) & filters.command("gift"))
async def gift(client, message):

	uid = message.from_user.id
	q   = Query()
	db  = TinyDB("database/db.json")
	now = int(time.time())

	try:
		target = int(message.command[1])
		days   = int(message.command[2])
	except:
		return


	search_for_user = db.search(q.id == target)
	if len(search_for_user) == 0:
		await message.reply_text("User not found!")
		return

	last_expire = search_for_user[0]["expire"]
	
	if last_expire != None:
		diff = int(int(last_expire - now) / 86400)
		days += diff


	new_expire = now + (int(days * 86400))
	db.update({
		"type": "vip",
		"expire": new_expire,
		"alert": True
	}, q.id == target)

	await message.reply_text("OK")

	# create invite_link
	link = await client.create_chat_invite_link(var.private_channel, member_limit=1)
	invite_link = link.invite_link

	await client.send_message(
		chat_id = target,
		text = var.gift_text.format(days = days),
		reply_markup = InlineKeyboardMarkup(
		    [
		        [
		            InlineKeyboardButton(
		                var.invite_link_button,
		                url = invite_link
		            )
		        ]
		    ]
		)
	)


@Client.on_message(filters.user(var.admin) & filters.command("db"))
async def send_db(client, message):


	try:
		await client.send_document(message.from_user.id, "database/db.json")
	except:
		await message.reply_text("Error!")


@Client.on_message(filters.user(var.admin) & filters.command("info"))
async def info(client, message):

	q = Query()
	db = TinyDB("database/db.json")
	now = int(time.time())

	try:
		target = int(message.command[1])
	except:
		return

	search_for_user = db.search(q.id == target)
	if len(search_for_user) == 0:
		await message.reply_text("User not found!")
		return

	# get info
	user_type = search_for_user[0]["type"]
	expire    = search_for_user[0]["expire"]

	days      = int((expire - now) / 86400)

	await message.reply_text(f"type: {user_type}\nexpire: {days} days")


@Client.on_message(filters.user(var.admin) & filters.command("len"))
async def length(client, message):

	q = Query()
	db = TinyDB("database/db.json")

	free_len = len(db.search(q.type == "free"))
	vip_len  = len(db.search(q.type == "vip"))

	all_len  = free_len + vip_len

	await message.reply_text(f"free: {free_len}\nvip: {vip_len}\nall: {all_len}")