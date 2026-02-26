import math
import random
#Table matchup for calculating damage
TYPE_MATCHUP = {
    ('Normal', 'Normal'): 1, ('Normal', 'Fire'): 1, ('Normal', 'Water'): 1,
    ('Normal', 'Electric'): 1, ('Normal', 'Grass'): 1,
    ('Fire', 'Normal'): 1, ('Fire', 'Fire'): 0.5, ('Fire', 'Water'): 0.5,
    ('Fire', 'Electric'): 1, ('Fire', 'Grass'): 2,
    ('Water', 'Normal'): 1, ('Water', 'Fire'): 2, ('Water', 'Water'): 0.5,
    ('Water', 'Electric'): 1, ('Water', 'Grass'): 0.5,
    ('Electric', 'Normal'): 1, ('Electric', 'Fire'): 1, ('Electric', 'Water'): 2,
    ('Electric', 'Electric'): 0.5, ('Electric', 'Grass'): 0.5,
    ('Grass', 'Normal'): 1, ('Grass', 'Fire'): 0.5, ('Grass', 'Water'): 2,
    ('Grass', 'Electric'): 1, ('Grass', 'Grass'): 0.5,
}

# Using formula
def calculate_damage(move, attacker, defender):
    stab = 1.5 if move.type == attacker.type else 1.0
    type_eff = TYPE_MATCHUP.get((move.type, defender.type), 1.0)
    random_mult = random.uniform(0.5, 1.0)

    damage = (move.power * attacker.attack / defender.defense)
    damage *= stab * type_eff * random_mult

    return math.ceil(damage)


def execute_move(attacker, defender, move, team_name):
    damage = calculate_damage(move, attacker, defender)
    defender.take_damage(damage)
    attacker.use_move(move)

    print(f"{team_name}'s {attacker.name} cast '{move.name}' to {defender.name}:")
    print(f"Damage to {defender.name} is {damage} points.")

    if defender.is_fainted():
        print(f"Now {defender.name} faints back to poke ball, and {attacker.name} has {attacker.current_hp} HP.")
    else:
        print(f"Now {attacker.name} has {attacker.current_hp} HP, and {defender.name} has {defender.current_hp} HP.")
