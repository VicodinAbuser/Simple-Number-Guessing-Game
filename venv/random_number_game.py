import random
import sys

#Generate a Random Number
#answer = random.randint(int(sys.argv[1]),int(sys.argv[2]))
answer = random.randint(int(sys.argv[1]),int(sys.argv[2]))


#Ask the user to guess the number
while True:
    guess = int(input(f'Enter a number between {sys.argv[1]} and {sys.argv[2]}.'))
    guess_number(guess)
    try:
        def guess_number(guess):
            if guess == answer:
                print("You got it right!!")

            elif guess < sys.argv[1] and guess > sys.argv[2]:
                print(f'Enter a number between {sys.argv[1]} and {sys.argv[2]} for God\'s sake!!!')
    except ValueError:
        print("Enter a number")
