from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from .. import buttons
from . import messages

section_name = '💳 Частые вопросы о БК'

router = Router()
#img_path = 'telegram/img/'

@router.message(F.text.in_(section_name))
async def start_bank_card_questions(message: Message):
	mess = messages.start_message
	await message.answer(mess, reply_markup=buttons.get_bank_card_questions_keyboard())


@router.callback_query(F.data.in_('card_cost'))
async def get_section_date(call: CallbackQuery):
    mess = messages.card_cost_answer

    await call.message.answer(mess)


@router.callback_query(F.data.in_('card_count_pay'))
async def get_section_date(call: CallbackQuery):
    mess = messages.card_count_pay_answer

    await call.message.answer(mess)

@router.callback_query(F.data.in_('card_history'))
async def get_section_date(call: CallbackQuery):
    mess = messages.card_history_answer

    await call.message.answer(mess)

@router.callback_query(F.data.in_('card_error'))
async def get_section_date(call: CallbackQuery):
    mess = messages.card_error_answer

    await call.message.answer(mess)


@router.callback_query(F.data.in_('card_error_phone'))
async def get_section_date(call: CallbackQuery):
    mess = messages.card_error_phone_answer

    await call.message.answer(mess)


@router.callback_query(F.data.in_('card_debt'))
async def get_section_date(call: CallbackQuery):
    mess = messages.card_debt_answer

    await call.message.answer(mess)
