# 100 énigmes mathématiques résolues avec python
# 1.17

# Analysis
#
# The lowest square number that we can build is necessarily greater than
# 1 + 2 = 3.
#
# The largest square number that we can build is necessarily lower than
# 14 + 15 = 29.
#
# Let's generate the list of all square numbers lower than 29.
#
# The list of the possible square numbers is very short: 4, 9, 16 and 25.
#
# Thus, for any permutation of the list of integers from 1 to 15, the
# sum of two consecutive numbers must be contained in the list of
# possible squares.

# Algorithmic complexity: O(n³)

from timeit import default_timer as timer

# start benchmark
start = timer()

numbers = [x for x in range(1, 16)]

first_n = numbers[0]
second_n = numbers[0]
last_n = numbers[-1]
second_to_last_n = numbers[-2]

lower_limit = int((first_n + second_n) ** (1 / 2)) + 1
upper_limit = int((last_n + second_to_last_n) ** (1 / 2))

squares = [x ** 2 for x in range(lower_limit, upper_limit + 1)]

print('lower_limit:', lower_limit)
print('upper_limit:', upper_limit)
print('squares:', squares)
print()

sequences = [[x] for x in numbers]

while True:
    next_sequences = []

    for sequence in sequences:
        sub_sequences = []

        for number in numbers:
            if number not in sequence and sequence[-1] + number in squares:
                new_sequence = list(sequence)
                new_sequence.append(number)
                sub_sequences.append(new_sequence)

        next_sequences.extend(sub_sequences)

    if not next_sequences:
        break

    sequences = next_sequences

    # @debug
    # print(sequences)
    # print()

for sequence in sequences:
    print('sequence:', sequence)
    print('len sequence:', len(sequence))
    print()

# stop benchmark
end = timer()
duration = end - start
print('duration:', duration)

# lower_limit: 2
# upper_limit: 5
# squares: [4, 9, 16, 25]
#
# sequence: [8, 1, 15, 10, 6, 3, 13, 12, 4, 5, 11, 14, 2, 7, 9]
# len sequence: 15
#
# sequence: [9, 7, 2, 14, 11, 5, 4, 12, 13, 3, 6, 10, 15, 1, 8]
# len sequence: 15
#
# duration: 0.0024712829617783427

