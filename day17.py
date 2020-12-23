# --- Day 17: Conway Cubes ---
#
# As your flight slowly drifts through the sky, the Elves at the Mythical Information Bureau at the North Pole contact you. They'd like some help debugging a malfunctioning experimental energy source aboard one of their super-secret imaging satellites.
#
# The experimental energy source is based on cutting-edge technology: a set of Conway Cubes contained in a pocket dimension! When you hear it's having problems, you can't help but agree to take a look.
#
# The pocket dimension contains an infinite 3-dimensional grid. At every integer 3-dimensional coordinate (x,y,z), there exists a single cube which is either active or inactive.
#
# In the initial state of the pocket dimension, almost all cubes start inactive. The only exception to this is a small flat region of cubes (your puzzle input); the cubes in this region start in the specified active (#) or inactive (.) state.
#
# The energy source then proceeds to boot up by executing six cycles.
#
# Each cube only ever considers its neighbors: any of the 26 other cubes where any of their coordinates differ by at most 1. For example, given the cube at x=1,y=2,z=3, its neighbors include the cube at x=2,y=2,z=2, the cube at x=0,y=2,z=3, and so on.
#
# During a cycle, all cubes simultaneously change their state according to the following rules:
#
#     If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
#     If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.
#
# The engineers responsible for this experimental energy source would like you to simulate the pocket dimension and determine what the configuration of cubes should be at the end of the six-cycle boot process.
#
# For example, consider the following initial state:
#
# .#.
# ..#
# ###
#
# Even though the pocket dimension is 3-dimensional, this initial state represents a small 2-dimensional slice of it. (In particular, this initial state defines a 3x3x1 region of the 3-dimensional space.)
#
# Simulating a few cycles from this initial state produces the following configurations, where the result of each cycle is shown layer-by-layer at each given z coordinate (and the frame of view follows the active cells in each cycle):
#
# Before any cycles:
#
# z=0
# .#.
# ..#
# ###
#
#
# After 1 cycle:
#
# z=-1
# #..
# ..#
# .#.
#
# z=0
# #.#
# .##
# .#.
#
# z=1
# #..
# ..#
# .#.
#
#
# After 2 cycles:
#
# z=-2
# .....
# .....
# ..#..
# .....
# .....
#
# z=-1
# ..#..
# .#..#
# ....#
# .#...
# .....
#
# z=0
# ##...
# ##...
# #....
# ....#
# .###.
#
# z=1
# ..#..
# .#..#
# ....#
# .#...
# .....
#
# z=2
# .....
# .....
# ..#..
# .....
# .....
#
#
# After 3 cycles:
#
# z=-2
# .......
# .......
# ..##...
# ..###..
# .......
# .......
# .......
#
# z=-1
# ..#....
# ...#...
# #......
# .....##
# .#...#.
# ..#.#..
# ...#...
#
# z=0
# ...#...
# .......
# #......
# .......
# .....##
# .##.#..
# ...#...
#
# z=1
# ..#....
# ...#...
# #......
# .....##
# .#...#.
# ..#.#..
# ...#...
#
# z=2
# .......
# .......
# ..##...
# ..###..
# .......
# .......
# .......
#
# After the full six-cycle boot process completes, 112 cubes are left in the active state.
#
# Starting with your given initial configuration, simulate six cycles. How many cubes are left in the active state after the sixth cycle?


from copy import deepcopy
from collections import deque

lines = []
with open('day17input.txt') as input_file:
    lines = input_file.read().splitlines()

# lines = [
#     '.#.',
#     '..#',
#     '###'
# ]

cal_list = [(a, b, c) for a in (-1, 0, 1) for b in (-1, 0, 1) for c in (-1, 0, 1)]
cal_list.remove((0, 0, 0))

def find_immediate_neighbours(point):
    return [(point[0]+cal[0], point[1]+cal[1], point[2]+cal[2]) for cal in cal_list]

# test_point = (1,1,1)
# print(find_immediate_neighbours(test_point))
# print()

points_active = []
points_to_test = []
index_z = 0
for index_y, line in enumerate(lines):
    for index_x, c in enumerate(line):
        if c == '#':
            points_active.append((index_x, index_y, index_z))
            list_immediate_neighbours = find_immediate_neighbours(
                (index_x, index_y, index_z))
            for point in list_immediate_neighbours:
                if point not in points_to_test:
                    points_to_test.append(point)
            if (index_x, index_y, index_z) not in points_to_test:
                points_to_test.append((index_x, index_y, index_z))

for _ in range(6):
    points_active_next = deepcopy(list(points_active))
    for point in points_to_test:
        list_immediate_neighbours = find_immediate_neighbours(point)
        neighbour_active_count = 0
        for neighbour in list_immediate_neighbours:
            if neighbour in points_active:
                neighbour_active_count += 1
        if point in points_active:
            if neighbour_active_count != 2 and neighbour_active_count != 3:
                points_active_next.remove(point)
        else:
            if neighbour_active_count == 3:
                points_active_next.append(point)
    points_to_test = []
    for point in points_active_next:
        list_immediate_neighbours = find_immediate_neighbours(point)
        for point_neighbour in list_immediate_neighbours:
            if point_neighbour not in points_to_test:
                points_to_test.append(point_neighbour)
        if point not in points_to_test:
            points_to_test.append(point)
    points_active = set(points_active_next)
    # for z in [-2, -1, 0, 1, 2]:
    #     for y in [-2, -1, 0, 1, 2, 3, 4, 5]:
    #         for x in [-2, -1, 0, 1, 2, 3, 4, 5]:
    #             if (x, y, z) in points_active:
    #                 print('#', end='')
    #             else:
    #                 print('.', end='')
    #         print()
    #     print()

print(f'Active cubes: {len(points_active)}')


# --- Part Two ---
#
# For some reason, your simulated results don't match what the experimental energy source engineers expected. Apparently, the pocket dimension actually has four spatial dimensions, not three.
#
# The pocket dimension contains an infinite 4-dimensional grid. At every integer 4-dimensional coordinate (x,y,z,w), there exists a single cube (really, a hypercube) which is still either active or inactive.
#
# Each cube only ever considers its neighbors: any of the 80 other cubes where any of their coordinates differ by at most 1. For example, given the cube at x=1,y=2,z=3,w=4, its neighbors include the cube at x=2,y=2,z=3,w=3, the cube at x=0,y=2,z=3,w=4, and so on.
#
# The initial state of the pocket dimension still consists of a small flat region of cubes. Furthermore, the same rules for cycle updating still apply: during each cycle, consider the number of active neighbors of each cube.
#
# For example, consider the same initial state as in the example above. Even though the pocket dimension is 4-dimensional, this initial state represents a small 2-dimensional slice of it. (In particular, this initial state defines a 3x3x1x1 region of the 4-dimensional space.)
#
# Simulating a few cycles from this initial state produces the following configurations, where the result of each cycle is shown layer-by-layer at each given z and w coordinate:
#
# Before any cycles:
#
# z=0, w=0
# .#.
# ..#
# ###
#
#
# After 1 cycle:
#
# z=-1, w=-1
# #..
# ..#
# .#.
#
# z=0, w=-1
# #..
# ..#
# .#.
#
# z=1, w=-1
# #..
# ..#
# .#.
#
# z=-1, w=0
# #..
# ..#
# .#.
#
# z=0, w=0
# #.#
# .##
# .#.
#
# z=1, w=0
# #..
# ..#
# .#.
#
# z=-1, w=1
# #..
# ..#
# .#.
#
# z=0, w=1
# #..
# ..#
# .#.
#
# z=1, w=1
# #..
# ..#
# .#.
#
#
# After 2 cycles:
#
# z=-2, w=-2
# .....
# .....
# ..#..
# .....
# .....
#
# z=-1, w=-2
# .....
# .....
# .....
# .....
# .....
#
# z=0, w=-2
# ###..
# ##.##
# #...#
# .#..#
# .###.
#
# z=1, w=-2
# .....
# .....
# .....
# .....
# .....
#
# z=2, w=-2
# .....
# .....
# ..#..
# .....
# .....
#
# z=-2, w=-1
# .....
# .....
# .....
# .....
# .....
#
# z=-1, w=-1
# .....
# .....
# .....
# .....
# .....
#
# z=0, w=-1
# .....
# .....
# .....
# .....
# .....
#
# z=1, w=-1
# .....
# .....
# .....
# .....
# .....
#
# z=2, w=-1
# .....
# .....
# .....
# .....
# .....
#
# z=-2, w=0
# ###..
# ##.##
# #...#
# .#..#
# .###.
#
# z=-1, w=0
# .....
# .....
# .....
# .....
# .....
#
# z=0, w=0
# .....
# .....
# .....
# .....
# .....
#
# z=1, w=0
# .....
# .....
# .....
# .....
# .....
#
# z=2, w=0
# ###..
# ##.##
# #...#
# .#..#
# .###.
#
# z=-2, w=1
# .....
# .....
# .....
# .....
# .....
#
# z=-1, w=1
# .....
# .....
# .....
# .....
# .....
#
# z=0, w=1
# .....
# .....
# .....
# .....
# .....
#
# z=1, w=1
# .....
# .....
# .....
# .....
# .....
#
# z=2, w=1
# .....
# .....
# .....
# .....
# .....
#
# z=-2, w=2
# .....
# .....
# ..#..
# .....
# .....
#
# z=-1, w=2
# .....
# .....
# .....
# .....
# .....
#
# z=0, w=2
# ###..
# ##.##
# #...#
# .#..#
# .###.
#
# z=1, w=2
# .....
# .....
# .....
# .....
# .....
#
# z=2, w=2
# .....
# .....
# ..#..
# .....
# .....
#
# After the full six-cycle boot process completes, 848 cubes are left in the active state.
#
# Starting with your given initial configuration, simulate six cycles in a 4-dimensional space. How many cubes are left in the active state after the sixth cycle?

# lines = [
#     '.#.',
#     '..#',
#     '###'
# ]

# def find_immediate_neighbours_2(point):
#     list_immediate_neighbours = []
#     for x in [-1, 0, 1]:
#         for y in [-1, 0, 1]:
#             for z in [-1, 0, 1]:
#                 for s in [-1, 0, 1]:
#                     list_immediate_neighbours.append(
#                         (point[0]+x, point[1]+y, point[2]+z, point[3]+s))
#     list_immediate_neighbours.remove(point)
#     return list_immediate_neighbours

print('------------------------')

cal_list_2 = [(a, b, c, d) for a in (-1, 0, 1) for b in (-1, 0, 1) for c in (-1, 0, 1) for d in (-1, 0, 1)]
cal_list_2.remove((0, 0, 0, 0))

def find_immediate_neighbours_2(point):
    return [(point[0]+cal[0], point[1]+cal[1], point[2]+cal[2], point[3]+cal[3]) for cal in cal_list_2]

points_active = []
points_to_test = []
index_z = 0
index_s = 0
for index_y, line in enumerate(lines):
    for index_x, c in enumerate(line):
        if c == '#':
            points_active.append((index_x, index_y, index_z, index_s))
            list_immediate_neighbours = find_immediate_neighbours_2(
                (index_x, index_y, index_z, index_s))
            for point in list_immediate_neighbours:
                if point not in points_to_test:
                    points_to_test.append(point)
            if (index_x, index_y, index_z, index_s) not in points_to_test:
                points_to_test.append((index_x, index_y, index_z, index_s))


for i in range(6):
    print(f'Running cycle {i+1}! We have {len(points_to_test)} points to test...')
    points_active_next = deepcopy(list(points_active))
    for point in points_to_test:
        list_immediate_neighbours = find_immediate_neighbours_2(point)
        neighbour_active_count = 0
        for neighbour in list_immediate_neighbours:
            if neighbour in points_active:
                neighbour_active_count += 1
        if point in points_active:
            if neighbour_active_count != 2 and neighbour_active_count != 3:
                points_active_next.remove(point)
        else:
            if neighbour_active_count == 3:
                points_active_next.append(point)
    points_to_test = deque([])
    if i != 5:
        for point in points_active_next:
            points_to_test.extend(find_immediate_neighbours_2(point))
            points_to_test.append(point)
    points_to_test = set(points_to_test)
    points_active = set(points_active_next)

print(f'Active cubes: {len(points_active)}')
