from django.core.management.base import BaseCommand

import asyncio
from telegram import dispatcher

class Command(BaseCommand):
	help = 'Запуск бота'

	def handle(self, *args, **options):
		asyncio.run(dispatcher.polling())