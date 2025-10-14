from mmorpg_app.repositories.BaseRepository import BaseRepository
from mmorpg_app.models import Character

class CharacterRepository(BaseRepository):
    def __init(self):
        super().__init__(Character)