from solver import Solver
from guess import Guess


class KnuthSolver(Solver):
    valid_guesses = []

    def find_best_guess(self):
        best_score = -1
        best_guess = []
        self.valid_guesses = self.generate_s()
        if len(self.valid_guesses) == 1:
            print("I Know it.")
            return self.valid_guesses[0]
        for i, g in enumerate(self.valid_guesses):
            score_i = self.calc_score(g)
            if score_i <= best_score: continue
            best_score = score_i
            best_guess = g
        self.game.test_guess = None
        return best_guess

    def calc_score(self, guess):
        bad = [g for g in self.game.guesses if g.is_correct(guess)]
        if bad: return -1
        guess_responses = self.get_valid_guess_responses(guess)
        scores = [self.calc_score_of_guess_response(g) for g in guess_responses]
        return min(scores)

    def calc_score_of_guess_response(self, guess_response):
        self.game.test_guess = guess_response
        return len(self.valid_guesses) - guess_response.score

    def get_valid_guess_responses(self, guess):
        resp_o = [0, 1, 2, 3, 4]
        options = [(i, j) for i in resp_o for j in resp_o if i + j < 5]
        poss_guesses = [Guess(guess, o) for o in options]
        valid_guesses = [g for g in poss_guesses if self.is_valid_guess_response(g)]
        return valid_guesses

    def is_valid_guess_response(self, guess):
        self.game.test_guess = guess
        #guess.score = len(self.generate_s()) # oh my :/
        guess.score = len(self.generate_s_prime()) # oh my :/
        return guess.score > 0

    def generate_s_prime(self):
        guesses = self.valid_guesses
        return [g for g in guesses if self.game.is_valid(g)]