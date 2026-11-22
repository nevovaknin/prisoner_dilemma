# Prisoner's Dilemma

A simple Python implementation of the iterated prisoner's dilemma. Two strategies play a number of rounds against each other, and the total score of each player is returned. A round-robin tournament between several strategies is also included.

## The game

Each round, both players choose to cooperate or defect. The payoffs are:

| Player 1  | Player 2  | Player 1 payoff | Player 2 payoff |
|-----------|-----------|-----------------|-----------------|
| Cooperate | Cooperate | 3               | 3               |
| Cooperate | Defect    | 0               | 5               |
| Defect    | Cooperate | 5               | 0               |
| Defect    | Defect    | 1               | 1               |

## Files

- `game_rules.py` - the two moves (`COOPERATE = True`, `DEFECT = False`) and the payoff table `points`
- `strategies.py` - the strategies: `always_defect`, `tit_for_tat`, `always_opposite`
- `play_game.py` - `play_game(strategy1, strategy2, rounds, game)`, plays a game and returns both scores
- `tournament.py` - `play_tournament(strategies, games_per_pair, rounds_per_game, game)`, plays a round-robin tournament and returns the total score of each strategy
- `run_games.py` - runs two example games and a tournament, and prints the results
- `test_all.py` - tests for the strategies, `play_game` and `play_tournament`

## How it works

A strategy is a function that takes two lists, the history of its own moves and the history of the opponent's moves, and returns its next move (`True` for cooperate, `False` for defect).

The strategies:

- `always_defect` - always defects
- `tit_for_tat` - cooperates on the first round, then copies the opponent's last move
- `always_opposite` - cooperates on the first round, then plays the opposite of the opponent's last move

The game is a dictionary that maps a pair of moves to a pair of payoffs, for example `(COOPERATE, DEFECT)` gives `(0, 5)`.

## Usage

```python
from game_rules import points
from strategies import tit_for_tat, always_defect, always_opposite
from play_game import play_game
from tournament import play_tournament

# play one game: returns the total score of each player
play_game(tit_for_tat, always_defect, 10, points)  # (9, 14)

# play a tournament: every strategy plays every other strategy
play_tournament([tit_for_tat, always_defect, always_opposite], 1, 10, points)
# {'tit_for_tat': 30, 'always_defect': 64, 'always_opposite': 26}
```

## Running the examples

```
python3 run_games.py
```

The results are reproducible, because none of the strategies use randomness:

- tit for tat vs always opposite, 10 rounds: (21, 26)
- tit for tat vs always defect, 10 rounds: (9, 14)
- tournament of the three strategies, 1 game per pair, 10 rounds: tit for tat 30, always defect 64, always opposite 26

## Running the tests

The tests are in `test_all.py`. Run them from the project folder with:

```
pytest -v
```
