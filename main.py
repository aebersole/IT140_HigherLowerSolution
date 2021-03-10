# Higher Lower Game - Complete

# Package import section for random generation and pauses
import random
import time

# User welcome and initial input section
user_name = input('What is your name? ')
print('Welcome to the higher/lower game ' + str(user_name) + '! \n')
time.sleep(1)
lower = int(input('Please enter the lower number: '))
upper = int(input('Please enter the upper number: '))

# Initial check loop to be sure that the higher number is actually higher then lower number
invalid = 1

while invalid == 1:
    if upper <= lower:
        print('Invalid entry, upper must be a higher number than lower. Please try again. \n')
        time.sleep(0.5)
        upper = int(input('What is the upper number? '))
        invalid = 1
    else:
        print('Got it, thanks! \n')
        time.sleep(1)
        invalid = 2

# Stores secret number and gets users first guess
secret = random.randint(int(lower), int(upper))
guess = int(input('Please enter a number between ' + str(lower) + ' and ' + str(upper) + ': '))

# Second check loop section to be sure user guess is between upper and lower numbers
badguess = 1

while badguess == 1:
    if int(guess) < int(lower) or int(guess) > int(upper):
        print('Invalid entry, guess must be between ' + str(lower) + ' and ' + str(upper) + '. Please try again.')
        time.sleep(0.5)
        guess = int(input('Please enter a number between ' + str(lower) + ' and ' + str(upper) + ': '))
        badguess = 1
    else:
        badguess = 2

# Guessing loop section that takes input and compares it to secret stored earlier
guessbreak = 1

while guessbreak == 1:
    if guess == secret:
        print(str(guess) + ' is correct, you win!')
        guessbreak = 2
    elif guess < secret:
        print('Too low, try going higher! \n')
        time.sleep(0.5)
        guess = int(input('Please enter a number between ' + str(lower) + ' and ' + str(upper) + ': '))
        guessbreak = 1
    elif guess > secret:
        print('Too high, try going lower! \n')
        time.sleep(0.5)
        guess = int(input('Please enter a number between ' + str(lower) + ' and ' + str(upper) + ': '))
        guessbreak = 1

