# Slot Machine Program
import random

def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐️']

    return [random.choice(symbols) for symbol in range(3)]


def print_row(row):
    print('************')
    print(' | '.join(row))
    print('************')

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return  bet * 20
    return 0


def main():
    balance = 100

    print('***********************')
    print('Welcome to python slots')
    print('Symbols: 🍒🍉🍋🔔⭐️')
    print('***********************')

    while balance > 0:
        print(f'Current balance: £{balance}')

        bet = input('Place your bet amount: ')

        if not bet.isdigit():
            print('You did not enter a valid amount!')
            continue

        bet = int(bet)

        if bet > balance:
            print('Insufficient funds')
            continue

        if bet <= 0:
            print('Bet must be greater than 0')
            continue

        balance -= bet

        row = spin_row()
        print('Spinning...\n')
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f'You won £{payout}')
        else:
            print('Sorry, you lost this round')

        balance += payout

        play_again = input("Do you want to play again ('y/n')").lower()

        if play_again != 'y':
            break

    print('*******************************************')
    print(f'Game Over! Your final balace is: £{balance}')
    print('*******************************************')


if __name__ == '__main__':
    main()
