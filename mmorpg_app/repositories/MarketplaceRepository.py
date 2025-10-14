from mmorpg_app.models import Marketplace
from mmorpg_app.repositories.BaseRepository import BaseRepository

class MarketplaceRepository(BaseRepository):
    def __init(self):
        super().__init__(Marketplace)