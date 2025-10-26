from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register(r'characters', views.CharacterViewSet, basename='character')
router.register(r'players', views.PlayerViewSet, basename='player')
router.register(r'guilds', views.GuildViewSet, basename='guild')
router.register(r'inventories', views.InventoryViewSet, basename='inventory')
router.register(r'items', views.ItemViewSet, basename='item')
router.register(r'inventory-items', views.InventoryItemViewSet, basename='inventoryitem')
router.register(r'quests', views.QuestViewSet, basename='quest')
router.register(r'quest-rewards', views.QuestRewardsItemViewSet, basename='questrewardsitem')
router.register(r'character-quests', views.CharacterQuestViewSet, basename='characterquest')
router.register(r'marketplace', views.MarketplaceViewSet, basename='marketplace')

urlpatterns = [
    path('', include(router.urls)),
    path('reports/guild-stats/', views.GuildStatsReportView.as_view(), name='guild-stats-report'),
]
