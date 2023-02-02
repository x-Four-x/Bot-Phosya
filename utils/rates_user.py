import sql_func 
from aiogram import types 
from loader import dp
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .ranks import *
from math import floor


def rates_inl(sign, id, call_start):
    balance = int(sql_func.check_balance(id, False))
    st_rate, nd_rate, rd_rate = floor(balance/4), floor(balance/3), floor(balance/2)
    ikb_rates = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text=f'{sign} {str(ranks_int(st_rate)).partition(".")[0] + "." + ranks_int(st_rate)[ranks_int(st_rate).find(".")+1] + "k"*ranks_int(st_rate).count(".")}$',
                                        callback_data=f'{call_start}{" "}{st_rate}'),
                                        InlineKeyboardButton(text=f'{sign} {str(ranks_int(nd_rate)).partition(".")[0] + "." + ranks_int(nd_rate)[ranks_int(nd_rate).find(".")+1] + "k"*ranks_int(nd_rate).count(".")}$',
                                        callback_data=f'{call_start}{" "}{nd_rate}'),
                                        InlineKeyboardButton(text=f'{sign} {str(ranks_int(rd_rate)).partition(".")[0] + "." + ranks_int(rd_rate)[ranks_int(rd_rate).find(".")+1] + "k"*ranks_int(rd_rate).count(".")}$',
                                        callback_data=f'{call_start}{" "}{rd_rate}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{sign} Ва-банк',
                                        callback_data=f'{call_start}{" "}{balance}')
                                    ]
                                ])
    return ikb_rates

