from mmorpg_app.models import Guild
from mmorpg_app.repositories.BaseRepository import BaseRepository
from django.db.models import Count, Avg

class GuildRepository(BaseRepository):
    def __init__(self):
        super().__init__(Guild)

    def get_guild_statistics(self):
        return self.model.objects.annotate(
            member_count=Count('members'),
            average_level=Avg('members__level')
        ).values(
            'name',
            'city',
            'member_count',
            'average_level',
            'description'
        )