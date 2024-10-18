from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from .. import buttons
from . import messages

router = Router()
#img_path = 'telegram/img/'

@router.callback_query(F.data.in_('route_schedule'))
async def start_schedule_routes(call: CallbackQuery, state: FSMContext):
	mess = messages.start_message
	await state.clear()
	
	await call.message.answer(mess, reply_markup=buttons.get_schedule_date_keyboard())
	await call.answer()
	

