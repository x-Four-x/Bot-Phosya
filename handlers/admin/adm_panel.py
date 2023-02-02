from data.config import admin_id
from aiogram import types 
from loader import dp
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.inline_kb_adm import ikb_adm

@dp.message_handler(lambda message: message.from_user.id == admin_id, commands=['adm_panel'])
async def admin_panel(message: types.Message):
    await message.answer("Вы вошли в панель админа\n"
    "Выберите действие из меню ниже", reply_markup=ikb_adm)