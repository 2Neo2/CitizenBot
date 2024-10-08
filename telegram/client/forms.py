from aiogram.fsm.state import StatesGroup, State

class ScheduleRouteForm(StatesGroup):
    get_municipality = State()
    get_route = State()

# class OrderForm(StatesGroup):
# 	get_value = State()
# 	choice_payment_method = State()
# 	get_address = State()
# 	accept_pay = State()


# class CalcForm(StatesGroup):
# 	choice_crypt = State()
# 	get_value = State()

# class CaptchaForm(StatesGroup):
# 	get_captcha = State()

# class RefWithdrawalForm(StatesGroup):
# 	accept_withdrawal = State()
