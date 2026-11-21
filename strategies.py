from game_rules import COOPERATE

# every strategy gets both histories and returns the next move
#defining always defect strat
def always_defect(my_history, opponent_history):
    return False

# defining tit for tat strat
def tit_for_tat(my_history, opponent_history):
    if len(opponent_history) == 0:
        return COOPERATE
    return opponent_history[-1]

# cooperates first, then plays the opposite of the opponent's last move
def always_opposite(my_history, opponent_history):
    if len(opponent_history) == 0:
        return COOPERATE
    return not opponent_history[-1]
