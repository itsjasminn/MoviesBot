from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeChat
from db.base import db as database

ADMINS_IDS = 7556384250,


async def on_startup(bot: Bot):
    commands = [BotCommand(command="start", description="boshlash"),
                BotCommand(command="help", description="yordam")]
    await database.create_all()
    await bot.set_my_commands(commands)
    for admin in ADMINS_IDS:
        await bot.set_my_commands([BotCommand(command="admin", description="admin panel"),],
                                  BotCommandScopeChat(chat_id=admin))


async def on_shutdown():
    pass
