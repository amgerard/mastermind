import random
from guess import Guess
from color import Color
from simple_solver import SimpleSolver
from knuth_solver import KnuthSolver


class AnalystPlayer:
    def __init__(self, game):
        self.game = game

    def get_initial_guess(self):
        return [Color.White, Color.White, Color.Yellow, Color.Yellow]
        return [Color.White, Color.Yellow, Color.Blue, Color.Red]

    def get_guess(self):
        #return Guess([Color.Yellow,Color.Yellow, Color.Red, Color.Blue])
        if self.game.guesses == []: return Guess(self.get_initial_guess())
        return Guess(self.get_knuth_guess())
        return Guess(self.get_simple_guess())
        return Guess(self.get_max_entropy_guess())

    def get_max_entropy_guess(self):
        return [random.choice(list(Color)) for _ in range(self.game.N)]

    def get_simple_guess(self):
        solver = SimpleSolver(self.game)
        return solver.find_best_guess()

    def get_knuth_guess(self):
        solver = KnuthSolver(self.game)
        return solver.find_best_guess()