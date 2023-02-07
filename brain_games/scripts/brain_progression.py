import prompt
import random


def main():
    print("What number is missing in the progression?")
    game_cycle()


if __name__ == '__main__':
    main()


def game_question():
    global result
    first_number = random.randint(1, 20)
    amount = random.randint(5, 10)
    step = random.randint(2, 10)
    last_number = first_number + (amount - 1) * step
    index = random.randint(0, (amount - 1))
    progression = []
    for i in range(first_number, (last_number + step), step):
        progression.append(i)
    result = progression[index]
    progression[index] = ".."
    print(f'Question: {progression}')


def game_cycle():
    i = 0
    while i < 3:
        game_question()
        answer = int(prompt.string('Your answer: '))
        if answer == result:
            print('Correct!')
            i = i + 1
            if i >= 3:
                print('Congratulations!')
                break
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.")
            print("Let's try again!")
            break
