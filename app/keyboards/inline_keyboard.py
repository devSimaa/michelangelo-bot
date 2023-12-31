from aiogram.types import (
    ReplyKeyboardRemove,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from loader import _

def base_ikb():
    ikb = InlineKeyboardMarkup(
        resize_keyboard=True,
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Название", callback_data="Калбек"),
            ],
        ],
    )
    return ikb


def delete_profile_yes_or_not():
    ikb = InlineKeyboardMarkup(
        resize_keyboard=True,
        inline_keyboard=[
            [
                InlineKeyboardButton(text=_("Да"), callback_data="delete_yes"),
                InlineKeyboardButton(text=_("Нет"), callback_data="delete_no"),
            ],
        ],
    )
    return ikb
