from mmorpg_app.models import Quest
from mmorpg_app.repositories.BaseRepository import BaseRepository

class QuestRepository(BaseRepository):
    def __init__(self):
        super().__init__(Quest)