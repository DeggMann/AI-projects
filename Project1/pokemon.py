#Defines Pokemon and move set


class Move:
    def __init__(self, name, move_type, power):
        self.name = name
        self.type = move_type
        self.power = power
    
    def __str__(self):
        return self.name

# Pokemon Object 
class Pokemon:
    def __init__(self, name, poke_type, hp, attack, defense):
        self.name = name
        self.type = poke_type
        self.max_hp = hp
        self.current_hp = hp
        self.attack = attack
        self.defense = defense
        self.moves = []  # List of Move objects
        self.available_moves = []  # Moves that haven't been used yet
    

    def add_move(self, move):
        self.moves.append(move)
        self.available_moves.append(move)
    
    def use_move(self, move):
        if move in self.available_moves:
            self.available_moves.remove(move)
        
        # If all moves have been used, reset available moves
        if len(self.available_moves) == 0:
            self.available_moves = self.moves.copy()
    
    def take_damage(self, damage):
        self.current_hp -= damage
        if self.current_hp < 0:
            self.current_hp = 0
    
    def is_fainted(self):
        return self.current_hp <= 0
    
    def __str__(self):
        return self.name