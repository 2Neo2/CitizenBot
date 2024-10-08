from aiogram import Router, F
from aiogram.filters.callback_data import CallbackQuery
from aiogram.fsm.context import FSMContext

from ...servicies.rnis import RNIS
from .. import buttons, forms, callbacks
from . import messages
import json

import os
from dotenv import load_dotenv
load_dotenv()


router = Router()
#img_path = 'telegram/img/'

async def get_route_data(data):
    async with RNIS(login=os.environ['RNIS_LOGIN'], password=os.environ['RNIS_PASSWORD'], token=os.environ['RNIS_TOKEN']) as rnis:
        route_data = await rnis.API.Geo.Route.to_list(
            all_pages=True,
            delay=4,
            status = '1abd2f98-7845-11e7-be3f-3a4e0357cc4a',
            mun = data['route_info']['municipality_uuid'],
            name = data['route_info'].get('route_name'),
            number = data['route_info'].get('route_number'),
            response_data = ['items/uuid', 'items/title', 'items/number']
        )

        return route_data

@router.callback_query(forms.ScheduleRouteForm.get_route, callbacks.RouteInputCallback.filter())
async def input_route_number(callback_query: CallbackQuery, callback_data: callbacks.RouteInputCallback, state: FSMContext):
    input_type = callback_data.action

    if input_type == 'number':
        mess = messages.input_route_number_message
    if input_type == 'name':
        mess = messages.input_route_name_message

    data = await state.get_data()
    print(data)

    # data['route_info']['route_name'] = 'Балашиха'
    # response = await get_route_data(data)

    # print(json.dumps(response, indent=3, ensure_ascii=False))

    await callback_query.message.answer(mess)

