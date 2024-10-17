from aiogram.fsm.storage.base import BaseStorage, StorageKey
from aiogram.fsm.state import State

from typing import Any, Dict, Optional

from control_db.models import Client


class SQLStorage(BaseStorage):
    def __init__(self):
        pass

    async def get_client(self, key: StorageKey) -> Client:
        client, _ = await Client.objects.aget_or_create(tg_id=key.user_id)
        return client

    async def set_state(self, key: StorageKey, state: str = None) -> None:
        client = await self.get_client(key)
        await client.set_state(state.state if isinstance(state, State) else state)

    async def get_state(self, key: StorageKey) -> Optional[str]:
        client = await self.get_client(key)
        return client.state

    async def set_data(self, key: StorageKey, data: Dict[str, Any]) -> None:
        client = await self.get_client(key)
        client.set_data(data)

    async def get_data(self, key: StorageKey) -> Dict[str, Any]:
        client = await self.get_client(key)
        return client.data
    
    async def close(self) -> None:
        pass
