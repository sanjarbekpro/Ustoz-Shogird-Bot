
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


asosiy = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Hodim kerak"), KeyboardButton(text="Ustoz kerak")],
        [KeyboardButton(text="Sherik kerak"), KeyboardButton(text="Ish joyi kerak")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)