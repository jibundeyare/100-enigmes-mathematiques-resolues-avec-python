# 100 énigmes mathématiques résolues avec python
# 2.17

# Analysis
#
# Letters: N, E, U, F, O, Z
# Number of letters: 6
#
# Each letter can represent 1 digit out of 10.
# But each letter must represent a different digits.
# So when 1 digit out of the 10 have been choosen for a letter, the
# next letter can represent only 1 digit out of 9. And so on.
#
# Maximum number of iterations needed to find a solution:
# 10 * 9 * 8 * 7 * 6 * 5 = 151200
#
# There's another contraint: the letters N, U and O can not represent
# 0 because they occupy the leftmost position. So these letters can not
# represent 1 digit ou of 10 but one less (e.g. only 1 digit out of 9).
#
# But the following computation gives a wrong number of iterations
# needed to find a solution:
# 9 * 9 * 7 * 7 * 5 * 5 = 99225
#
# To obtain the right number of iterations, we need to reorder the
# letters to the maximize the factorial.
#
# Letters: N, U, O, E, F, Z
#
# Precise number of iterations needed to find a solution:
# 9 * 8 * 7 * 7 * 6 * 5 = 105840
#
# We can create a formula to find the maximal number of
# iterations to find a solution.
#
# Let d be the number of possible digit one letter can represent.
# Let l be the number of letters.
# Let i be the maximal number of iterations to find a solution.
#
# This gives: i = d! / (d - l)!

# Algorithmic complexity: O(n!)

from timeit import default_timer as timer

# start benchmark
start = timer()

i = 0

for n in range(1, 10):
    for e in range(0, 10):
        if e == n:
            continue

        for u in range(1, 10):
            if u == n or u == e:
                continue

            for f in range(0, 10):
                if f == n or f == e or f == u:
                    continue

                for o in range(1, 10):
                    if o == n or o == e or o == u or o == f:
                        continue

                    for z in range(0, 10):
                        if z == n or z == e or z == u or z == f or z == o:
                            continue

                        neuf = n * 1000 + e * 100 + u * 10 + f
                        un = u * 10 + n
                        onze = o * 1000 + n * 100 + z * 10 + e

                        if neuf + un + un == onze:
                            print('n:', n)
                            print('e:', e)
                            print('u:', u)
                            print('f:', f)
                            print('o:', o)
                            print('z:', z)

                        i += 1

print('i:', i)

# stop benchmark
end = timer()
duration = end - start
print('duration:', duration)

# n: 1
# e: 9
# u: 8
# f: 7
# o: 2
# z: 4
# i: 105840
# duration: 0.25482987199984564

