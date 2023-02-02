from aiogram import types
from loader import dp, bot
from utils.link_user import *
from data.config import *
from random import choice

@dp.message_handler(text="Контакты 👤")
async def contact_commands(message: types.Message):
    await message.answer(f"{choice(info)} По вопросам и предложениям писать - <a href='https://t.me/x_FouR_x'>x_FouR_x</a>")