from game_rules import points
from strategies import tit_for_tat, always_defect, always_opposite
from play_game import play_game
from tournament import play_tournament

# game 1: tit for tat vs always opposite, 10 rounds -> (21, 26)
result = play_game(tit_for_tat, always_opposite, 10, points)
print(result)

# game 2: tit for tat vs always defect, 10 rounds -> (9, 14)
result2 = play_game(tit_for_tat, always_defect, 10, points)
print(result2)

# tournament: all three strategies, 1 game per pair, 10 rounds -> tit for tat 30, always defect 64, always opposite 26
print(play_tournament([tit_for_tat, always_defect, always_opposite], 1, 10, points))