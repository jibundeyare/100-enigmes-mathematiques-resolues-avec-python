# 100 énigmes mathématiques résolues avec python
# 2.11

# Analysis
#
# This version of the script should be less data intensive compared to
# the v1 as data quantity n tends to grow.
#
# This script stores the impossible sums instead of the possible sums.
# As the algorithm goes on, there are less and less impossible sums and
# more and more possible ones.
# Which means it is a better strategy to store the impossible sums if we
# want to spare storage memory.

# Algorithmic time complexity: O(n)
# Algorithmic space complexity: O(n)

from timeit import default_timer as timer

# start benchmark
start = timer()

impossible_sums = [i for i in range(1, 11)]

consecutive_numbers = 3
highest_impossible_sum = 10
i = 14

while consecutive_numbers < 11:
    if i - 11 not in impossible_sums \
    or i - 12 not in impossible_sums \
    or i - 13 not in impossible_sums:
        consecutive_numbers += 1
    else:
        impossible_sums.append(i)
        consecutive_numbers = 0

    i += 1

print(impossible_sums)
print(f'{impossible_sums[-1]=}')

# stop benchmark
end = timer()
duration = end - start
print(f'{duration=}')

# [1,  2,  3,  4,  5,  6,  7,  8,  9,  10, 14, 15, 16, 17, 18, 19, 20, 21, 27, 28, 29, 30, 31, 32, 40, 41, 42, 43, 53, 54]
# impossible_sums[-1]=54
# duration=0.0001495860001341498

