from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from .. import forms
from . import messages
from control_db.models import ClientAppeal, Client
import random, string


router = Router()

@router.callback_query(F.data.in_('add_questions'))
async def start_consultation(call: CallbackQuery, state: FSMContext):
    mess = messages.start_question_message
    await state.set_state(forms.ConsultationForm.get_question)
    await call.message.answer(mess)
    await call.answer()


@router.message(forms.ConsultationForm.get_question, F.text)
async def get_consultation_question(message: Message, state: FSMContext):
    mess = messages.end_consultation_message
    await state.clear()
    client, _ = await Client.objects.aget_or_create(tg_id=message.from_user.id)

    appeal = await ClientAppeal.objects.acreate(
        appeal_id=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(12)),
        client=client,
        appeal=message.text,
    )

    mess = messages.end_consultation_message.format(
        appeal=appeal
    )
    await message.answer(mess)