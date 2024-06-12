from random import randint


EXERCISE = 'What number is missing in the progression?'


def generate_question():
    n, numbers = generate_random()
    correct_answer = numbers[n]
    numbers[n] = ".."
    sequence_numbers = " ".join(map(str, numbers[0:10]))
    return sequence_numbers, correct_answer


def generate_random():
    num1 = randint(1, 10)
    num2 = randint(100, 120)
    n = randint(2, 9)
    numbers = []
    for i in range(num1, num2, n):
        numbers.append(i)
    return n, numbers