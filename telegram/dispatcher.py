from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
from aiogram_dialog import setup_dialogs
from aiogram.types import BotCommand

import os
from dotenv import load_dotenv
load_dotenv()

from . import client
from .storage import SQLStorage
from .middlewares import LoggerMiddleware

import logging


bot = Bot(
	token=os.environ['BOT_TOKEN'],
	default=DefaultBotProperties(parse_mode='HTML', link_preview_is_disabled=True)
)
dp = Dispatcher(storage=SQLStorage())


async def set_bot_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Запуск"),
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

dp.include_routers(*routers)
setup_dialogs(dp)
dp.update.outer_middleware(LoggerMiddleware())
