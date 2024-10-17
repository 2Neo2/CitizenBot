from control_db.models import Client

import re


class RouteInputNumberValueValidator:
    incorrect_value_error = '⛔️ Некорректное значение, попробуйте еще раз'

    def __init__(self, enter_value: str):
        self.enter_value = enter_value.replace(' ', '')
        print(self.enter_value)
        self.error = ''

    async def is_valid(self) -> bool:
        pattern = r'^\d+[а-яА-Яa-zA-Z]?$'
        if re.match(pattern, self.enter_value):
            return True
        else:
            self.error = RouteInputNumberValueValidator.incorrect_value_error
            return False
        
