from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackQuery
from datetime import datetime

from ...servicies.data_manager.rnis_manager import get_municipality_data
from .. import buttons, forms, callbacks
from . import messages, calendar
from datetime import datetime as dt

router = Router()
ITEMS_PER_PAGE = 7


def get_municipality_keyboard(municipality_data, page: int = 0):
    builder = InlineKeyboardBuilder()
    
    start_idx = page * ITEMS_PER_PAGE
    end_idx = start_idx + ITEMS_PER_PAGE
    page_data = list(municipality_data.items())[start_idx:end_idx]
    
    for name, uuid in page_data:
        builder.button(
            text=name,
            callback_data=callbacks.ScheduleCallback(
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
        await state.set_data({
            "route_info": {
                "date": dt.now().date().strftime("%Y-%m-%d")
            }
        })
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
    data = await state.get_data()

    for key, value in municipality_data.items():
        if value == callback_data.municipality_uuid:
            municipality_name = key
            break

    mess = messages.type_input_route_message.format(
        municipality_name = municipality_name,
        date=data['route_info']['date']
    )
    keyboard = buttons.get_route_input_type_keyboard()
    data['route_info']['municipality_name'] = municipality_name
    data['route_info']['municipality_uuid'] = callback_data.municipality_uuid

    await state.set_data(data)
    await state.set_state(forms.ScheduleRouteForm.get_route)
    await callback_query.message.edit_text(mess, reply_markup=keyboard)
    await callback_query.answer()
    

@router.callback_query(F.data.in_('get_date'))
async def start_schedule_routes(callback_query: CallbackQuery):
    current_date = datetime.now()
    year = current_date.year
    month = current_date.month
    mess = messages.date_choice_message
    await callback_query.message.edit_text(mess, reply_markup=calendar.generate_calendar_keyboard(year, month))
    await callback_query.answer()


@router.callback_query(lambda c: c.data and (c.data.startswith('prev_month:') or c.data.startswith('next_month:')))
async def process_month_change(callback_query: CallbackQuery):
    action, year, month = callback_query.data.split(":")
    year = int(year)
    month = int(month)

    if action == 'prev_month':
        if month == 1:
            month = 12
            year -= 1
        else:
            month -= 1
    elif action == 'next_month':
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1

    await callback_query.message.edit_reply_markup(reply_markup=calendar.generate_calendar_keyboard(year, month))
    await callback_query.answer()


@router.callback_query(lambda c: c.data and c.data.startswith('day:'))
async def process_day_selection(callback_query: CallbackQuery, state: FSMContext):
    _, year, month, day = callback_query.data.split(":")
    try: 
        mess = messages.municipality_message
        municipality_data = await get_municipality_data()
        keyboard = get_municipality_keyboard(municipality_data, page=0)
        
        await state.set_state(forms.ScheduleRouteForm.get_municipality)
        await state.set_data({
            "route_info": {
                "date": f'{year}-{month}-{day}'
            }
        })
        await callback_query.message.edit_text(mess, reply_markup=keyboard)
        await callback_query.answer()
    except Exception:
        mess = messages.error_message
        await callback_query.message.answer(mess)