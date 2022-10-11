# 100 énigmes mathématiques résolues avec python
# 2.10

# Analysis
#
# ...

# Algorithmic time complexity: O(n ** 3)
# Algorithmic space complexity: O(n ** 2)

from timeit import default_timer as timer

# start benchmark
start = timer()

amount = 100
coins = [5, 2, 1]

all_compositions = {}

for current_amount in range(0, amount + 1):
    all_compositions[current_amount] = []

    for coin in coins:
        composition_root = []

        if coin <= current_amount:
            remainder = current_amount - coin
            composition_root.append(coin)

            if remainder:
                for sub_composition in all_compositions[remainder]:
                    # add sub composition only if the first coin of the sub composition is smaller than current coin
                    # this avoids having duplicates like [2, 1] and [1, 2]
                    if sub_composition[0] <= coin:
                        all_compositions[current_amount].append(composition_root + sub_composition)
            else:
                all_compositions[current_amount].append(composition_root)

count = len(all_compositions[amount])
print(f'{count=}')

# stop benchmark
end = timer()
duration = end - start
print('duration:', duration)

# count=541
# duration: 0.03146210900013102

