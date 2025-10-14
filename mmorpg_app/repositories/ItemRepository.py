from mmorpg_app.models import Item
from mmorpg_app.repositories.BaseRepository import BaseRepository

class ItemRepository(BaseRepository):
    def __init(self):
        super().__init__(Item)