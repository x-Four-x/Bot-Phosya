import asyncio

from random import choice, randint

from aiogram import types
from aiogram.types import CallbackQuery

from time import sleep
from data.config import *
from keyboards.inline import ikb_cube, ikb_stock
from loader import bot, dp
from sql_func import *
from utils.link_user import *
from utils.rates_user import *
from utils.cup_rates import *



@dp.callback_query_handler(lambda call: call.data.startswith("Стак"))
async def cup_play(call: CallbackQuery):
    user_id = call.from_user.id
    add_game(user_id, 'cup')
    number = int(call.data.replace("Стак ", ""))
    await call.message.edit_text(f"<b>[Игры - 🥛 Стаканчик]</b> {link_user(user_id)},\nВыбран стаканчик под номером «{number}» {choice(info)}\n"
    "🥛 Напиши сумму ставки 1 10к(Ставка 10к на 1 стаканчик)\n"
    f"{choice(info)} Минимальная ставка 100$\n"
    f"{check_balance(user_id, True)}", reply_markup=cup_rates_inl(user_id, number))
    await bot.answer_callback_query(call.id, cache_time=5)

@dp.callback_query_handler(lambda call: call.data.startswith("Ста"))
async def cup_bid(call: CallbackQuery):
    print(122)
    user_url = call.from_user.url
    user_id = call.from_user.id
    sum_bid = int(call.data.split()[1])
    number = int(call.data.split()[2])
    right_number = randint(1, 3)
    if sum_bid >= 100:
        if check_money(int(sum_bid), user_id):
            if int(number) == int(right_number):
                profit = choice(profit_cup)
                add_money(int(sum_bid*profit), user_id)
                await call.message.edit_text(f"<b>[Игры - Стаканчик 🥛]</b> {link_user(user_id)}, {choice(right)},\n"
                f"💸 Приз: +{ranks_int(int(sum_bid*choice(profit_cup)))}$ (x{profit}) {choice(joi)}\n"
                f"{check_balance(user_id, True)}", reply_markup=cup_rates_inl(user_id, number, f'{sum_bid} {number}'))
            else:
                withdraw_money(int(sum_bid), user_id)
                await call.message.edit_text(f"<b>[Игры - Стаканчик 🥛]</b> {link_user(user_id)}, {choice(wrong)}, это был стаканчик под номером «{right_number}» {choice(sad)}\n"
                f"{choice(info)} Ваша ставка обнулилась -{ranks_int(sum_bid)}$ {choice(sad)}\n"
                f"{check_balance(user_id, True)}", reply_markup=cup_rates_inl(user_id, number, f'{sum_bid} {number}'))
        else:
            await call.message.answer(f"<b>[Игры - Стаканчик 🥛]</b> {link_user(user_id)}, у вас не достаточно средств {choice(sad)}\n"
            f"{check_balance(user_id, True)}")
    else:
        await call.message.answer(f"<b>[Игры - Стаканчик 🥛]</b> {link_user(user_id)}, минимальная ставка 100$ {choice(info)}\n"
        f"{check_balance(user_id, True)}")
    await bot.answer_callback_query(call.id, cache_time=50)

@dp.callback_query_handler(lambda call: call.data.startswith('Каз'))
async def casino_play(call: CallbackQuery):
    user_id = call.from_user.id
    sum_bid = int(call.data.split()[1])
    if sum_bid >= 100:
        if check_money(int(sum_bid), user_id):
            st_slot, nd_slot, rd_slot = choice(item_list), choice(item_list), choice(item_list)
            profit = round(item_profit.get(st_slot) + item_profit.get(nd_slot) + item_profit.get(rd_slot), 1)
            profit_sum = int(sum_bid * profit - sum_bid)
            add_money(profit_sum, user_id)
            if profit_sum > 0:
                await call.message.edit_text(f"<b>[Игры - Казино 🎰]</b> {link_user(user_id)}, вы выиграли {ranks_int(profit_sum)}$ {choice(joi)}\n"
                f"🎰 Выпали слоты: [{st_slot}|{nd_slot}|{rd_slot}] (x{profit})\n"
                f"{check_balance(user_id, True)}", reply_markup=rates_inl('🎰', user_id, "Каз"))
            elif profit_sum == 0:
                await call.message.edit_text(f"<b>[Игры - Казино 🎰]</b> {link_user(user_id)}, деньги остаются у вас {choice(joi)}\n"
                f"🎰 Выпали слоты: [{st_slot}|{nd_slot}|{rd_slot}] (x{profit})\n"
                f"{check_balance(user_id, True)}", reply_markup=rates_inl('🎰', user_id, "Каз"))
            else:
                await call.message.edit_text(f"<b>[Игры - Казино 🎰]</b> {link_user(user_id)}, вы проиграли {ranks_int(profit_sum*-1)}$ {choice(sad)}\n"
                f"🎰 Выпали слоты: [{st_slot}|{nd_slot}|{rd_slot}] (x{profit})\n"
                f"{check_balance(user_id, True)}", reply_markup=rates_inl('🎰', user_id, "Каз"))
        else:
            await call.message.edit_text(f"<b>[Игры - Казино 🎰]</b> {link_user(user_id)}, у вас не достаточно средств {choice(sad)}")
    else:
        await call.message.edit_text(f"<b>[Игры - Казино 🎰]</b> {link_user(user_id)}, минимальная ставка 100$ {choice(info)}")
    await bot.answer_callback_query(call.id, cache_time=5)

@dp.callback_query_handler(lambda call: call.data.startswith("Фут"))
async def football(call: CallbackQuery):
    user_id = call.from_user.id
    chat_id = call.message.chat.id
    sum_bid = int(call.data.split()[1])
    if sum_bid >= 100:
        if check_money(sum_bid, user_id):
            dice_msg = await bot.send_dice(chat_id, emoji='⚽')
            football_num = dice_msg.dice.value
            profit = football_profit.get(football_num)
            profit_sum = int(sum_bid * profit - sum_bid)
            add_money(profit_sum, user_id)
            await asyncio.sleep(4.9)
            if profit_sum > 0:
                await call.message.answer(f"<b>[Игры - Футбол ⚽]</b> {link_user(user_id)}, вы выиграли {ranks_int(profit_sum)}$ ({profit}x) {choice(joi)}\n"
                f"{check_balance(user_id, True)}", reply_markup=rates_inl('⚽', user_id, "Фут"))
            elif profit_sum == 0:
                await call.message.answer(f"<b>[Игры -  Футбол ⚽]</b> {link_user(user_id)}, деньги остаются у вас ({profit}x) {choice(joi)}\n"
                f"{check_balance(user_id, True)}", reply_markup=rates_inl('⚽', user_id, "Фут"))
            else:
                await call.message.answer(f"<b>[Игры -  Футбол ⚽]</b> {link_user(user_id)}, вы проиграли {ranks_int(profit_sum*-1)}$ ({profit}x) {choice(sad)}\n"
                f"{check_balance(user_id, True)}", reply_markup=rates_inl('⚽', user_id, "Фут"))
        else:
            await call.message.answer(f"<b>[Игры - Футбол ⚽]</b> {link_user(user_id)}, у вас не достаточно средств {choice(sad)}")
    else:
        await call.message.answer(f"<b>[Игры - Футбол ⚽]</b> {link_user(user_id)}, минимальная ставка 100$ {choice(info)}")

    await bot.answer_callback_query(call.id, cache_time=5)


@dp.callback_query_handler(lambda call: call.data.startswith("Куб"))
async def cube_play(call: CallbackQuery):
    user_id = call.from_user.id
    number = int(call.data.replace("Куб ", ""))
    right_number = randint(1,6)
    if right_number == number:
        add_money(1000000, user_id)
        await call.message.edit_text(f"<b>[Игры - Кубик 🎲]</b> {link_user(user_id)}, {choice(right)} {choice(joi)}\n"
        "💸 Приз: 1kk$\n"
        f"{check_balance(user_id, True)}", reply_markup=ikb_cube)
    else:
        add_money(10000, user_id)
        await call.message.edit_text(f"<b>[Игры - Кубик 🎲]</b> {link_user(user_id)}, {choice(wrong)}, это было число «{right_number}» {choice(sad)}\n"
        f"💸 Приз 10k$\n"
        f"{check_balance(user_id, True)}", reply_markup=ikb_cube)
    await bot.answer_callback_query(call.id, cache_time=5)


@dp.callback_query_handler(lambda call: call.data.startswith("Дар"))
async def darts(call: CallbackQuery):
    user_id = call.from_user.id
    chat_id = call.message.chat.id
    sum_bid = int(call.data.split()[1])
    if sum_bid >= 100:
        if check_money(sum_bid, user_id):
            dice_msg = await bot.send_dice(chat_id, emoji='🎯')
            darts_num = dice_msg.dice.value
            profit = darts_profit.get(darts_num)
            profit_sum = int(sum_bid * profit - sum_bid)
            print(profit_sum)
            print(sum_bid * profit - sum


@dp.callback_query_handler(lambda call: call.data.startswith("Акц"))
async def stock_play(call: CallbackQuery):
    user_id = call.from_user.id
    number = call.data.replace("Акц ", "")
    price = price_stock.get(int(number))
    if check_money(sum_money=price, id=user_id) is False:
        await call.message.answer(f"<b>[Игры - Акции 📈]</b> {link_user(user_id)}, у вас не достаточно средств {choice(sad)}\n"
        f"💸 Стоимость акции: {ranks_int(price)}$\n"
        f"{check_balance(user_id, True)}\n", reply_markup=ikb_stock)
    else:
        multiply = choice(profit)
        income = int(price * multiply - price)
        add_money(sum_money=income, id=user_id)
        if income>0:
            await call.message.edit_text(f"<b>[Игры - Акции 📈]</b> {link_user(user_id)}, вы выиграли {ranks_int(income)}$ (x{multiply}) {choice(joi)}\n"
            f"{check_balance(user_id, True)}\n"
            "⬇ Выбери номер акции ниже что бы купить ее 💸", reply_markup=ikb_stock)
        elif income == 0:
            await call.message.edit_text(f"<b>[Игры - Акции 📈]</b> {link_user(user_id)}, ваши деньги остаются у вас (x{multiply}) {choice(joi)}\n"
            f"{check_balance(user_id, True)}\n"
            "⬇ Выбери номер акции ниже что бы купить ее 💸", reply_markup=ikb_stock)
        else:
            await call.message.edit_text(f"<b>[Игры - Акции 📈]</b> {link_user(user_id)}, вы проиграли {ranks_int(income*-1)}$ (x{multiply}) {choice(sad)}\n"
            f"{check_balance(user_id, True)}\n"
            "⬇ Выбери номер акции ниже что бы купить ее 💸", reply_markup=ikb_stock)
    await bot.answer_callback_query(call.id, cache_time=5)
    
