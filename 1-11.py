# 100 énigmes mathématiques résolues avec python
# 1.11

# Algorithmic complexity: O(n)

from timeit import default_timer as timer

# start benchmark
start = timer()

import math

# min square is 139854276
# sqrt(139854276) = 11826
min_value = 11826
max_value = math.ceil(math.sqrt(987654321))

digits = {}

for i in range(max_value, min_value, -1):
    square = i * i
    square_digits = [int(x) for x in str(square)]

    unique_digits = True
    digits = {}

    for j in square_digits:
        if j in digits.keys():
            unique_digits = False
            break
        else:
            digits[j] = True

    if unique_digits:
        print('i:', i, 'square:', square)
        break

# stop benchmark
end = timer()
duration = end - start
print('duration:', duration)

# i: 30384 square: 923187456
# duration: 0.0057134539965773

