from guess import Guess
from game_type import GameType
from analyst_player import AnalystPlayer
from adversary_player import AdversaryPlayer


class Game:
    N = 4

    def __init__(self, gameType):
        self.guesses = []
        self.test_guess: Guess = None
        self.gameType: GameType = gameType
        self.analystPlayer = AnalystPlayer(self)
        self.adversaryPlayer = AdversaryPlayer(self)

    def is_over(self):
        return len(self.guesses) > 0 and self.guesses[-1].num_black == self.N

    def play_round(self, verbose):
        guess = self.analystPlayer.get_guess()
        if verbose: print(guess.to_str())
        self.add_guess(guess)
        self.adversaryPlayer.update_guess_results()

    def is_valid(self, guess):
        test_guess = self.test_guess
        guesses = self.guesses if not test_guess else self.guesses + [test_guess]
        valid_guesses = all([g.is_valid(guess) for g in guesses])
        return valid_guesses

    def add_guess(self, guess):
        self.guesses.append(guess)