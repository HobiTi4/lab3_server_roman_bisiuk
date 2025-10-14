from mmorpg_app.repositories.BaseRepository import BaseRepository
from mmorpg_app.models import Player

class PlayerRepository(BaseRepository):
    def __init__(self):
        super().__init__(Player)
