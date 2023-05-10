from random import randint


def get_array_of_given_size(size=5000):
    result = []
    for _ in range(size):
        number = randint(0, 10000)
        result.append(number)

    return result


if __name__ == "__main__":
    print(get_array_of_given_size())
