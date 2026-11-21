from game_rules import points
from strategies import tit_for_tat, always_defect, always_opposite
from play_game import play_game

result = play_game(tit_for_tat, always_opposite, 10, points)
print(result)

result2 = play_game(tit_for_tat, always_defect, 10, points)
print(result2)
