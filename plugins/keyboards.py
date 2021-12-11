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

show_tutorial_kb = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                var.first_tutorial,
                url = "https://t.me/kermitium"
            ),
            InlineKeyboardButton(
                var.second_tutorial,
                url = "https://t.me/hangeotako"
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

