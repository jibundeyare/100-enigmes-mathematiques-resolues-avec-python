# 100 énigmes mathématiques résolues avec python
# 1.04

# Analysis
#
# 3162 ** 2 == 9998244
# 3163 ** 2 == 10004569
# 9999 ** 2 == 99980001
# 10000 ** 2 == 100000000
#
# Algorithmic complexity: O(n²)

from timeit import default_timer as timer

def get_digit_list(number):
    return [int(x) for x in str(number)]

# start benchmark
start = timer()

squares = []
stop = False

for i in range(3163, 10000):
    square1 = i ** 2
    number1 = get_digit_list(square1)

    for j in range(i + 1, 10000):
        square2 = j ** 2
        number2 = get_digit_list(square2)
        number2_reversed = number2[::-1]

        if number1 == number2_reversed:
            print(i, '** 2:', square1)
            print(j, '** 2:', square2)
            stop = True
            break

    if stop:
        break

# stop benchmark
end = timer()
duration = end - start
print('duration:', duration)

# 3168 ** 2: 10036224
# 6501 ** 2: 42263001
# duration: 0.11960198500310071

