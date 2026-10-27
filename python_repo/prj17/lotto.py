import random


def make_lotto():
    numbers = random.sample(range(1, 46),6)
    numbers.sort()
    return numbers

if __name__ == "__main__":
    print(make_lotto())