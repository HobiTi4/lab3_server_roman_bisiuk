import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mmorpg_serverlab.settings')
django.setup()

from mmorpg_app.repositories.RepositoryManager import RepositoryManager

def main():
    repo = RepositoryManager()
    try:
        character_id_to_find = 3

        character = repo.characters.get_by_id(character_id_to_find)

        if not character:
            print(f"Персонажа з ID {character_id_to_find} не знайдено.")
            return

        print(f"--- Пошук квестів для персонажа: {character.name} ---")

        character_quests = character.characterquest_set.all()

        if not character_quests.exists():
            print(f"У {character.name} немає активних квестів.")
            return

        for cq in character_quests:
            print(f"  -> Квест: {cq.quest.title} (Статус: {cq.status})")

    except Exception as e:
        print(f"Сталася помилка: {e}")
if __name__ == '__main__':
    main()
