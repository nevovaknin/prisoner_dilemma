from strategies import always_defect, tit_for_tat, always_opposite
from game_rules import COOPERATE, DEFECT, points
from play_game import play_game

# always defect tests
def test_always_defect_on_first_round():
    assert always_defect([], []) == DEFECT

def test_always_defect_ignores_history():
    assert always_defect([COOPERATE, COOPERATE], [COOPERATE, COOPERATE]) == DEFECT

# tit for tat tests
def test_tit_for_tat_cooperates_on_first_round():
    assert tit_for_tat([], []) == COOPERATE

def test_tit_for_tat_copies_defect():
    assert tit_for_tat([COOPERATE], [DEFECT]) == DEFECT

def test_tit_for_tat_copies_cooperate():
    assert tit_for_tat([DEFECT], [COOPERATE]) == COOPERATE
    
def test_tit_for_tat_looks_only_at_last_move():
    assert tit_for_tat([COOPERATE, COOPERATE], [DEFECT, COOPERATE]) == COOPERATE

# always opposite tests
def test_always_opposite_cooperates_on_first_round():
    assert always_opposite([], []) == COOPERATE

def test_always_opposite_flips_cooperate():
    assert always_opposite([COOPERATE], [COOPERATE]) == DEFECT

def test_always_opposite_flips_defect():
    assert always_opposite([DEFECT], [DEFECT]) == COOPERATE

# game test
def test_play_game_tit_for_tat_vs_always_opposite():
    assert play_game(tit_for_tat, always_opposite, 10, points) == (21, 26)

def test_play_game_tit_for_tat_vs_always_defect():
    assert play_game(tit_for_tat, always_defect, 10, points) == (9, 14)

def test_play_game_with_zero_rounds():
    assert play_game(tit_for_tat, always_defect, 0, points) == (0, 0)

