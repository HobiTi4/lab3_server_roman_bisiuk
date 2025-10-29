from django.db import models

class Player(models.Model):
    player_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=100, unique=True)
    password_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'player'

    def __str__(self):
        return self.username


class Guild(models.Model):
    guild_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guild'

    def __str__(self):
        return self.name


class Character(models.Model):
    character_id = models.AutoField(primary_key=True)
    player = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='characters')
    guild = models.ForeignKey('Guild', on_delete=models.SET_NULL, blank=True, null=True, related_name='members')
    name = models.CharField(max_length=20)
    level = models.IntegerField(default=1)
    gold = models.IntegerField(default=0)
    class_name = models.CharField(db_column='class', max_length=20, blank=True, null=True)
    role = models.CharField(max_length=9, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'character'

    def __str__(self):
        return f"{self.name} (Lvl {self.level})"


class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    rarity = models.CharField(max_length=9)

    class Meta:
        managed = False
        db_table = 'item'

    def __str__(self):
        return f"{self.name} [{self.rarity}]"


class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    character = models.ForeignKey('Character', on_delete=models.CASCADE, related_name='inventories')
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventory'

    def __str__(self):
        return f"{self.character.name}'s Inventory: {self.name or 'Default'}"


class InventoryItem(models.Model):
    inventory_item_id = models.AutoField(primary_key=True)
    inventory = models.ForeignKey('Inventory', on_delete=models.CASCADE, related_name='items')
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        managed = False
        db_table = 'inventory_item'
        unique_together = (('inventory', 'item'),)

    def __str__(self):
        return f"{self.item.name} x{self.quantity}"


class Quest(models.Model):
    quest_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    reward_gold = models.IntegerField(default=0)

    class Meta:
        managed = False
        db_table = 'quest'

    def __str__(self):
        return self.title


class QuestRewardsItem(models.Model):
    quest = models.ForeignKey('Quest', on_delete=models.CASCADE, primary_key=True)
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        managed = False
        db_table = 'quest_rewards_item'
        unique_together = (('quest', 'item'),)

    def __str__(self):
        return f"{self.item.name} x{self.quantity} (Reward for {self.quest.title})"


class CharacterQuest(models.Model):
    character = models.ForeignKey('Character', on_delete=models.CASCADE, primary_key=True)
    quest = models.ForeignKey('Quest', on_delete=models.CASCADE)
    status = models.CharField(max_length=9, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'character_quest'
        unique_together = (('character', 'quest'),)

    def __str__(self):
        return f"{self.character.name} - {self.quest.title} ({self.status})"


class Marketplace(models.Model):
    marketplace_id = models.AutoField(primary_key=True)
    inventory_item = models.ForeignKey('InventoryItem', on_delete=models.CASCADE)
    character = models.ForeignKey('Character', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=8, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'marketplace'

    def __str__(self):
        return f"{self.item_name()} - {self.price} gold"

    def item_name(self):
        return self.inventory_item.item.name