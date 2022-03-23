# 100 énigmes mathématiques résolues avec python
# 1.03

# Algorithmic complexity: O(n)

from timeit import default_timer as timer

def get_nth_digit(number, position):
    tmp = number % (10 ** position)

    return tmp // (10 ** (position - 1))

def get_number_size(number):
    size = len(str(number))

    return size

def get_number_size_numerical(number):
    size = 1
    while number // (10 ** size) > 1:
        size += 1

    return size

def get_digit_list(number):
    return [int(x) for x in str(number)]

def get_digit_list_numerical(number):
    digits = []
    size = get_number_size(number)

    for i in range(size, 0, -1):
        digit = get_nth_digit(number, i)
        digits.append(digit)

    return digits

# start benchmark
start = timer()

all_digits = []

for i in range(1, 10):
    all_digits.append(i)

for i in range(123, 987 + 1):
    square = i ** 2
    number_digits = get_digit_list(i) + get_digit_list(square)
    number_digits.sort()

    if all_digits == number_digits:
        print(i, i ** 2)

# stop benchmark
end = timer()
duration = end - start
print('duration:', duration)

# 567 321489
# 854 729316
# duration: 0.0050639200053410605

