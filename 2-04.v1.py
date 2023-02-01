# 100 énigmes mathématiques résolues avec python
# 2.04

# Analysis
#
# Let x be the amount.
# x's integer part is necessariliy between 1 and 99. This is because it
# is not possible to swap 100 or more euros with 100 or more cents,
# 100 or more cents becoming euros. The same logic applies to x's
# fractional part which is necessarily between 0.00 and 0.99.
#
# Let's write the equation of the question.
#
# Note that :
#
# - to ease the computation, x is multiplied by 100
# - (x / 100) is the amount we are looking for
# - (x % 100) is the fractional part that becomes the integer part
# - ((x // 100) / 100) is the integer part that becomes the fractional
#   part
#
# 2 * (x / 100) == (x % 100) + ((x // 100) / 100) - 1.30

# Algorithmic complexity: O(n)

from timeit import default_timer as timer

# start benchmark
start = timer()

for x in range(0, 10000):
    if 2 * (x / 100) == (x % 100) + ((x // 100) / 100) - 1.30:
        print('x:', x / 100)

# stop benchmark
end = timer()
duration = end - start
print('duration:', duration)

# x: 22.46
# duration: 0.00800137199985329

