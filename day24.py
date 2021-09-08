# --- Day 24: Lobby Layout ---
#
# Your raft makes it to the tropical island; it turns out that the small crab was an excellent navigator. You make your way to the resort.
#
# As you enter the lobby, you discover a small problem: the floor is being renovated. You can't even reach the check-in desk until they've finished installing the new tile floor.
#
# The tiles are all hexagonal; they need to be arranged in a hex grid with a very specific color pattern. Not in the mood to wait, you offer to help figure out the pattern.
#
# The tiles are all white on one side and black on the other. They start with the white side facing up. The lobby is large enough to fit whatever pattern might need to appear there.
#
# A member of the renovation crew gives you a list of the tiles that need to be flipped over (your puzzle input). Each line in the list identifies a single tile that needs to be flipped by giving a series of steps starting from a reference tile in the very center of the room. (Every line starts from the same reference tile.)
#
# Because the tiles are hexagonal, every tile has six neighbors: east, southeast, southwest, west, northwest, and northeast. These directions are given in your list, respectively, as e, se, sw, w, nw, and ne. A tile is identified by a series of these directions with no delimiters; for example, esenee identifies the tile you land on if you start at the reference tile and then move one tile east, one tile southeast, one tile northeast, and one tile east.
#
# Each time a tile is identified, it flips from white to black or from black to white. Tiles might be flipped more than once. For example, a line like esew flips a tile immediately adjacent to the reference tile, and a line like nwwswee flips the reference tile itself.
#
# Here is a larger example:
#
# sesenwnenenewseeswwswswwnenewsewsw
# neeenesenwnwwswnenewnwwsewnenwseswesw
# seswneswswsenwwnwse
# nwnwneseeswswnenewneswwnewseswneseene
# swweswneswnenwsewnwneneseenw
# eesenwseswswnenwswnwnwsewwnwsene
# sewnenenenesenwsewnenwwwse
# wenwwweseeeweswwwnwwe
# wsweesenenewnwwnwsenewsenwwsesesenwne
# neeswseenwwswnwswswnw
# nenwswwsewswnenenewsenwsenwnesesenew
# enewnwewneswsewnwswenweswnenwsenwsw
# sweneswneswneneenwnewenewwneswswnese
# swwesenesewenwneswnwwneseswwne
# enesenwswwswneneswsenwnewswseenwsese
# wnwnesenesenenwwnenwsewesewsesesew
# nenewswnwewswnenesenwnesewesw
# eneswnwswnwsenenwnwnwwseeswneewsenese
# neswnwewnwnwseenwseesewsenwsweewe
# wseweeenwnesenwwwswnew
#
# In the above example, 10 tiles are flipped once (to black), and 5 more are flipped twice (to black, then back to white). After all of these instructions have been followed, a total of 10 tiles are black.
#
# Go through the renovation crew's list and determine which tiles they need to flip. After all of the instructions have been followed, how many tiles are left with the black side up?


from copy import deepcopy
from collections import deque

with open('day24input.txt') as input_file:
    lines = input_file.read().splitlines()

# lines = [
#     'sesenwnenenewseeswwswswwnenewsewsw',
#     'neeenesenwnwwswnenewnwwsewnenwseswesw',
#     'seswneswswsenwwnwse',
#     'nwnwneseeswswnenewneswwnewseswneseene',
#     'swweswneswnenwsewnwneneseenw',
#     'eesenwseswswnenwswnwnwsewwnwsene',
#     'sewnenenenesenwsewnenwwwse',
#     'wenwwweseeeweswwwnwwe',
#     'wsweesenenewnwwnwsenewsenwwsesesenwne',
#     'neeswseenwwswnwswswnw',
#     'nenwswwsewswnenenewsenwsenwnesesenew',
#     'enewnwewneswsewnwswenweswnenwsenwsw',
#     'sweneswneswneneenwnewenewwneswswnese',
#     'swwesenesewenwneswnwwneseswwne',
#     'enesenwswwswneneswsenwnewswseenwsese',
#     'wnwnesenesenenwwnenwsewesewsesesew',
#     'nenewswnwewswnenesenwnesewesw',
#     'eneswnwswnwsenenwnwnwwseeswneewsenese',
#     'neswnwewnwnwseenwseesewsenwsweewe',
#     'wseweeenwnesenwwwswnew'
# ]


def move_to_tile(direction, current_pos):
    if direction == 'e':
        current_pos = (current_pos[0] + 2, current_pos[1])
    elif direction == 'w':
        current_pos = (current_pos[0] - 2, current_pos[1])
    elif direction == 'ne':
        current_pos = (current_pos[0] + 1, current_pos[1] + 1)
    elif direction == 'nw':
        current_pos = (current_pos[0] - 1, current_pos[1] + 1)
    elif direction == 'se':
        current_pos = (current_pos[0] + 1, current_pos[1] - 1)
    elif direction == 'sw':
        current_pos = (current_pos[0] - 1, current_pos[1] - 1)
    return current_pos


tiles_flipped = deque()

for line in lines:
    directions = deque(line)
    pos = [0, 0]
    while directions:
        direction = directions.popleft()
        if direction not in ('e', 'w'):
            direction += directions.popleft()
        pos = move_to_tile(direction, pos)
    if pos in tiles_flipped:
        tiles_flipped.remove(pos)
    else:
        tiles_flipped.append(pos)

print(f'Tiles with the black side up: {len(tiles_flipped)}')
print('---------')


# --- Part Two ---
#
# The tile floor in the lobby is meant to be a living art exhibit. Every day, the tiles are all flipped according to the following rules:
#
#     Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
#     Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black.
#
# Here, tiles immediately adjacent means the six tiles directly touching the tile in question.
#
# The rules are applied simultaneously to every tile; put another way, it is first determined which tiles need to be flipped, then they are all flipped at the same time.
#
# In the above example, the number of black tiles that are facing up after the given number of days has passed is as follows:
#
# Day 1: 15
# Day 2: 12
# Day 3: 25
# Day 4: 14
# Day 5: 23
# Day 6: 28
# Day 7: 41
# Day 8: 37
# Day 9: 49
# Day 10: 37
#
# Day 20: 132
# Day 30: 259
# Day 40: 406
# Day 50: 566
# Day 60: 788
# Day 70: 1106
# Day 80: 1373
# Day 90: 1844
# Day 100: 2208
#
# After executing this process a total of 100 times, there would be 2208 black tiles facing up.
#
# How many tiles will be black after 100 days?


cal_list = [(1, 1), (2, 0), (1, -1), (-1, -1), (-2, 0), (-1, 1)]


def find_immediate_neighbours(tile):
    return [(tile[0]+cal[0], tile[1]+cal[1]) for cal in cal_list]


tiles_to_test = []

for tile in tiles_flipped:
    list_immediate_neighbours = find_immediate_neighbours(tile)
    for tile in list_immediate_neighbours:
        if tile not in tiles_to_test:
            tiles_to_test.append(tile)
    if tile not in tiles_to_test:
        tiles_to_test.append(tile)

print(f'Day 0: {len(tiles_flipped)}')
for i in range(100):
    tiles_flipped_next = deepcopy(deque(tiles_flipped))
    for tile in tiles_to_test:
        list_immediate_neighbours = find_immediate_neighbours(tile)
        neighbour_flipped_count = 0
        for neighbour in list_immediate_neighbours:
            if neighbour in tiles_flipped:
                neighbour_flipped_count += 1
        if tile in tiles_flipped:
            if neighbour_flipped_count == 0 or neighbour_flipped_count > 2:
                tiles_flipped_next.remove(tile)
        else:
            if neighbour_flipped_count == 2:
                tiles_flipped_next.append(tile)
    tiles_to_test = deque()
    for tile in tiles_flipped_next:
        list_immediate_neighbours = find_immediate_neighbours(tile)
        for tile_neighbour in list_immediate_neighbours:
            tiles_to_test.append(tile_neighbour)
        tiles_to_test.append(tile)
    tiles_to_test = set(tiles_to_test)
    tiles_flipped = set(tiles_flipped_next)
    if (i + 1) % 10 == 0:
        print(f'Day {i+1}: {len(tiles_flipped)}')
