# 100 énigmes mathématiques résolues avec python
# 2.04

# Analysis
#
# Let x be the integer part of the amount.
# Let y be the decimal part of the amount.
#
# To work with integer values instead of decimal values, we'll multiply
# the values by 100:
#
# x = integer_part * 100
# y = decimal_part * 100
# news_paper = 1.3 * 100 = 130
#
# Let's write the equation of the question.
#
# y * 100 + x / 100 - 130 = 2 * (x + y)
# <=> y * 100 + x / 100 - 130 = 2 * x + 2 * y
# <=> 100 * y + x / 100 - 130 - 2 * x - 2 * y = 0
# <=> 100 * y - 2 * y + x / 100 - 2 * x - 130 = 0
# <=> 98 * y + x / 100 - 100 * (2 * x) / 100 - 130 = 0
# <=> 98 * y + x / 100 - (200 * x) / 100 - 130 = 0
# <=> 98 * y + (x - 200 * x) / 100 - 130 = 0
# <=> 98 * y + (- 199 * x) / 100 - 130 = 0
# <=> 98 * y + (- 199 / 100) * x - 130 = 0
# <=> 98 * y - (199 / 100) * x - 130 = 0

from timeit import default_timer as timer

# start benchmark
start = timer()

stop = False

for x in range(100, 10000):
    for y in range(1, 100):
        amount = x + y
        amount /= 100

        equation = 98 * y - (199 / 100) * x - 130
        # print(equation)

        if equation == 0:
            print(f'{amount = }')
            stop = True
            break

    if stop:
        break

# stop benchmark
end = timer()
duration = end - start
print('duration:', duration)

# amount = 22.46
# duration: 0.13737126200430794

