from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from .. import buttons
from . import messages


router = Router()
#img_path = 'telegram/img/'

@router.callback_query(F.data.in_('card_questions'))
async def start_bank_card_questions(call: CallbackQuery, state: FSMContext):
    mess = messages.start_message
    await state.clear()
    await state.set_data({})
    await call.message.answer(mess, reply_markup=buttons.get_bank_card_questions_keyboard())
    await call.answer()


@router.callback_query(F.data.in_('card_cost'))
async def get_section_date(call: CallbackQuery):
    mess = messages.card_cost_answer.format(
        question='Сколько стоит проезд?'
    )

    await call.message.answer(mess)


@router.callback_query(F.data.in_('card_count_pay'))
async def get_section_date(call: CallbackQuery):
    mess = messages.card_count_pay_answer.format(
        question='Сколько раз можно оплатить проезд?'
    )

    await call.message.answer(mess)

@router.callback_query(F.data.in_('card_history'))
async def get_section_date(call: CallbackQuery):
    mess = messages.card_history_answer.format(
        question='Где можно посмотреть историю поездок?'
    )

    await call.message.answer(mess)

@router.callback_query(F.data.in_('card_error'))
async def get_section_date(call: CallbackQuery):
    mess = messages.card_error_answer.format(
        question='Не удалось оплатить проезд?'
    )

    await call.message.answer(mess)


@router.callback_query(F.data.in_('card_error_phone'))
async def get_section_date(call: CallbackQuery):
    mess = messages.card_error_phone_answer.format(
        question='Не удалось оплатить проезд телефоном?'
    )

    await call.message.answer(mess)


@router.callback_query(F.data.in_('card_debt'))
async def get_section_date(call: CallbackQuery):
    mess = messages.card_debt_answer.format(
        question='Как погасить задолженность?'
    )

    await call.message.answer(mess)
