import prompt
import random


def main():
    print('Answer "yes" if the number is even, otherwise answer "no". ')
    game_cycle()


if __name__ == '__main__':
    main()


def is_number_even(number):
    global result
    if (number % 2 == 0):
        result = 'yes'
    else:
        result = 'no'


def game_cycle():
    global answer
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
