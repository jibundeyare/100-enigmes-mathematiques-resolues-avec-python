# 100 énigmes mathématiques résolues avec python
# 1.01

# Algorithmic complexity: O(n)

import math
from timeit import default_timer as timer

# start benchmark
start = timer()

# limit of possible values
min_n = math.ceil(1000 ** (1 /2))
max_n = math.ceil(9999 ** (1 / 2))
min_m = math.ceil(10 ** (1 / 2))
max_m = math.ceil(99 ** (1 / 2))

for i in range(min_n, max_n):
    square = i * i

    a = int(str(square)[0:2])
    b = int(str(square)[2:4])

    a_is_square = False
    b_is_square = False

    for j in range(min_m, max_m):
        part_square = j * j

        if part_square == a:
            a_is_square = True

        if part_square == b:
            b_is_square = True

    if a_is_square and b_is_square:
        print('square:', square)

# stop benchmark
end = timer()
duration = end - start
print('duration:', duration)

# square: 1681
# duration: 0.0004213439970044419

