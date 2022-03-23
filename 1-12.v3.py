# 100 énigmes mathématiques résolues avec python
# 1.12

# Algorithmic complexity: O(n)

import math
from timeit import default_timer as timer

# start benchmark
start = timer()

def is_square(n):
    max_i = math.floor(math.sqrt(n)) + 1
    i = 1

    while i < max_i:
        if i * i == n:
            return True

        i += 1

    return False

i = 1

while True:
    square = i * i
    n = square - 1

    if  is_square(n / 13):
        print('n:', n)
        break

    i += 1

# stop benchmark
end = timer()
duration = end - start
print('duration:', duration)

# n: 421200
# duration: 0.010571524006081745

