import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mmorpg_serverlab.settings')
django.setup()

from mmorpg_app.repositories.RepositoryManager import RepositoryManager

def main():
    repo = RepositoryManager()
    print("Creating player: \n ")
    #player = repo.players.create(username = "lockinchik", email = "mykola_shclyarow2006@gmail.com", password_hash = "hfd123f")
    #print(f"Player {player.username} created successfully")

    print("\n Getting all players \n")
    for p in repo.players.get_all():
        print("-", p.username, "|", p.email)

    print("\n Getting player by id: \n")
    id = 9
    player = repo.players.get_by_id(id)
    print(f"Player with id: {id} found successfully! \n {player}")

    print("\n Updating player: \n")

    player = repo.players.update(id, username = "full4Focus")
    print(f"Player with id: {id} updated successfully! \n {player}")

    print("\n Deleting player: \n")
    player = repo.players.delete(id)
    print(f"Player with id: {id} deleted successfully! \n {player}")

    print("\n List of current players: \n")
    for p in repo.players.get_all():
        print("-", p.username, "|", p.email)
if __name__ == '__main__':
    main()
