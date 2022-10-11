# 100 énigmes mathématiques résolues avec python
# 2.06

# Analysis
#
# Let a, b, c, d, e be positive integers.
# 
# a + b + c + d + e = 200
# 12 * a + 3 * b + c + d / 2 + e / 3 = 200
#
# Then the folliwing rules must be respected:
#
# - a, b and c can be any positive integer
# - d is necessarily a multiple of 2
# - e is necessarily a multiple of 3
#
# The lowest possible value of a, b, and c is 1.
# The lowest possible value of d is 2.
# The lowest possible value of e is 3.
#
# Let's find the highest possible value of a:
#
# 12 * a <= 200 - 3 * b - c - d / 2 - e / 3
# => 12 * a <= 200 - 3 - 1 - 2 - 3
# <=> 12 * a <= 191
# <=> a <= 191 / 12 # but 191 is not divisible by 12
# => a <= 180 / 12 # 180 is the highest number lower or equal to 191 which is divisible by 12
# <=> a <= 15
#
# Thus, the highest possible value of a is 15.
#
# Let's find the highest possible value of b:
#
# 3 * b <= 200 - 12 * a - c - d / 2 - e / 3
# => 3 * b <= 200 - 12 - 1 - 2 - 3
# <=> 3 * b <= 182
# <=> b <= 182 / 3 # but 182 is not divisible by 3
# => b <= 180 / 3 # 180 is the highest number lower or equal to 182 which is divisible by 3
# <=> a <= 60
#
# Thus, the highest possible value of b is 60.
#
# Let's find the highest possible value of c:
#
# c <= 200 - 12 * a - 3 * b - d / 2 - e / 3
# => c <= 200 - 12 - 3 - 2 - 3
# <=> c <= 180
#
# Thus, the highest possible value of c is 180.
#
# Let's find the highest possible value of d:
#
# d <= 200 - a - b - c - e
# => d <= 200 - 1 - 1 - 1 - 3
# <=> d <= 194 # 194 is divisible by 2
#
# Thus, the highest possible value of d is 194.
#
# Let's find the highest possible value of e:
#
# e <= 200 - a - b - c - d
# => d <= 200 - 1 - 1 - 1 - 2
# <=> d <= 195 # 195 is divisible by 3
#
# Thus, the highest possible value of d is 195.

# Algorithmic time complexity: O(?)
# Algorithmic space complexity: O(?)

from timeit import default_timer as timer

# start benchmark
start = timer()

count = 0

for a in range(1, 16):
    for b in range(1, 61):
        for c in range(1, 181):
            # for loop with a step of 2
            for d in range(2, 194, 2):
                # for loop with a step of 3
                for e in range(3, 195, 3):
                    if a + b + c + d + e == 200 and 12 * a + 3 * b + c + d / 2 + e / 3 == 200:
                        print(a, b, c, d, e)
                        count += 1

print('count:', count)

# stop benchmark
end = timer()
duration = end - start
print('duration:', duration)

# 1 1 173 22 3
# 1 1 174 18 6
# 1 1 175 14 9
# ...
# 6 12 33 56 93
# 6 12 34 52 96
# 6 12 35 48 99
# ...
# 11 1 1 10 177
# 11 1 2 6 180
# 11 1 3 2 183
# count: 6627
# duration: 348.6189789220002

