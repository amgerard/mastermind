from color import Color
from game_type import GameType
import random


class AdversaryPlayer:
    def __init__(self, game):
        self.game = game
        self.code = self.get_code()

    def get_code(self):
        #return [Color.Yellow, Color.Green, Color.Blue, Color.Black]
        return [random.choice(list(Color)) for _ in range(self.game.N)]

    def update_guess_results(self):
        guess = self.game.guesses[-1]
        if self.game.gameType == GameType.PlayerAnalyst:
            response = input("Enter results from guess: ")
            res = [int(x) for x in response.split(',')]
            guess.update_results_directly(res)
            return
        guess.update_results(self.code)