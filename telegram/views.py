from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import HttpResponse

from .dispatcher import bot, dp

import json
from aiogram.types.update import Update


@csrf_exempt
@require_POST
async def process_update(request):
	update = Update(**(json.loads(request.body.decode('utf-8'))))
	await dp.feed_update(bot, update)

	return HttpResponse('ok')
