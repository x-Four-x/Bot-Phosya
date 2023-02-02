from aiogram import types
from loader import dp, bot
from utils.link_user import *
from sql_func import *
from random import choice
from data.config import *
from keyboards.default.kb_menu import *
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_chanell = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Подпишись ✅', url=link_chanell),
                                    ],
                                ])

@dp.message_handler(text="Наш канал 📢")
async def menu_commands(message: types.Message):
    await message.answer(f"📢 Наши каналы:\n"
    f"1⃣ <a href='{link_chanell}'>Bot Phosya 🎮 | Новости 📢</a> - [{await bot.get_chat_member_count(id_chanell)} уч.]\n"
    f"{choice(info)} Самые свежие новости о нововедениях и ивентах <a href='{link_chanell}'>тут</a>",
    reply_markup=ikb_chanell)