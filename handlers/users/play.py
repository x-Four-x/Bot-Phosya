from random import choice
from random import randint
from utils.rates_user import *
from keyboards.inline import *
from aiogram import types
from loader import dp, bot
from data.config import *
from aiogram.dispatcher import FSMContext
from keyboards.default import kb_play_list
from sql_func import *
from fuzzywuzzy import fuzz


@dp.message_handler(commands=["games"])
async def play(message: types.Message):
    user_id = message.from_user.id
    user_url = message.from_user.url
    await message.answer(
        f"<b>[Игры]</b> {link_user(user_id)}, выбери одну игру из списка игр нижне ⬇",
        reply_markup=kb_play_list)


@dp.message_handler(lambda message: any([fuzz.ratio(f"{message.text.lower()}", "игры") >= 75, fuzz.ratio(f"{message.text.lower()}", "игра") >= 75,
fuzz.ratio(f"{message.text.lower()}", "игра") >= 75, fuzz.ratio(f"{message.text.lower()}", "Список игр") >= 75]))
async def play(message: types.Message):
    user_id = message.from_user.id
    user_url = message.from_user.url
    await message.answer(
        f"<b>[Игры]</b> {link_user(user_id)}, выбери одну игру из списка игр нижне ⬇",
        reply_markup=kb_play_list)

@dp.message_handler(lambda message: fuzz.ratio(f"{message.text.lower()}", "футбол") >= 75)
async def football(message: types.Message):
    user_id = message.from_user.id
    add_game(id=user_id, game='football')
    await message.answer(f"<b>[Игры - Футбол ⚽]</b> {link_user(user_id)}, напиши сумму ставки\n"
    f"{choice(info)} Минимальная сумма ставки - 100$\n"
    f"{check_balance(user_id, True)}", reply_markup=rates_inl("⚽", user_id, "Фут"))


@dp.message_handler(lambda message: fuzz.ratio(f"{message.text.lower()}", "дартс") >= 75)
async def football(message: types.Message):
    user_id = message.from_user.id
    add_game(id=user_id, game='darts')
    await message.answer(f"<b>[Игры - Дартс 🎯]</b> {link_user(user_id)}, напиши сумму ставки\n"
    f"{choice(info)} Минимальная сумма ставки - 100$\n"
    f"{check_balance(user_id, True)}", reply_markup=rates_inl("🎯", user_id, "Дар"))


@dp.message_handler(lambda message: fuzz.ratio(f"{message.text.lower()}", "казино") >= 75)
async def casino(message: types.Message):
    user_id = message.from_user.id
    user_url = message.from_user.url
    add_game(id=user_id, game='casino')
    await message.answer(f"<b>[Игры - Казино 🎰]</b> {link_user(user_id)}, напиши сумму ставки\n"
    f"{choice(info)} Минимальная сумма ставки - 100$\n"
    f"{check_balance(user_id, True)}", reply_markup=rates_inl("🎰", user_id, "Каз"))


@dp.message_handler(lambda message: fuzz.ratio(f"{message.text.lower()}", "стаканчик") >= 70)
async def cup(message: types.Message):
    user_id = message.from_user.id
    user_url = message.from_user.url
    add_game(user_id, "cup")
    await message.answer(f"<b>[Игры - Стаканчик 🥛]</b> {link_user(user_id)}, для игры в «Стаканчик» напишите 1 10к(Ставка 10к на 1 стаканчик) или 1 10000\n"
    f"{choice(info)} Цель игры - угадать стаканчик и получить приумноженную ставку",
    reply_markup=ikb_сup)


@dp.message_handler(lambda message: fuzz.ratio(f"{message.text.lower()}", "кубик") >= 75)
async def cube(message: types.Message):
    user_id = message.from_user.id
    user_url = message.from_user.url
    await message.answer(
        f"<b>[Игры - Кубик 🎲]</b> {link_user(user_id)}, для игры в «Кубик» выберите число от 1 до 6\n"
        f"{choice(info)} Цель игры: Угадать сторну кубика и получить награду", reply_markup=ikb_cube)


@dp.message_handler(lambda message: fuzz.ratio(f"{message.text.lower()}", "акции") >= 75)
async def investments(message: types.Message):
    user_id = message.from_user.id
    user_url = message.from_user.url
    await message.answer(
        f"<b>[Игры - Акции 📈]</b> {link_user(user_id)}, выбери в какую акцию тебе вложиться:\n\n"
        "1⃣ Компания по производству игрушек конструкторов\n💰 Cтоимость - 10k$\n\n"
        "2⃣ Космическая компания по изучению космоса\n💰 Стоимость - 100k$\n\n"
        "3⃣ Компания по добыче газа\n💰 Стоимость - 1kk$\n\n"
        "4⃣ Нефтедобывающая компания\n💰 Cтоимость - 5kk$\n\n"
        f"{check_balance(user_id, True)}\n"
        "⬇ Выбери номер акции ниже что бы купить ее 💸",
        reply_markup=ikb_stock)
