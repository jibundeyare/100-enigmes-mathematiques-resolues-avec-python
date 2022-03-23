# 100 énigmes mathématiques résolues avec python
# 1.08

# Algorithmic complexity: O(n²)

import math
from timeit import default_timer as timer

# start benchmark
start = timer()

n = 2018
square = n ** 2

stop = False

for i in range(n, 0, -1):
    i_square = i ** 2

    for j in range(1, i + 1):
        square2 = i_square + j ** 2

        if square2 > square:
            break

        if square2 == square:
            print('i:', i, 'j:', j)
            stop = True
            break

    if stop:
        break

# stop benchmark
end = timer()
duration = end - start
print('duration:', duration)

# i: 1680 j: 1118
# duration: 0.17383470499771647

