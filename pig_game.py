import random


# Function to roll a die (1-6)
def roll():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)


# Get the number of players (must be between 2 and 4)
while True:
    players = input('Enter the number of players (2-4): ')
    if players.isdigit():  # Check if input is a number
        players = int(players)
        if 2 <= players <= 4:
            break  # Valid input, exit loop
        else:
            print('Must be between 2-4 players.')
    else:
        print('Invalid input, please enter a number.')

# Game settings
max_score = 50  # Winning score threshold
player_scores = [0 for _ in range(players)]  # Initialize scores for each player

# Main game loop - continues until a player reaches max_score
while max(player_scores) < max_score:
    for player_idx in range(players):
        print('\nPlayer', player_idx + 1, "turn has just started!\n")
        print('Your total score is:', player_scores[player_idx], '\n')

        current_score = 0  # Reset current score for this turn

        # Turn loop: player rolls until they choose to stop or roll a 1
        while True:
            should_roll = input('Would you like to roll (y)? ')
            if should_roll.lower() != 'y':  # Stop rolling if player inputs anything other than 'y'
                break

            value = roll()  # Roll the die
            if value == 1:
                print('You rolled a 1! Turn done!')
                current_score = 0  # Reset current score to 0
                break
            else:
                current_score += value  # Add roll value to current score
                print('You rolled a:', value)

            print('Your score this turn is:', current_score)

        # Add current turn's score to player's total
        player_scores[player_idx] += current_score
        print('Your total score is:', player_scores[player_idx])

# Determine the winner (player with the highest score)
max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print('\nPlayer number', winning_idx + 1, 'is the winner with a score of:', max_score)
