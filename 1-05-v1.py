# 100 énigmes mathématiques résolues avec python
# 1.05

# Algorithmic complexity: O(n²)

from timeit import default_timer as timer

# start benchmark
start = timer()

n = 2018

stop = False

for i in range(0, n):
    for j in range(i, n):
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
# duration: 0.020324981996964198

