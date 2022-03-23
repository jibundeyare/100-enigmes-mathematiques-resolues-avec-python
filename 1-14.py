# 100 énigmes mathématiques résolues avec python
# 1.14

# Mise en équation
#
# x = a ** 2 + 39
# x = (a + 1) ** 2 - 50
#
# Résolution
#
# a ** 2 + 39 = (a + 1) ** 2 - 50
# (a + 1) ** 2 - a ** 2 = 39 + 50
# (a + 1) ** 2 - a ** 2 = 89
#
# On utilise l'identité remarquable :
# a ** 2 - b ** 2 = (a + b) * (a - b)
# pour factoriser la partie gauche de l'équation
#
# ((a + 1) + a) * ((a + 1) - a) = 89
# (a + 1 + a) * (a + 1 - a) = 89
# (2 * a + 1) * 1 = 89
# 2 * a + 1 = 89
# 2 * a = 89 - 1
# 2 * a = 88
# a = 88 / 2
# a = 44
#
# Vérification
#
# x1 = a ** 2 + 39 = 44 ** 2 + 39 = 1975
# x2 = (a + 1) ** 2 - 50 = (44 + 1) ** 2 - 50 = 1975
# x1 = x2
# x = 1975 cqfd
#
# Algorithmic complexity: O(0)

from timeit import default_timer as timer

# start benchmark
start = timer()

# stop benchmark
end = timer()
duration = end - start
print('duration:', duration)

# duration: 1.9919825717806816e-06

