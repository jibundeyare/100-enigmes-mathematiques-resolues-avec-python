# 100 énigmes mathématiques résolues avec python
# 2.01

# Analysis
#
# First, let's create the list of all combination of length of the four
# numbers to sum. The sum of the lengths always equals to 9 because
# we use only 9 digits.
# For such a sum, no number should be greater than 6.
# To avoid computing numbers greater than 9, we verify some conditions:
# - if the sum of the first two numbers is greater than 7, then the
#   final sum will be greater than 9.
# - if the sum of the first three numbers is greater than 8, then the
#   final sum will be greater than 9.
# - and lastly, we verify that the final sum of the four numbers is not
#   greater or lower than 9.
#
# Example:
# - if we sum 1 + 2 + 3 + 456789 we have four numbers of length 1, 1, 1
#   and 6
# - if we sum 12 + 34 + 56 + 789 we have four numbers of length 2, 2, 2
#   and 3
# - ...
#
# Then it's possible to use the binary form of the numbers from 0 to
# 2 ** 4 - 1 (ie 7) to find all the possible permutations of three +
# and - symbols.
#
# Example:
# - 000 is +++
# - 001 is ++-
# - ...
#
# Now we just need to verify wich sums give 100.

# Algorithmic complexity: O(n**5)

from timeit import default_timer as timer

# start benchmark
start = timer()

digits = '123456789'

for i in range(1, 7):
    for j in range(1, 7):
        if i + j > 7:
            break

        for k in range(1, 7):
            if i + j + k > 8:
                break

            for l in range(1, 7):
                if i + j + k + l > 9:
                    break
                elif i + j + k + l < 9:
                    continue
                else:
                    # @debug
                    # print(i, j, k , l)

                    # get the four numbers
                    i_part = int(digits[0:i])
                    j_part = int(digits[i:i + j])
                    k_part = int(digits[i + j:i + j + k])
                    l_part = int(digits[i + j + k:])

                    # @debug
                    # print(i_part, j_part, k_part, l_part)

                    for operators in range(0, 8):
                        operators = format(operators, '03b')
                        operators = operators.replace('0', '+')
                        operators = operators.replace('1', '-')

                        # @debug
                        # print(operators)

                        my_sum = i_part

                        if operators[0] == '+':
                            my_sum += j_part
                        else:
                            my_sum -= j_part

                        if operators[1] == '+':
                            my_sum += k_part
                        else:
                            my_sum -= k_part

                        if operators[2] == '+':
                            my_sum += l_part
                        else:
                            my_sum -= l_part

                        if my_sum == 100:
                            print(i_part, operators[0], j_part, operators[1], k_part, operators[2], l_part, '= 100')

# stop benchmark
end = timer()
duration = end - start
print('duration:', duration)

# 123 - 45 - 67 + 89 = 100
# duration: 0.0013107599952491

