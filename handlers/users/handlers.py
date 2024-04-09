from aiogram.types import Message, CallbackQuery
from aiogram import F


from .router import router


@router.message(F.text.startswitch('/start'))
async def start_command(message: Message):
    await message.answer(
        text=f'Hello {message.from_user.first_name}'
    )
