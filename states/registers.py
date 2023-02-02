from aiogram.dispatcher.filters.state import StatesGroup, State


class register(StatesGroup):
    nickname = State()

