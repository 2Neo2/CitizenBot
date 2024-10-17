from aiogram import Router, F
from aiogram.types import CallbackQuery, ReplyKeyboardMarkup

from aiogram.fsm.context import FSMContext

from .. import buttons
from . import messages


router = Router()


@router.callback_query(F.data.in_('ref_info'))
async def start_reference_info(call: CallbackQuery, state: FSMContext):
	mess = messages.start_message
	await state.clear()
	await state.set_data({})
	await call.message.answer(mess, reply_markup=buttons.get_sections_info_keyboard())
