from aiogram.dispatcher.filters.state import StatesGroup, State


class register(StatesGroup):
    name = State()
    phone = State()

class accept(StatesGroup):
    user_id = State()