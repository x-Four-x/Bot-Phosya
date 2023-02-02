from aiogram import Dispatcher

from .admin_group import IsAdmin
from .private_chat import IsPrivate


# Функция которая выполняет установку кастомных фильтров
def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsPrivate) # Устанавливаем кастомный фильтр на приватный чат с ботом
    dp.filters_factory.bind(IsAdmin)
