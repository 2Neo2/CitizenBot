from aiogram import Router, F
from aiogram.types import ReplyKeyboardMarkup, CallbackQuery

from aiogram.fsm.context import FSMContext

from .. import buttons
from . import messages

router = Router()
#img_path = 'telegram/img/'

@router.callback_query(F.data.in_('strelka_questions'))
async def start_strelka_questions(call: CallbackQuery, state: FSMContext):
	mess = messages.start_message
	await state.clear()
	await state.set_data({})
	
	await call.message.answer(mess, reply_markup=buttons.get_sections_strelka_keyboard())
	

@router.callback_query(F.data.in_('exchange'))
async def start_strelka_questions(call: CallbackQuery):
	mess = messages.start_message
	await call.message.answer(mess, reply_markup=buttons.exchenge_section_keyboard())
	

@router.callback_query(F.data.in_('tariffs'))
async def start_strelka_questions(call: CallbackQuery):
	mess = messages.start_message
	await call.message.answer(mess, reply_markup=buttons.tariffs_section_keyboard())
	

@router.callback_query(F.data.in_('benefits'))
async def start_strelka_questions(call: CallbackQuery):
	mess = messages.start_message
	await call.message.answer(mess, reply_markup=buttons.benefits_section_keyboard())
