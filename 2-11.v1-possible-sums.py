# 100 énigmes mathématiques résolues avec python
# 2.11

# Analysis
#
# Each score set has a lowest initial possible score.
# This is 3 for rugby and 13 for the quizz.
# Let n be the lowest initial possible score for a game G.
# Notice that if we can obtain n consecutive numbers from the sum of the
# possible scores from the initial set, we can create all the next
# numbers.
#
# x + 1 : possible_sum_a
# x + 2 : possible_sum_b
# x + 3 : possible_sum_c
# ...
# x + n : possible_sum_n
# x + 1 + n : possible_sum_a + n
# x + 2 + n : possible_sum_b + n
# x + 3 + n : possible_sum_c + n
# ...
# x + n + n : possible_sum_n + n
#
# Let's test with the following initial scores:
#
# scores = [3, 5, 7]
#
# 1 : ∅
# 2 : ∅
# 3 : 3
# 4 : ∅
# 5 : 5         1 consecutive numbers
# 6 : 3 + 3     2 consecutive numbers
# 7 : 7         3 consecutive numbers
# ...           from here it's possible to obtain any number by adding 3
#               to the number that is 3 positions behind
#
# Now let's test with the following initial scores:
#
# scores = [11, 12, 13]
#
# 1 : ∅
# 2 : ∅
# 3 : ∅
# 4 : ∅
# 5 : ∅
# 6 : ∅
# 7 : ∅
# 8 : ∅
# 9 : ∅
# 10 : ∅
# 11 : 11
# 12 : 12
# 13 : 13
# 14 : ∅
# 15 : ∅
# 16 : ∅
# 17 : ∅
# 18 : ∅
# 19 : ∅
# 20 : ∅
# 21 : ∅
# 22 : 11 + 11
# 23 : 12 + 11
# 24 : 12 + 12
# 25 : 13 + 12
# 26 : 13 + 13
# 27 : ∅
# 28 : ∅
# 29 : ∅
# 30 : ∅
# 31 : ∅
# 32 : ∅
# 33 : 22 + 11
# 34 : 22 + 12
# 35 : 22 + 13, 24 + 11
# 36 : 24 + 12
# 37 : 24 + 13
# 38 : 26 + 12
# 39 : 26 + 13
# 40 : ∅
# 41 : ∅
# 42 : ∅
# 43 : ∅
# 44 : 33 + 11
# 45 : 33 + 12
# 46 : 33 + 13
# 47 : 36 + 11
# 48 : 37 + 11
# 49 : 38 + 11
# 50 : 39 + 11
# 51 : 39 + 12
# 52 : 39 + 13
# 53 : ∅
# 54 : ∅
# 55 : 44 + 11  1 consecutive numbers
# 56 : 45 + 11  2 consecutive numbers
# 57 : 46 + 11  3 consecutive numbers
# 58 : 47 + 11  4 consecutive numbers
# 59 : 48 + 11  5 consecutive numbers
# 60 : 49 + 11  6 consecutive numbers
# 61 : 50 + 11  7 consecutive numbers
# 62 : 51 + 11  8 consecutive numbers
# 63 : 52 + 11  9 consecutive numbers
# 64 : 52 + 12  10 consecutive numbers
# 65 : 51 + 13  11 consecutive numbers
# ...           from here it's possible to obtain any number by adding
#               11 to the number that is 11 positions behind

# Algorithmic time complexity: O(n)
# Algorithmic space complexity: O(n)

from timeit import default_timer as timer

# start benchmark
start = timer()

possible_sums = [11, 12, 13]

consecutive_numbers = 3
highest_impossible_sum = 10
i = 14

while consecutive_numbers < 11:
    if i - 11 in possible_sums \
    or i - 12 in possible_sums \
    or i - 13 in possible_sums:
        possible_sums.append(i)
        consecutive_numbers += 1
    else:
        highest_impossible_sum = i
        consecutive_numbers = 0

    i += 1

print(possible_sums)
print(f'{highest_impossible_sum=}')

# stop benchmark
end = timer()
duration = end - start
print(f'{duration=}')

# [11, 12, 13, 22, 23, 24, 25, 26, 33, 34, 35, 36, 37, 38, 39, 44, 45, 46, 47, 48, 49, 50, 51, 52, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65]
# highest_impossible_sum=54
# duration=0.0001393770071445033

