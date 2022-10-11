# 100 énigmes mathématiques résolues avec python
# 2.09

# Algorithmic time complexity: O(n ** 2)
# Algorithmic space complexity: O(?)

from timeit import default_timer as timer

# start benchmark
start = timer()

numbers = [i for i in range(1, 21)]

while len(numbers) > 1:
    numbers = [numbers[i] + numbers[i + 1] for i in range(0, len(numbers) - 1)]

    # @debug
    # print(numbers)

print(numbers)

# stop benchmark
end = timer()
duration = end - start
print('duration:', duration)

# [5505024]
# duration: 0.0001423110006726347

