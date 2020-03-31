import math
from random import random, randint


def exponential(lmd):
    return -1 * math.log(random()) / lmd


def poisson(lmd):
    s = 0
    n = -1

    while True:
        s += exponential(lmd)
        n += 1

        if s > lmd:
            break

    return n


def normal(half, variance):
    while True:
        exp_1 = exponential(1)
        exp_2 = exponential(1)

        if exp_2 - (exp_1 - 1)**2 / 2 > 0:
            x = exp_1 * math.sqrt(variance) + half

            return x if random() <= 1/2 else -1 * x


def select_random_type():
    rnd_type = randint(0, 100)

    if rnd_type <= 45:
        return 1
    elif rnd_type <= 70:
        return 2
    elif rnd_type <= 80:
        return 3

    return 4
