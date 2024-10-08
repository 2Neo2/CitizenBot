from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup

from aiogram.fsm.context import FSMContext

from .. import buttons
from . import messages

#cancel_menu = ReplyKeyboardMarkup(keyboard=[[buttons.cancel_button]], resize_keyboard=True)

strelka_section_name = 'Справочное инфо'

router = Router()
#img_path = 'telegram/img/'

@router.message(F.text.in_(strelka_section_name))
async def start_reference_info(message: Message, state: FSMContext):
	mess = messages.start_message
	await message.answer(mess, reply_markup=buttons.get_sections_info_keyboard())
