from random import randint
from ProgressBar import progressBar

# MonteCarlo.py
# This program uses a Monte Carlo approach to estimate the probability of winning the dice game "Approach" with different
# "hold" values.
# Recall that approach works like this:
# Both players agree on a limit n.
# Player 1 rolls first. They go until they either exceed n or hold.
# Then player 2 rolls. They go until they either exceed n or beat player 1's score.
# The player who is closest to n without going over wins.
# Note:
# We can reduce this to the problem of player 1 choosing the best value at which to hold.
# This is called a policy; once we know the best number to hold at, we can act optimally.

# To estimate the best number to hold at, we'll try to estimate the probability of winning
# for each possible hold value between n-5 and n.
# Once we have this, we will know which hold value to use for our strategy.

# This function should try each possible hold value 1000000 times. For each time, play a random
# game. If Player 1 wins, increment the appropriate value in the win_table dictionary.

# n is the limit.

def monte_carlo_approach(n) :
    win_table = {}
    for i in range(n-5,n+1) :
        win_table[i] = 0

    for hold_val in range(n-5,n+1):
        print(f"\nStarting simulations for hold_val = {hold_val}")
        for i in range(100000):
            # player 1 plays
            player1_score = 0
            while player1_score < hold_val:
                player1_score += randint(1,6)
            
            if player1_score > n:
                continue

            # player 2 plays
            player2_score = 0
            while player2_score <= player1_score:
                player2_score += randint(1,6)
            
            if player2_score > n or player2_score <= player1_score:
                win_table[hold_val] += 1

            progressBar(i, 100000)
        
    print("\n\n")
    for item in win_table.keys() :
        print("%d: %f" % (item, win_table[item]/100000))
    
if __name__ == "__main__":
    monte_carlo_approach(100)
