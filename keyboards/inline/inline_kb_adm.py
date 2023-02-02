from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_adm = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Новости 💭', callback_data='Адм нов'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='Реклама 📢', callback_data='Адм рек')
                                    ],
                                    [
                                        InlineKeyboardButton(text='Просмотреть репорты ⚠️', callback_data='Адм реп'),
                                    ]
                                ])