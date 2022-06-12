class MaxEntropySolver:
    def __init__(self, game) -> None:
        self.game = game

    def find_best_guess(self):
        best_entropy = 0
        best_guess = None
        for guess in self.get_possible_guesses():
            info_arr = []
            for response in self.get_possible_responses(guess):
                info_arr.append(self.calc_info(guess, response))
            entropy = sum(info_arr)
            if entropy < best_entropy: continue
            best_entropy = entropy
            best_guess = guess
        return best_guess

    def calc_info(self, guess, response):
        pass

    def calc_entropy(self, guess, response):
        pass

    def calc_message_probability(self, guess, response):
        pass

    def get_possible_guesses(self):
        pass

    def get_possible_responses(self, guess):
        pass