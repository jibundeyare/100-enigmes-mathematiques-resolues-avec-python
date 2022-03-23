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

squares_2 = []

for i in range(4, 10):
    squares_2.append(i ** 2)

squares_3 = []

for i in range(10, 32):
    squares_3.append(i ** 2)

stop = False

for square1 in squares_3:
    for square2 in squares_3:

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

        for i in squares_2:
            if a == i:
                a_square = True

            if b == i:
                b_square = True

            if c == i:
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
# duration: 0.001443747998564504

