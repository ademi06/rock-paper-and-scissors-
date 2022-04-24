import random


import time


def print_pause(message_display):
    # function to format messages displayed
    print(message_display)
    time.sleep(1)


def gen_message():
    # the first line messages printed to the screen
    print_pause("Let's play Rock, Paper & Scissors. Go!")
    print_pause("This game allows a round of 5")


class Player:
    # moves list to be selected
    moves = ['rock', 'paper', 'scissors']

    def __init__(self):
        # initialization function for the move function

        self.my_move = self.moves
        self.their_move = random.choice(self.moves)

    def move(self):
        # function to return rock when it is called

        return 'rock'

    def learn(self, my_move, their_move):
        # function to store the moves of players
        self.my_move = my_move
        self.their_move = their_move


class Random_player(Player):
    # Random player subclass

    def move(self):
        # random move
        return random.choice(self.moves)

    def learn(self, my_move, their_move):
        pass


class Human_player(Player):
    # Human player subclass

    def move(self):
        # display statements to player for selection
        # and validates the human input
        while True:
            human_input = input("Rock, Paper, scissors? >> ")
            if human_input.lower() in self.moves:
                return human_input
            else:
                print_pause("Wrong input, Try Again/n")

    def learn(self, my_move, their_move):
        pass


class Reflect_player(Player):
    # function to copy the players previous input

    def move(self):
        return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


class Cycle_player(Player):
    # choice of next move from the last round

    def move(self):
        if self.my_move == self.moves[0]:
            return self.moves[1]
        elif self.my_move == self.moves[1]:
            return self.moves[2]
        else:
            return self.moves[0]

    def learn(self, my_move, their_move):
        self.my_move = my_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        # players score initialization
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        # function to play round
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        # if statement to determine and display
        # the result of players in each rounds
        if beats(move1, move2):
            self.p1_score += 1
            win_message = '*** Player one wins this round ***'
        elif beats(move2, move1):
            self.p2_score += 1
            win_message = '*** Player two wins this round ***'
        elif (move1 == move2):
            self.p1_score += 0
            self.p2_score += 0
            win_message = '*** TIE ***'

        print(f"You played {move1}")
        print(f"Opponent played {move2}")
        print(f"{win_message}")
        print(f"Score: Player One {self.p1_score}, Player Two {self.p2_score}")

    def play_game(self):
        # function to intiate the start of the game
        print_pause("Game start!")
        gen_message()
        # a loop statement to execute the function 5 times
        for round in range(5):
            print_pause(f"Round {round}:")
            self.play_round()
        self.overall_winner()

    def overall_winner(self):
        # function to determine the overall winner and restart the game
        if self.p1_score > self.p2_score:
            print_pause('******* PLAYER ONE WINS THE GAME ******')
        elif self.p1_score < self.p2_score:
            print_pause('******* PLAYER TWO WINS THE GAME ******')
        elif self.p1_score == self.p2_score:
            print_pause('******* THE GAME ENDED IN TIE ******')
        self.continue_game()

    def continue_game(self):
        # function to repeat or quit the game
        cont_game = input(
            'Enter Play to play again or'
            ' Quit to quit the game? >> '
        )
        if "play" in cont_game.lower():
            self.p1_score = 0
            self.p2_score = 0
            game.play_game()

        elif "quit" in cont_game.lower():
            print_pause("Game over!")
            exit(0)


if __name__ == '__main__':
    # random selection of players to play against
    players = [
        Random_player(),
        Reflect_player(),
        Cycle_player()

    ]
    # organize the game with a human player
    p1 = Human_player()
    p2 = random.choice(players)
    game = Game(p1, p2)
    game.play_game()
