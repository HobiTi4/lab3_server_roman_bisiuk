from mmorpg_app.models import CharacterQuest
from mmorpg_app.repositories.BaseRepository import BaseRepository

class CharacterQuestRepository(BaseRepository):
    def __init__(self):
        super().__init__(CharacterQuest)
