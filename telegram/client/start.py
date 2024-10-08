from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from . import buttons, messages
from control_db.models import Client

router = Router()


@router.message(Command('start'))
async def start_command_handler(message: Message, state: FSMContext, error=False):
	client, new = await Client.objects.aget_or_create(tg_id=message.chat.id)
	if new:
		if message.chat.username:
			username = message.chat.username
		else:
			username = message.chat.first_name

		if username:
			client.username = username
			await client.asave()

	await state.clear()
	await state.set_data({})

	if error:
		await message.answer(messages.error_message, reply_markup=buttons.get_main_keyboard())
	else:
		await message.answer(messages.start_message, reply_markup=buttons.get_main_keyboard())


@router.message(Command('help'))
async def help_command_handler(message: Message, state: FSMContext, error=False):
	if error:
		await message.answer(messages.error_message, reply_markup=buttons.get_main_keyboard())
	else:
		await message.answer(messages.help_message, reply_markup=buttons.get_main_keyboard())


@router.message(Command('contacts'))
async def contacts_command_handler(message: Message, state: FSMContext, error=False):
	if error:
		await message.answer(messages.error_message, reply_markup=buttons.get_main_keyboard())
	else:
		await message.answer(messages.contacts_message, reply_markup=buttons.get_main_keyboard())
