from pyrogram import Client, filters
from . import var

from .keyboards import (
	start_kb
)

@Client.on_message(filters.regex(var.edit_test))
async def send_edit_text(client, message):

	uid = message.from_user.id
	await client.send_document(uid, "../files/edit.zip", reply_markup = start_kb)

@Client.on_message(filters.regex(var.tr_test))
async def send_tr_text(client, message):

	uid = message.from_user.id
	await client.send_document(uid, "../files/translate.zip", reply_markup = start_kb)

@Client.on_message(filters.regex(var.type_test))
async def send_type_text(client, message):

	uid = message.from_user.id
	# file = open("../files/type.zip")
	await client.send_document(uid, "../files/type.zip", reply_markup = start_kb)
