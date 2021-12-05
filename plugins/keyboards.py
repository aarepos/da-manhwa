from . import var
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton
)




non_vip_start_kb = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                var.non_vpi_start_button,
                callback_data = "show_plans"
            )
        ]
    ]
)


vip_start_kb = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                var.show_status_button,
                callback_data = "show_status"
            )
        ]
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