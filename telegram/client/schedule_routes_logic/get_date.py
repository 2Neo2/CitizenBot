from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackQuery
from aiogram_dialog import DialogManager, Dialog, Window, StartMode
from aiogram_dialog.widgets.kbd import Calendar
from aiogram_dialog.widgets.text import Const

from ...servicies.data_manager.rnis_manager import get_municipality_data
from .. import buttons, forms, callbacks
from . import messages
from datetime import datetime as dt

router = Router()

ITEMS_PER_PAGE = 7

async def on_date_selected(dialog_manager, date: str, **kwargs):
    await dialog_manager.current_context().bot.send_message(
        dialog_manager.current_user.id,
        f"Вы выбрали дату: {date}"
    )


async def create_calendar_dialog():
    return Dialog(
        Window(
            Const("Выберите дату:"),
            Calendar(id="calendar"),
            state=forms.DialogDateForm.get_data
        )
    )

def get_municipality_keyboard(municipality_data, page: int = 0):
    builder = InlineKeyboardBuilder()
    
    start_idx = page * ITEMS_PER_PAGE
    end_idx = start_idx + ITEMS_PER_PAGE
    page_data = list(municipality_data.items())[start_idx:end_idx]
    
    for name, uuid in page_data:
        builder.button(
            text=name,
            callback_data=callbacks.ScheduleCallback(
                date=dt.now().date().strftime("%Y-%m-%d"), 
                municipality_uuid=uuid
            ).pack()
        )

    builder.adjust(1)
    nav_buttons = []

    if page > 0:
        nav_buttons.append(InlineKeyboardButton(
            text='⬅️', callback_data=f"prev_page_{page}"
        ))
    
    if end_idx < len(municipality_data):
        nav_buttons.append(InlineKeyboardButton(
            text='➡️', callback_data=f"next_page_{page}"
        ))
    
    if nav_buttons:
        builder.row(*nav_buttons)
        
    return builder.as_markup()


@router.callback_query(F.data.in_('today'))
async def start_schedule_routes(callback_query: CallbackQuery, state: FSMContext):
    try: 
        mess = messages.municipality_message
        municipality_data = await get_municipality_data()
        keyboard = get_municipality_keyboard(municipality_data, page=0)
        
        await state.set_state(forms.ScheduleRouteForm.get_municipality)
        await callback_query.message.edit_text(mess, reply_markup=keyboard)
        await callback_query.answer()
    except Exception:
        mess = messages.error_message
        await callback_query.message.answer(mess)


@router.callback_query(lambda c: c.data.startswith('prev_page_') or c.data.startswith('next_page_'))
async def handle_pagination(callback_query: CallbackQuery):
    try:
        page = int(callback_query.data.split('_')[-1])
        municipality_data = await get_municipality_data()
        if 'prev_page' in callback_query.data:
            new_page = page - 1
        elif 'next_page' in callback_query.data:
            new_page = page + 1
    
        keyboard = get_municipality_keyboard(municipality_data, new_page)

        await callback_query.message.edit_reply_markup(reply_markup=keyboard)
        await callback_query.answer()
    except Exception:
        mess = messages.error_message
        await callback_query.message.answer(mess)


@router.callback_query(forms.ScheduleRouteForm.get_municipality, callbacks.ScheduleCallback.filter())
async def choiced_municipality(callback_query: CallbackQuery, callback_data: callbacks.ScheduleCallback, state: FSMContext):
    municipality_name = ''
    municipality_data = await get_municipality_data()

    for key, value in municipality_data.items():
        if value == callback_data.municipality_uuid:
            municipality_name = key
            break

    mess = messages.type_input_route_message.format(
        municipality_name = municipality_name
    )
    keyboard = buttons.get_route_input_type_keyboard()

    await state.set_data({
        'route_info' : {
            'date': callback_data.date,
            'municipality_name': municipality_name,
            'municipality_uuid': callback_data.municipality_uuid
        }
    })
    await state.set_state(forms.ScheduleRouteForm.get_route)
    await callback_query.message.edit_text(mess, reply_markup=keyboard)
    await callback_query.answer()
    

@router.callback_query(F.data.in_('get_date'))
async def start_schedule_routes(call: CallbackQuery, dialog_manager: DialogManager):
    calendar_dialog = await create_calendar_dialog()
    await dialog_manager.start(state=forms.DialogDateForm.get_data, mode=StartMode.NORMAL)
