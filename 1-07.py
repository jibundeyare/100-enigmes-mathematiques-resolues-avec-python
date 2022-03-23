# 100 énigmes mathématiques résolues avec python
# 1.07

# Algorithmic complexity: O(sqrt(n))

import math
from timeit import default_timer as timer

# start benchmark
start = timer()

min_n = math.ceil(100000 ** (1 / 2))
max_n = math.floor(999999 ** (1 / 2))

print('min_n:', min_n)
print('max_n:', max_n)

for i in range(min_n, max_n + 1):
    square = i ** 2

    digit1 = square // 100000
    digit2 = (square // 10000) % 10
    digit3 = (square // 1000) % 10
    digit4 = (square // 100) % 10
    digit5 = (square // 10) % 10
    digit6 = square % 10

    if digit1 == digit6 and digit2 == digit5 and digit3 == digit4:
        print('i:', i)
        print('square:', square)
        break

# stop benchmark
end = timer()
duration = end - start
print('duration:', duration)

# min_n: 317
# max_n: 999
# i: 836
# square: 698896
# duration: 0.0006380500126397237

