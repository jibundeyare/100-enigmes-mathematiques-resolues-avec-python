# 100 énigmes mathématiques résolues avec python
# 1.02

# Algorithmic complexity: O(sqrt(n))

import math
from timeit import default_timer as timer

# start benchmark
start = timer()

# limit of possible values
min_n = math.ceil(10000000 ** (1 /2))
max_n = math.ceil(99999900 ** (1 / 2))

for i in range(min_n, max_n):
    square = i * i

    # get first four digits
    a = square // 10000

    # get last four digits
    b = square % 10000

    # b - a == 1 is slower than b == a + 1
    if b == a + 1:
        print('square:', square)

# stop benchmark
end = timer()
duration = end - start
print('duration:', duration)

# square: 60996100
# duration: 0.0038489180005853996

