def min(x, y):
    return y if x < y else x


def max(values_list):
    max = values_list[0]
    for value in values_list:
        if value > max:
            max = value
    return max


def len(values_list):
    count = 0
    for item in values_list:
        count += 1
    return count


def multiply(x, y):
    if y == 0:
        return 0
    if y > 0:
        return x + multiply(x, y-1)
    if y < 0:
        return -multiply(x, -y)

def pow(x, y):
    pass


def divmod(x, y):
    pass


if __name__ == "__main__":
    result = multiply(3,4)
    print(result)
