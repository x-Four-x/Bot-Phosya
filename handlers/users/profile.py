from aiogram import types
from loader import dp, bot
from sql_func import *
from fuzzywuzzy import fuzz
from utils.profile_user import *
from utils.link_user import *

@dp.message_handler(commands=["profile"])
async def profile(message: types.Message):
    user_id = message.from_user.id
    user_url = message.from_user.url
    sp = check_profile(user_id)
    await message.answer(f"<b>[Профиль 📋]</b> {link_user(user_id)}, ваш профиль {choice(info)}:\n"
    f"👤 Имя - {link_user(user_id)}\n"
    f"💰 На руках - {ranks_int(sp['money'])}$\n"
    f"💠 Фокенов - {sp['foken']} штук\n"
    f"📅 Дата регистрации - {sp['date_reg']}", parse_mode='html')

@dp.message_handler(lambda message: any([fuzz.ratio('профиль', message.text.lower()) >= 75, fuzz.ratio('мой профиль', message.text.lower()) >= 75, fuzz.ratio('profile', message.text.lower()) >= 75,
fuzz.ratio('my profile', message.text.lower()) >= 75]))
async def profile(message: types.Message):
    user_id = message.from_user.id
    user_url = message.from_user.url
    sp = check_profile(user_id)
    await message.answer(f"<b>[Профиль 📋]</b> {link_user(user_id)}, ваш профиль {choice(info)}:\n"
    f"👤 Имя - {sp['name']}\n"
    f"💰 На руках - {ranks_int(sp['money'])}$\n"
    f"💠 Фокенов - {sp['foken']} штук\n"
    f"📅 Дата регистрации - {sp['date_reg']}", parse_mode='html')
