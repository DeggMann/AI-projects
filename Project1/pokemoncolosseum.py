import random
from data_loader import load_moves, load_pokemon
from battle import execute_move
from AIplayer import AIPlayer

class PokemonColosseum:
    #initializes player and ai player
    def __init__(self):
        self.player_name = ""
        self.ai = AIPlayer()

    # Randomly selects pokemon and loads them into a team
    def setup_teams(self, all_pokemon, num_pokemon):
        selected = random.sample(all_pokemon, num_pokemon)
        return selected

    # Player chooses available moves
    def get_player_move(self, pokemon):
        while True:
            print(f"Choose the move for {pokemon.name}:")
            for i, move in enumerate(pokemon.moves, 1):
                label = move.name if move in pokemon.available_moves else f"{move.name} (N/A)"
                print(f"{i}. {label}")

            try:
                choice = int(input(f"Team {self.player_name}'s choice: "))
                move = pokemon.moves[choice - 1]
                if move in pokemon.available_moves:
                    return move
                print("That move is not available. Please choose another.")
            except:
                print("Invalid input. Please enter a number.")

    # Main Gameplay starts here
    def play(self):
        # Greeting
        print("Welcome to Pokemon Colosseum!")
        self.player_name = input("Enter Player Name: ")

        #CSV Parsing
        moves = load_moves('moves-data.csv')
        pokemon = load_pokemon('pokemon-data.csv', moves)

        # Team Initilization
        poknum = int(input("Enter how many pokemon per team: "))
        team_rocket = self.setup_teams(pokemon, poknum)
        team_player = self.setup_teams(pokemon, poknum)

        print(f"Team Rocket enters with {', '.join(p.name for p in team_rocket)}.")
        print(f"Team {self.player_name} enters with {', '.join(p.name for p in team_player)}.")
        print("Let the battle begin!")

        # Coin flip for first turn 
        rocket_turn = random.choice([True, False])
        print(
            "Coin toss goes to ----- Team Rocket to start the attack!"
            if rocket_turn
            else f"Coin toss goes to ----- Team {self.player_name} to start the attack!"
        )

        # Load Pokemon into a queue
        rocket_queue = team_rocket[:]
        player_queue = team_player[:]

        # Turn-based game logic
        while rocket_queue and player_queue:
            rocket = rocket_queue[0]
            player = player_queue[0]

            # Gameplay for AI player
            if rocket_turn:
                move = self.ai.choose_move(rocket, player)
                execute_move(rocket, player, move, "Team Rocket")
                if player.is_fainted():
                    player_queue.pop(0)
                    if not player_queue:
                        print(f"All of Team {self.player_name}'s Pokemon fainted, and Team Rocket prevails!")
                        return
                    print(f"Next for Team {self.player_name}, {player_queue[0].name} enters battle!")
            # Gameplay for player
            else:
                move = self.get_player_move(player)
                execute_move(player, rocket, move, f"Team {self.player_name}")
                if rocket.is_fainted():
                    rocket_queue.pop(0)
                    if not rocket_queue:
                        print(f"All of Team Rocket's Pokemon fainted, and Team {self.player_name} prevails!")
                        return
                    print(f"Next for Team Rocket, {rocket_queue[0].name} enters battle!")

            rocket_turn = not rocket_turn

def main():
    game = PokemonColosseum()
    game.play()

if __name__ == "__main__":
    main()