from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from .. import buttons
from . import messages


router = Router()
#img_path = 'telegram/img/'

@router.callback_query(F.data.in_('troika_questions'))
async def start_troika_questions(call: CallbackQuery, state: FSMContext):
    mess = messages.start_message
    await state.clear()
    await state.set_data({})
    await call.message.answer(mess, reply_markup=buttons.get_troika_questions_keyboard())


@router.callback_query(F.data.in_('troika_cost'))
async def get_section_date(call: CallbackQuery):
    mess = messages.troika_cost_answer.format(
        question='Сколько стоит проезд?'
    )

    await call.message.answer(mess)


@router.callback_query(F.data.in_('troika_loyalty'))
async def get_section_date(call: CallbackQuery):
    mess = messages.troika_loyalty_answer.format(
        question='Действует ли лояльность при оплате Тройкой?'
    )

    await call.message.answer(mess)


@router.callback_query(F.data.in_('troika_fill'))
async def get_section_date(call: CallbackQuery):
    mess = messages.troika_fill_answer.format(
        question='Как пополнить Тройку?'
    )

    await call.message.answer(mess)


@router.callback_query(F.data.in_('troika_buy'))
async def get_section_date(call: CallbackQuery):
    mess = messages.troika_buy_answer.format(
        question='Где купить Тройку?'
    )

    await call.message.answer(mess)
