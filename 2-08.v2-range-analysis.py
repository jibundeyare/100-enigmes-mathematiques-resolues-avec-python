# 100 énigmes mathématiques résolues avec python
# 2.08

# Analysis
#
# Note that the 10 weighing is the complete set of all possible weighing
# two by two.
#
# Let a, b, c, d, e be the weight f the bales.
#
# a + b is the same as b + a.
# b + c is the same as c + b and so on.
#
# So we only need to the followoing weighing:
#
# a + b, a + c, a + d, a + e    # 4 weighing
# b + c, b + d, b + e           # 3 weighing
# c + d, c + e                  # 2 weighing
# d + e                         # 1 weighing
#
# Which is a total of 10 weighing.
# Also note that any bale is weighted exactly 4 times.
#
# First, let's find the minimum possible weight of a bale.
#
# Let's imagine there is at least one bale whose weight is 1 Kg.
# We know that all bales are weighted 4 times. This means that the other
# 4 bales weight must be in the following set:
#
# 110 - 1 = 109
# 112 - 1 = 111
# 113 - 1 = 112
# 114 - 1 = 113
# 115 - 1 = 114
# 116 - 1 = 115
# 117 - 1 = 116
# 118 - 1 = 118
# 120 - 1 = 119
# 121 - 1 = 120
#
# We note that all the weights are greater or equal to 109 Kg. But this
# is not possible because if all other bales are 109 Kg or more, their
# minimum weighing 109 + 109 = 218 Kg is greater than the heaviest
# weighing which is 121 Kg.
#
# The same conclusion stays true with 2 Kg, 3 Kg, 4 Kg and so on.
#
# Until 50 Kg. 50 Kg is the first possible minimum weight because the
# other 4 bales weight must be in the following set:
#
# 110 - 50 = 60
# 112 - 50 = 62
# 113 - 50 = 63
# 114 - 50 = 64
# 115 - 50 = 65
# 116 - 50 = 66
# 117 - 50 = 67
# 118 - 50 = 68
# 120 - 50 = 70
# 121 - 50 = 71
#
# We note that all the weights are greater or equal to 60 Kg. At last,
# this is possible because if all other bales are 60 Kg or more, their
# minimum weighing 60 + 60 = 120 Kg is lower or equal to the heaviest
# weighing which is 121 Kg.
#
# We know for sure that the search range's lower bound is 50 Kg.
#
# Now let's find the maximum possible weight of a bale.
#
# Let's imagine there is at least one bale whose weight is 109 Kg.
# We know that all bales are weighted 4 times. This means that the other
# 4 bales weight must be in the following set:
#
# 110 - 109 = 1
# 112 - 109 = 3
# 113 - 109 = 4
# 114 - 109 = 5
# 115 - 109 = 6
# 116 - 109 = 7
# 117 - 109 = 8
# 118 - 109 = 9
# 120 - 109 = 10
# 121 - 109 = 11
#
# We note that all the weights are lower or equal to 11 Kg. But this
# is not possible because if all other bales are 11 Kg or less, their
# maximum weighing 11 + 11 = 22 Kg is lower than the lightest weighing
# which is 110 Kg.
#
# The same conclusion stays true with 108 Kg, 107 Kg, 106 Kg and so on.
#
# Until 66 Kg. 66 Kg is the first possible maximum weight because the
# other 4 bales weight must be in the following set:
#
# 110 - 66 = 44
# 112 - 66 = 46
# 113 - 66 = 47
# 114 - 66 = 48
# 115 - 66 = 49
# 116 - 66 = 50
# 117 - 66 = 51
# 118 - 66 = 52
# 120 - 66 = 53
# 121 - 66 = 55
#
# We note that all the weights are lower or equal to 55 Kg. At last,
# this is possible because if all other bales are 55 Kg or less, their
# maximum weighing 55 + 55 = 110 Kg is greater or equal to the lightest
# weighing which is 110 Kg.
#
# Now we know for sure that the search range's upper bound is 66 Kg.

# Algorithmic time complexity: O(n ** 5)
# Algorithmic space complexity: O(?)

from timeit import default_timer as timer

# start benchmark
start = timer()

weights = [110, 112, 113, 114, 115, 116, 117, 118, 120, 121]
min_weight = 50
max_weight = 66

for i in range(min_weight, max_weight + 1):
    for j in range(i, max_weight + 1):
        # @debug
        # print(f'{i=} {j=}')

        for k in range(j, max_weight + 1):
            for l in range(k, max_weight + 1):
                for m in range(l, max_weight + 1):
                    candidates = [i, j, k, l, m]
                    candidates_weights = []

                    for n in range(0, len(candidates)):
                        for o in range(n + 1, len(candidates)):
                            weight = candidates[n] + candidates[o]
                            candidates_weights.append(weight)

                    candidates_weights.sort()

                    # @debug
                    # print(f'{candidates=}')
                    # print(f'{candidates_weights=}')

                    if candidates_weights == weights:
                        print(candidates)

# stop benchmark
end = timer()
duration = end - start
print('duration:', duration)

# [54, 56, 58, 59, 62]
# duration: 0.16446626000106335

