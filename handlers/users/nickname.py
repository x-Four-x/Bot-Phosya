from aiogram import types
from loader import dp, bot
from utils.link_user import *
from sql_func import *
from utils.link_user import *
from fuzzywuzzy import fuzz
import emoji
import html


@dp.message_handler(lambda message: any([fuzz.ratio("ник", message.text.lower().split()[0])>=75, fuzz.ratio("никнейм", message.text.lower().split()[0])>=75,
fuzz.ratio("имя", message.text.lower().split()[0])>=75, fuzz.ratio("nick", message.text.lower().split()[0])>=75, fuzz.ratio("nickname", message.text.lower().split()[0])>=75]))
async def nickname(message: types.Message):
    user_id = message.from_user.id
    nick = message.text.partition(' ')[2]
    if nick != '':
        nick_len = int(len(nick)) - emoji.emoji_count(nick) + emoji.emoji_count(nick)*2
        if nick_len >= 16:
            await message.answer(f"⚡️ НИК ➜ {link_user(user_id)} ой... "
            f"максимальная длина ника 16 символов {choice(info)}")
        elif nick_len <= 2:
            await message.answer(f"⚡️ НИК ➜ {link_user(user_id)} ой... "
            f"минимальная длина ника 3 символа {choice(info)}")
        else:
            edit_nick(str(nick), user_id)
            await message.answer(f"⚡️ НИК ➜ теперь ты «{html.escape(nick)}»")
    else:
        add_game(user_id, 'nick')
        await message.answer(f"⚡️ НИК ➜ {link_user(user_id)} введи желаемый ник")

@dp.message_handler(lambda message: check_game(message.from_user.id)=='nick')
async def nickname(message: types.Message):
    user_id = message.from_user.id
    nick = message.text
    nick_len = int(len(nick)) - emoji.emoji_count(nick) + emoji.emoji_count(nick)*2
    if nick_len >= 16:
        await message.answer(f"⚡️ НИК ➜ {link_user(user_id)} ой... "
        f"максимальная длина ника 16 символов {choice(info)}")
    elif nick_len <= 2:
        await message.answer(f"⚡️ НИК ➜ {link_user(user_id)} ой... "
        f"минимальная длина ника 3 символа {choice(info)}")
    else:
        edit_nick(str(nick), user_id)
        add_game(user_id, '')
        await message.answer(f"⚡️ НИК ➜ теперь ты «{html.escape(nick)}»")
