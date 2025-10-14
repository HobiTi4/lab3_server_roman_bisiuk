import django
import os
from mmorpg_app.repositories.RepositoryManager import RepositoryManager

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mmorpg_serverlab.settings')
django.setup()

def main():
    repo = RepositoryManager()
    player = repo.players.create(username = "lockinchik", email = "mykola_shclyarow2006@gmail.com", password_hash = "hfd123f")
    print(f"Player {player.username} created successfully")

    print("Getting all players")
    for p in repo.players.get_all():
        print("-", p.username, "|", p.email)

if __name__ == '__main__':
    main()
