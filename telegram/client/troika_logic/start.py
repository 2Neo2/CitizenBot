from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from .. import buttons
from . import messages

section_name = '🎫 Частые вопросы о Тройке'

router = Router()
#img_path = 'telegram/img/'

@router.message(F.text.in_(section_name))
async def start_troika_questions(message: Message):
	mess = messages.start_message
	await message.answer(mess, reply_markup=buttons.get_troika_questions_keyboard())
	

@router.callback_query(F.data.in_('troika_cost'))
async def get_section_date(call: CallbackQuery):
    mess = messages.troika_cost_answer

    await call.message.answer(mess)


@router.callback_query(F.data.in_('troika_loyalty'))
async def get_section_date(call: CallbackQuery):
    mess = messages.troika_loyalty_answer

    await call.message.answer(mess)


@router.callback_query(F.data.in_('troika_fill'))
async def get_section_date(call: CallbackQuery):
    mess = messages.troika_fill_answer

    await call.message.answer(mess)


@router.callback_query(F.data.in_('troika_buy'))
async def get_section_date(call: CallbackQuery):
    mess = messages.troika_buy_answer

    await call.message.answer(mess)
