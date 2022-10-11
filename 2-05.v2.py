# 100 énigmes mathématiques résolues avec python
# 2.05

# Analysis
#
# The square will contain the sum of all numbers from 1 to 16 :
#
# s = (n * (n + 1)) / 2
# s = (n / 2) * (n + 1)
# s = (16 / 2) * (16 + 1)
# s = 8 * 17
# s = 136
#
# This means that the total of all the numbers from each row of the
# square is equal to 136.
#
# We also know that the total of the numbers from one row is equal
# to the total of numbers of any other row. In other words, all the
# totals of the numbers of a row are equal.
#
# Thus the total of numbers of a row must be equal to 136 / 4 = 34.
#
# The total of the numbers of a diagonal is also 34. The rest of the
# numbers from the diagonal with the 3 and 4 in it, must sum up to
# 34 - (3 + 4) = 27.  This means we can test all the numbers from 5 to
# 16 and see which ones can sum up to 34.
#
# 27 - 5 = 22
# 27 - 6 = 21
# ...
#
# There are no 22, 21, ... in the list, which means the diagonal can not
# contain any 5, §, ....
#
# 27 - 11 = 16
# 27 - 12 = 15
# ...
# 27 - 16 = 11
#
# Now we have all the combinations we can try.
#
# For each combination, we can try to compute the rest of the rows the
# same way because we will also have two numbers per row.

# Algorithmic complexity: O(n ** 6)
#
# The algorithmic complexity is very bad. But acceptable for small
# values of n. At least it is much better than a factorial or an
# exponential growth.

from timeit import default_timer as timer

# start benchmark
start = timer()

def is_magic_square(rows):
    line1 = sum(rows[0])
    line2 = sum(rows[1])
    line3 = sum(rows[2])
    line4 = sum(rows[3])
    column1 = rows[0][0] + rows[1][0] + rows[2][0] + rows[3][0]
    column2 = rows[0][1] + rows[1][1] + rows[2][1] + rows[3][1]
    column3 = rows[0][2] + rows[1][2] + rows[2][2] + rows[3][2]
    column4 = rows[0][3] + rows[1][3] + rows[2][3] + rows[3][3]
    diagonal1 = rows[0][0] + rows[1][1] + rows[2][2] + rows[3][3]
    diagonal2 = rows[0][3] + rows[1][2] + rows[2][1] + rows[3][0]

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

max_value = 16
fixed_values = [1, 2, 3, 4]
total = 34
rows = [
    [0, 0, 1, 0],
    [0, 4, 0, 0],
    [2, 0, 0, 0],
    [0, 0, 0, 3],
]

differences = [0] * 6
used_values = fixed_values.copy()

# find diagonal 1 numbers
differences[0] = total - (rows[1][1] + rows[3][3])

for i in range(differences[0] - max_value, max_value + 1):
    i2 = differences[0] - i

    if i == i2 or i in used_values or i2 in used_values:
        continue

    if i < 1 or i2 < 1 or i2 > max_value:
        continue

    used_values.append(i)
    used_values.append(i2)

    rows[0][0] = i
    rows[2][2] = i2

    # find row 1 numbers
    differences[1] = total - (rows[0][0] + rows[0][2])

    for j in range(differences[1] - max_value, max_value + 1):
        j2 = differences[1] - j

        if j == j2 or j in used_values or j2 in used_values:
            continue

        if j < 1 or j2 < 1 or j2 > max_value:
            continue

        used_values.append(j)
        used_values.append(j2)

        rows[0][1] = j
        rows[0][3] = j2

        # find row 3 numbers
        differences[2] = total - (rows[2][0] + rows[2][2])

        for k in range(differences[2] - max_value, max_value + 1):
            k2 = differences[2] - k

            if k == k2 or k in used_values or k2 in used_values:
                continue

            if k < 1 or k2 < 1 or k2 > max_value:
                continue

            used_values.append(k)
            used_values.append(k2)

            rows[2][1] = k
            rows[2][3] = k2

            # find diagonal 2 numbers
            differences[3] = total - (rows[0][3] + rows[2][1])

            for l in range(differences[3] - max_value, max_value + 1):
                l2 = differences[3] - l

                if l == l2 or l in used_values or l2 in used_values:
                    continue

                if l < 1 or l2 < 1 or l2 > max_value:
                    continue

                used_values.append(l)
                used_values.append(l2)

                rows[1][2] = l
                rows[3][0] = l2

                # find row 2 numbers
                differences[4] = total - (rows[1][1] + rows[1][2])

                for m in range(differences[4] - max_value, max_value + 1):
                    m2 = differences[4] - m

                    if m == m2 or m in used_values or m2 in used_values:
                        continue

                    if m < 1 or m2 < 1 or m2 > max_value:
                        continue

                    used_values.append(m)
                    used_values.append(m2)

                    rows[1][0] = m
                    rows[1][3] = m2

                    # find row 4 numbers
                    differences[5] = total - (rows[3][0] + rows[3][3])

                    for n in range(differences[5] - max_value, max_value + 1):
                        n2 = differences[5] - n

                        if n == n2 or n in used_values or n2 in used_values:
                            continue

                        if n < 1 or n2 < 1 or n2 > max_value:
                            continue

                        # We don't append n and n2 to used_values list because
                        # there are no more upper loop.
                        # It is necessary to have same number of append() and pop()
                        # function calls. Otherwise, unused values will stay in
                        # the used_values list.

                        rows[3][1] = n
                        rows[3][2] = n2

                        if is_magic_square(rows):
                            for row in rows:
                                print(row)

                            print()

                    used_values.pop()
                    used_values.pop()

                used_values.pop()
                used_values.pop()

            used_values.pop()
            used_values.pop()

        used_values.pop()
        used_values.pop()

    used_values.pop()
    used_values.pop()

# stop benchmark
end = timer()
duration = end - start
print('duration:', duration)

# [11, 8, 1, 14]
# [15, 4, 5, 10]
# [2, 9, 16, 7]
# [6, 13, 12, 3]
#
# [15, 8, 1, 10]
# [11, 4, 5, 14]
# [2, 13, 12, 7]
# [6, 9, 16, 3]
#
# duration: 0.013134819000697462

