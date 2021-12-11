from pyrogram import Client, filters
from . import var

from .keyboards import (
	start_kb,
	cancel
)



@Client.on_message(filters.command("start") | filters.regex(var.back_to_main))
async def start_command(client, message):

	await message.reply_text(
		var.start_text,
		reply_markup = start_kb
	)

