import random


# The is let the computer think of a random number
# within a certain range, and challenge the user to guess the number.

number = random.randrange(1, 10)
player = int(input('Guess a number '))

print(player)
guess = "y"

while guess == "y":
    if player > number:
        print('Guess is too high')

    elif player< number:
        print('Guess is too low')

    elif player == number:
        print('Congratulations, you guessed right')
        guess == 'n'


    guess = input('do you want to continue y/n ')
