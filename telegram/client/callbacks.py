from aiogram.filters.callback_data import CallbackData

class ScheduleCallback(CallbackData, prefix='choice_schedule'):
	municipality_uuid: str
	
class RouteInputCallback(CallbackData, prefix="route_input"):
    action: str

class RouteInfoCallback(CallbackData, prefix="route_info"):
    route_uuid: str

class StrelkaQuestionCallback(CallbackData, prefix="strelka_question"):
    number_question: str
