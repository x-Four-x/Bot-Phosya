import logging

from aiogram.utils.exceptions import (BotBlocked, RetryAfter, TelegramAPIError)

from datetime import datetime
from loader import dp

@dp.errors_handler()
async def errors_handler(update, exception):
    now = datetime.now()
    if isinstance(exception, BotBlocked):
        logging.info(f"[{now.strftime('%H-%M')}] Bot blocked by user ...")
        return True
    elif isinstance(exception, RetryAfter):
        logging.info(f"[{now.strftime('%H-%M')}] Spam warning!!!")
        return True