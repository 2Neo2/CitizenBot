from aiogram.fsm.state import StatesGroup, State

class ScheduleRouteForm(StatesGroup):
    get_municipality = State()
    get_route = State()

class RouteInfoImputForm(StatesGroup):
    input_name = State()
    input_number = State()
    select_route = State()

class DialogDateForm(StatesGroup):
    get_data = State()

class ConsultationForm(StatesGroup):
    get_question = State()
