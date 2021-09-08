# --- Day 20: Jurassic Jigsaw ---
#
# The high-speed train leaves the forest and quickly carries you south. You can even see a desert in the distance! Since you have some spare time, you might as well see if there was anything interesting in the image the Mythical Information Bureau satellite captured.
#
# After decoding the satellite messages, you discover that the data actually contains many small images created by the satellite's camera array. The camera array consists of many cameras; rather than produce a single square image, they produce many smaller square image tiles that need to be reassembled back into a single image.
#
# Each camera in the camera array returns a single monochrome image tile with a random unique ID number. The tiles (your puzzle input) arrived in a random order.
#
# Worse yet, the camera array appears to be malfunctioning: each image tile has been rotated and flipped to a random orientation. Your first task is to reassemble the original image by orienting the tiles so they fit together.
#
# To show how the tiles should be reassembled, each tile's image data includes a border that should line up exactly with its adjacent tiles. All tiles have this border, and the border lines up exactly when the tiles are both oriented correctly. Tiles at the edge of the image also have this border, but the outermost edges won't line up with any other tiles.
#
# For example, suppose you have the following nine tiles:
#
# Tile 2311:
# ..##.#..#.
# ##..#.....
# #...##..#.
# ####.#...#
# ##.##.###.
# ##...#.###
# .#.#.#..##
# ..#....#..
# ###...#.#.
# ..###..###
#
# Tile 1951:
# #.##...##.
# #.####...#
# .....#..##
# #...######
# .##.#....#
# .###.#####
# ###.##.##.
# .###....#.
# ..#.#..#.#
# #...##.#..
#
# Tile 1171:
# ####...##.
# #..##.#..#
# ##.#..#.#.
# .###.####.
# ..###.####
# .##....##.
# .#...####.
# #.##.####.
# ####..#...
# .....##...
#
# Tile 1427:
# ###.##.#..
# .#..#.##..
# .#.##.#..#
# #.#.#.##.#
# ....#...##
# ...##..##.
# ...#.#####
# .#.####.#.
# ..#..###.#
# ..##.#..#.
#
# Tile 1489:
# ##.#.#....
# ..##...#..
# .##..##...
# ..#...#...
# #####...#.
# #..#.#.#.#
# ...#.#.#..
# ##.#...##.
# ..##.##.##
# ###.##.#..
#
# Tile 2473:
# #....####.
# #..#.##...
# #.##..#...
# ######.#.#
# .#...#.#.#
# .#########
# .###.#..#.
# ########.#
# ##...##.#.
# ..###.#.#.
#
# Tile 2971:
# ..#.#....#
# #...###...
# #.#.###...
# ##.##..#..
# .#####..##
# .#..####.#
# #..#.#..#.
# ..####.###
# ..#.#.###.
# ...#.#.#.#
#
# Tile 2729:
# ...#.#.#.#
# ####.#....
# ..#.#.....
# ....#..#.#
# .##..##.#.
# .#.####...
# ####.#.#..
# ##.####...
# ##..#.##..
# #.##...##.
#
# Tile 3079:
# #.#.#####.
# .#..######
# ..#.......
# ######....
# ####.#..#.
# .#...#.##.
# #.#####.##
# ..#.###...
# ..#.......
# ..#.###...
#
# By rotating, flipping, and rearranging them, you can find a square arrangement that causes all adjacent borders to line up:
#
# #...##.#.. ..###..### #.#.#####.
# ..#.#..#.# ###...#.#. .#..######
# .###....#. ..#....#.. ..#.......
# ###.##.##. .#.#.#..## ######....
# .###.##### ##...#.### ####.#..#.
# .##.#....# ##.##.###. .#...#.##.
# #...###### ####.#...# #.#####.##
# .....#..## #...##..#. ..#.###...
# #.####...# ##..#..... ..#.......
# #.##...##. ..##.#..#. ..#.###...
#
# #.##...##. ..##.#..#. ..#.###...
# ##..#.##.. ..#..###.# ##.##....#
# ##.####... .#.####.#. ..#.###..#
# ####.#.#.. ...#.##### ###.#..###
# .#.####... ...##..##. .######.##
# .##..##.#. ....#...## #.#.#.#...
# ....#..#.# #.#.#.##.# #.###.###.
# ..#.#..... .#.##.#..# #.###.##..
# ####.#.... .#..#.##.. .######...
# ...#.#.#.# ###.##.#.. .##...####
#
# ...#.#.#.# ###.##.#.. .##...####
# ..#.#.###. ..##.##.## #..#.##..#
# ..####.### ##.#...##. .#.#..#.##
# #..#.#..#. ...#.#.#.. .####.###.
# .#..####.# #..#.#.#.# ####.###..
# .#####..## #####...#. .##....##.
# ##.##..#.. ..#...#... .####...#.
# #.#.###... .##..##... .####.##.#
# #...###... ..##...#.. ...#..####
# ..#.#....# ##.#.#.... ...##.....
#
# For reference, the IDs of the above tiles are:
#
# 1951    2311    3079
# 2729    1427    2473
# 2971    1489    1171
#
# To check that you've assembled the image correctly, multiply the IDs of the four corner tiles together. If you do this with the assembled tiles from the example above, you get 1951 * 3079 * 2971 * 1171 = 20899048083289.
#
# Assemble the tiles into an image. What do you get if you multiply together the IDs of the four corner tiles?

import os
import re
from time import sleep
from math import sqrt, prod

with open('day20input.txt') as input_file:
    lines = input_file.read().splitlines()


def transform_tile(tile, rot, flip):
    if flip:
        # tile = tile[::-1] works too
        tile.reverse()
    rot %= 4
    while rot != 0:
        # Rotate 90 degrees to the right
        tile = list(zip(*tile[::-1]))
        # Rotate 90 degrees to the left
        # tile = list(zip(*tile))[::-1]
        rot -= 1
    return tile


def find_borders(tile):
    border_t = ''.join(tile[0])
    border_b = ''.join(tile[-1])
    # When comparing, the following commented out line will create a major issue
    # border_l = ''.join([line[0] for line in tile])[::-1]
    border_l = ''.join([line[0] for line in tile])
    border_r = ''.join([line[-1] for line in tile])
    border_list = [border_t, border_b, border_l, border_r] + [border[::-1]
                                                              for border in [border_t, border_b, border_l, border_r]]
    return border_list


def print_tile_single(tile):
    for row in tile:
        print(''.join(row))
    print()


def find_top_left_id(tiles, tile_dict):
    for tile_id, tile_index in tile_dict.items():
        tile = tiles[tile_index]
        border_outer_count = 0
        borders = find_borders(tile)
        for border in borders:
            if borders_all_list.count(border) != 2:
                # print(f'{borders_all_list.count(border)=}')
                border_outer_count += 1
        # print(f'{border_outer_count // 2=}')
        if border_outer_count == 4:
            break
    tile_id_tl = tiles.index(tile)
    borders = find_borders(tile)
    while borders_all_list.count(borders[0]) != 1 or borders_all_list.count(borders[2]) != 1:
        tiles[tile_id_tl] = transform_tile(tiles[tile_id_tl], 1, False)
        borders = find_borders(tiles[tile_id_tl])
    border_to_match_r, border_to_match_b = borders[3], borders[1]
    return tiles, tile_id, tile_id_tl, border_to_match_r, border_to_match_b


def match_border_left_or_top(tile_list, tile_id, border_to_match_r, border_to_match_b, found_count, len_row):
    matched = False
    border_to_match = border_to_match_b if found_count % len_row == 0 else border_to_match_r
    borders = find_borders(tile_list[tile_dict[tile_id]])
    border_to_eval = borders[0] if found_count % len_row == 0 else borders[2]
    if border_to_eval == border_to_match:
        matched = True
    else:
        for i in [1, 2, 3]:
            tile_list[tile_dict[tile_id]] = transform_tile(tile_list[tile_dict[tile_id]], i, False)
            borders = find_borders(tile_list[tile_dict[tile_id]])
            border_to_eval = borders[0] if found_count % len_row == 0 else borders[2]
            if border_to_eval == border_to_match:
                matched = True
                break
        else:
            tile_list[tile_dict[tile_id]] = transform_tile(tile_list[tile_dict[tile_id]], 0, True)
            borders = find_borders(tile_list[tile_dict[tile_id]])
            if border_to_eval == border_to_match:
                matched = True
            else:
                for i in [1, 2, 3]:
                    tile_list[tile_dict[tile_id]] = transform_tile(tile_list[tile_dict[tile_id]], i, False)
                    borders = find_borders(tile_list[tile_dict[tile_id]])
                    border_to_eval = borders[0] if found_count % len_row == 0 else borders[2]
                    if border_to_eval == border_to_match:
                        matched = True
                        break
    if matched:
        if found_count % len_row == 0:
            border_to_match_r, border_to_match_b = borders[3], borders[1]
        else:
            border_to_match_r = borders[3]
    return tile_list, tile_id, border_to_match_r, border_to_match_b, matched


def print_image(image):
    for line in image:
        print(line)


def build_image(tile_list, tile_dict, tile_found_index_list):
    actual_image = []
    for row in range(len_row):
        for line in range(1, 9):
            image_line = ''
            for col in range(len_row):
                image_line += ''.join(tile_list[tile_dict[tile_found_index_list[row * len_row + col]]][line][1:-1])
            actual_image.append(image_line)
    return actual_image


def build_image_1(tile_list, tile_dict, tile_found_index_list):
    actual_image = []
    for row in range(len_row):
        for line in range(0, 10):
            image_line = ''
            for col in range(len_row):
                if row * len_row + col < len(tile_found_index_list):
                    image_line += ''.join(tile_list[tile_dict[tile_found_index_list[row * len_row + col]]][line]) + ' '
            actual_image.append(image_line)
        actual_image.append(' ')
    return actual_image


num_tiles = (len(lines)+1) // 12
tile_dict = {}
tile_list = []
tile_remaining_index_list = [i for i in range(num_tiles)]
borders_all_list = []

for num in range(num_tiles):
    tile_id = lines[num * 12].split(' ')[1].replace(':', '')
    tile = [[char for char in line] for line in lines[num*12+1:(num+1)*12-1]]
    tile_list.append(tile)
    borders_all_list += find_borders(tile)
    tile_dict[tile_id] = num

tile_list, tile_id, tile_tl_id, border_to_match_r, border_to_match_b = find_top_left_id(tile_list, tile_dict)
tile_remaining_index_list.remove(tile_tl_id)
len_row = int(sqrt(num_tiles))
found_count = 1
tile_found_index_list = [tile_id]

while len(tile_remaining_index_list) != 0:
    for tile_id, tile_index in tile_dict.items():
        if tile_index in tile_remaining_index_list:
            tile_list, tile_id, border_to_match_r, border_to_match_b, matched = match_border_left_or_top(
                tile_list, tile_id, border_to_match_r, border_to_match_b, found_count, len_row)
            if matched:
                tile_remaining_index_list.remove(tile_dict[tile_id])
                tile_found_index_list.append(tile_id)
                found_count += 1
                os.system('cls')
                actual_image = build_image_1(tile_list, tile_dict, tile_found_index_list)
                print_image(actual_image)
                sleep(0.1)

corners = [
    int(tile_found_index_list[0]),
    int(tile_found_index_list[len_row-1]),
    int(tile_found_index_list[-len_row]),
    int(tile_found_index_list[-1])
]

# print(f'Prod of IDs: {prod(corners)}')


# --- Part Two ---
#
# Now, you're ready to check the image for sea monsters.
#
# The borders of each tile are not part of the actual image; start by removing them.
#
# In the example above, the tiles become:
#
# .#.#..#. ##...#.# #..#####
# ###....# .#....#. .#......
# ##.##.## #.#.#..# #####...
# ###.#### #...#.## ###.#..#
# ##.#.... #.##.### #...#.##
# ...##### ###.#... .#####.#
# ....#..# ...##..# .#.###..
# .####... #..#.... .#......
#
# #..#.##. .#..###. #.##....
# #.####.. #.####.# .#.###..
# ###.#.#. ..#.#### ##.#..##
# #.####.. ..##..## ######.#
# ##..##.# ...#...# .#.#.#..
# ...#..#. .#.#.##. .###.###
# .#.#.... #.##.#.. .###.##.
# ###.#... #..#.##. ######..
#
# .#.#.### .##.##.# ..#.##..
# .####.## #.#...## #.#..#.#
# ..#.#..# ..#.#.#. ####.###
# #..####. ..#.#.#. ###.###.
# #####..# ####...# ##....##
# #.##..#. .#...#.. ####...#
# .#.###.. ##..##.. ####.##.
# ...###.. .##...#. ..#..###
#
# Remove the gaps to form the actual image:
#
# .#.#..#.##...#.##..#####
# ###....#.#....#..#......
# ##.##.###.#.#..######...
# ###.#####...#.#####.#..#
# ##.#....#.##.####...#.##
# ...########.#....#####.#
# ....#..#...##..#.#.###..
# .####...#..#.....#......
# #..#.##..#..###.#.##....
# #.####..#.####.#.#.###..
# ###.#.#...#.######.#..##
# #.####....##..########.#
# ##..##.#...#...#.#.#.#..
# ...#..#..#.#.##..###.###
# .#.#....#.##.#...###.##.
# ###.#...#..#.##.######..
# .#.#.###.##.##.#..#.##..
# .####.###.#...###.#..#.#
# ..#.#..#..#.#.#.####.###
# #..####...#.#.#.###.###.
# #####..#####...###....##
# #.##..#..#...#..####...#
# .#.###..##..##..####.##.
# ...###...##...#...#..###
#
# Now, you're ready to search for sea monsters! Because your image is monochrome, a sea monster will look like this:
#
#                   #
# #    ##    ##    ###
#  #  #  #  #  #  #
#
# When looking for this pattern in the image, the spaces can be anything; only the # need to match. Also, you might need to rotate or flip your image before it's oriented correctly to find sea monsters. In the above image, after flipping and rotating it to the appropriate orientation, there are two sea monsters (marked with O):
#
# .####...#####..#...###..
# #####..#..#.#.####..#.#.
# .#.#...#.###...#.##.O#..
# #.O.##.OO#.#.OO.##.OOO##
# ..#O.#O#.O##O..O.#O##.##
# ...#.#..##.##...#..#..##
# #.##.#..#.#..#..##.#.#..
# .###.##.....#...###.#...
# #.####.#.#....##.#..#.#.
# ##...#..#....#..#...####
# ..#.##...###..#.#####..#
# ....#.##.#.#####....#...
# ..##.##.###.....#.##..#.
# #...#...###..####....##.
# .#.##...#.##.#.#.###...#
# #.###.#..####...##..#...
# #.###...#.##...#.##O###.
# .O##.#OO.###OO##..OOO##.
# ..O#.O..O..O.#O##O##.###
# #.#..##.########..#..##.
# #.#####..#.#...##..#....
# #....##..#.#########..##
# #...#.....#..##...###.##
# #..###....##.#...##.##.#
#
# Determine how rough the waters are in the sea monsters' habitat by counting the number of # that are not part of a sea monster. In the above example, the habitat's water roughness is 273.
#
# How many # are not part of a sea monster?


sleep(1)
actual_image = build_image(tile_list, tile_dict, tile_found_index_list)
os.system('cls')
print_image(actual_image)
sleep(1)

monster_pattern = [
    '                  # ',
    '#    ##    ##    ###',
    ' #  #  #  #  #  #   '
]

monster_pattern_re_list = [
    r'.{18}\#.{1}',
    r'\#.{4}\#\#.{4}\#\#.{4}\#\#\#',
    r'.{1}\#.{2}\#.{2}\#.{2}\#.{2}\#.{2}\#.{3}'
]

re_objects = [re.compile(pattern) for pattern in monster_pattern_re_list]
pattern_1 = re.compile(monster_pattern_re_list[0])
pattern_2 = re.compile(monster_pattern_re_list[1])
pattern_3 = re.compile(monster_pattern_re_list[2])

len_monster_pattern = 20
monster_found = False
count_hash_monster = 15
count_monster = 0
count_hash = 0
for line in actual_image:
    count_hash += line.count("#")


def find_monsters(re_objects, len_grid, len_monster_pattern):
    points = []
    count_monster = 0
    for row_start in range(0, len_grid-2):
        for col_start in range(0, len_grid-len_monster_pattern+3):
            for index_pattern, pattern in enumerate(re_objects):
                if not pattern.match(actual_image[row_start+index_pattern][col_start:col_start+len_monster_pattern]):
                    break
            else:
                count_monster += 1
                points.append((row_start, col_start))
    return points, count_monster


def reveal_monsters(points, image, monster_pattern):
    image = [[char for char in image_line] for image_line in image]
    for point in points:
        for line_index, line in enumerate(monster_pattern):
            for index_char, char in enumerate(line):
                if char == '#':
                    image[line_index+point[0]][index_char+point[1]] = 'O'
    image = [''.join(image_line) for image_line in image]
    return image


len_grid = len(actual_image[0])
points = []

for i in [1, 2, 3]:
    points, count_monster = find_monsters(re_objects, len_grid, len_monster_pattern)
    if count_monster != 0:
        break
    actual_image = [''.join(line) for line in transform_tile(actual_image, i, False)]
    os.system('cls')
    print_image(actual_image)
    sleep(0.5)
actual_image = [''.join(line) for line in transform_tile(actual_image, 0, True)]
os.system('cls')
print_image(actual_image)
sleep(0.5)
for row_start in range(0, len_grid-2):
    points, count_monster = find_monsters(re_objects, len_grid, len_monster_pattern)
    if count_monster != 0:
        break
for i in [1, 2, 3]:
    points, count_monster = find_monsters(re_objects, len_grid, len_monster_pattern)
    if count_monster != 0:
        break
    actual_image = [''.join(line) for line in transform_tile(actual_image, i, False)]
    os.system('cls')
    print_image(actual_image)
    sleep(0.5)

count_hash = 0
for line in actual_image:
    count_hash += line.count("#")

os.system('cls')
print_image(actual_image)
sleep(1)
actual_image = reveal_monsters(points, actual_image, monster_pattern)
os.system('cls')
print_image(actual_image)
sleep(0.4)

# print(f'# count: {count_hash-count_hash_monster*count_monster}')
