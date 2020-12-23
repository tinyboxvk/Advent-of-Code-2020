# --- Day 23: Crab Cups ---
#
# The small crab challenges you to a game! The crab is going to mix up some cups, and you have to predict where they'll end up.
#
# The cups will be arranged in a circle and labeled clockwise (your puzzle input). For example, if your labeling were 32415, there would be five cups in the circle; going clockwise around the circle from the first cup, the cups would be labeled 3, 2, 4, 1, 5, and then back to 3 again.
#
# Before the crab starts, it will designate the first cup in your list as the current cup. The crab is then going to do 100 moves.
#
# Each move, the crab does the following actions:
#
#     The crab picks up the three cups that are immediately clockwise of the current cup. They are removed from the circle; cup spacing is adjusted as necessary to maintain the circle.
#     The crab selects a destination cup: the cup with a label equal to the current cup's label minus one. If this would select one of the cups that was just picked up, the crab will keep subtracting one until it finds a cup that wasn't just picked up. If at any point in this process the value goes below the lowest value on any cup's label, it wraps around to the highest value on any cup's label instead.
#     The crab places the cups it just picked up so that they are immediately clockwise of the destination cup. They keep the same order as when they were picked up.
#     The crab selects a new current cup: the cup which is immediately clockwise of the current cup.
#
# For example, suppose your cup labeling were 389125467. If the crab were to do merely 10 moves, the following changes would occur:
#
# -- move 1 --
# cups: (3) 8  9  1  2  5  4  6  7 
# pick up: 8, 9, 1
# destination: 2
#
# -- move 2 --
# cups:  3 (2) 8  9  1  5  4  6  7 
# pick up: 8, 9, 1
# destination: 7
#
# -- move 3 --
# cups:  3  2 (5) 4  6  7  8  9  1 
# pick up: 4, 6, 7
# destination: 3
#
# -- move 4 --
# cups:  7  2  5 (8) 9  1  3  4  6 
# pick up: 9, 1, 3
# destination: 7
#
# -- move 5 --
# cups:  3  2  5  8 (4) 6  7  9  1 
# pick up: 6, 7, 9
# destination: 3
#
# -- move 6 --
# cups:  9  2  5  8  4 (1) 3  6  7 
# pick up: 3, 6, 7
# destination: 9
#
# -- move 7 --
# cups:  7  2  5  8  4  1 (9) 3  6 
# pick up: 3, 6, 7
# destination: 8
#
# -- move 8 --
# cups:  8  3  6  7  4  1  9 (2) 5 
# pick up: 5, 8, 3
# destination: 1
#
# -- move 9 --
# cups:  7  4  1  5  8  3  9  2 (6)
# pick up: 7, 4, 1
# destination: 5
#
# -- move 10 --
# cups: (5) 7  4  1  8  3  9  2  6 
# pick up: 7, 4, 1
# destination: 3
#
# -- final --
# cups:  5 (8) 3  7  4  1  9  2  6 
#
# In the above example, the cups' values are the labels as they appear moving clockwise around the circle; the current cup is marked with ( ).
#
# After the crab is done, what order will the cups be in? Starting after the cup labeled 1, collect the other cups' labels clockwise into a single string with no extra characters; each number except 1 should appear exactly once. In the above example, after 10 moves, the cups clockwise from 1 are labeled 9, 2, 6, 5, and so on, producing 92658374. If the crab were to complete all 100 moves, the order after cup 1 would be 67384529.
#
# Using your labeling, simulate 100 moves. What are the labels on the cups after cup 1?


from collections import deque
from itertools import cycle, chain

puzzle_input = '624397158'
# puzzle_input = '389125467'

cups = deque([int(num) for num in puzzle_input])
cycle_index_current_cup = cycle(range(9))

for i in range(100):
    # if i % 10 == 9:
    #     print(f'-- move {i+1} --')
    # print(f'cups: {", ".join(str(cup) for cup in cups)}')
    index_current_cup = next(cycle_index_current_cup)
    current_cup = cups[index_current_cup]
    # print(f'current: {current_cup}')
    cups_picked_up = deque()
    index_pickup = index_current_cup + 1
    for _ in range(3):
        if index_pickup == 9:
            index_pickup = 0
        cups_picked_up.append(cups[index_pickup])
        index_pickup += 1
    # print(f'pick up: {", ".join(str(cup) for cup in cups_picked_up)}')
    for cup in cups_picked_up:
        cups.remove(cup)
    destination_cup = current_cup - 1
    while destination_cup not in cups:
        if destination_cup == 0:
            destination_cup = 10
        destination_cup -= 1
    # print(f'destination: {destination_cup}')
    index_destination_cup = cups.index(destination_cup)
    cups.insert(index_destination_cup, cups_picked_up.popleft())
    cups.insert(index_destination_cup + 1, cups_picked_up.popleft())
    cups.insert(index_destination_cup + 2, cups_picked_up.popleft())
    cups.remove(destination_cup)
    cups.insert(index_destination_cup, destination_cup)
    index_delta = index_current_cup - cups.index(current_cup)
    cups.rotate(index_delta)
    # print()

index_delta = cups.index(1)
cups.rotate(-index_delta-1)
print(''.join(str(num) for num in cups)[:-1])
print('------------------')


# --- Part Two ---
#
# Due to what you can only assume is a mistranslation (you're not exactly fluent in Crab), you are quite surprised when the crab starts arranging many cups in a circle on your raft - one million (1000000) in total.
#
# Your labeling is still correct for the first few cups; after that, the remaining cups are just numbered in an increasing fashion starting from the number after the highest number in your list and proceeding one by one until one million is reached. (For example, if your labeling were 54321, the cups would be numbered 5, 4, 3, 2, 1, and then start counting up from 6 until one million is reached.) In this way, every number from one through one million is used exactly once.
#
# After discovering where you made the mistake in translating Crab Numbers, you realize the small crab isn't going to do merely 100 moves; the crab is going to do ten million (10000000) moves!
#
# The crab is going to hide your stars - one each - under the two cups that will end up immediately clockwise of cup 1. You can have them if you predict what the labels on those cups will be when the crab is finished.
#
# In the above example (389125467), this would be 934001 and then 159792; multiplying these together produces 149245887792.
#
# Determine which two cups will end up immediately clockwise of cup 1. What do you get if you multiply their labels together?


puzzle_input_list = [int(num) for num in puzzle_input]

class Cup:
    def __init__(self, value):
        self.value = value
        self.prev  = None
        self.next  = None

def build_doubly_linked_list(total_len):
    initial_values = chain(puzzle_input_list, range(len(puzzle_input_list) + 1, total_len + 1))
    cups = [None] * (total_len + 1)
    first = next(initial_values)
    cups[first] = Cup(first)
    first = cups[first]
    prev = first
    for value in initial_values:
        cur = cups[value] = Cup(value)
        cur.prev = prev
        prev.next = cur
        prev = cur
    cur.next = first
    return first, cups

total_cups = 1000000
total_moves = 10000000
first, cups = build_doubly_linked_list(total_cups)
current_cup = first

for i in range(total_moves):
    if i % 1000000 == 999999:
        print(f'-- move {i+1} --')
    first_cup  = current_cup.next
    mid_cup    = first_cup.next
    last_cup   = mid_cup.next
    cups_picked_up = (first_cup.value, mid_cup.value, last_cup.value)
    current_cup.next = last_cup.next
    current_cup.next.prev = current_cup
    destination_cup = current_cup.value - 1 if current_cup.value > 1 else total_cups
    while destination_cup in cups_picked_up:
        destination_cup = destination_cup - 1 if destination_cup > 1 else total_cups
    first_cup.prev = cups[destination_cup]
    last_cup.next = cups[destination_cup].next
    cups[destination_cup].next = first_cup
    current_cup = current_cup.next

print(f'{cups[1].next.value} * {cups[1].next.next.value} = {cups[1].next.value * cups[1].next.next.value}')
