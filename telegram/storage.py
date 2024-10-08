from aiogram.fsm.storage.base import BaseStorage, StorageKey
from aiogram.fsm.state import State

from typing import Any, Dict, Optional

from control_db.models import Client


class SQLStorage(BaseStorage):
	def __init__(self):
		pass

	async def set_state(self, key: StorageKey, state: str = None) -> None:
		exists = await Client.exists(key.user_id)
		if exists:
			client = await Client.objects.aget(tg_id=key.user_id)
			await client.set_state(state.state if isinstance(state, State) else state)

	async def get_state(self, key: StorageKey) -> Optional[str]:
		exists = await Client.exists(key.user_id)
		if exists:
			client = await Client.objects.aget(tg_id=key.user_id)
			return client.state

		return ''

	async def set_data(self, key: StorageKey, data: Dict[str, Any]) -> None:
		exists = await Client.exists(key.user_id)
		if exists:
			client = await Client.objects.aget(tg_id=key.user_id)
			client.data = data
			await client.asave()

	async def get_data(self, key: StorageKey) -> Dict[str, Any]:
		exists = await Client.exists(key.user_id)
		if exists:
			client = await Client.objects.aget(tg_id=key.user_id)
			return client.data

		return {}

	async def close(self) -> None:
		pass
