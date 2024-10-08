from aiogram.filters.callback_data import CallbackData

class ScheduleCallback(CallbackData, prefix='choice_schedule'):
	date: str
	municipality_uuid: str
	
class RouteInputCallback(CallbackData, prefix="route_input"):
    action: str