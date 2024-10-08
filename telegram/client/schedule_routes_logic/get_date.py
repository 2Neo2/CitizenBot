from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackQuery

from ...servicies.rnis import RNIS
from .. import buttons, forms, callbacks
from . import messages
from datetime import datetime as dt

import os
from dotenv import load_dotenv
load_dotenv()

router = Router()
#img_path = 'telegram/img/'

# МУНИКИ, ГДЕ НЕТ МАРШРУТОВ!!!
# Ивантеевка МО, Рошаль МО
# Власиха МО (ЗАТО), Восход (ЗАТО) МО
# Красноармейск МО, Звенигород МО
# Молодежный МО (ЗАТО), Солнечногорск МО
# Кашира МО, Луховицы МО
# Ликино-Дулево (Орехово-Зуевский ), Озёры ( Коломна )


CLOSE_DATA = [
	'Москва',
	'Не используется (для ЖКХ)'
]

ITEMS_PER_PAGE = 5 

async def get_municipality_data():
    async with RNIS(login=os.environ['RNIS_LOGIN'], password=os.environ['RNIS_PASSWORD'], token=os.environ['RNIS_TOKEN']) as rnis:
        dictionary_data = await rnis.API.Dictionary.to_list(
            dictionary='communal_municipalities',
            retries=2,
            error_print=True
        )
        dictionary_data = dictionary_data['payload']['documents']
        municipality_data = {
            normilize_municipality_name(item['name']): item['uuid']
            for item in dictionary_data if item['name'] not in CLOSE_DATA
        }

        return municipality_data
     

def normilize_municipality_name(municipality_name):
	replace_list = ['МО', 'Городской округ', 'в настоящее время - ', 'городской округ', 'МО', 'Территориальное управление']
	for replace in replace_list:
		municipality_name = municipality_name.replace(replace, '')
	return municipality_name.strip()


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
        
    builder.adjust(1)
    return builder.as_markup()


@router.callback_query(F.data.in_('today'))
async def start_schedule_routes(callback_query: CallbackQuery, state: FSMContext):
    try: 
        mess = messages.municipality_message
        municipality_data = await get_municipality_data()
        keyboard = get_municipality_keyboard(municipality_data, page=0)
        
        await state.set_state(forms.ScheduleRouteForm.get_municipality)
        await callback_query.message.answer(mess, reply_markup=keyboard)
    except Exception:
        mess = messages.error_message
        await callback_query.message.answer(mess)


@router.callback_query(lambda c: c.data.startswith('prev_page_') or c.data.startswith('next_page_'))
async def handle_pagination(callback_query: CallbackQuery, state: FSMContext):
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

    print(await state.get_data())
    await callback_query.message.answer(mess, reply_markup=keyboard)
    

@router.callback_query(F.data.in_('get_date'))
async def start_schedule_routes(message: Message):
	mess = messages.start_message
	await message.answer(mess, reply_markup=buttons.get_schedule_date_keyboard())
