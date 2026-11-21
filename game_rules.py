COOPERATE = True
DEFECT = False

# payoff table: (player1_move, player2_move) -> (player1_points, player2_points)
points = {
    (COOPERATE, COOPERATE): (3, 3),
    (DEFECT, DEFECT): (1, 1),
    (COOPERATE, DEFECT): (0, 5),
    (DEFECT, COOPERATE): (5, 0),
}