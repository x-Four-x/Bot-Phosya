from aiogram.dispatcher.filters.state import StatesGroup, State

class mail_list(StatesGroup):
    link = State()
    preview = State()
    descript = State()
    finish_ads = State()