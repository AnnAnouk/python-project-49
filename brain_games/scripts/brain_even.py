import prompt
import random
from brain_games import *


def main():
    print('Answer "yes" if the number is even, otherwise answer "no". ')
    game_cycle()
    if game_cycle() is True:
        print("Congratulations, ", "! '")
    if game_cycle() is False:
        print("'", "'", "is wrong answer ;(. Correct answer was '", "'. ")
        print("Let's try again, ", "! ")


if __name__ == '__main__':
    main()


def is_number_even(number):
    if (number % 2 == 0):
        return True
    return False


def game_cycle():
    i = 0
    while i <= 3:
        number = random.randint(1, 20)
        print("Question: ", number)
        answer = prompt.string("Your answer: ")
        result = is_number_even(number)
        
        if ((result is True) and (str(answer) == 'yes')) or ((result is False) and (str(answer) == 'no')):
            print("Correct!")
            i = i + 1
        return True
    
    
    else: #if ((result is False) and (str(answer) == 'yes')) or ((result is True) and (str(answer) == 'no')):
        return False
    