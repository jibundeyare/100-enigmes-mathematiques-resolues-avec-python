# 100 énigmes mathématiques résolues avec python
# 1.05

# Analysis
#
# sqrt(2018) = 44.92...
#
# If 2018 is the sum of two square numbers, the quare root of those
# numbers must be lower or equal to 44. Otherwise their sum will be
# larger than 2018. Example: 0² + 45² = 2025
#
# Algorithmic complexity: O(n)

from timeit import default_timer as timer

# start benchmark
start = timer()

max_n = 44
n = 2018

stop = False

for i in range(0, max_n + 1):
    for j in range(i, max_n + 1):
        if i ** 2 + j ** 2 == n:
            print(i, '** 2 +', j, '** 2 ==', n)
            stop = True
            break

    if stop:
        break

# stop benchmark
end = timer()
duration = end - start
print('duration:', duration)

# 13 ** 2 + 43 ** 2 == 2018
# duration: 0.0004424299986567348

