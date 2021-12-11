from pyrogram import Client, filters
from . import var
from .keyboards import (
	start_kb,
	plans,
	back_to_main_menu
)

from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton
)

@Client.on_callback_query(filters.regex("show_plans"))
async def show_plans(client, data):

	await data.answer("", show_alert = False)
	await data.message.edit(var.choose_plan_text, reply_markup = plans)







@Client.on_callback_query(filters.regex("one_month"))
async def one_month_plan(client, data):

	plan   = "یک ماهه"
	fee    = var.one_month_fee
	url    = var.one_month_payment_url
	uid    = data.from_user.id

	await data.answer("", show_alert = False)
	await data.message.edit(
		var.basic_payment_text.format(plan = plan, fee = fee, uid = uid, admin = var.admin2),
		parse_mode = "markdown",
		reply_markup = InlineKeyboardMarkup(
		    [
		        [
		            InlineKeyboardButton(
		                var.payment_button,
		                url = url
		            )
		        ],
		        [
		            InlineKeyboardButton(
		                var.home_page_button,
		                callback_data = "home_page"
		            )
		        ]
		    ]
		)
	)

@Client.on_callback_query(filters.regex("three_month"))
async def three_month_plan(client, data):

	plan   = "سه ماهه"
	fee    = var.three_month_fee
	url    = var.three_month_payment_url
	uid    = data.from_user.id

	await data.answer("", show_alert = False)
	await data.message.edit(
		var.basic_payment_text.format(plan = plan, fee = fee, uid = uid, admin = var.admin2),
		parse_mode = "markdown",
		reply_markup = InlineKeyboardMarkup(
		    [
		        [
		            InlineKeyboardButton(
		                var.payment_button,
		                url = url
		            )
		        ],
		        [
		            InlineKeyboardButton(
		                var.home_page_button,
		                callback_data = "home_page"
		            )
		        ]
		    ]
		)
	)



@Client.on_callback_query(filters.regex("six_month"))
async def six_month_plan(client, data):

	plan   = "شش ماهه"
	fee    = var.six_month_fee
	url    = var.six_month_payment_url
	uid    = data.from_user.id

	await data.answer("", show_alert = False)
	await data.message.edit(
		var.basic_payment_text.format(plan = plan, fee = fee, uid = uid, admin = var.admin2),
		parse_mode = "markdown",
		reply_markup = InlineKeyboardMarkup(
		    [
		        [
		            InlineKeyboardButton(
		                var.payment_button,
		                url = url
		            )
		        ],
		        [
		            InlineKeyboardButton(
		                var.home_page_button,
		                callback_data = "home_page"
		            )
		        ]
		    ]
		)
	)



@Client.on_callback_query(filters.regex("one_year"))
async def one_year_plan(client, data):

	plan   = "یک ساله"
	fee    = var.one_year_fee
	url    = var.one_year_payment_url
	uid    = data.from_user.id

	await data.answer("", show_alert = False)
	await data.message.edit(
		var.basic_payment_text.format(plan = plan, fee = fee, uid = uid, admin = var.admin2),
		parse_mode = "markdown",
		reply_markup = InlineKeyboardMarkup(
		    [
		        [
		            InlineKeyboardButton(
		                var.payment_button,
		                url = url
		            )
		        ],
		        [
		            InlineKeyboardButton(
		                var.home_page_button,
		                callback_data = "home_page"
		            )
		        ]
		    ]
		)
	)