from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_play_list = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='Акции 📈'),
            KeyboardButton(text='Казино 🎰'),
            KeyboardButton(text='Кубик 🎲')
        ],
        [
            KeyboardButton(text='Стаканчик 🥛'),
            KeyboardButton(text='Футбол ⚽')
            KeyboardButton(text='Дартс 🎯')
        ],
        [
            KeyboardButton("⏪ Главное меню")
        ]
    ],
    resize_keyboard=True
)
