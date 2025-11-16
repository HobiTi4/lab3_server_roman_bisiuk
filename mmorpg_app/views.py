from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import *
from .repositories.RepositoryManager import RepositoryManager
from rest_framework.views import APIView
from .models import QuestRewardsItem, InventoryItem, CharacterQuest

repo = RepositoryManager()

class BaseRepositoryViewSet(viewsets.ViewSet):
    repository = None
    serializer_class = None

    def list(self, request):
        items = self.repository.get_all()
        serializer = self.serializer_class(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        item = self.repository.get_by_id(pk)
        if item is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(item)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            new_item = self.repository.create(**serializer.validated_data)
            return Response(self.serializer_class(new_item).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            updated_item = self.repository.update(pk, **serializer.validated_data)
            if not updated_item:
                return Response(status=status.HTTP_404_NOT_FOUND)
            return Response(self.serializer_class(updated_item).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        updated_item = self.repository.update(pk, **request.data)
        if not updated_item:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(self.serializer_class(updated_item).data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        success = self.repository.delete(pk)
        if not success:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)

class CharacterViewSet(BaseRepositoryViewSet):
    repository = repo.characters
    serializer_class = CharacterSerializer

class PlayerViewSet(BaseRepositoryViewSet):
    repository = repo.players
    serializer_class = PlayerSerializer

class GuildViewSet(BaseRepositoryViewSet):
    repository = repo.guilds
    serializer_class = GuildSerializer

class InventoryViewSet(BaseRepositoryViewSet):
    repository = repo.inventory
    serializer_class = InventorySerializer

class ItemViewSet(BaseRepositoryViewSet):
    repository = repo.items
    serializer_class = ItemSerializer

class InventoryItemViewSet(BaseRepositoryViewSet):
    repository = repo.inventoryItems
    serializer_class = InventoryItemSerializer

class QuestViewSet(BaseRepositoryViewSet):
    repository = repo.quests
    serializer_class = QuestSerializer

class QuestRewardsItemViewSet(BaseRepositoryViewSet):
    repository = repo.questRewardsItems
    serializer_class = QuestRewardsItemSerializer

class CharacterQuestViewSet(BaseRepositoryViewSet):
    repository = repo.characterQuests
    serializer_class = CharacterQuestSerializer

class MarketplaceViewSet(BaseRepositoryViewSet):
    repository = repo.marketplaces
    serializer_class = MarketplaceSerializer

class GuildStatsReportView(APIView):
    def get(self, request, format=None):
        stats = repo.guilds.get_guild_statistics()
        return Response(stats, status=status.HTTP_200_OK)
