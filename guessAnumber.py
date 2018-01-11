import random



player = int(input('Guess a number '))
number = random.randrange(1, 10)
guess = "y"
print(player)

while guess == "y":
    if player > number:
    print('Guess is too high')

    elif player< number:

    print('Guess is too low')

    else:
    player = number
    print('Congratulations, you guessed right')

    guess = int(inpu)
