from mmorpg_app.repositories.CharacterQuestRepository import CharacterQuestRepository
from mmorpg_app.repositories.CharacterRepository import CharacterRepository
from mmorpg_app.repositories.GuildRepository import GuildRepository
from mmorpg_app.repositories.InventoryItemRepository import InventoryItemRepository
from mmorpg_app.repositories.InventoryRepository import InventoryRepository
from mmorpg_app.repositories.ItemRepository import ItemRepository
from mmorpg_app.repositories.MarketplaceRepository import MarketplaceRepository
from mmorpg_app.repositories.PlayerRepository import PlayerRepository
from mmorpg_app.repositories.QuestRepository import QuestRepository
from mmorpg_app.repositories.QuestRewardsItemRepository import QuestRewardsItemRepository

class RepositoryManager:
    def __init__(self):
        self.players = PlayerRepository()
        self.quests = QuestRepository()
        self.characters = CharacterRepository()
        self.guilds = GuildRepository()
        self.inventory = InventoryRepository()
        self.inventoryItems = InventoryItemRepository()
        self.marketplaces = MarketplaceRepository()
        self.questRewardsItems = QuestRewardsItemRepository()
        self.characterQuests = CharacterQuestRepository()
        self.items = ItemRepository()

