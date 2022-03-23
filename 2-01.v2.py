# 100 énigmes mathématiques résolues avec python
# 2.01

# Analysis
#
# digit:    123456789
# index:    012345678
#
# All three operators must have an operand on the left and on the right.
# Therefore, the first operator must be on index 1 at least, the third
# operator can be on index 8 at most and the second operator must be in
# between.
#
# Let's find all the possible positions of the three operators.
#
# - first operator can only have positions 1 to 6, where position n is
#   right before element with index n
# - second operator can only have positions 2 to 7
# - third operator can only have positions 3 to 8
#
# Now that we have all the possible positions of the three operators,
# we can create all the possible sums of the nine digits.

# Algorithmic complexity: O(n**5)

from timeit import default_timer as timer

# start benchmark
start = timer()

digits = '123456789'

for i in range(1, 7):
    for j in range(i + 1, 8):
        for k in range(j + 1, 9):
            # @debug
            # print(i, j, k)

            part_1 = int(digits[0:i])
            part_2 = int(digits[i:j])
            part_3 = int(digits[j:k])
            part_4 = int(digits[k:])

            # @debug
            # print(part_1, part_2, part_3, part_4)

            for operators in range(0, 8):
                operators = format(operators, '03b')
                operators = operators.replace('0', '+')
                operators = operators.replace('1', '-')

                # @debug
                # print(operators)

                my_sum = part_1

                if operators[0] == '+':
                    my_sum += part_2
                else:
                    my_sum -= part_2

                if operators[1] == '+':
                    my_sum += part_3
                else:
                    my_sum -= part_3

                if operators[2] == '+':
                    my_sum += part_4
                else:
                    my_sum -= part_4

                if my_sum == 100:
                    print(part_1, operators[0], part_2, operators[1], part_3, operators[2], part_4, '= 100')

# stop benchmark
end = timer()
duration = end - start
print('duration:', duration)

# 123 - 45 - 67 + 89 = 100
# duration: 0.0017184010066557676

