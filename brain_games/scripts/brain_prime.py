import prompt
import random


def main():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    game_cycle()


if __name__ == '__main__':
    main()


def is_number_prime(number):
    global result
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    if number in prime_numbers:
        result = 'yes'
    else:
        result = 'no'


def game_cycle():
    i = 0
    while i <= 3:
        number = random.randint(2, 50)
        print("Question: ", number)
        answer = prompt.string("Your answer: ")
        is_number_prime(number)
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
