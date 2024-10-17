from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

admin_questions_button = KeyboardButton(text='Мои обращения')
all_questions_button = KeyboardButton(text='Все обращения')

start_menu = ReplyKeyboardMarkup(
	keyboard = [
		[admin_questions_button, all_questions_button],
	],
	resize_keyboard = True,
)

def get_answer_keyboard(appeal_id):
    buttons = [
        [InlineKeyboardButton(text='Добавить в свои', callback_data=f'create_{appeal_id}')],
        [InlineKeyboardButton(text='Назад', callback_data='all_back')]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_send_keyboard(appeal_id):
    buttons = [
        [InlineKeyboardButton(text='Отправить', callback_data=f'send_{appeal_id}')],
        [InlineKeyboardButton(text='Отмена', callback_data='cancel')]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard