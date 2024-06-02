from random import randint


EXERCISE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_prime(num1):
    if num1 % 2 == 0:
        return True
    else:
        return False


def generate_question():
    num1 = randint(1, 20)
    if is_prime(num1) is True:
        return num1, 'yes'
    else:
        return num1, 'no'