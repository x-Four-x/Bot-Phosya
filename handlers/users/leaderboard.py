from aiogram import types
from loader import dp, bot
from utils.link_user import *
from sql_func import *
from utils.link_user import *
from utils.rates_int import *
from fuzzywuzzy import fuzz

@dp.message_handler(commands=["top"])
async def leaderboard_user(message: types.Message):
    top = check_top_balance()
    user_id = message.from_user.id
    await message.answer(f"{link_user(user_id)} топ 10 игроков по балансу:\n\n"
    f"1️⃣ {link_user(top[0][1])} - {rate_int(top[0][0])}\n"
    f"2️⃣ {link_user(top[1][1])} - {rate_int(top[1][0])}\n"
    f"3️⃣ {link_user(top[2][1])} - {rate_int(top[2][0])}\n"
    f"4️⃣ {link_user(top[3][1])} - {rate_int(top[3][0])}\n"
    f"5️⃣ {link_user(top[4][1])} - {rate_int(top[4][0])}\n"
    f"6️⃣ {link_user(top[5][1])} - {rate_int(top[5][0])}\n"
    f"7️⃣ {link_user(top[6][1])} - {rate_int(top[6][0])}\n"
    f"8️⃣ {link_user(top[7][1])} - {rate_int(top[7][0])}\n"
    f"9️⃣ {link_user(top[8][1])} - {rate_int(top[8][0])}\n"
    f"🔟 {link_user(top[9][1])} - {rate_int(top[9][0])}\n")

@dp.message_handler(lambda message: any([fuzz.ratio("top", message.text.lower())>=75, fuzz.ratio("топ", message.text.lower())>=75,
fuzz.ratio("топ игроков", message.text.lower())>=75]))
async def leaderboard_user(message: types.Message):
    top = check_top_balance()
    user_id = message.from_user.id
    await message.answer(f"{link_user(user_id)} топ 10 игроков по балансу:\n\n"
    f"1️⃣ {link_user(top[0][1])} - {rate_int(top[0][0])}\n"
    f"2️⃣ {link_user(top[1][1])} - {rate_int(top[1][0])}\n"
    f"3️⃣ {link_user(top[2][1])} - {rate_int(top[2][0])}\n"
    f"4️⃣ {link_user(top[3][1])} - {rate_int(top[3][0])}\n"
    f"5️⃣ {link_user(top[4][1])} - {rate_int(top[4][0])}\n"
    f"6️⃣ {link_user(top[5][1])} - {rate_int(top[5][0])}\n"
    f"7️⃣ {link_user(top[6][1])} - {rate_int(top[6][0])}\n"
    f"8️⃣ {link_user(top[7][1])} - {rate_int(top[7][0])}\n"
    f"9️⃣ {link_user(top[8][1])} - {rate_int(top[8][0])}\n"
    f"🔟 {link_user(top[9][1])} - {rate_int(top[9][0])}\n")