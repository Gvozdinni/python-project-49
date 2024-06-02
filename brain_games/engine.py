from brain_games import cli


def start_game(game):
    name = cli.welcome_user()
    print(game.EXERCISE)
    x = 0
    while x < 3:
        question, correct_answer = game.generate_question()
        print(f'Question: {question}')
        user_answer = get_answer()
        if user_answer == str(correct_answer):
            print('Correct!')
            x += 1
            continue
        elif user_answer != correct_answer:
            print(f"""{answer} is wrong answer ;(. Correct answer was {correct_answer}.
Let's try again, {name}!""")
            break
    else:
        print(f'Congratulations, {name}!')


def get_answer():
    answer = input('Your answer: ')
    return answer
