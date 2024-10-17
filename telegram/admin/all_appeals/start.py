from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
from aiogram.fsm.context import FSMContext

from .. import forms, callbacks, buttons
from . import messages
from control_db.models import ClientAppeal, Client

section_name = 'Все обращения'
router = Router()

ITEMS_PER_PAGE = 7


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
    appeals = ClientAppeal.objects.filter(status='processing')
    mess = messages.start_message.format(
        appeals_count=appeals.count()
    )
    await state.clear()
    await state.set_data({})

    keyboard = get_appeals_keyboard(appeals, page=0)
    await state.set_state(forms.AppealForm.get_appeal)
    await message.answer(mess, reply_markup=keyboard)


@router.callback_query(lambda c: c.data.startswith('prev_appeal_page_') or c.data.startswith('next_appeal_page_'))
async def handle_pagination(callback_query: CallbackQuery):
    try:
        appeals = ClientAppeal.objects.filter(status='processing')
        page = int(callback_query.data.split('_')[-1])
        if 'prev_page' in callback_query.data:
            new_page = page - 1
        elif 'next_page' in callback_query.data:
            new_page = page + 1
    
        keyboard = get_appeals_keyboard(appeals, new_page)

        await callback_query.message.edit_reply_markup(reply_markup=keyboard)
        await callback_query.answer()
    except Exception:
        mess = messages.error_message
        await callback_query.message.answer(mess)


@router.callback_query(forms.AppealForm.get_appeal, callbacks.AppealCallback.filter())
async def selected_appeal(callback_query: CallbackQuery, callback_data: callbacks.AppealCallback, state: FSMContext):
    appeal = ClientAppeal.objects.get(appeal_id=callback_data.appeal_id)
    await callback_query.message.edit_text(appeal.appeal, reply_markup=buttons.get_answer_keyboard(appeal.appeal_id))


@router.callback_query(forms.AppealForm.get_appeal, F.data.in_('all_back'))
async def back_select_appeal(callback_query: CallbackQuery, state: FSMContext):
    appeals = ClientAppeal.objects.filter(status='processing')
    mess = messages.start_message.format(
        appeals_count=appeals.count()
    )

    keyboard = get_appeals_keyboard(appeals, page=0)
    await callback_query.message.edit_text(mess, reply_markup=keyboard)


@router.callback_query(forms.AppealForm.get_appeal, lambda c: c.data.startswith('create_'))
async def back_select_appeal(callback_query: CallbackQuery, state: FSMContext):
    data = callback_query.data.split('_')[1]
    appeal = ClientAppeal.objects.get(appeal_id=data)
    client = Client.objects.get(tg_id=callback_query.from_user.id)

    appeal.consultant = client
    appeal.status = 'work'
    appeal.save()

    mess = messages.appeal_add_message.format(
        appeal_id=appeal.appeal_id
    )

    await state.clear()
    await state.set_data({})

    await callback_query.message.edit_text(mess)