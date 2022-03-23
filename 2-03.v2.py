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

# Algorithmic complexity: O(?)

from timeit import default_timer as timer

# start benchmark
start = timer()

delta = 1664

# the number of items that will be combinated
items = 6
items_last_index = items - 1

digits = [n for n in range(1, 10, 2)]
numbers = [n * 10 ** i for i in range(0, 3) for n in digits]

# @dev
# print(numbers)

indeces = [i for i in range(0, items)]
# the limits are the last possible value, unlike in range() where the upper bound is the "possible value + 1"
limits = [(len(numbers) - (items - i)) for i in range(0, items)]

combinations = []

loop = True

# @dev
# print(indeces)

while loop:
    combination = []
    my_sum = 0

    for i in indeces:
        my_sum += numbers[i]
        combination.append(numbers[i])

    if my_sum == delta:
        combinations.append(combination)

    # @dev
    # print(combination)
    # print(my_sum)

    # backward search for an index we can increment
    # assume all possibilities are exhausted
    possibilities_exhausted = True

    for i in range(items_last_index, -1, -1):
        if indeces[i] < limits[i] and (i == items_last_index or indeces[i] < indeces[i + 1]):
            # we found an index we can increment
            # all possibilities are not exhausted yet
            possibilities_exhausted = False
            indeces[i] += 1

            # reset indeces following the current one
            for j in range(i + 1, items):
                indeces[j] = indeces[i] + (j - i)

            break

    # @dev
    # print(indeces)

    if possibilities_exhausted:
        break

for combination in combinations:
    print(combination)

# stop benchmark
end = timer()
duration = end - start
print('duration:', duration)

# [1, 3, 10, 50, 700, 900]
# duration: 0.03963853900495451

