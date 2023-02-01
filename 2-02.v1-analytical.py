# 100 énigmes mathématiques résolues avec python
# 2.02

# Analysis
#
# 1000 is an even number. To obtain an even number with a sum, we must
# add up two even numbers or two odd numbers. Which means there are no
# two consecutive numbers (wich must be odd and even) which can add up
# to 1000.
#
# We need at least three consecutive numbers to add up to 1000.
#
# - if we sum three numbers, we must have odd + even + odd = even
# - if we sum four numbers, we can have odd + even + odd + even = even
#   or even + odd + even + odd
#
# More generally, is we sum an even quantity of numbers, the
# consecutive numbers may start by an odd or an even number. If we sum
# an odd quantity of numbers, the consecutive numbers must start with
# an odd number.
#
# We can also define equations to find the consecutive numbers.
#
# The equation for the sum of three consecutive numbers:
# n + (n + 1) + (n + 2) = 1000
# <=> 3 * n + 3 = 1000
# <=> 3 * n = 1000 - 3
# <=> 3 * n = 997
# 997 is not divisible by 3, so there's no solution with three numbers.
#
# The equation for the sum of four consecutive numbers:
# n + (n + 1) + (n + 2) + (n + 3) = 1000
# <=> 4 * n + 6 = 1000
# <=> 4 * n = 1000 - 6
# <=> 4 * n = 994
# 994 is not divisible by 4, so there's no solution with three numbers.
#
# We can generalize the equation for the m consecutive numbers to be:
# s(n, m) = m * n + f(m)
# where f(m) = (m ** 2 - m) / 2 is the sum of the integers from 1 to
# (m - 1).
#
# Details of the derivation of f(m):
# f(m) = ((m - 1) * ((m - 1) + 1)) / 2
# <=> f(m) = ((m - 1) * (m - 1 + 1)) / 2
# <=> f(m) = ((m - 1) * m) / 2
# <=> f(m) = (m ** 2 - m) / 2
#
# The expanded equation we get is:
# s(n, m) = m * n + (m ** 2 - m) / 2
#
# The equation for the sum of five consecutive numbers:
# s(n, 5) = 1000
# <=> 5 * n + (5 ** 2 - 5) / 2 = 1000
# <=> 5 * n + 10 = 1000
# <=> 5 * n = 1000 - 10
# <=> 5 * n = 990
# <=> n = 990 / 5
# <=> n = 198
#
# The result n = 198 and five consecutive numbers is the one presented
# in the definition of the problem.
#
# Now we can reformulate the question using the new equation.
# If 1000 - f(m) is divisible by m, then there exist a solution.
#
# This also means that we need to choose "m" such a way that
# f(m) < 1000 and also that 1000 - f(m) >= m.
#
# This because:
# - if f(m) >= 1000, then 1000 - f(m) <= 0
# - if m > 1000 - f(m), then (1000 - f(m)) / m < 1 wich means that
#  1000 - f(m) will not be divisible by m

# Algorithmic complexity: O(n)

from timeit import default_timer as timer

# start benchmark
start = timer()

def f(m):
    return (m ** 2 - m) / 2

# this value which the sum of consecutive numbers must be equal to
x = 1000
# start with m = 5 because there are no solution with lower values
m = 5
# save the result to avoid computing it again
fm = f(m)

# stop when f(m) >= 1000 because there are no solutions anymore
while fm < x:
    delta = x - fm
    quotient = delta / m

    # check if delta is divisible by m
    if quotient == int(quotient):
        # get the m consecutive numbers starting from n = quotient
        quotient = int(quotient)
        numbers = [n for n in range(quotient, quotient + m)]

        # @debug
        # print(numbers)

        # the sum must be equal to 1000
        my_sum = sum(numbers)

        # @debug
        # print(my_sum)

        print('m =', m, ':', ' + '.join(map(str, numbers)), '=', my_sum)

    m += 1
    # save the result to avoid computing it again
    fm = f(m)

# @debug
print('max m:', m)

# stop benchmark
end = timer()
duration = end - start
print('duration:', duration)

# m = 5 : 198 + 199 + 200 + 201 + 202 = 1000
# m = 16 : 55 + 56 + 57 + 58 + 59 + 60 + 61 + 62 + 63 + 64 + 65 + 66 + 67 + 68 + 69 + 70 = 1000
# m = 25 : 28 + 29 + 30 + 31 + 32 + 33 + 34 + 35 + 36 + 37 + 38 + 39 + 40 + 41 + 42 + 43 + 44 + 45 + 46 + 47 + 48 + 49 + 50 + 51 + 52 = 1000
# max m: 46
# duration: 0.00020221699378453195

