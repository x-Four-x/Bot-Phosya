from fuzzywuzzy import fuzz
from aiogram import types
from loader import dp, bot
from utils.link_user import *
from sql_func import *
from random import choice
from data.config import *
from keyboards.default.kb_menu import *

@dp.message_handler(commands=["menu"])
async def menu_commands(message: types.Message):
    user_id = message.from_user.id
    user_url = message.from_user.url
    await message.answer(f"<b>[Меню]</b> {link_user(user_id)}, главное меню {choice(like)}",
    reply_markup=kb_menu)

@dp.message_handler(lambda message: any([fuzz.ratio("menu", message.text.lower())>=75, fuzz.ratio("меню", message.text.lower())>=75,
fuzz.ratio("главное меню", message.text.lower())>=75]))
async def menu_commands(message: types.Message):
    user_id = message.from_user.id
    user_url = message.from_user.url
    await message.answer(f"<b>[Меню]</b> {link_user(user_id)}, главное меню {choice(like)}",
    reply_markup=kb_menu)

