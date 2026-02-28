from battle import calculate_damage

#Ai choosing best move based on max damage instead of random
class AIPlayer:
    def choose_move(self, attacker, defender):
        best_move = None
        max_damage = -1

        for move in attacker.available_moves:
            damage = calculate_damage(move, attacker, defender)
            if damage > max_damage:
                max_damage = damage
                best_move = move

        return best_move
