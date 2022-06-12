from solver import Solver


class SimpleSolver(Solver):
    def find_best_guess(self):
        possibles = self.generate_s()
        print(len(possibles))
        return possibles[0]