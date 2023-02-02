from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("Основное 🚀"),
            KeyboardButton("Реферальная система ✉️"),
        ],
        [
            KeyboardButton("Игры 🎮"),
            KeyboardButton("Задания 🧩")
        ],
        [
            KeyboardButton("Настройки ⚙️"),
            KeyboardButton("Профиль 📋"),
        ],
        [
            KeyboardButton("Наш канал 📢"),
            KeyboardButton("Контакты 👤")
        ]
    ],
    resize_keyboard=True
)