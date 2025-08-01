import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = input('Enter the number of players (2-4): ')
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break

max_score = 150
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:

    for player_idx in range(players):
        print('\nPlayer number', player_idx + 1, 'Turn has just started\n')
        print('Your total score is:', player_scores[player_idx], '\n')
        current_score = 0

        while True:
            should_roll = input('Would you like to roll (y)? ')
            if should_roll.lower() != 'y':
                break

            value = roll()
            if value == 1:
                print('You rolled 1! Turn Done!')
                current_score = 0
                break
            else:
                current_score += value
                print(f'You rolled a: {value}')

            print(f'Your current score is {current_score}')

        player_scores[player_idx] += current_score
        print('Your total score is:', player_scores[player_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print('Player number', winning_idx + 1, 'is the winner with a score of:',max_score)






