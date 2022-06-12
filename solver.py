import itertools
from color import Color


class Solver:
    def __init__(self, game) -> None:
        self.game = game
        self.all_possible_guesses = self.generate_all()

    def generate_s(self):
        all_guesses = self.all_possible_guesses
        return [g for g in all_guesses if self.game.is_valid(g)]

    def generate_all(self):
        l = [e for e in Color]
        a = [l for _ in range(self.game.N)]
        return [list(x) for x in itertools.product(*a)]