# 100 énigmes mathématiques résolues avec python
# 1.10

# Algorithmic complexity: O(n³)

from timeit import default_timer as timer

# start benchmark
start = timer()

scores = {}

for i in range(2, 100):
    for j in range(2, 100):
        for k in range(j, 100):
            if i ** 2 == j ** 2 + k ** 2:
                # @debug
                # print('i:', i, 'j:', j, 'k:', k)

                if i not in scores:
                    scores[i] = 1
                else:
                    scores[i] += 1

max_score = max(scores, key=scores.get)
print('max_score:', max_score, 'score:', scores[max_score])

# stop benchmark
end = timer()
duration = end - start
print('duration:', duration)

# max_score: 65 score: 4
# duration: 0.4894148089988448

