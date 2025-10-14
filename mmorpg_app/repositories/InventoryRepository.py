from mmorpg_app.models import Inventory
from mmorpg_app.repositories.BaseRepository import BaseRepository

class InventoryRepository(BaseRepository):
    def __init__(self):
        super().__init__(Inventory)