# 100 énigmes mathématiques résolues avec python
# 2.05

# Analysis
#
# Let's try brute force.
#
# Find all permutations of the numbers from 5 to 16 :
#
# 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16
# 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 15
# 5, 6, 7, 8, 9, 10, 11, 12, 13, 16, 14, 15
# 5, 6, 7, 8, 9, 10, 11, 12, 13, 16, 15, 14
# ...
#
# For each permutation, insert the predefined values and compute the sum
# of the rows, columns and diagonals to see if the current configuration
# is a magic square or not.
#
# This approach is totaly inefficient because there are too many
# possible permutations :
#
# 16 * 15 * 14 * 13 * 12 * 11 * 10 * 9 * 8 * 7 * 6 * 5 = 871 782 912 000
#
# Which is approximately 871 * 10^8.
#
# This is a factorial. Which is totaly a worst case scenario.

# Algorithmic complexity: O(n!)

from timeit import default_timer as timer

# start benchmark
start = timer()

def build_complete_data(constant_data, variable_data):
    return \
        variable_data[0:2] \
        + [constant_data[0]] \
        + variable_data[2:4] \
        + [constant_data[1]] \
        + variable_data[4:6] \
        + [constant_data[2]] \
        + variable_data[6:9] \
        + variable_data[9:12] \
        + [constant_data[3]]

def is_magic_square(data):
    line1 = data[0] + data[1] + data[2] + data[3]
    line2 = data[4] + data[5] + data[6] + data[7]
    line3 = data[8] + data[9] + data[10] + data[11]
    line4 = data[12] + data[13] + data[14] + data[15]
    column1 = data[0] + data[4] + data[8] + data[12]
    column2 = data[1] + data[5] + data[9] + data[13]
    column3 = data[2] + data[6] + data[10] + data[14]
    column4 = data[3] + data[7] + data[11] + data[15]
    diagonal1 = data[0] + data[5] + data[10] + data[15]
    diagonal2 = data[3] + data[6] + data[9] + data[12]

    if line1 == line2 \
        and line1 == line3 \
        and line1 == line4 \
        and line1 == column1 \
        and line1 == column2 \
        and line1 == column3 \
        and line1 == column4 \
        and line1 == diagonal1 \
        and line1 == diagonal2:
        return True

    return False

def permute_data(data, positions):
    new_data = [None] * len(data)

    for old_position, new_position in enumerate(positions):
        new_data[new_position] = data[old_position]

    return new_data

constant_data = [1, 4, 2, 3]
variable_data = [
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
]

complete_data = build_complete_data(constant_data, variable_data)

data_length = len(complete_data)
possible_positions = [i for i in range(0, data_length)]
# this list contains a permutation of the possible positions of the data
current_positions = possible_positions.copy()
last_index = data_length - 1

# start looking for next incrementable value from the end of the list
i = last_index

permuted_data = permute_data(complete_data, current_positions)

# @debug
# print(current_positions)
# print(permuted_data)

if is_magic_square(permuted_data):
    print(permuted_data)

# @warning don't store the data to spare memory
# permutations.append(current_positions.copy())

while i >= 0:
    # @debug
    # print('i:', i)

    found = False

    # ensure current position next value is not greater than the maximum possible value
    for next_value in range(current_positions[i] + 1, data_length):
        # ensure current position next value is not already used in a previous position
        if next_value not in current_positions[0:i]:
            found = True

            # found current position next value
            current_positions[i] = next_value

            # @debug
            # print(f'found current position next value: {i} = {current_positions[i]}')
            # print(f'increment current_positions[{i}]')
            # print('current_positions:', current_positions)

            # fill following positions possible values
            for j in range(i + 1, data_length):
                unavailable_values = current_positions[0:j]

                # @debug
                # print(f'look for usable value from {j}')
                # print('unavailable_values:', unavailable_values)

                for k in possible_positions:
                    # @debug
                    # print('k:', k)
                    if k not in unavailable_values:
                        current_positions[j] = k

                        # @debug
                        # print(f'found usable value: {j} = {k}')
                        # print('current_positions:', current_positions)

                        break

            permuted_data = permute_data(complete_data, current_positions)

            # @debug
            # print(current_positions)
            print(permuted_data)

            if is_magic_square(permuted_data):
                print(permuted_data)

            # @warning don't store the data to spare memory
            # permutations.append(current_positions.copy())

            # restart looking for next incrementable value from the end of the list
            i = last_index

        if found:
            break

    if not found:
        # current position next value is not available
        # continue looking for next incrementable value one position on the left
        i -= 1

# stop benchmark
end = timer()
duration = end - start
print('duration:', duration)

