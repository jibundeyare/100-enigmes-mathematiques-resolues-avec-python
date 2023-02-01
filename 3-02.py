# 100 énigmes mathématiques résolues avec python
# 3.02

# Algorithmic time complexity: O(n ** 2)
# Algorithmic space complexity: O(?)

from timeit import default_timer as timer

# start benchmark
start = timer()

multiplicative_persistence_number = None
multiplicative_persistence_steps = 0

for number in range(10, 1000000):
    steps = 0
    product = 1
    digits = number

    while True:
        while digits != 0:
            digit = digits % 10
            digits //= 10
            product *= digit

            if product == 0:
                break

        steps += 1

        # @debug
        # print(number, product)

        if product < 10:
            break

        digits = product
        product = 1

    # @debug
    # if product != 0:
    #     print(f'{number = } {steps = } {product = }')

    if steps > multiplicative_persistence_steps:
        # @debug
        # print(f'{number = } {steps = } {product = }')

        multiplicative_persistence_steps = steps
        multiplicative_persistence_number = number

print(f'{multiplicative_persistence_number = }')
print(f'{multiplicative_persistence_steps = }')

# stop benchmark
end = timer()
duration = end - start
print('duration:', duration)

# multiplicative_persistence_number = 68889
# multiplicative_persistence_steps = 7
# duration: 4.356146065998473

