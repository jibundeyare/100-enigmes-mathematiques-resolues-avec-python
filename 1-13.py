# 100 énigmes mathématiques résolues avec python
# 1.13

# Analysis
#
# Pyramids with a square base have specific numberof bullets:
# - 1 * 1 = 1
# - 1 * 1 + 2 * 2 = 1 + 2 * 2 = 5
# - 1 * 1 + 2 * 2 + 3 * 3 = 5 + 3 * 3 = 14
# - ...
#
# The valuse are:
#
# - 0 0
# - 1 1
# - 2 5
# - 3 14
# - 4 30
# - 5 55
# - 6 91
# - 7 140
# - 8 204
# - 9 285
# - 10 385
#
# The following sequence produces the number of bullets:
#
# U0 = 0
# U1 = 1
# Un+1 = (n + 1) * (n + 1) + Un
# Un+1 = n² + 2n + 1 + Un
#
# Or using this simpler sequence:
#
# U0 = 0
# U1 = 1
# Un = n * n + Un-1
# Un = n ** 2 + Un-1
#
# The sequence can also be rewritten as a sum:
#
# \sum\limits_{i=1}^n i^2
#
# Algorithmic complexity: O(n)

from timeit import default_timer as timer

# start benchmark
start = timer()

class Cache:
    data = {}

def pyramid_items(rank: int) -> int:

    if rank == 0:
        return 0
    elif rank == 1:
        return 1

    if rank in Cache.data:
        return Cache.data[rank]

    last_u = 1

    for i in range(2, rank + 1):
        u = i * i + last_u
        last_u = u

    Cache.data[rank] = u

    return u

stop = False
i = 2

while True:
    square = i * i
    j = 2

    while True:
        n = pyramid_items(j)

        if n > square:
            break
        elif n == square:
            stop = True
            break

        j += 1

    if stop:
        break

    i += 1

print('n:', n)

# stop benchmark
end = timer()
duration = end - start
print('duration:', duration)

# n: 4900
# duration: 0.000707574999978533

