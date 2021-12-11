from pyrogram import Client, filters
from . import var

from .keyboards import (
	start_kb
)

@Client.on_message(filters.regex(var.edit_test))
async def send_edit_text(client, message):

	await message.reply_text("TEXT & FILE", reply_markup = start_kb)

@Client.on_message(filters.regex(var.tr_test))
async def send_tr_text(client, message):

	await message.reply_text("TEXT & FILE", reply_markup = start_kb)

@Client.on_message(filters.regex(var.type_test))
async def send_type_text(client, message):

	await message.reply_text("TEXT & FILE", reply_markup = start_kb)

@Client.on_message(filters.regex(var.clean_test))
async def send_clean_text(client, message):

	await message.reply_text("TEXT & FILE", reply_markup = start_kb)