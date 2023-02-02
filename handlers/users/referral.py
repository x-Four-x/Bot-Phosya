from aiogram import types
from loader import dp, bot
from sql_func import *
from fuzzywuzzy import fuzz
from utils.profile_user import *
from utils.link_user import *
from aiogram.utils.deep_linking import get_start_link

@dp.message_handler(commands=["referral"])
async def referal(message: types.Message):
    user_id = message.from_user.id
    user_url = message.from_user.url
    referal_link = await get_start_link(user_id)
    await message.answer(f"{link_user(user_id)}, твоя ссылка: <code>{referal_link}</code>\n"
    f"⚠️ Если по ней перейдет человек не игравший в бота ты получишь награду: игровую валюту кейсы, а иногда и фокены {choice(joi)}\n"
    f"{choice(info)} Твой текущий уровень рефералки - {check_ref_lev(user_id)} {choice(like)}")


@dp.message_handler(lambda message: any([fuzz.ratio('реф ссылка', message.text.lower()) >= 75, fuzz.ratio('реф', message.text.lower()) >= 75, fuzz.ratio('реферал', message.text.lower()) >= 75,
fuzz.ratio('реферальная ссылка', message.text.lower()) >= 75, fuzz.ratio('referral', message.text.lower()) >= 75, fuzz.ratio('ref', message.text.lower()) >= 75, fuzz.ratio('реферал ссылка', message.text.lower()) >=75]))
async def referal(message: types.Message):
    user_id = message.from_user.id
    user_url = message.from_user.url
    referal_link = await get_start_link(user_id)
    await message.answer(f"{link_user(user_id)}, твоя ссылка: <code>{referal_link}</code>\n"
    f"⚠️ Если по ней перейдет человек который не играл в бота ты получишь награду: игровую валюту кейсы, а иногда и фокены {choice(joi)}\n"
    f"{choice(info)} Твой текущий уровень рефералки - {check_ref_lev(user_id)} {choice(like)}")

