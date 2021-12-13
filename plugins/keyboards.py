from . import var
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton
)


start_kb = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                var.non_vpi_start_button,
                callback_data = "show_plans"
            )
        ],
        [
            InlineKeyboardButton(
                var.tutorial_txt,
                callback_data = "tutorial"
            ),
            InlineKeyboardButton(
                var.solve_test_txt,
                url = var.testgir_bot
            )
        ],
        [
            InlineKeyboardButton(
                var.donate_text,
                url = "http://idpay.ir/dastream"
            )
        ],
    ]
)

plans = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                var.one_month,
                callback_data = "one_month"
            ),
            InlineKeyboardButton(
                var.three_month,
                callback_data = "three_month"
            )

        ],
        [
            InlineKeyboardButton(
                var.six_month,
                callback_data = "six_month"
            ),
            InlineKeyboardButton(
                var.one_year,
                callback_data = "one_year"
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


back_to_main_menu = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                var.home_page_button,
                callback_data = "home_page"
            )
        ]
    ]
)

show_tutorial_kb = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                var.first_tutorial,
                url = "https://t.me/editdamanhwa/17"
            ),
            InlineKeyboardButton(
                var.second_tutorial,
                url = "https://t.me/editdamanhwa/2"
            ),
        ],
        [
            InlineKeyboardButton(
                var.home_page_button,
                callback_data = "home_page"
            )
        ]
    ]
)

