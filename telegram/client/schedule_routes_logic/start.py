from aiogram import Router, F
from aiogram.types import Message

from .. import buttons
from . import messages

section_name = '🚌 Показать расписание маршрута'

router = Router()
#img_path = 'telegram/img/'

@router.message(F.text.in_(section_name))
async def start_schedule_routes(message: Message):
	mess = messages.start_message
	await message.answer(mess, reply_markup=buttons.get_schedule_date_keyboard())
	

