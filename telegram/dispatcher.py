from aiogram import Bot, Dispatcher, Router
from aiogram.client.bot import DefaultBotProperties
from aiogram.types import BotCommand
from aiogram_dialog import setup_dialogs

import os
from dotenv import load_dotenv
load_dotenv()

from . import client, admin
from .storage import SQLStorage
from .middlewares import LoggerMiddleware
from aiogram.fsm.storage.memory import MemoryStorage

import logging


bot = Bot(
    token=os.environ['BOT_TOKEN'],
    default=DefaultBotProperties(parse_mode='HTML', link_preview_is_disabled=True)
)

dp = Dispatcher(storage=MemoryStorage())

async def set_bot_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Главное меню"),
        BotCommand(command="/contacts", description="Контакты"),
        BotCommand(command="/help", description="Помощь")
    ]
    await bot.set_my_commands(commands)


async def polling():
    logger = logging.getLogger('BOT')
    logger.debug('RUN POLLING')
      
    await set_bot_commands(bot)

    await dp.start_polling(bot)


routers = []
routers += client.routers
routers += admin.routers

setup_dialogs(dp)

dp.include_routers(*routers)
dp.update.outer_middleware(LoggerMiddleware())
