from mmorpg_app.models import Guild
from mmorpg_app.repositories.BaseRepository import BaseRepository

class GuildRepository(BaseRepository):
    def __init(self):
        super().__init__(Guild)