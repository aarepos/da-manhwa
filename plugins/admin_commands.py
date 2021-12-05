from pyrogram import Client, filters
from tinydb import TinyDB, Query
from . import var


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