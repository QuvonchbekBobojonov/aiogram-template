from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

admin_btns = ReplyKeyboardMarkup(resize_keyboard=True)

admin_btns.add(KeyboardButton(text="Xabar jo'natish"))
admin_btns.add(KeyboardButton(text="Statistika"))
