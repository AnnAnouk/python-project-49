import random
import prompt 
from brain_games import cli
#from games import brain_even
#from brain_games import brain_even

def main():
    game_cycle()

if __name__ == '__main__':
    main()


cli.welcome_user()
brain_even.is_number_even()

def game_cycle():
    i = 0
    while i <= 3:
        number = random.randint(1, 20)
        print("Question: ", number)
        answer = prompt.string("Your answer: ")
        is_number_even(number)
        if result == answer:
            print("Correct!")
            i = i + 1
            if i >= 3:
                print("Congratulations!")
                break
        elif result != answer:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.")
            print("Let's try again!")
            break
        else:
            print("Let's try again!")
            break

