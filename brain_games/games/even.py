from random import randint


EXERCISE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_prime(num1):
    '''Checking numbers for even'''
    if num1 % 2 == 0:
        return True
    else:
        return False


def generate_question():
    '''Generates random number and returns the correct answer.'''
    num1 = randint(1, 20)
    if is_prime(num1) is True:
        return num1, 'yes'
    else:
        return num1, 'no'