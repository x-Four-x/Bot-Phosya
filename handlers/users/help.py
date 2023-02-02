from aiogram import types 
from loader import dp

@dp.message_handler(commands=["help"])
async def command_start(message: types.Message):
    await message.answer(f"Привет {message.from_user.first_name}!\nЭто будущий образец команды /help")