strategy_file = open("strategy_guide.txt", "r")
content = strategy_file.read().splitlines()
strategy_file.close()

scores = {
    'A': 1, # Rock
    'B': 2, # Paper
    'C': 3, # Scissors
    'X': 1, # Rock
    'Y': 2, # Paper
    'Z': 3, # Scissors
}

opponent_score = 0
my_score = 0

for line in content:
    opponent_move = line[0]
    my_move = line[2]

    if scores[opponent_move] == scores[my_move]:
        opponent_score += 3 + scores[opponent_move]
        my_score += 3 + scores[my_move]
        print(f"Draw: {opponent_move} vs {my_move}")

    elif scores[opponent_move] == 1 and scores[my_move] == 3:
        opponent_score += 6 + scores[opponent_move]
        my_score += 0 + scores[my_move]
        print(f"Loss: {opponent_move} vs {my_move}")

    elif scores[opponent_move] == 2 and scores[my_move] == 1:
        opponent_score += 6 + scores[opponent_move]
        my_score += 0 + scores[my_move]
        print(f"Loss: {opponent_move} vs {my_move}")

    elif scores[opponent_move] == 3 and scores[my_move] == 2:
        opponent_score += 6 + scores[opponent_move]
        my_score += 0 + scores[my_move]
        print(f"Loss: {opponent_move} vs {my_move}")

    else:
        my_score += 6 + scores[my_move]
        opponent_score += 0 + scores[opponent_move]
        print(f"Win: {opponent_move} vs {my_move}")


alt_opponent_score = 0
alt_my_score = 0

for line in content:
    opponent_move = line[0]
    outcome = line[2]

    if outcome == 'X': # Loss
        if opponent_move == 'A': # Rock
          my_move = 'C' # Scissors
        elif opponent_move == 'B': # Paper
          my_move = 'A' # Rock
        elif opponent_move == 'C': # Scissors
          my_move = 'B' # Paper

        alt_opponent_score += 6 + scores[opponent_move]
        alt_my_score += 0 + scores[my_move]
        print(f"Loss: {opponent_move} vs {my_move}")

    elif outcome == 'Y': # Draw
        my_move = opponent_move
        alt_opponent_score += 3 + scores[opponent_move]
        alt_my_score += 3 + scores[my_move]

    elif outcome == 'Z': # Win
        if opponent_move == 'A': # Rock
          my_move = 'B' # Paper
        elif opponent_move == 'B': # Paper
          my_move = 'C' # Scissors
        elif opponent_move == 'C': # Scissors
          my_move = 'A' # Rock

        alt_my_score += 6 + scores[my_move]
        alt_opponent_score += 0 + scores[opponent_move]

print("== Strategy 1 ==")
print(f"Opponent score: {opponent_score}")
print(f"My score: {my_score}")
print("\n")
print("== Strategy 2 ==")
print(f"Opponent score: {alt_opponent_score}")
print(f"My score: {alt_my_score}")