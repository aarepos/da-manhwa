from pyrogram import Client, filters
from . import var
from .keyboards import (
	non_vip_start_kb,
	vip_start_kb,
	plans,
	back_to_main_menu
)

@Client.on_callback_query(filters.regex("show_plans"))
async def show_plans(client, data):

	await data.answer("", show_alert = False)
	await data.message.edit(var.choose_plan_text, reply_markup = plans)







@Client.on_callback_query(filters.regex("one_month"))
async def one_month_plan(client, data):

	expire = 30
	url    = "https://google.com"
	fee    = var.one_month_fee

	await data.answer("", show_alert = False)
	await data.message.edit(
		var.one_month_plan_text.format(fee = fee, expire = expire, url = url),
		reply_markup = back_to_main_menu
	)

@Client.on_callback_query(filters.regex("three_month"))
async def three_month_plan(client, data):

	expire = 90
	url    = "https://google.com"
	fee    = var.one_month_fee

	await data.answer("", show_alert = False)
	await data.message.edit(
		var.one_month_plan_text.format(fee = fee, expire = expire, url = url),
		reply_markup = back_to_main_menu
	)



@Client.on_callback_query(filters.regex("six_month"))
async def six_month_plan(client, data):

	expire = 180
	url    = "https://google.com"
	fee    = var.one_month_fee

	await data.answer("", show_alert = False)
	await data.message.edit(
		var.one_month_plan_text.format(fee = fee, expire = expire, url = url),
		reply_markup = back_to_main_menu
	)



@Client.on_callback_query(filters.regex("one_year"))
async def one_year_plan(client, data):

	expire = 365
	url    = "https://google.com"
	fee    = var.one_month_fee

	await data.answer("", show_alert = False)
	await data.message.edit(
		var.one_month_plan_text.format(fee = fee, expire = expire, url = url),
		reply_markup = back_to_main_menu
	)