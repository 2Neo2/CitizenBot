from aiogram.fsm.state import StatesGroup, State

class AppealForm(StatesGroup):
    get_appeal = State()
    start_answer_appeal = State()
    input_answer = State()