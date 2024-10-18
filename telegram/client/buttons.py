from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from .callbacks import StrelkaQuestionCallback, RouteInputCallback


# Main menu buttons.
def get_main_keyboard():
    buttons = [
        [InlineKeyboardButton(text='🚌 Показать расписание маршрута', callback_data="route_schedule")],
        [InlineKeyboardButton(text='💸 Узнать стоимость проезда', callback_data="route_cost")],
        [InlineKeyboardButton(text='🚀 Частые вопросы о Стрелке', callback_data="strelka_questions")],
        [InlineKeyboardButton(text='🎫 Частые вопросы о Тройке', callback_data="troika_questions")],
        [InlineKeyboardButton(text='💳 Частые вопросы о БК', callback_data="card_questions")],
        [InlineKeyboardButton(text='💡 Общие вопросы', callback_data="general_questions")],
        [InlineKeyboardButton(text='🙋🏻‍♂️ Другие вопросы / Консультация', callback_data="add_questions")],
        [InlineKeyboardButton(text='ℹ️ Справочное инфо', callback_data="ref_info")],
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

# Schedule routes inline buttons.
def get_schedule_date_keyboard():
    buttons = [
        [InlineKeyboardButton(text='Сегодня', callback_data="today")],
        [InlineKeyboardButton(text='Выбрать дату', callback_data="get_date")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def get_route_input_type_keyboard():
    buttons = [
        [InlineKeyboardButton(text='Ввести название', callback_data=RouteInputCallback(action='name').pack())],
        [InlineKeyboardButton(text='Ввести номер', callback_data=RouteInputCallback(action='number').pack())]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

# Strelka inline buttons.
exchenge_section_questions = [
    'Как обменять Стрелку?',
    'Почему могут отказать в обмене?',
    'Как получить залоговую стоимость Стрелки?',
    'Как сделать возврат средств со Стрелки?',
    'Как вернуть деньги за билеты на Ж/Д?',
    'Как перенести деньги со старой Стрелки?',
    '⬅️ Назад'
]

tariffs_section_questions = [
    'Сколько стоит проезд по синей Стрелке?',
    'Сколько стоит проезд по Стрелке учащегося?',
    'Сколько стоит проезд по Стрелке льготной?',
    '⬅️ Назад'
]

benefits_section_questions = [
    'Кто может получить Стрелку учащегося?',
    'Кто может получить Стрелку льготная?',
    'Как получить льготу по Стрелке учащегося?',
    '⬅️ Назад'
]

def exchenge_section_keyboard():
    buttons = []
    for index, item in enumerate(exchenge_section_questions, start=1):
        if 'Назад' in item:
            buttons.append([InlineKeyboardButton(text=item, callback_data='strelka_back')])
        else:
            buttons.append([InlineKeyboardButton(text=item, callback_data=StrelkaQuestionCallback(number_question=f'exchange_{index}').pack())])
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def tariffs_section_keyboard():
    buttons = []
    for index, item in enumerate(tariffs_section_questions, start=1):
        if 'Назад' in item:
            buttons.append([InlineKeyboardButton(text=item, callback_data='strelka_back')])
        else:
            buttons.append([InlineKeyboardButton(text=item, callback_data=StrelkaQuestionCallback(number_question=f'tariffs_{index}').pack())])
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def benefits_section_keyboard():
    buttons = []
    for index, item in enumerate(benefits_section_questions, start=1):
        if 'Назад' in item:
            buttons.append([InlineKeyboardButton(text=item, callback_data='strelka_back')])
        else:    
            buttons.append([InlineKeyboardButton(text=item, callback_data=StrelkaQuestionCallback(number_question=f'benefits_{index}').pack())])
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_sections_strelka_keyboard():
    buttons = [
        [InlineKeyboardButton(text='Обмен и возврат', callback_data="exchange")],
        [InlineKeyboardButton(text='Тарифы', callback_data="tariffs")],
        [InlineKeyboardButton(text='Карты льготной тарификации', callback_data="benefits")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

# Troika inline buttons.
troika_questions = [
    ('Сколько стоит проезд?', 'troika_cost'),
    ('Действует ли лояльность при оплате Тройкой?', 'troika_loyalty'),
    ('Как пополнить Тройку?', 'troika_fill'),
    ('Где купить Тройку?', 'troika_buy'),
]

def get_troika_questions_keyboard():
    buttons = []
    for question in troika_questions:
        buttons.append([InlineKeyboardButton(text=question[0], callback_data=question[1])])
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


# Bank card inline buttons.
bank_card_questions = [
    ('Сколько стоит проезд?', 'card_cost'),
    ('Сколько раз можно оплатить проезд?', 'card_count_pay'),
    ('Где можно посмотреть историю поездок?', 'card_history'),
    ('Не удалось оплатить проезд?', 'card_error'),
    ('Не удалось оплатить проезд телефоном?', 'card_error_phone'),
    ('Как погасить задолженность?', 'card_debt'),
]

def get_bank_card_questions_keyboard():
    buttons = []
    for question in bank_card_questions:
        buttons.append([InlineKeyboardButton(text=question[0], callback_data=question[1])])
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


# Reference info inline buttons.
def get_sections_info_keyboard():
    buttons = [
        [InlineKeyboardButton(text='Перечень', callback_data="list")],
        [InlineKeyboardButton(text='Ведомство', callback_data="department")],
    ] 

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

# Cancel buttons.
