from . import var
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton
)





choose_test_kb = ReplyKeyboardMarkup(
    [
        
        [
            KeyboardButton(var.edit_test),
            KeyboardButton(var.tr_test),
            KeyboardButton(var.type_test)
        ],

        [KeyboardButton(var.back_to_main)]
    
    ],
    
    resize_keyboard=True,
    one_time_keyboard=True,
)



start_kb = ReplyKeyboardMarkup(
    [
        
        [KeyboardButton(var.send_tests)],
        [KeyboardButton(var.get_tests)]
    
    ],
    
    resize_keyboard=True,
    one_time_keyboard=True,
)

cancel = ReplyKeyboardMarkup(
    [
        
        [KeyboardButton(var.cancel_button)]
    
    ],
    
    resize_keyboard=True,
    one_time_keyboard=True,
)




