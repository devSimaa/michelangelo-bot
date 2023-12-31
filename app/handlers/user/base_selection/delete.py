from aiogram import types, Dispatcher
from loader import dp, bot,_
from database.users import delete_profile
from app.keyboards import delete_profile_yes_or_not

# from app.handlers.user.start import lang_command


@dp.message_handler(text="❌")
async def delete_comm(message: types.Message):
    await message.answer(text=_("Вы точно хотите удалить анкету?"),
                          reply_markup=delete_profile_yes_or_not()
    )


@dp.callback_query_handler(text=["delete_yes", "delete_no"])
async def delete_yes_or_no(callback: types.CallbackQuery):
    if callback.data == "delete_yes":
        await delete_profile(callback.from_user.id)
        await callback.answer(text=_("Ваша анкета успешно удалена."))
    elif callback.data == "delete_no":
        pass
