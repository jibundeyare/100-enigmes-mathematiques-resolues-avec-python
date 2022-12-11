# 100 énigmes mathématiques résolues avec python
# 2.12

# Analysis
#
# Let a = {1, 2}
#
# 2 parts:
# 1 + 2
#
# Let a = {1, 2, 3}
#
# 2 parts:
# 1 + 23
# 12 + 3
#
# 3 parts:
# 1 + 2 + 3
#
# Let a  = {1, 2, 3, 4}
#
# 2 parts:
# 1 + 234
# 12 + 34
# 123 + 4
#
# 3 parts:
# 1 + 2 + 34
# 1 + 23 + 4
# 12 + 3 + 4
#
# 4 parts:
# 1 + 2 + 3 + 4
#
# It is possible to build all the partitions of the numbers from 1 to 9
# if we start by building the smallest possible blocks.
# This seems to be a typical bottom up dynamic programming approach.
#
# For example, let's start building all the partitions from the first
# right most digits.
#
# Let a  = {1, 2, 3, 4}
#
# 4:
#   [4]
# 34:
#   [34]
#   [3] + partitions_of(4) => [3] + [4]
# 234:
#   [234]
#   [23] + partitions_of(4) => [23]  + [4]
#   [2] + partitions_of(34) => [2] + [34], [2] + [3] + [4]
# 1234:
#   [1234]
#   [123] + partitions_of(4) => [123] + [4]
#   [12] + partitions_of(34) => [12] + [34], [12] + [3] + [4]
#   [1] + partitions_of(234) => [1] + [234], [1] + [23] + [4], [1] + [2] + [34], [1] + [2] + [3] + [4]

# Algorithmic time complexity: O(n ** 3)
# Algorithmic space complexity: O(n ** 2)

from pprint import pprint
from timeit import default_timer as timer

# start benchmark
start = timer()

def split_number(number: int, position: int) -> tuple[int, int]:
    """Returns left and right parts of an integer using given position.
    Position >= len(str(number)) returns 0 as left part and number as right part.
    Position 0 returns number as left part and 0 as right part.
    Position < 0 returns unexpected values

    number int the number to split in two parts
    position int where to split the number
    return tuple[int, int]
    """
    mask = 10 ** position

    left_part = number // mask
    right_part = number % mask

    return left_part, right_part

numbers = 123456789
expected_sum = 1269
all_partitions = {}

for i in range(1, 10):
    partitions = []
    _, base_part = split_number(numbers, i)

    # @debug
    # print(f'{base_part = }')

    partitions.append([base_part])

    for j in range(1, i):
        left_part, right_part = split_number(base_part, j)

        # @debug
        # print(f'{left_part = }')
        # print(f'{right_part = }')
        # print()

        for partition in all_partitions[right_part]:
            partitions.append([left_part] + partition)

    all_partitions[base_part] = partitions

# @debug
# pprint(all_partitions)
# print()

for parts in all_partitions[numbers]:
    my_sum = 0

    for part in parts:
        my_sum += part

    if my_sum == expected_sum:
        formula = ' + '.join(map(str, parts)) + ' = ' + str(expected_sum)
        print(formula)

# stop benchmark
end = timer()
duration = end - start
print(f'{duration=}')

# 1234 + 5 + 6 + 7 + 8 + 9 = 1269
# 1 + 23 + 456 + 789 = 1269
# duration=0.0007131570018827915

