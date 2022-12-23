from pathlib import Path

# read in the data file
data = Path("day2_input.txt").read_text().split("\n")

# Map the input tp a dictionary
map_inputs = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors', 'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}
points = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
game_result = {'Win': 6, 'Lose': 0, 'Draw': 3}

def rounds(game_input):
    opponent = map_inputs[game_input[0]]
    mine = map_inputs[game_input[2]]
    if opponent == mine:
        return game_result['Draw'] + points[mine]
    elif (opponent, mine) in [('Rock', 'Scissors'), ('Scissors', 'Paper'), ('Paper', 'Rock')]:
        return game_result['Lose'] + points[mine]
    else:
        return game_result['Win'] + points[mine]

results = []

for i in data:
    total = rounds(i)
    results.append(total)

print(sum(results))

# Part 2

new_mapping_inputs = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors', 'X': 'Lose', 'Y': 'Draw', 'Z': 'Win'}

def round2(game_input):
    opponent = map_inputs[game_input[0]]
    strategy = map_inputs[game_input[2]]