from aiogram.types import KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from .callbacks import RouteInputCallback


# Main menu buttons.
route_schedule_button = KeyboardButton(text='🚌 Показать расписание маршрута')
cost_travel_bttuon = KeyboardButton(text='💸 Узнать стоимость проезда')
strelka_question_button = KeyboardButton(text='🚀 Частые вопросы о Стрелке')
troika_question_button = KeyboardButton(text='🎫 Частые вопросы о Тройке')
card_question_button = KeyboardButton(text='💳 Частые вопросы о БК')
general_question_button = KeyboardButton(text='💡 Общие вопросы')
consultation_button = KeyboardButton(text='🙋🏻‍♂️ Другие вопросы / Консультация')
info_button = KeyboardButton(text='ℹ️ Справочное инфо')

def get_main_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard = [
            [route_schedule_button],
            [cost_travel_bttuon],
            [strelka_question_button],
            [troika_question_button],
            [card_question_button],
            [general_question_button],
            [consultation_button],
            [info_button],
        ],
        resize_keyboard = True,
    )
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
    'Как поменять карту "Стрелка?"',
    'Как вернуть карту "Стрелка" и получить залоговую стоимость карты?',
    'Как сделать возврат средств с карты "Стрелка" на банковский счет?',
    'Как вернуть денежные средства за билеты/абонементы для проезда на пригородных электричках, записанные на карту "Стрелка"?',
    'Как перенести остаток денежных средств с карты "Стрелка" на новую карту?',
    'После обмена сохраняются ли накопленные скидки по карте "Стрелка", если пассажиру выдают новую карту ?'
]

tariffs_section_questions = [
    'Сколько стоит проезд по льготной карте "Стрелка"?',
    'Сколько стоит проезд по карте "Стрелка" учащегося и "Стрелка" учащегося сельской местности?',
    '',
    '',
    '',
    ''
]

mobile_section_questions = [
    'Как пользоваться мобильным приложением "Стрелка"?',
    'Преимущества мобильного приложения "Стрелка"'
]

def get_sections_strelka_keyboard():
    buttons = [
        [InlineKeyboardButton(text='Обмен и возврат', callback_data="exchange")],
        [InlineKeyboardButton(text='Тарифы и маршруты', callback_data="tariffs")],
        [InlineKeyboardButton(text='Мобильное приложение', callback_data="mobile")]
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
    ('Сколько раз можно оплатить проезд БК на одном рейсе?', 'card_count_pay'),
    ('Где можно посмотреть историю поездок?', 'card_history'),
    ('Не удалось оплатить проезд?', 'card_error'),
    ('Не удалось оплатить проезд БК с помощью телефона?', 'card_error_phone'),
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
