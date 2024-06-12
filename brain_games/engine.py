import prompt
NUMBER_OF_GAME = 3


def start_game(game):
    name = get_name()
    print(game.EXERCISE)
    x = 0
    while x < NUMBER_OF_GAME:
        question, correct_answer = game.generate_question()
        print(f'Question: {question}')
        user_answer = get_answer()
        if user_answer == str(correct_answer):
            print('Correct!')
            x += 1
            continue
        elif user_answer != correct_answer:
            print(f"""{user_answer} is wrong answer ;(. Correct answer was {correct_answer}.
Let's try again, {name}!""")
            break
    else:
        print(f'Congratulations, {name}!')


def get_answer():
    answer = input('Your answer: ')
    return answer


def get_name():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name
