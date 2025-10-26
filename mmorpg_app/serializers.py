from rest_framework import serializers
from.models import *

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        exclude = ['password_hash']

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = '__all__'

class GuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guild
        fields = '__all__'

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'

class MarketplaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marketplace
        fields = '__all__'

class QuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quest
        fields = '__all__'

class QuestRewardsItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestRewardsItem
        fields = '__all__'

class CharacterQuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterQuest
        fields = '__all__'