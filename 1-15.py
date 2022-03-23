# 100 énigmes mathématiques résolues avec python
# 1.15

# Algorithmic complexity: O(n)

from timeit import default_timer as timer

# start benchmark
start = timer()

n = 0
i = 150

while n == 0:
    square = i ** 2
    square_str = str(square)

    if square_str[0:4] == '2222':
        n = i

    i += 1

print('n:', n)
print('square:', square)

# stop benchmark
end = timer()
duration = end - start
print('duration:', duration)

# n: 4714
# square: 22221796
# duration: 0.00485940498765558

