#!/usr/bin/env python3

import random
import sys

def run_round():
    moves: dict = {'rock': "ROK", 'paper': 'PAPE', 'scissors': 'SKIZZAS'}
    valid_moves: list[str] = list(moves.keys())
    while True:

        user_move: str = input("Rock, paper, or scissors? >> ").lower()

        if user_move == 'exit':
            print('Thanks for playing, playa.')
            sys.exit()

        if user_move not in valid_moves:
            print("Invalid move...")
            continue

        ai_move: str = random.choice(valid_moves)
        print("----")
        print(f"You: {moves[user_move]}")
        print(f"AI: {moves[ai_move]}")
        print("----")

        #check moves
        if user_move == ai_move:
            print('It is a tie!')
            return False

        elif user_move == 'rock' and ai_move == 'scissors':
            print("You Win!")
            return True

        elif user_move == 'scissors' and ai_move == 'paper':
            print("You Win!")
            return True

        elif user_move == 'paper' and ai_move == 'rock':
            print("You Win!")
            return True

        else:
            print("AI wins...WompWomp")
            return False

print("welcome to RPS, to beat the game, win three times. If you want to give up, type exit")
wins = 0
losses = 0
rounds = 0
while True:

    if run_round() == True: wins += 1
    else: losses += 1

    if wins == 3:
        print(f"Congrats, you won in {wins + losses} rounds, {wins}-{losses}.")
        sys.exit()
    else:
        continue
