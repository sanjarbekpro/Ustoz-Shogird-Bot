from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# second = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text="Ha", callback_data="yes"), InlineKeyboardButton(text="Yo'q", callback_data="no")],
#         [InlineKeyboardButton(text="Raqamni", request_contact=True), InlineKeyboardButton(text="Lokatsiya", request_location=True)]
#     ]
# )

second = InlineKeyboardMarkup(row_width=2)
yes = InlineKeyboardButton(text="Ha", callback_data="yes")
no = InlineKeyboardButton(text="Yo'q", callback_data="no")

second.insert(yes)
second.insert(no)