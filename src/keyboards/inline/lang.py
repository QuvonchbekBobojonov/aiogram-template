from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

long_buttons = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🇺🇿 Uzbek", callback_data='uz'),
        InlineKeyboardButton(text="🇷🇺 Русский", callback_data='ru')
    ]
])
