def play_game(strategy1, strategy2, rounds, game):
    history1 = []
    history2 = []
    score1 = 0
    score2 = 0

    for _ in range(rounds):
        move1 = strategy1(history1, history2)
        move2 = strategy2(history2, history1)
        payoff1, payoff2 = game[(move1, move2)]
        score1 += payoff1
        score2 += payoff2
        history1.append(move1)
        history2.append(move2)
    return score1, score2

