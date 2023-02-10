import math
import prompt
import random


def main():
    print("Find the greatest common divisor of given numbers.")
    game_cycle()


if __name__ == '__main__':
    main()


def game_question():
    global result
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    print(f'Question: {first_number}, {second_number}')
    result = math.gcd(first_number, second_number)


def game_cycle():
    i = 0
    while i < 3:
        game_question()
        answer = int(prompt.string("Your answer: "))
        if answer == result:
            print('Correct!')
            i = i + 1
            if i >= 3:
                print('Congratulations!')
                break
        else:
            print(f"'{answer}' was wrong answer ;(. Correct answer was '{result}'.")
            print("Let's try again!")
            break
