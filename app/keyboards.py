from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Фото')],
    [KeyboardButton(text='Видео YouTube'),
     # KeyboardButton(text='Аудио')
     ]
], resize_keyboard=True)
