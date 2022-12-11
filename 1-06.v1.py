# 100 énigmes mathématiques résolues avec python
# 1.06

# Analysis
#
# Smalest square of three digits is:
#
# 100 = 10 ** 2
#
# Biggest square of three digits is:
#
# 961 = 31 ** 2
#
# Smalest square of two digits is:
#
# 16 = 4 ** 2
#
# Biggest square of two digits is:
#
# 81 = 9 ** 2
#
# Algorithmic complexity: O(n³)

from timeit import default_timer as timer

# start benchmark
start = timer()

min_n = 10
max_n = 31

squares = []

for i in range(4, 10):
    squares.append(i ** 2)

stop = False

for i in range(min_n, max_n + 1):
    for j in range(min_n, max_n + 1):
        square1 = i ** 2
        square2 = j ** 2

        a1 = square1 // 100
        b1 = (square1 // 10) % 10
        c1 = square1 % 10

        a2 = square2 // 100
        b2 = (square2 // 10) % 10
        c2 = square2 % 10

        a = a1 * 10 + a2
        b = b1 * 10 + b2
        c = c1 * 10 + c2

        a_square = False
        b_square = False
        c_square = False

        for k in squares:
            if a == k:
                a_square = True

            if b == k:
                b_square = True

            if c == k:
                c_square = True

        if a_square and b_square and c_square:
            print('square1:', square1)
            print('square2:', square2)
            stop = True
            break

    if stop:
        break

# stop benchmark
end = timer()
duration = end - start
print('duration:', duration)

# square1: 841
# square2: 196
# duration: 0.0017530499899294227

