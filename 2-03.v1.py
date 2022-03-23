# 100 énigmes mathématiques résolues avec python
# 2.03

# Analysis
#
#   111
# + 333
# + 555
# + 777
# + 999
# -----
#  2775
#
# The problem is to replace 6 digits by zeros so the sum becomes 1111.
#
# First, note that replacing 111 by 110 is like doing:
#
# 111 - 1 = 111 - 10 ** 0 = 110
#
# Replacing 111 by 101 is like doing:
#
# 111 - 10 = 111 - 10 ** 1 = 101
#
# Replacing 111 by 011 is like doing:
#
# 111 - 100 = 111 - 10 ** 2 = 11
#
# And so on.
#
# Secondly, note that the difference between 2775 and 1111 is:
#
# 2775 - 1111 = 1664
#
# This means that substracting from 2775 to obtain 1111 is like summing
# values to obtain 1664.
#
# But in order to solve the problem we can only sum values that are, on
# one hand, multiples of 1, 3, 5, 7, 9 and, on the onther hand,
# multiples of power of 10 from 10 ** 0 to 10 ** 2.
#
# Here is the full list of those numbers: 1, 3, 5, 7, 9, 10, 30, 50, 70,
# 90, 100, 300, 500, 700, 900
#
# Now, finding six numbers that sum up to 1664 is just a matter of
# finding the right combination.
#
# In fact this is possible with a pencil, paper and a little bit
# of patience.
#
# To ease a little bit our calculations, instead of summing numbers,
# we will be substracting from 1664 until we reach 0. This is exactly
# the same as summing numbers and reach 1664.
#
# The last digit of 1664 is a 4. The only numbers for which the last
# number of their sum is a 4 are:
#
# 1 + 3 = 4
# or
# 5 + 9 = 14
#
# Let's try with 1 + 3 = 4.
#
#   1664
# -    1
# -    3
# ------
#   1660
#
# The last non zero digit of 1660 is a 6. The only numbers for which the
# last number of their sum is a 6 are:
#
# 1 + 5 = 6
# or
# 7 + 9 = 16
#
# Let's try with 1 + 5 = 6.
#
#   1660
# -   10
# -   50
# ------
#   1600
#
# The last non zero digit of 1600 is again a 6. The only numbers for
# which the last number of their sum is a 6 are:
#
# 1 + 5 = 6
# or
# 7 + 9 = 16
#
# This time we'll use 7 + 9 = 16 which exactly adds up to 16.
#
#   1660
# -  700
# -  900
# ------
#      0
#
# This means that summing these numbers gives 1664:
#
# 1 + 3 + 10 + 50 + 700 + 900 = 1664
#
# Now we can find exactly which digit we need to replace by a zero:
#
#   111
# -   1
# -  10
# + 333
# -   3
# + 555
# -  50
# + 777
# - 700
# + 999
# - 900
# -----
#   100
# + 330
# + 505
# + 077
# + 099
# -----
#  1111

from timeit import default_timer as timer

# start benchmark
start = timer()

# stop benchmark
end = timer()
duration = end - start
print('duration:', duration)

