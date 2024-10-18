from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
import calendar


russian_months = [
    "", "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", 
    "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"
]


def generate_calendar_keyboard(year: int, month: int):
    builder = InlineKeyboardBuilder()

    month_days = calendar.monthcalendar(year, month)
    month_name = russian_months[month]

    builder.row(InlineKeyboardButton(text=f'{month_name} {year}', callback_data='ignore'))

    week_days = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
    builder.row(*[InlineKeyboardButton(text=day, callback_data='ignore') for day in week_days])

    for week in month_days:
        buttons = []
        for day in week:
            if day == 0:
                buttons.append(InlineKeyboardButton(text=' ', callback_data='ignore'))
            else:
                buttons.append(InlineKeyboardButton(text=str(day), callback_data=f"day:{year}:{month}:{day}"))
        builder.row(*buttons)

    builder.row(
        InlineKeyboardButton(text='<<', callback_data=f"prev_month:{year}:{month}"),
        InlineKeyboardButton(text='>>', callback_data=f"next_month:{year}:{month}")
    )

    return builder.as_markup()
