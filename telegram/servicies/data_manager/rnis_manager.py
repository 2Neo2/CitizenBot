from ..rnis import RNIS

import os
import json
from dotenv import load_dotenv
load_dotenv()


CLOSE_DATA = [
	'Москва',
	'Не используется (для ЖКХ)'
]

# МУНИКИ, ГДЕ НЕТ МАРШРУТОВ!!!
# Ивантеевка МО, Рошаль МО
# Власиха МО (ЗАТО), Восход (ЗАТО) МО
# Красноармейск МО, Звенигород МО
# Молодежный МО (ЗАТО), Солнечногорск МО
# Кашира МО, Луховицы МО
# Ликино-Дулево (Орехово-Зуевский ), Озёры ( Коломна )


async def get_route_data(data):
    async with RNIS(login=os.environ['RNIS_LOGIN'], password=os.environ['RNIS_PASSWORD'], token=os.environ['RNIS_TOKEN']) as rnis:
        route_data = await rnis.API.Geo.Route.to_list(
            all_pages=True,
            delay=4,
            limit=50,
            status = '1abd2f98-7845-11e7-be3f-3a4e0357cc4a',
            mun = data['route_info']['municipality_uuid'],
            name = data['route_info'].get('route_name'),
            number = 125,
            response_data = ['items/uuid', 'items/title', 'items/number']
        )

        print(route_data)

        return route_data['payload']['items']


async def get_schedule_data(data):
    async with RNIS(login=os.environ['RNIS_LOGIN'], password=os.environ['RNIS_PASSWORD'], token=os.environ['RNIS_TOKEN']) as rnis:
        schedule_data = await rnis.API.Geo.Schedule.to_list(
            route_uuid=data['route_info']['route_uuid'],
            date=data['route_info']['date'],
            status='1ae17c18-7845-11e7-8cb9-89de9538062c',
            response_data=[],
            all_pages=True,
            delay=4
        )

        return schedule_data['payload']['items']

 
async def get_bus_stop_data(bus_stop_uuid):
    with open('static/bus_stop_list.json', 'r') as file:
        response = json.load(file)

    for bus_stop in response:
        if bus_stop['uuid'] == bus_stop_uuid:
            return bus_stop['title']


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

        municipality_data_sorted = {
            key: municipality_data[key]
            for key in sorted(municipality_data)
        }

        return municipality_data_sorted
     

def normilize_municipality_name(municipality_name):
	replace_list = ['МО', 'Городской округ', 'в настоящее время - ', 'городской округ', 'МО', 'Территориальное управление']
	for replace in replace_list:
		municipality_name = municipality_name.replace(replace, '')
	return municipality_name.strip()
