class OrderValueValidator:
	many_digits_error = '⛔️ Некорректное значение, допустимо не больше <b>8</b> знаков после запятой'
	incorrect_value_error = '⛔️ Некорректное значение, попробуйте еще раз'
	min_value_error = 'Минимальное значение: <b>{rub_value} RUB</b> или <b>{crypt_value} {crypt}</b>'
	wallet_error = '⛔️ Произошли технические неполадки, попробуйте позже'

	def __init__(self, enter_value: str):
		self.client = client
		self.enter_value = enter_value.replace(',', '.')
		self.crypt = crypt
		self.error = ''

		self.rub_value = None
		self.crypt_value = None
		self.course = None
		self.crypt_settings = None

	async def is_valid(self) -> bool:
		try:
			enter_value = float(self.enter_value)
			if enter_value <= 0: # Сумма должна быть больше 0.
				self.error = OrderValueValidator.incorrect_value_error
				return False

			# Проверка кол-ва знаков после точки.
			if '.' in self.enter_value:
				index = self.enter_value.index('.')
				substring = self.enter_value[index+1:]
				if len(substring) > 8: # Допустимо не больше 8 знаков после запятой.
					self.error = OrderValueValidator.many_digits_error
					return False
		except:
			self.error = OrderValueValidator.incorrect_value_error
			return False
