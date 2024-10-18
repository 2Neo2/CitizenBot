from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from ..callbacks import StrelkaQuestionCallback

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


@router.callback_query(StrelkaQuestionCallback.filter())
async def get_answer_question(callback_query: CallbackQuery, callback_data: StrelkaQuestionCallback, state: FSMContext):
    data = callback_data.number_question.split('_')	
    section = data[0]
    question_number = data[1]
    
    if section == 'exchange':
        if question_number == 1:
            mess = messages.change_strelka_message.format(
                question='Как обменять Стрелку?'
            )
        elif question_number == 2:
            mess = messages.change_error_strelka_message.format(
                question='Почему могут отказать в обмене?'
            )
        elif question_number == 3:
            mess = messages.get_strelka_deposit_message.format(
                question='Как вернуть Стрелку и получить залоговую стоимость?'
            )
        elif question_number == 4:
            mess = messages.refund_strelka_message.format(
                question='Как сделать возврат средств со Стрелки?'
            )
        elif question_number == 5:
            mess = messages.tickets_strelka_message.format(
                question='Как вернуть деньги за билеты на Ж/Д?'
            )
        elif question_number == 6:
            mess = messages.old_strelka_message.format(
                question='Как перенести деньги со старой Стрелки?'
            )
    elif section == 'tariffs':
        if question_number == 1:
            mess = messages.cost_blue_strelka_message.format(
                question='Сколько стоит проезд по синей Стрелке?'
            )
        elif question_number == 2:
            mess = messages.cost_study_strelka_message.format(
                question='Сколько стоит проезд по Стрелке учащегося?'
            )
        elif question_number == 3:
            mess = messages.cost_beneficial_strelka_message.format(
                question='Сколько стоит проезд по Стрелке льготной?'
            )
    else:
        if question_number == 1:
            mess = messages.blue_strelka_message.format(
                question='Кто может получить Стрелку учащегося?'
            )
        elif question_number == 2:
            mess = messages.study_strelka_message.format(
                question='Кто может получить Стрелку льготная?'
            )
        elif question_number == 3:
            mess = messages.beneficial_strelka_message.format(
                question='Как подтвердить право на льготу по Стрелке учащегося?'
            )

    await callback_query.answer(mess)   



