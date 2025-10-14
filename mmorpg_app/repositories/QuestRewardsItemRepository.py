from mmorpg_app.models import QuestRewardsItem
from mmorpg_app.repositories.BaseRepository import BaseRepository

class QuestRewardsItemRepository(BaseRepository):
    def __init__(self):
        super().__init__(QuestRewardsItem)