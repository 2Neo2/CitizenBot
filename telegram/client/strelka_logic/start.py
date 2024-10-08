from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup

from aiogram.fsm.context import FSMContext

from .. import buttons
from . import messages

section_name = 'Частые вопросы о Стрелке'

router = Router()
#img_path = 'telegram/img/'

@router.message(F.text.in_(section_name))
async def start_strelka_questions(message: Message, state: FSMContext):
	mess = messages.start_message
	await message.answer(mess, reply_markup=buttons.get_sections_strelka_keyboard())
