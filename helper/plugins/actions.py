from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
from . import var
import asyncio

from .keyboards import (
	choose_test_kb,
	cancel,
	start_kb
)

@Client.on_message(filters.regex(var.get_tests))
async def get_tests(client, message):

	await message.reply_text(
		var.choose_test_text,
		reply_markup = choose_test_kb
	)



@Client.on_message(filters.regex(var.send_tests))
async def send_tests(client, message):

	try:
		test = await client.ask(
			message.from_user.id,
			var.send_me_test,
			timeout = 59,
			reply_markup = cancel
		)
	except asyncio.exceptions.TimeoutError:
		await message.reply_text(var.your_time_is_out, reply_markup = start_kb)
		return

	if test.text == var.cancel_button:
		await message.reply_text(var.start_text, reply_markup = start_kb)
		return


	try:
		file_id = test["document"]["file_id"]
	except:
		await message.reply_text(var.send_me_a_file, reply_markup = start_kb)
		return


	uid = message.from_user.id
	await client.send_document(
		chat_id = var.admin,
		document = file_id,
		caption = f"برای مشاهده مشخصات فرستنده ‌[اینجا کلیک](tg://user?id={uid}) کنید.",
		reply_markup = InlineKeyboardMarkup(
		    [
		        [
		            InlineKeyboardButton(
		                var.no,
		                callback_data = f"no-{uid}"
		            ),
		            InlineKeyboardButton(
		                var.yes,
		                callback_data = f"yes-{uid}"
		            ),
		        ]
		    ]
		)
	)

	await message.reply_text(var.sent, reply_markup = start_kb)



@Client.on_callback_query(filters.all)
async def handle_func(client, data):
	
	calld = data.data.split("-")
	ctype = calld[0]
	user  = int(calld[1])

	await data.answer(var.sent_for_user, show_alert = True)

	if ctype == "no":
		await client.send_message(
			chat_id = user,
			text = var.rad_text
		)
	else:
		await client.send_message(
			chat_id = user,
			text = var.done_text
		)