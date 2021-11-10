from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Uruchomić bota"),
        types.BotCommand("menu", "menu"),
        types.BotCommand("help", "Pomoc"),
    ])
