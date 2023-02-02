from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_stock = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='1⃣', callback_data='Акц 1'),
                                        InlineKeyboardButton(text='2⃣', callback_data='Акц 2'),
                                        InlineKeyboardButton(text='3⃣', callback_data='Акц 3'),
                                        InlineKeyboardButton(text='4⃣', callback_data='Акц 4'),
                                    ]
                                ])
ikb_cube = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='🎲 1', callback_data='Куб 1'),
                                        InlineKeyboardButton(text='🎲 2', callback_data='Куб 2'),
                                        InlineKeyboardButton(text='🎲 3', callback_data='Куб 3')
                                    ],
                                    [
                                        InlineKeyboardButton(text='🎲 4', callback_data='Куб 4'),
                                        InlineKeyboardButton(text='🎲 5', callback_data='Куб 5'),
                                        InlineKeyboardButton(text='🎲 6', callback_data='Куб 6')
                                    ]
                                ])


ikb_сup = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='1-й🥛', callback_data='Стак 1'),
                                        InlineKeyboardButton(text='2-й🥛', callback_data='Стак 2'),
                                        InlineKeyboardButton(text='3-й🥛', callback_data='Стак 3')
                                    ]
                                ])
