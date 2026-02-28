import csv
import ast
from pokemon import Pokemon, Move

# Loads CSV into a Moves Class
def load_moves(filename):
    moves = {}
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            power = int(row['Power']) if row['Power'].isdigit() else 0
            moves[row['Name']] = Move(row['Name'], row['Type'], power)
    return moves

# Loads CSV + Moves Class into a Pokemon class
def load_pokemon(filename, moves):
    pokemon_list = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            p = Pokemon(
                row['Name'],
                row['Type'],
                int(row['HP']),
                int(row['Attack']),
                int(row['Defense'])
            )

            try:
                move_names = ast.literal_eval(row['Moves'])
            except:
                move_names = [m.strip().strip("'\"") for m in row['Moves'].strip("[]").split(",")]

            for name in move_names:
                if name in moves:
                    p.add_move(moves[name])

            pokemon_list.append(p)

    return pokemon_list
