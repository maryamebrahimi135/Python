import random

computer_num = random.randint(1, 101)

print('Hi! Welcome to Guess the Number Game!\nI choose a number between 1 and 100. You must guess it!!!!!!')

while True:
    guess_num = int(input('Please enter your guess number: '))
    if guess_num >= 0 and guess_num <= 100:
        if guess_num > computer_num:
            print('Your guess is too high!!!!')
        elif guess_num  < computer_num:
            print('Your guess is too low!!!')
        else:
            break
    else:
        print('Invalid Input!!! Please enter a number between 1 and 100.')

print('Congratulations! Your guess is True! It is {}.'.format(computer_num))