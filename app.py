import logging
import filters

from aiogram import executor
from handlers import dp 
from termcolor import cprint
from time import sleep
from sql_func import *


async def on_startup(dp):
    filters.setup(dp)
    logging.basicConfig(level=logging.INFO)
    cprint(f'{"="*80}\n'
           f'{"="*33} Бот запущен! {"="*33}\n'
           f'{"="*80}\n'
           "Список задач:\n\t"
           "По фиксить ошибку при работе с числом Эйлера - Сделанно\n\t"
           "Сделать новую игру\n\t"
           "Сделать стартовую выдачу денег 5к - Сделанно", color='green', attrs=['bold'])

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, on_startup=on_startup)




