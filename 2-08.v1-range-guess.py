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
# Now let's find the minimum and maximum weight of a bale.
#
# The minimum possible weight of a bale if 1 Kg.
#
# Let's find the maximum weight of a bale.
# The heaviest weighing is 121. If the lightest bale was weighted in
# this weighing, the other bale must be 120 Kg.
# But a bale of 120 Kg is not possible because the other weights are
# greater or equal to 120 Kg and any bale is weighted exactly 4 times.
# Thus, the heaviest bale must be lighter.
# Repeating the reasoning with 119, 118 and 117 we concluse that the
# heaviest possible weight is 116 Kg.
#
# The algorithmic complexity O(n ** 5) is very high.
# To accelerate the process, it is possible to guess the possible 
# average weight of a bale and try to find the weights starting with a
# reasonable possible range.
#
# The lightest weight is 110 Kg and the heaviest weight is 121 Kg. The
# average should be closer to a value between 55 and 61. We can try
# guessing by starting to look for the possible real weights in a range
# of 10 Kg under and 10 Kg over the range. Which gives 45 and 70 as a
# starting range.
#
# If the answer is not there, we can widen the range to 35 and 80, 25
# and 90 and so on.

# Algorithmic time complexity: O(n ** 5)
# Algorithmic space complexity: O(?)

from timeit import default_timer as timer

# start benchmark
start = timer()

weights = [110, 112, 113, 114, 115, 116, 117, 118, 120, 121]
min_weight = 45
max_weight = 70

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
# duration: 1.1426639769997564

