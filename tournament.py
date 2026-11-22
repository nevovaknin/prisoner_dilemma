from play_game import play_game


# plays a round-robin tournament and returns the total score of each strategy
def play_tournament(strategies, games_per_pair, rounds_per_game, game):
    # start every strategy with 0 points, keyed by the function's name
    scores = {}
    for strategy in strategies:
        scores[strategy.__name__] = 0

    # go over every pair once: i is the first player, j is any strategy after it
    for i in range(len(strategies)):
        for j in range(i + 1, len(strategies)):
            for _ in range(games_per_pair):
                score_i, score_j = play_game(strategies[i], strategies[j], rounds_per_game, game)
                scores[strategies[i].__name__] += score_i
                scores[strategies[j].__name__] += score_j

    return scores
