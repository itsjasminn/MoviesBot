from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def on_startup(bot: Bot):
    commands = [BotCommand(command="start", description="boshlash"),
                BotCommand(command="help", description="yordam"),
                BotCommand(command="admin", description="admin")]
    await bot.set_my_commands(commands, BotCommandScopeDefault())


async def on_shutdown():
    pass
