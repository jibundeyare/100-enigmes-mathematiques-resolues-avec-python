# 100 énigmes mathématiques résolues avec python
# 1.12

# Algorithmic complexity: O(n)

import math
from timeit import default_timer as timer

# start benchmark
start = timer()

squares = {}
i = 1

while True:
    square = i * i
    squares[square] = True
    n = square - 1

    if  n / 13 in squares:
        print('n:', n)
        break

    i += 1

# stop benchmark
end = timer()
duration = end - start
print('duration:', duration)

# n: 421200
# duration: 0.00046277100045699626

