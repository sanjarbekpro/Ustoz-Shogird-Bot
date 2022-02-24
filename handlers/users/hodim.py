from loader import dp
from aiogram import types
from keyboards.inline.yesno import second

@dp.message_handler(text='Hodim kerak')
async def h(message: types.Message):
    # msg = "Quyidagilardan birini tanlang"
    await message.answer(f"Quyidagilardan birini tanlang", reply_markup=second)

