from aiogram.filters.callback_data import CallbackData

class AppealCallback(CallbackData, prefix="appeal_info"):
    appeal_id: str