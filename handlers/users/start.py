from aiogram import types 
from loader import dp
from sql_func import *
from aiogram.dispatcher import FSMContext
from utils.link_user import link_user
from data.config import *
from random import choice
from keyboards.default.kb_menu import *
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import CallbackQuery
from datetime import timedelta, datetime

@dp.message_handler(lambda message: user_exists(message.from_user.id) is None)
async def command_start(message: types.Message):
    user_url = message.from_user.url
    user_id = message.from_user.id
    args = message.get_args()
    if args is not None:
        if args != 0 and args.isdigit():
            if check_valid_id(args) == True:
                await add_ref(args, user_id)
    add_user(message.from_user.id, user_url)
    await message.answer(f"👋 Добро пожаловать {link_user(user_id)}, это игровой бот «Фося» 🎮!\n"
    f"Он не даст тебе заскучать своими играми, ивентами, конкурсами и... хотя ты сам увидишь всё интересное в нём! {choice(joi)}\n"
    f"В боте есть множество команд их всех ты можешь увидеть в кнопочке «меню» левее от ввода букв\n"
    f"И кстати... подпишись на наш <a href='{link_chanell}'>канал</a> 🙂!\n"
    "Ps: Бот еще сырой о багах сообщайте - @x_FouR_x", reply_markup=kb_menu)


