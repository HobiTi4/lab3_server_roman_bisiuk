from mmorpg_app.models import Guild
from mmorpg_app.repositories.BaseRepository import BaseRepository

class GuildRepository(BaseRepository):
    def __init__(self):
        super().__init__(Guild)