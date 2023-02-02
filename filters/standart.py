from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from sql_func import *
from aiogram.types import CallbackQuery

class IsStandart(BoundFilter):
    async def check(self, call: CallbackQuery):
        user_id = call.from_user.id
        balance = check_balance(id, False)
        bid = int(call.data.split()[1])
        return True if balance >= bid else False