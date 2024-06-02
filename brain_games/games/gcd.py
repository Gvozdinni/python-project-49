from random import randrange


EXERCISE = 'Find the greatest common divisor of given numbers.'


def gcd(num1, num2):
    while num1 != num2:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return num2


def generate_question():
    num1 = randrange(1, 20)
    num2 = randrange(20, 50)
    number = (f'{num2} {num1}')
    correct_answer = gcd(num1, num2)
    return number, correct_answer
