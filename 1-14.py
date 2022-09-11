# 100 énigmes mathématiques résolues avec python
# 1.14

# Let's put the problem into equation:
#
# x = a ** 2 + 39
# x = (a + 1) ** 2 - 50
#
# Now let's solve the equation:
#
# a ** 2 + 39 = (a + 1) ** 2 - 50
# (a + 1) ** 2 - a ** 2 = 39 + 50
# (a + 1) ** 2 - a ** 2 = 89
#
# We can use the following equality:
# a ** 2 - b ** 2 = (a + b) * (a - b)
# to factorize the left part of the equation.
#
# ((a + 1) + a) * ((a + 1) - a) = 89
# (a + 1 + a) * (a + 1 - a) = 89
# (2 * a + 1) * 1 = 89
# 2 * a + 1 = 89
# 2 * a = 89 - 1
# 2 * a = 88
# a = 88 / 2
# a = 44
#
# Let's verify our findings:
#
# x1 = a ** 2 + 39 = 44 ** 2 + 39 = 1975
# x2 = (a + 1) ** 2 - 50 = (44 + 1) ** 2 - 50 = 1975
# x1 = x2
# x = 1975 QED
#
# Algorithmic complexity: O(0)

from timeit import default_timer as timer

# start benchmark
start = timer()

# stop benchmark
end = timer()
duration = end - start
print('duration:', duration)

# duration: 1.9919825717806816e-06

