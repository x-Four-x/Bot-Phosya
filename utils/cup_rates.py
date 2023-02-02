import sql_func 
from aiogram import types 
from loader import dp
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .ranks import *
from math import floor

def cup_rates_inl(id, num, text=None):
    balance = int(sql_func.check_balance(id, False))
    st_rate, nd_rate = floor(balance/4), floor(balance/2)
    if text is None:
        ikb_rates = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='1-й🥛', callback_data='Стак 1'),
                                        InlineKeyboardButton(text='2-й🥛', callback_data='Стак 2'),
                                        InlineKeyboardButton(text='3-й🥛', callback_data='Стак 3')
                                    ],
                                    [
                                        InlineKeyboardButton(text="💰1/4$",
                                        callback_data=f'Ста{" "}{str(st_rate)}{" "}{num}'),
                                        InlineKeyboardButton(text="💰1/2$",
                                        callback_data=f'Ста{" "}{str(nd_rate)}{" "}{num}'),
                                        InlineKeyboardButton(text="💰 Ва-банк",
                                        callback_data=f'Ста{" "}{str(sql_func.check_balance(id, False))}{" "}{num}')
                                    ]
                                ])
        return ikb_rates
    else:
        sp_val = text.split()
        print(sp_val)
        ikb_rates2 = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='1-й🥛', callback_data='Стак 1'),
                                        InlineKeyboardButton(text='2-й🥛', callback_data='Стак 2'),
                                        InlineKeyboardButton(text='3-й🥛', callback_data='Стак 3')
                                    ],
                                    [
                                        InlineKeyboardButton(text="💰1/4$",
                                        callback_data=f'Ста{" "}{str(st_rate)}{" "}{num}'),
                                        InlineKeyboardButton(text="💰1/2$",
                                        callback_data=f'Ста{" "}{str(nd_rate)}{" "}{num}'),
                                        InlineKeyboardButton(text="💰 Ва-банк",
                                        callback_data=f'Ста{" "}{str(sql_func.check_balance(id, False))}{" "}{num}'),
                                    ]
                                ])
        return ikb_rates2

