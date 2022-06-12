from game import Game
from game_type import GameType


def play_game(gameType, verbose = False):
    game = Game(gameType)
    if verbose:
        print("Code:")
        print(game.adversaryPlayer.code)
    while not game.is_over():
        game.play_round(verbose)
        if not verbose: continue
        print("Guess #%s:" % len(game.guesses))
        print(game.guesses[-1].to_str())
    return len(game.guesses)


if __name__ == "__main__":
    # yellow, green, blue, black
    gameType = GameType.PlayerAnalyst
    #gameType = GameType.Computer
    while True:
        print(play_game(gameType, True))