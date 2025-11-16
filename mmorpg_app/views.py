from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import *
from .repositories.RepositoryManager import RepositoryManager
from rest_framework.views import APIView
from .models import QuestRewardsItem, InventoryItem, CharacterQuest

repo = RepositoryManager()
class CharacterViewSet(viewsets.ViewSet):
    def list(self, request):
        characters = repo.characters.get_all()
        serializer = CharacterSerializer(characters, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        character = repo.characters.get_by_id(pk)
        if character is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CharacterSerializer(character)
        return Response(serializer.data)

    def create(self, request):
        serializer = CharacterSerializer(data=request.data)
        if serializer.is_valid():
            new_character = repo.characters.create(**serializer.validated_data)
            return Response(CharacterSerializer(new_character).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        serializer = CharacterSerializer(data=request.data)
        if serializer.is_valid():
            updated_character = repo.characters.update(pk, **serializer.validated_data)
            if not updated_character:
                return Response(status=status.HTTP_404_NOT_FOUND)
            return Response(CharacterSerializer(updated_character).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        updated_character = repo.characters.update(pk, **request.data)
        if not updated_character:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(CharacterSerializer(updated_character).data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        success = repo.characters.delete(pk)
        if not success:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)


class PlayerViewSet(viewsets.ViewSet):
    def list(self, request):
        players = repo.players.get_all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        player = repo.players.get_by_id(pk)
        if player is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PlayerSerializer(player)
        return Response(serializer.data)

    def create(self, request):
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            new_player = repo.players.create(**serializer.validated_data)
            return Response(PlayerSerializer(new_player).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            updated_player = repo.players.update(pk, **serializer.validated_data)
            if not updated_player:
                return Response(status=status.HTTP_404_NOT_FOUND)
            return Response(PlayerSerializer(updated_player).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        updated_player = repo.players.update(pk, **request.data)
        if not updated_player:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(PlayerSerializer(updated_player).data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        success = repo.players.delete(pk)
        if not success:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)


class GuildViewSet(viewsets.ViewSet):
    def list(self, request):
        guilds = repo.guilds.get_all()
        serializer = GuildSerializer(guilds, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        guild = repo.guilds.get_by_id(pk)
        if guild is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = GuildSerializer(guild)
        return Response(serializer.data)

    def create(self, request):
        serializer = GuildSerializer(data=request.data)
        if serializer.is_valid():
            new_guild = repo.guilds.create(**serializer.validated_data)
            return Response(GuildSerializer(new_guild).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        serializer = GuildSerializer(data=request.data)
        if serializer.is_valid():
            updated_guild = repo.guilds.update(pk, **serializer.validated_data)
            if not updated_guild:
                return Response(status=status.HTTP_404_NOT_FOUND)
            return Response(GuildSerializer(updated_guild).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        updated_guild = repo.guilds.update(pk, **request.data)
        if not updated_guild:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(GuildSerializer(updated_guild).data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        success = repo.guilds.delete(pk)
        if not success:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)


class InventoryViewSet(viewsets.ViewSet):
    def list(self, request):
        inventory = repo.inventory.get_all()
        serializer = InventorySerializer(inventory, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        inventory = repo.inventory.get_by_id(pk)
        if inventory is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = InventorySerializer(inventory)
        return Response(serializer.data)

    def create(self, request):
        serializer = InventorySerializer(data=request.data)
        if serializer.is_valid():
            new_inventory = repo.inventory.create(**serializer.validated_data)
            return Response(InventorySerializer(new_inventory).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        serializer = InventorySerializer(data=request.data)
        if serializer.is_valid():
            updated_inventory = repo.inventory.update(pk, **serializer.validated_data)
            if not updated_inventory:
                return Response(status=status.HTTP_404_NOT_FOUND)
            return Response(InventorySerializer(updated_inventory).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        updated_inventory = repo.inventory.update(pk, **request.data)
        if not updated_inventory:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(InventorySerializer(updated_inventory).data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        success = repo.inventory.delete(pk)
        if not success:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ItemViewSet(viewsets.ViewSet):
    def list(self, request):
        items = repo.items.get_all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        item = repo.items.get_by_id(pk)
        if item is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    def create(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            new_item = repo.items.create(**serializer.validated_data)
            return Response(ItemSerializer(new_item).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            updated_item = repo.items.update(pk, **serializer.validated_data)
            if not updated_item:
                return Response(status=status.HTTP_404_NOT_FOUND)
            return Response(ItemSerializer(updated_item).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        updated_item = repo.items.update(pk, **request.data)
        if not updated_item:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(ItemSerializer(updated_item).data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        success = repo.items.delete(pk)
        if not success:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)


class QuestViewSet(viewsets.ViewSet):
    def list(self, request):
        quests = repo.quests.get_all()
        serializer = QuestSerializer(quests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        quest = repo.quests.get_by_id(pk)
        if quest is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = QuestSerializer(quest)
        return Response(serializer.data)

    def create(self, request):
        serializer = QuestSerializer(data=request.data)
        if serializer.is_valid():
            new_quest = repo.quests.create(**serializer.validated_data)
            return Response(QuestSerializer(new_quest).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        serializer = QuestSerializer(data=request.data)
        if serializer.is_valid():
            updated_quest = repo.quests.update(pk, **serializer.validated_data)
            if not updated_quest:
                return Response(status=status.HTTP_404_NOT_FOUND)
            return Response(QuestSerializer(updated_quest).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        updated_quest = repo.quests.update(pk, **request.data)
        if not updated_quest:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(QuestSerializer(updated_quest).data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        success = repo.quests.delete(pk)
        if not success:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)


class MarketplaceViewSet(viewsets.ViewSet):
    def list(self, request):
        listings = repo.marketplaces.get_all()
        serializer = MarketplaceSerializer(listings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        listing = repo.marketplaces.get_by_id(pk)
        if listing is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MarketplaceSerializer(listing)
        return Response(serializer.data)

    def create(self, request):
        serializer = MarketplaceSerializer(data=request.data)
        if serializer.is_valid():
            new_listing = repo.marketplaces.create(**serializer.validated_data)
            return Response(MarketplaceSerializer(new_listing).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        serializer = MarketplaceSerializer(data=request.data)
        if serializer.is_valid():
            updated_listing = repo.marketplaces.update(pk, **serializer.validated_data)
            if not updated_listing:
                return Response(status=status.HTTP_404_NOT_FOUND)
            return Response(MarketplaceSerializer(updated_listing).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        updated_listing = repo.marketplaces.update(pk, **request.data)
        if not updated_listing:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(MarketplaceSerializer(updated_listing).data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        success = repo.marketplaces.delete(pk)
        if not success:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)


class InventoryItemViewSet(viewsets.ViewSet):
    def list(self, request):
        inventory_items = repo.inventoryItems.get_all()
        serializer = InventoryItemSerializer(inventory_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        inventory_item = repo.inventoryItems.get_by_id(pk)
        if inventory_item is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = InventoryItemSerializer(inventory_item)
        return Response(serializer.data)

    def create(self, request):
        serializer = InventoryItemSerializer(data=request.data)
        if serializer.is_valid():
            new_item = repo.inventoryItems.create(**serializer.validated_data)
            return Response(InventoryItemSerializer(new_item).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        serializer = InventoryItemSerializer(data=request.data)
        if serializer.is_valid():
            updated_item = repo.inventoryItems.update(pk, **serializer.validated_data)

            if not updated_item:
                return Response(status=status.HTTP_404_NOT_FOUND)

            return Response(InventoryItemSerializer(updated_item).data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        updated_item = repo.inventoryItems.update(pk, **request.data)
        if not updated_item:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(InventoryItemSerializer(updated_item).data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        success = repo.inventoryItems.delete(pk)
        if not success:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_204_NO_CONTENT)


class QuestRewardsItemViewSet(viewsets.ViewSet):
    def list(self, request):
        items = repo.questRewardsItems.get_all()
        serializer = QuestRewardsItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        quest_id = pk
        item_id = request.query_params.get('item_id')

        if item_id:
            reward = get_object_or_404(QuestRewardsItem, quest_id=quest_id, item_id=item_id)
            serializer = QuestRewardsItemSerializer(reward)
            return Response(serializer.data)
        else:
            rewards = QuestRewardsItem.objects.filter(quest_id=quest_id)
            serializer = QuestRewardsItemSerializer(rewards, many=True)
            return Response(serializer.data)

    def create(self, request):
        serializer = QuestRewardsItemSerializer(data=request.data)
        if serializer.is_valid():
            new_item = repo.questRewardsItems.create(**serializer.validated_data)
            return Response(QuestRewardsItemSerializer(new_item).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        item_id = request.data.get('item_id')
        if not item_id:
            return Response({"error": "item_id required in body"}, status=status.HTTP_400_BAD_REQUEST)

        rows = QuestRewardsItem.objects.filter(quest_id=pk, item_id=item_id).update(**request.data)
        if rows == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response({"status": "Updated", "quest": pk, "item": item_id}, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        item_id = request.data.get('item_id')
        if not item_id:
            return Response({"error": "item_id required in body"}, status=status.HTTP_400_BAD_REQUEST)

        rows = QuestRewardsItem.objects.filter(quest_id=pk, item_id=item_id).update(**request.data)
        if rows == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response({"status": "Updated", "quest": pk, "item": item_id}, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        item_id = request.query_params.get('item_id')
        if not item_id:
            return Response({"error": "Provide ?item_id=X to delete"}, status=status.HTTP_400_BAD_REQUEST)

        deleted, _ = QuestRewardsItem.objects.filter(quest_id=pk, item_id=item_id).delete()
        if deleted == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)


class CharacterQuestViewSet(viewsets.ViewSet):
    def list(self, request):
        items = repo.characterQuests.get_all()
        serializer = CharacterQuestSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        character_id = pk
        quest_id = request.query_params.get('quest_id')  # або просто quest

        if quest_id:
            cq = get_object_or_404(CharacterQuest, character_id=character_id, quest_id=quest_id)
            serializer = CharacterQuestSerializer(cq)
            return Response(serializer.data)
        else:
            cqs = CharacterQuest.objects.filter(character_id=character_id)
            serializer = CharacterQuestSerializer(cqs, many=True)
            return Response(serializer.data)

    def create(self, request):
        serializer = CharacterQuestSerializer(data=request.data)
        if serializer.is_valid():
            new_item = repo.characterQuests.create(**serializer.validated_data)
            return Response(CharacterQuestSerializer(new_item).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        # pk = character_id
        quest_id = request.data.get('quest_id') or request.data.get('quest')
        if not quest_id:
            return Response({"error": "quest_id required in body"}, status=status.HTTP_400_BAD_REQUEST)

        rows = CharacterQuest.objects.filter(character_id=pk, quest_id=quest_id).update(**request.data)
        if rows == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response({"status": "Updated"}, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        quest_id = request.data.get('quest_id') or request.data.get('quest')
        if not quest_id:
            return Response({"error": "quest_id required in body"}, status=status.HTTP_400_BAD_REQUEST)

        rows = CharacterQuest.objects.filter(character_id=pk, quest_id=quest_id).update(**request.data)
        if rows == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response({"status": "Updated"}, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        quest_id = request.query_params.get('quest_id')
        if not quest_id:
            return Response({"error": "Provide ?quest_id=X to delete"}, status=status.HTTP_400_BAD_REQUEST)

        deleted, _ = CharacterQuest.objects.filter(character_id=pk, quest_id=quest_id).delete()
        if deleted == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)


class GuildStatsReportView(APIView):
    def get(self, request, format=None):
        stats = repo.guilds.get_guild_statistics()
        return Response(stats, status=status.HTTP_200_OK)
