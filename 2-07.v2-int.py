# 100 énigmes mathématiques résolues avec python
# 2.07

# Analysis
#
# comic_price * comic_count + dvd_price * dvd_count + board_game_price * board_game_count = 1000
# <=> 100 * (comic_price * comic_count + dvd_price * dvd_count + board_game_price * board_game_count) = 100 * 1000
# <=> (100 * comic_price) * comic_count + (100 * dvd_price) * dvd_count + (100 * board_game_price) * board_game_count = 100000

# Algorithmic time complexity: O(n ** 3)
# Algorithmic space complexity: O(?)

from timeit import default_timer as timer

# start benchmark
start = timer()

total = 1000 * 100
comic_price = int(19.35 * 100)
dvd_price = int(24.55 * 100)
board_game_price = int(39.15 * 100)

for comic_count in range(int(total // comic_price), -1, -1):
    total_minus_comic = total - comic_price * comic_count

    for dvd_count in range(int(total_minus_comic // dvd_price), -1, -1):
        total_minus_comic_dvd = total_minus_comic - dvd_price * dvd_count

        for board_game_count in range(int(total_minus_comic_dvd // board_game_price), -1, -1):
            total_minus_comic_dvd_board_game = total_minus_comic_dvd - board_game_price * board_game_count

            # @debug
            # print('comic:', comic_count, 'dvd:', dvd_count, 'board_game:', board_game_count)
            # print('total_minus_comic_dvd_board_game:', total_minus_comic_dvd_board_game)
            # print()

            if total_minus_comic_dvd_board_game == 0:
                print('comic:', comic_count, 'dvd:', dvd_count, 'board_game:', board_game_count)

# stop benchmark
end = timer()
duration = end - start
print('duration:', duration)

# comic: 19 dvd: 13 board_game: 8
# duration: 0.003514074999998229

