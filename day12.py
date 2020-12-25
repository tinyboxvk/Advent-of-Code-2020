# --- Day 12: Rain Risk ---
#
# Your ferry made decent progress toward the island, but the storm came in faster than anyone expected. The ferry needs to take evasive actions!
#
# Unfortunately, the ship's navigation computer seems to be malfunctioning; rather than giving a route directly to safety, it produced extremely circuitous instructions. When the captain uses the PA system to ask if anyone can help, you quickly volunteer.
#
# The navigation instructions (your puzzle input) consists of a sequence of single-character actions paired with integer input values. After staring at them for a few minutes, you work out what they probably mean:
#
#     Action N means to move north by the given value.
#     Action S means to move south by the given value.
#     Action E means to move east by the given value.
#     Action W means to move west by the given value.
#     Action L means to turn left the given number of degrees.
#     Action R means to turn right the given number of degrees.
#     Action F means to move forward by the given value in the direction the ship is currently facing.
#
# The ship starts by facing east. Only the L and R actions change the direction the ship is facing. (That is, if the ship is facing east and the next instruction is N10, the ship would move north 10 units, but would still move east if the following action were F.)
#
# For example:
#
# F10
# N3
# F7
# R90
# F11
#
# These instructions would be handled as follows:
#
#     F10 would move the ship 10 units east (because the ship starts by facing east) to east 10, north 0.
#     N3 would move the ship 3 units north to east 10, north 3.
#     F7 would move the ship another 7 units east (because the ship is still facing east) to east 17, north 3.
#     R90 would cause the ship to turn right by 90 degrees and face south; it remains at east 17, north 3.
#     F11 would move the ship 11 units south to east 17, south 8.
#
# At the end of these instructions, the ship's Manhattan distance (sum of the absolute values of its east/west position and its north/south position) from its starting position is 17 + 8 = 25.
#
# Figure out where the navigation instructions lead. What is the Manhattan distance between that location and the ship's starting position?


lines = []
with open('day12input.txt') as input_file:
    lines = input_file.read().splitlines()

# lines = [
#     'F10',
#     'N3',
#     'F7',
#     'R90',
#     'F11'
# ]

direction_list = ['N', 'E', 'S', 'W']
direction_index = 1

x = 0
y = 0

def move(direction, value, x, y):
    if direction == 'N':
        y += value
    elif direction == 'S':
        y -= value
    elif direction == 'E':
        x += value
    elif direction == 'W':
        x -= value
    return x, y

for line in lines:
    action, value = line[0], int(line[1:])
    # print(f'{action} {value}')
    if action in direction_list:
        x, y = move(action, value, x, y)
    elif action in ['L', 'R']:
        if action == 'L':
            direction_index = (direction_index - value // 90) % 4
        else:
            direction_index = (direction_index + value // 90) % 4
    elif action == 'F':
        x, y = move(direction_list[direction_index], value, x, y)
    else:
        raise Exception('ERROR!')
    # print(f'{x=} {y=}')

print(f'Manhattan distance: {abs(x)+abs(y)}')


# --- Part Two ---
#
# Before you can give the destination to the captain, you realize that the actual action meanings were printed on the back of the instructions the whole time.
#
# Almost all of the actions indicate how to move a waypoint which is relative to the ship's position:
#
#     Action N means to move the waypoint north by the given value.
#     Action S means to move the waypoint south by the given value.
#     Action E means to move the waypoint east by the given value.
#     Action W means to move the waypoint west by the given value.
#     Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
#     Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
#     Action F means to move forward to the waypoint a number of times equal to the given value.
#
# The waypoint starts 10 units east and 1 unit north relative to the ship. The waypoint is relative to the ship; that is, if the ship moves, the waypoint moves with it.
#
# For example, using the same instructions as above:
#
#     F10 moves the ship to the waypoint 10 times (a total of 100 units east and 10 units north), leaving the ship at east 100, north 10. The waypoint stays 10 units east and 1 unit north of the ship.
#     N3 moves the waypoint 3 units north to 10 units east and 4 units north of the ship. The ship remains at east 100, north 10.
#     F7 moves the ship to the waypoint 7 times (a total of 70 units east and 28 units north), leaving the ship at east 170, north 38. The waypoint stays 10 units east and 4 units north of the ship.
#     R90 rotates the waypoint around the ship clockwise 90 degrees, moving it to 4 units east and 10 units south of the ship. The ship remains at east 170, north 38.
#     F11 moves the ship to the waypoint 11 times (a total of 44 units east and 110 units south), leaving the ship at east 214, south 72. The waypoint stays 4 units east and 10 units south of the ship.
#
# After these operations, the ship's Manhattan distance from its starting position is 214 + 72 = 286.
#
# Figure out where the navigation instructions actually lead. What is the Manhattan distance between that location and the ship's starting position?


# lines = [
#     'F10',
#     'N3',
#     'F7',
#     'R90',
#     'F11'
# ]

direction_list = ['N', 'E', 'S', 'W']
direction_index = 1

x = 0
y = 0
x_wp = 10
y_wp = 1

def move_wp(direction, value, x_wp, y_wp):
    if direction == 'N':
        y_wp += value
    elif direction == 'S':
        y_wp -= value
    elif direction == 'E':
        x_wp += value
    elif direction == 'W':
        x_wp -= value
    return x_wp, y_wp

def rotate_wp(direction, value, x_wp, y_wp):
    value = (value // 90) % 4
    if direction == 'L':
        value = -value
        value += 4
    # print(f'{value=}')
    if value == 2:
        x_wp, y_wp = -x_wp, -y_wp
    elif value == 1:
        x_wp, y_wp = y_wp, -x_wp
    elif value == 3:
        x_wp, y_wp = -y_wp, x_wp
    return x_wp, y_wp

for line in lines:
    action, value = line[0], int(line[1:])
    # print(f'{action} {value}')
    if action in direction_list:
        x_wp, y_wp = move_wp(action, value, x_wp, y_wp)
    elif action in ['L', 'R']:
        x_wp, y_wp = rotate_wp(action, value, x_wp, y_wp)
    elif action == 'F':
        # print(f'F {x=} {y=} {x_wp=} {y_wp=}')
        y += value * y_wp
        x += value * x_wp
    else:
        raise Exception('ERROR!')
    # print(f'{x=} {y=} {x_wp=} {y_wp=}')

print(f'Manhattan distance: {abs(x)+abs(y)}')
