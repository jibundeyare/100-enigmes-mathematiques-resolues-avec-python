# 100 énigmes mathématiques résolues avec python
# 1.12

# Algorithmic complexity: O(n)

import math
from timeit import default_timer as timer

# start benchmark
start = timer()

i = 1

while True:
    square = i * i
    n = square * 13
    sqrt = math.sqrt(n + 1)

    if sqrt == int(sqrt):
        print('n:', n)
        break

    i += 1

# stop benchmark
end = timer()
duration = end - start
print('duration:', duration)

# n: 421200
# duration: 0.00020832099835388362

