import random

guesses = ['heads', 'tails']
print('Guess the coin toss! Enter heads or tails:')
guess = input().lower()
toss = random.choice(guesses)
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')