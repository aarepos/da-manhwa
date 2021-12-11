from pyrogram import Client, filters
from . import var

from .keyboards import (
	start_kb,
	show_tutorial_kb,

)

@Client.on_callback_query(filters.regex("tutorial"))
async def show_tutorial(client, data):

	await data.answer("", show_alert = False)
	await data.message.edit(
		var.choose_tutorial,
		reply_markup = show_tutorial_kb
	)



