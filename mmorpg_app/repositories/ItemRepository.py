from mmorpg_app.models import Item
from mmorpg_app.repositories.BaseRepository import BaseRepository

class ItemRepository(BaseRepository):
    def __init__(self):
        super().__init__(Item)