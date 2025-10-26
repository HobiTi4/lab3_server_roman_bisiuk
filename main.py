import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mmorpg_serverlab.settings')
django.setup()

from mmorpg_app.repositories.RepositoryManager import RepositoryManager

def main():
    repo = RepositoryManager()
    try:
        character_id_to_find = 3

        # 1. Отримуємо персонажа через репозиторій
        character = repo.characters.get_by_id(character_id_to_find)

        if not character:
            print(f"Персонажа з ID {character_id_to_find} не знайдено.")
            return

        print(f"--- Пошук квестів для персонажа: {character.name} ---")

        # 2. Використовуємо вбудований зворотний зв'язок Django.
        #    Оскільки у моделі CharacterQuest ви не вказали related_name
        #    для поля 'character', Django автоматично створює
        #    менеджер 'characterquest_set'.
        character_quests = character.characterquest_set.all()

        if not character_quests.exists():
            print(f"У {character.name} немає активних квестів.")
            return

        # 3. Перебираємо і виводимо
        for cq in character_quests:
            print(f"  -> Квест: {cq.quest.title} (Статус: {cq.status})")

    except Exception as e:
        print(f"Сталася помилка: {e}")
if __name__ == '__main__':
    main()
