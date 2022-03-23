# 100 énigmes mathématiques résolues avec python
# 1.09

# Algorithmic complexity: O(n)

import math
from timeit import default_timer as timer

# start benchmark
start = timer()

start = math.ceil(1000 ** (1 / 2))
end = math.floor(9999 ** (1 / 2))

for i in range(start, end + 1):
    square = i ** 2

    a = square // 1000
    b = square // 100 % 10
    c = square // 10 % 10
    d = square % 10

    if a == b and c == d:
        print('i:', i, 'square:', square)
        break

# stop benchmark
end = timer()
duration = end - start
print('duration:', duration)

# i: 88 square: 7744
# duration: 8681.232587695

