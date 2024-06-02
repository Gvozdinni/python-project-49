from brain_games import cli


def start_game(game):
    name = cli.welcome_user()
    print(game.EXERCISE)
    x = 0
    while x < 3:
        question, correct_answer = game.generate_question()
        get_question(question)
        user_answer = get_answer()
        if user_answer == str(correct_answer):
            print_correct()
            x += 1
            continue
        elif user_answer != correct_answer:
            print_wrong_answer(user_answer, name, correct_answer)
            break
    else:
        print_congratulate(name)


def get_question(n):
    print(f'Question: {n}')


def get_answer():
    answer = input('Your answer: ')
    return answer


def print_wrong_answer(answer, name, correct_answer):
    print(f"""{answer} is wrong answer ;(. Correct answer was {correct_answer}.
Let's try again, {name}!""")


def print_correct():
    print('Correct!')


def print_congratulate(name):
    print(f'Congratulations, {name}!')