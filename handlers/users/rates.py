import asyncio

from aiogram import types 
from loader import dp
from sql_func import *
from data.config import *
from random import choice
from utils.rates_user import *
from utils.link_user import *
from utils.cup_rates import *
from random import randint
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


@dp.message_handler(lambda message: message.text.replace(" ", "").replace('k', '000').replace('к', '000').isdigit() and check_game(message.from_user.id)=='football')
async def trigers_foot(message: types.Message):
    user_id = message.from_user.id
    sum_bid = int(message.text.replace('k', '000').replace('к', '000'))
    if sum_bid >= 100:
        if check_money(sum_bid, user_id):
            dice_msg = await bot.send_dice(message.chat.id, emoji='⚽')
            football_num = dice_msg.dice.value
            profit = football_profit.get(football_num)
            profit_sum = round(sum_bid * profit - sum_bid, 0)
            print(profit_sum)
            add_money(profit_sum, user_id)
            await asyncio.sleep(4.9)
            if profit_sum > 0:
                await message.answer(f"<b>[Игры - Футбол ⚽]</b> {link_user(user_id)}, вы выиграли {ranks_int(profit_sum)}$ ({profit}x) {choice(joi)}\n"
                f"{check_balance(user_id, True)}", reply_markup=rates_inl('⚽', user_id, "Фут"))
            elif profit_sum == 0:
                await message.answer(f"<b>[Игры -  Футбол ⚽]</b> {link_user(user_id)}, деньги остаются у вас ({profit}x) {choice(joi)}\n"
                f"{check_balance(user_id, True)}", reply_markup=rates_inl('⚽', user_id, "Фут"))
            else:
                await message.answer(f"<b>[Игры -  Футбол ⚽]</b> {link_user(user_id)}, вы проиграли {ranks_int(profit_sum*-1)}$ ({profit}x) {choice(sad)}\n"
                f"{check_balance(user_id, True)}", reply_markup=rates_inl('⚽', user_id, "Фут"))
        else:
            await message.answer(f"<b>[Игры - Футбол ⚽]</b> {link_user(user_id)}, у вас не достаточно средств {choice(sad)}")
    else:
        await message.answer(f"<b>[Игры - Футбол ⚽]</b> {link_user(user_id)}, минимальная ставка 100$ {choice(info)}")


@dp.message_handler(lambda message: message.text.replace(" ", "").replace('k', '000').replace('к', '000').isdigit() and check_game(message.from_user.id)=='casino')
async def trigers_cas(message: types.Message):
    user_id = message.from_user.id
    user_url = message.from_user.url
    sums = message.text.replace(" ", "")
    if int(sums) >= 100:
        if check_money(int(sums), user_id):
            st_slot, nd_slot, rd_slot = choice(item_list), choice(item_list), choice(item_list)
            profit = round(item_profit.get(st_slot) + item_profit.get(nd_slot) + item_profit.get(rd_slot), 1)
            profit_sum = int(int(sums) * profit - int(sums))
            add_money(profit_sum, user_id)
            if profit_sum > 0:
                await message.answer(f"<b>[Игры - Казино 🎰]</b> <a href='{user_url}'>{check_name(user_id)}</a>, вы выиграли {ranks_int(profit_sum)}$ {choice(joi)}\n"
                f"🎰 Выпали слоты: [{st_slot}|{nd_slot}|{rd_slot}] (x{profit})\n"
                f"{check_balance(user_id, True)}", reply_markup=rates_inl('🎰', user_id, "Каз"))
            elif profit_sum == 0:
                await message.answer(f"<b>[Игры - Казино 🎰]</b> <a href='{user_url}'>{check_name(user_id)}</a>, деньги остаются у вас {choice(joi)}\n"
                f"🎰 Выпали слоты: [{st_slot}|{nd_slot}|{rd_slot}] (x{profit})\n"
                f"{check_balance(user_id, True)}", reply_markup=rates_inl('🎰', user_id, "Каз"))
            else:
                await message.answer(f"<b>[Игры - Казино 🎰]</b> <a href='{user_url}'>{check_name(user_id)}</a>, вы проиграли {ranks_int(profit_sum*-1)}$ {choice(sad)}\n"
                f"🎰 Выпали слоты: [{st_slot}|{nd_slot}|{rd_slot}] (x{profit})\n"
                f"{check_balance(user_id, True)}", reply_markup=rates_inl('🎰', user_id, "Каз"))
        else:
            await message.answer(f"<b>[Игры - Казино 🎰]</b> <a href='{user_url}'>{check_name(user_id)}</a>, у вас не достаточно средств {choice(sad)}")
    else:
        await message.answer(f"<b>[Игры - Казино 🎰]</b> <a href='{user_url}'>{check_name(user_id)}</a>, минимальная ставка 100$ {choice(info)}")


@dp.message_handler(lambda message: message.text.replace(" ", "").replace('k', '000').replace('к', '000').isdigit() and check_game(message.from_user.id)=='darts')
async def trigers_bowl(message: types.Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    sum_bid = int(message.text.replace('k', '000').replace('к', '000'))
    if sum_bid >= 100:
        if check_money(sum_bid, user_id):
            dice_msg = await bot.send_dice(chat_id, emoji='🎯')
            darts_num = dice_msg.dice.value
            profit = darts_profit.get(darts_num)
            profit_sum = int(sum_bid * profit - sum_bid)
            add_money(profit_sum, user_id)
            await asyncio.sleep(4.9)
            if profit_sum > 0:
                await message.answer(f"<b>[Игры - Дартс 🎯]</b> {link_user(user_id)}, вы выиграли {ranks_int(profit_sum)}$ ({profit}x) {choice(joi)}\n"
                f"{check_balance(user_id, True)}", reply_markup=rates_inl('🎯', user_id, "Дар"))
            elif profit_sum == 0:
                await message.answer(f"<b>[Игры - Дартс 🎯]</b> {link_user(user_id)}, деньги остаются у вас ({profit}x) {choice(joi)}\n"
                f"{check_balance(user_id, True)}", reply_markup=rates_inl('🎯', user_id, "Дар"))
            else:
                await message.answer(f"<b>[Игры - Дартс 🎯]</b> {link_user(user_id)}, вы проиграли {ranks_int(profit_sum*-1)}$ ({profit}x) {choice(sad)}\n"
                f"{check_balance(user_id, True)}", reply_markup=rates_inl('🎯', user_id, "Дар"))
        else:
            await message.answer(f"<b>[Игры - Дартс 🎯]</b> {link_user(user_id)}, у вас не достаточно средств {choice(sad)}")
    else:
        await message.answer(f"<b>[Игры - Дартс 🎯]</b> {link_user(user_id)}, минимальная ставка 100$ {choice(info)}")

@dp.message_handler(lambda message: message.text.replace(" ", "").replace('k', '000').replace('к', '000').isdigit() and check_game(message.from_user.id)=='bowl')
async def trigers_darts(message: types.Message):
    user_id = call.from_user.id
    chat_id = call.message.chat.id
    sum_bid = int(call.data.split()[1])
    if sum_bid >= 100:
        if check_money(sum_bid, user_id):
            dice_msg = await bot.send_dice(chat_id, emoji='🎳')
            bowl_num = dice_msg.dice.value
            profit = football_profit.get(bowl_num)
            profit_sum = int(sum_bid * profit - sum_bid)
            add_money(profit_sum, user_id)
            print(bowl_num)
            await asyncio.sleep(4.9)
            if profit_sum > 0:
                await message.answer(f"<b>[Игры - Боулинг 🎳]</b> {link_user(user_id)}, страйк! {ranks_int(profit_sum)}$ ({profit}x) {choice(joi)}\n"
                f"{check_balance(user_id, True)}", reply_markup=rates_inl('🎳', user_id, "Боу"))
            elif profit_sum == 0:
                await message.answer(f"<b>[Игры - Боулинг 🎳]</b> {link_user(user_id)}, деньги остаются у вас ({profit}x) {choice(joi)}\n"
                f"{check_balance(user_id, True)}", reply_markup=rates_inl('🎳', user_id, "Боу"))
            else:
                await message.answer(f"<b>[Игры - Боулинг 🎳]</b> {link_user(user_id)}, вы проиграли {ranks_int(profit_sum*-1)}$ ({profit}x) {choice(sad)}\n"
                f"{check_balance(user_id, True)}", reply_markup=rates_inl('🎳', user_id, "Боу"))
        else:
            await message.answer(f"<b>[Игры - Боулинг 🎳]</b> {link_user(user_id)}, у вас не достаточно средств {choice(sad)}")
    else:
        await message.answer(f"<b>[Игры - Боулинг 🎳]</b> {link_user(user_id)}, минимальная ставка 100$ {choice(info)}")

@dp.message_handler(lambda message: message.text.replace(" ", "").replace('k', '000').replace('к', '000').isdigit() and check_game(message.from_user.id)=='cup')
async def trigers_cup(message: types.Message):
    user_id = message.from_user.id
    user_url = message.from_user.url
    number = message.text.partition(' ')[0]
    sum_bid = message.text.partition(' ')[2]
    if sum_bid == '':
        await message.answer(f"👻 Стаканчик ➜ {link_user(user_id)}, для игры в стаканчик введите сумму ставки\n"
        f"{choice(info)} Сумму ставки можно указывать так - 1 1000(ставка 10к на 1 стакан) или словами 1 все, 1 весь(ставка всего баланса на 1 стакан)")
    else:
        if int(sum_bid) >= 100:
            if check_money(int(sum_bid), user_id):
                sum_bid = int(sum_bid)
                right_number = randint(1, 3)
                if int(number) == int(right_number):
                    profit = choice(profit_cup)
                    add_money(int(sum_bid*profit), user_id)
                    await message.answer(f"<b>[Игры - Стаканчик 🥛]</b> {link_user(user_id)}, {choice(right)},\n"
                    f"💸 Приз: +{ranks_int(int(sum_bid*choice(profit_cup)))}$ (x{profit}) {choice(joi)}\n"
                    f"{check_balance(user_id, True)}", reply_markup=cup_rates_inl(user_id, number, f'{sum_bid} {number}'))
                else:
                    withdraw_money(int(sum_bid), user_id)
                    await message.answer(f"<b>[Игры - Стаканчик 🥛]</b> {link_user(user_id)}, {choice(wrong)}, это был стаканчик под номером «{right_number}» {choice(sad)}\n"
                    f"{choice(info)} Ваша ставка обнулилась -{ranks_int(sum_bid)}$ {choice(sad)}\n"
                    f"{check_balance(user_id, True)}", reply_markup=cup_rates_inl(user_id, number, f'{sum_bid} {number}'))
            else:
                await message.answer(f"<b>[Игры - Стаканчик 🥛]</b> {link_user(user_id)}, у вас не достаточно средств {choice(sad)}\n"
                f"{check_balance(user_id, True)}")
        else:
            await message.answer(f"<b>[Игры - Стаканчик 🥛]</b> {link_user(user_id)}, минимальная ставка 100$ {choice(info)}\n"
            f"{check_balance(user_id, True)}")