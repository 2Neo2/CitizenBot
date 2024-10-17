from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
from aiogram.fsm.context import FSMContext

from . import buttons, messages
from control_db.models import Client
from telegram.permissions import is_admin
from telegram.admin import buttons as admin_buttons, messages as admin_messages


router = Router()
img_path = 'telegram/img/main_logo.png'

@router.message(Command('start'))
async def start_command_handler(message: Message, state: FSMContext, error=False):
    client, new = await Client.objects.aget_or_create(tg_id=message.chat.id)

    if is_admin(client.tg_id):
        if error:
            await message.answer(admin_messages.error_message, reply_markup=admin_buttons.start_menu)
        else:
            await message.answer(admin_messages.start_message, reply_markup=admin_buttons.start_menu)
    else:
        if new:
            if message.chat.username:
                username = message.chat.username
            else:
                username = message.chat.first_name

            if username:
                client.username = username
                await client.asave()

        if error:
            await message.answer(messages.error_message, reply_markup=buttons.get_main_keyboard())
        else:
            await message.answer_photo(FSInputFile(path=img_path), caption=messages.start_message, reply_markup=buttons.get_main_keyboard())


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
