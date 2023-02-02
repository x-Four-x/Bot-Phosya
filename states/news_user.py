from aiogram.dispatcher.filters.state import StatesGroup, State


class news_bot(StatesGroup):
    text = State()
    preview = State()