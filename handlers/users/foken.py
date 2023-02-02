from loader import dp
from sql_func import *
from aiogram import types

"""Баланс фокенов"""

@dp.message_handler(commands=["foken"])
async def foken(message: types.Message):
    await message.answer(f"{message.from_user.first_name} у тебя {check_foken(message.from_user.id)} Фокена(ов)\nТы можешь заработать их - перейди по команде /help")