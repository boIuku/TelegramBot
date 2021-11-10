from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Peperoni")
        ],
[
            KeyboardButton(text="Capricosa")
        ],
[
            KeyboardButton(text="Margherita")
        ],
    ],
    resize_keyboard=True
)

taknie = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Tak")
        ],
[
            KeyboardButton(text="Nie")
        ],
    ],
    resize_keyboard=True
)