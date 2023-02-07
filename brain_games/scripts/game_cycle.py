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
