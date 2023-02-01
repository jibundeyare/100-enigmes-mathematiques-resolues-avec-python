# 100 énigmes mathématiques résolues avec python
# 2.02

# Algorithmic complexity: O(n ** 2)

from timeit import default_timer as timer

# start benchmark
start = timer()

my_sum = 0
numbers = []

for i in range(1, 500):
    numbers.append(i)
    my_sum = sum(numbers)

    while my_sum > 1000:
        numbers.pop(0)
        my_sum = sum(numbers)

    if my_sum == 1000:
        print(numbers)

# stop benchmark
end = timer()
duration = end - start
print('duration:', duration)

# [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]
# [55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70]
# [198, 199, 200, 201, 202]
# duration: 0.0011846479974337853

