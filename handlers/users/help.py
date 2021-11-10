from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from utils.misc import rate_limit


@rate_limit(5, 'help')
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = [
        'Lista poleceń : ',
        '/start - Rozpocznij dialog ',
        '/help - Uzyskać pomoc ',
        '/menu'
    ]
    await message.answer('\n'.join(text))
