from aiogram import BaseMiddleware

import asyncio, logging
from asgiref.sync import sync_to_async

from .client import start as client_start
from .permissions import is_admin


logger = logging.getLogger('BOT')


class ClientMiddleware(BaseMiddleware):
	async def __call__(self, handler, message, data):
		permissions = await sync_to_async(is_admin)(message.chat.id)
		if not permissions:
			return await handler(message, data)


class LoggerMiddleware(BaseMiddleware):
	async def __call__(self, handler, update, data):
		loop = asyncio.get_running_loop()
		start_time = loop.time()
		state = await data['state'].get_state()
		error = None

		match update.event_type:
			case 'message':
				message = update.message
			case 'callback_query':
				message = update.callback_query.message
			case _:
				return

		try:
			return await handler(update, data)
		except Exception as exp:
			error = exp
			permissions = await sync_to_async(is_admin)(message.chat.id)
			if not permissions:
				return await client_start.start(message, data['state'], error=True)
			# else:
			# 	return await admin_start.start(message, data['state'], error=True)
		finally:
			duration = round((loop.time() - start_time) * 1000)

			match update.event_type:
				case 'message':
					tg_id = update.message.chat.id
					content = update.message.text
				case 'callback_query':
					tg_id = update.callback_query.message.chat.id
					content = update.callback_query.data
				case _:
					return

			if error:
				logger.error({
					'tg_id': tg_id,
					'state': state,
					'content': content,
					'duration': f'{duration} ms',
					'error': error
				})
			else:
				logger.info({
					'tg_id': tg_id,
					'state': state,
					'content': content,
					'duration': f'{duration} ms'
				})
