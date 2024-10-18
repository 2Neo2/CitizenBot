from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
from aiogram.client.bot import DefaultBotProperties

from .. import forms, callbacks, buttons
from . import messages
from control_db.models import ClientAppeal, Client
import os
from dotenv import load_dotenv
load_dotenv()

section_name = 'Мои обращения'
router = Router()
ITEMS_PER_PAGE=7

def get_appeals_keyboard(appeals, page: int = 0):
    builder = InlineKeyboardBuilder()
    
    start_idx = page * ITEMS_PER_PAGE
    end_idx = start_idx + ITEMS_PER_PAGE
    page_data = list(appeals[start_idx:end_idx])
    
    for appeal in page_data:
        builder.button(
            text=appeal.appeal_id,
            callback_data=callbacks.AppealCallback(
                appeal_id=appeal.appeal_id
            ).pack()
        )

    builder.adjust(1)
    nav_buttons = []

    if page > 0:
        nav_buttons.append(InlineKeyboardButton(
            text='⬅️', callback_data=f"prev_appeal_page_{page}"
        ))
    
    if end_idx < len(appeals):
        nav_buttons.append(InlineKeyboardButton(
            text='➡️', callback_data=f"next_appeal_page_{page}"
        ))
    
    if nav_buttons:
        builder.row(*nav_buttons)
        
    return builder.as_markup()


@router.message(F.text.in_(section_name))
async def get_all_appeals(message: Message, state: FSMContext):
    admin = Client.objects.get(tg_id=message.from_user.id)
    appeals = ClientAppeal.objects.filter(consultant=admin, status='work')
    mess = messages.start_message.format(
        appeals_count=appeals.count()
    )
    await state.clear()

    keyboard = get_appeals_keyboard(appeals, page=0)
    await state.set_state(forms.AppealForm.start_answer_appeal)
    await message.answer(mess, reply_markup=keyboard)


@router.callback_query(forms.AppealForm.start_answer_appeal, callbacks.AppealCallback.filter())
async def input_answer(callback_query: CallbackQuery, callback_data: callbacks.AppealCallback, state: FSMContext):
    await state.set_data({"id": callback_data.appeal_id})
    await state.set_state(forms.AppealForm.input_answer)

    appeal = ClientAppeal.objects.get(appeal_id=callback_data.appeal_id)
    mess = messages.get_answer_message.format(
        appeal_id=callback_data.appeal_id,
        appeal_text=appeal.appeal,
        client_name=appeal.client.username
    )
    keyboard = buttons.get_back_keyboard()
    await callback_query.message.edit_text(mess, reply_markup=keyboard)
    await callback_query.answer()


@router.message(forms.AppealForm.input_answer, F.text)
async def check_answer(message: Message, state: FSMContext):
    data = await state.get_data()
    mess = message.text
    await message.answer(mess, reply_markup=buttons.get_send_keyboard(data['id']))


@router.callback_query(forms.AppealForm.input_answer, lambda c: c.data.startswith('send_'))
async def send_answer(callback_query: CallbackQuery, state: FSMContext):
    data_id = callback_query.data.split('_')[1]
    answer = callback_query.message.text

    appeal = ClientAppeal.objects.get(appeal_id=data_id)
    client_id = appeal.client.tg_id
    appeal.answer = answer
    appeal.status = 'completed'
    appeal.save()

    bot = Bot(
        token=os.environ['BOT_TOKEN'],
        default=DefaultBotProperties(parse_mode='HTML', link_preview_is_disabled=True)
    )

    client_message = messages.client_answer_message.format(
        appeal_id=appeal.appeal_id,
        appeal_text=appeal.appeal,
        appeal_answer=appeal.answer
    )

    await bot.send_message(client_id, client_message)

    mess = messages.end_appeal_message
    await callback_query.message.edit_text(mess)
    await callback_query.answer()


@router.callback_query(forms.AppealForm.input_answer, lambda c: c.data.startswith('cancel'))
async def cancel_answer(callback_query: CallbackQuery, state: FSMContext):
    await state.clear()
    mess = messages.cancel_message
    await callback_query.message.answer(mess)
    await callback_query.answer()



@router.callback_query(forms.AppealForm.input_answer, lambda c: c.data.startswith('back'))
async def cancel_answer(callback_query: CallbackQuery, state: FSMContext):
    admin = Client.objects.get(tg_id=callback_query.from_user.id)
    appeals = ClientAppeal.objects.filter(consultant=admin, status='work')
    mess = messages.start_message.format(
        appeals_count=appeals.count()
    )
    await state.clear()

    keyboard = get_appeals_keyboard(appeals, page=0)
    await state.set_state(forms.AppealForm.start_answer_appeal)

    await callback_query.message.edit_text(mess, reply_markup=keyboard)
    await callback_query.answer()
