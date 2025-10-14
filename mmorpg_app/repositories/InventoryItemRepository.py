from mmorpg_app.models import InventoryItem
from mmorpg_app.repositories.BaseRepository import BaseRepository

class InventoryItemRepository(BaseRepository):
    def __init(self):
        super().__init__(InventoryItem)