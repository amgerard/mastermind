class Guess:
    def __init__(self, guess, resp = (0, 0)):
        self.guess = guess
        self.num_black, self.num_white = resp
        self.score = 0

    def is_correct(self, code):
        return self.guess == code

    def is_valid(self, guess):
        return (self.num_black, self.num_white) == self.calc_repsonse(guess)

    def update_results_directly(self, results):
        self.num_black, self.num_white = results

    def update_results(self, code):
        self.num_black, self.num_white = self.calc_repsonse(code)

    def calc_repsonse(self, code):
        return (self.calc_num_black(code), self.calc_num_white(code))

    def calc_num_black(self, code):
        return sum([self.guess[i] == code[i] for i in range(len(code))])

    def calc_num_white(self, code):
        return len(Guess.intersect(self.guess, code)) - self.calc_num_black(code)

    def intersect(a, b):
        b = b[:]  # To prevent modifying the lists
        return [b.pop(b.index(i)) for i in a if i in b]

    def to_str(self):
        res = "%sB, %dW -> " % (self.num_black, self.num_white)
        g = [e.name for e in self.guess]
        return str(res) + str(g)