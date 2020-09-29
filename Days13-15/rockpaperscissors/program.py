from actors import Roll, Person
import random


def print_header():
    print('---------------------------------')
    print('     ROCK, PAPER, SCISSORS')
    print('---------------------------------')

def build_three_rolls():
    rock = Roll('Rock')
    paper = Roll('Paper')
    scissor = Roll('Scissor')

    rock.rolls_which_can_be_defeated = scissor
    rock.rolls_which_can_defeat_me = paper
    paper.rolls_which_can_be_defeated = rock
    paper.rolls_which_can_defeat_me = scissor
    scissor.rolls_which_can_be_defeated = paper
    scissor.rolls_which_can_defeat_me = rock

    return [rock, paper, scissor]

def get_players_name():
    name = input('Hi, what is your name? ')
    return name


def game_loop(player1, player2, rolls):
    count = 1
    player1_score = 0
    player2_score = 0

    while count <= 3:
        player2_roll = random.choice(rolls)
        print(f'Round: {count}')
        entry = input('Do you choose [r]ock, [p]aper, or [s]cissor? ')

        name = None
        if entry == 'r':
            name = 'Rock'
        if entry == 'p':
            name = 'Paper'
        if entry == 's':
            name = 'Scissor'

        for r in rolls:
            if r.name == name:
                player1_roll = r
                break

        outcome = player1_roll.can_defeat(player2_roll)

        if outcome == 'yes':
            winner = f'{player1.name}'
            player1_score += 1
        elif outcome == 'no':
            winner = f'{player2.name}'
            player2_score += 1
        else:
            winner = 'Tie'
            player1_score += 1
            player2_score += 1

        print(f'{player1.name} rolled {player1_roll.name}. {player2.name} rolled {player2_roll.name}.')
        print(f'Winner of this round is {winner}')

        count += 1

    if player1_score > player2_score:
        print(f'Winner of the game is {player1.name}')
    elif player2_score > player1_score:
        print(f'Winner of the game is {player2.name}')
    else:
        print('There was a tie, please try again!')

def main():
    print_header()
    rolls = build_three_rolls()
    name = get_players_name()
    player1 = Person(name)
    player2 = Person('Computer')
    game_loop(player1, player2, rolls)

if __name__ == '__main__':
    main()








