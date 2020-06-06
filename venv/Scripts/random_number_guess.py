import random
import sys

#Generate a Random Number
#answer = random.randint(int(sys.argv[1]),int(sys.argv[2]))

def guess_number(guess, answer):
    if guess == answer:
        print("You got it right!!")
        return True
    elif guess < 1 or guess > 10:
        print(f'Enter a number between 1 and 10 for God\'s sake!!!')

answer = random.randint(1,10)

if __name__ == '__main__':#Ask the user to guess the number
    while True:
        try:
            guess = int(input(f'Enter a number between 1 and 10.'))
            if guess_number(guess, answer):
                break
        except ValueError:
            print("Enter a number")
