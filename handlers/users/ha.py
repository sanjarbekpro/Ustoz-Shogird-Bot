from loader import dp
from aiogram import types
from keyboards.inline.yesno import second, yes

@dp.callback_query_handler(text='yes')
async def y(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('qabul qilindi')