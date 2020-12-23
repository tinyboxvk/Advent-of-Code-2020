# --- Day 13: Shuttle Search ---
#
# Your ferry can make it safely to a nearby port, but it won't get much further. When you call to book another ship, you discover that no ships embark from that port to your vacation island. You'll need to get from the port to the nearest airport.
#
# Fortunately, a shuttle bus service is available to bring you from the sea port to the airport! Each bus has an ID number that also indicates how often the bus leaves for the airport.
#
# Bus schedules are defined based on a timestamp that measures the number of minutes since some fixed reference point in the past. At timestamp 0, every bus simultaneously departed from the sea port. After that, each bus travels to the airport, then various other locations, and finally returns to the sea port to repeat its journey forever.
#
# The time this loop takes a particular bus is also its ID number: the bus with ID 5 departs from the sea port at timestamps 0, 5, 10, 15, and so on. The bus with ID 11 departs at 0, 11, 22, 33, and so on. If you are there when the bus departs, you can ride that bus to the airport!
#
# Your notes (your puzzle input) consist of two lines. The first line is your estimate of the earliest timestamp you could depart on a bus. The second line lists the bus IDs that are in service according to the shuttle company; entries that show x must be out of service, so you decide to ignore them.
#
# To save time once you arrive, your goal is to figure out the earliest bus you can take to the airport. (There will be exactly one such bus.)
#
# For example, suppose you have the following notes:
#
# 939
# 7,13,x,x,59,x,31,19
#
# Here, the earliest timestamp you could depart is 939, and the bus IDs in service are 7, 13, 59, 31, and 19. Near timestamp 939, these bus IDs depart at the times marked D:
#
# time   bus 7   bus 13  bus 59  bus 31  bus 19
# 929      .       .       .       .       .
# 930      .       .       .       D       .
# 931      D       .       .       .       D
# 932      .       .       .       .       .
# 933      .       .       .       .       .
# 934      .       .       .       .       .
# 935      .       .       .       .       .
# 936      .       D       .       .       .
# 937      .       .       .       .       .
# 938      D       .       .       .       .
# 939      .       .       .       .       .
# 940      .       .       .       .       .
# 941      .       .       .       .       .
# 942      .       .       .       .       .
# 943      .       .       .       .       .
# 944      .       .       D       .       .
# 945      D       .       .       .       .
# 946      .       .       .       .       .
# 947      .       .       .       .       .
# 948      .       .       .       .       .
# 949      .       D       .       .       .
#
# The earliest bus you could take is bus ID 59. It doesn't depart until timestamp 944, so you would need to wait 944 - 939 = 5 minutes before it departs. Multiplying the bus ID by the number of minutes you'd need to wait gives 295.
#
# What is the ID of the earliest bus you can take to the airport multiplied by the number of minutes you'll need to wait for that bus?


lines = []
with open('day13input.txt') as input_file:
    lines = input_file.read().splitlines()

# lines = [
#     '939',
#     '7,13,x,x,59,x,31,19'
# ]

timestamp_depart_me = int(lines[0])

schedules = lines[1].split(',')
schedules_in_service = [int(schedule) for schedule in schedules if schedule != 'x' ]
timestamps_depart_earliest = []

# print(timestamp_depart_me)
# print(schedules_in_service)

for schedule in schedules_in_service:
    multiplier = 1
    while (timestamp_depart_earliest := multiplier * schedule) < timestamp_depart_me:
        multiplier += 1
    timestamps_depart_earliest.append(timestamp_depart_earliest)

bus_id = schedules_in_service[timestamps_depart_earliest.index(min(timestamps_depart_earliest))]

minutes_wait = min(timestamps_depart_earliest) - timestamp_depart_me

print(f'Answer = {bus_id * minutes_wait}')


# --- Part Two ---
#
# The shuttle company is running a contest: one gold coin for anyone that can find the earliest timestamp such that the first bus ID departs at that time and each subsequent listed bus ID departs at that subsequent minute. (The first line in your input is no longer relevant.)
#
# For example, suppose you have the same list of bus IDs as above:
#
# 7,13,x,x,59,x,31,19
#
# An x in the schedule means there are no constraints on what bus IDs must depart at that time.
#
# This means you are looking for the earliest timestamp (called t) such that:
#
#     Bus ID 7 departs at timestamp t.
#     Bus ID 13 departs one minute after timestamp t.
#     There are no requirements or restrictions on departures at two or three minutes after timestamp t.
#     Bus ID 59 departs four minutes after timestamp t.
#     There are no requirements or restrictions on departures at five minutes after timestamp t.
#     Bus ID 31 departs six minutes after timestamp t.
#     Bus ID 19 departs seven minutes after timestamp t.
#
# The only bus departures that matter are the listed bus IDs at their specific offsets from t. Those bus IDs can depart at other times, and other bus IDs can depart at those times. For example, in the list above, because bus ID 19 must depart seven minutes after the timestamp at which bus ID 7 departs, bus ID 7 will always also be departing with bus ID 19 at seven minutes after timestamp t.
#
# In this example, the earliest timestamp at which this occurs is 1068781:
#
# time     bus 7   bus 13  bus 59  bus 31  bus 19
# 1068773    .       .       .       .       .
# 1068774    D       .       .       .       .
# 1068775    .       .       .       .       .
# 1068776    .       .       .       .       .
# 1068777    .       .       .       .       .
# 1068778    .       .       .       .       .
# 1068779    .       .       .       .       .
# 1068780    .       .       .       .       .
# 1068781    D       .       .       .       .
# 1068782    .       D       .       .       .
# 1068783    .       .       .       .       .
# 1068784    .       .       .       .       .
# 1068785    .       .       D       .       .
# 1068786    .       .       .       .       .
# 1068787    .       .       .       D       .
# 1068788    D       .       .       .       D
# 1068789    .       .       .       .       .
# 1068790    .       .       .       .       .
# 1068791    .       .       .       .       .
# 1068792    .       .       .       .       .
# 1068793    .       .       .       .       .
# 1068794    .       .       .       .       .
# 1068795    D       D       .       .       .
# 1068796    .       .       .       .       .
# 1068797    .       .       .       .       .
#
# In the above example, bus ID 7 departs at timestamp 1068788 (seven minutes after t). This is fine; the only requirement on that minute is that bus ID 19 departs then, and it does.
#
# Here are some other examples:
#
#     The earliest timestamp that matches the list 17,x,13,19 is 3417.
#     67,7,59,61 first occurs at timestamp 754018.
#     67,x,7,59,61 first occurs at timestamp 779210.
#     67,7,x,59,61 first occurs at timestamp 1261476.
#     1789,37,47,1889 first occurs at timestamp 1202161486.
#
# However, with so many bus IDs in your list, surely the actual earliest timestamp will be larger than 100000000000000!
#
# What is the earliest timestamp such that all of the listed bus IDs depart at offsets matching their positions in the list?


schedules = '7,13,x,x,59,x,31,19'.split(',')
# schedules = lines[1].split(',')
schedules_in_service = [int(schedule) for schedule in schedules if schedule != 'x' ][::-1]
schedules_in_service_delta = [schedules.index(schedule) for schedule in schedules if schedule != 'x' ][::-1]
schedules_multipliers = [1] * len(schedules_in_service)

# print(schedules_in_service)
# print(schedules_in_service_delta)
# print(schedules_multipliers)

# [19, 31, 59, 13, 7]
# [7, 6, 4, 1, 0]
# [1, 1, 1, 1, 1]

found = 0
index_a = 0
index_b = 1
while found < 5 and index_a < len(schedules_in_service)-1:
    while schedules_in_service[index_a] * schedules_multipliers[index_a] < schedules_in_service[index_b] * schedules_multipliers[index_b]:
        schedules_multipliers[index_a] += 1
    timestamp_delta = (schedules_in_service[index_a] * schedules_multipliers[index_a] - (schedules_in_service_delta[index_a] - schedules_in_service_delta[index_b])) % schedules_in_service[index_b] 
    if timestamp_delta == 0:
        found += 1
        index_b += 1
        if index_b == len(schedules_in_service):
            index_a += 1
            index_b = index_a + 1
    else:
        schedules_multipliers[index_b] += 1
        index_a = 0
        index_b = 1
        found = 0

    # if found > 3:
    #     print(found)
    #     print(schedules_multipliers)
    # print(found)
    # print(schedules_multipliers)

print(f'Answer = {schedules_in_service[0]*schedules_multipliers[0]-schedules_in_service_delta[0]}')

##################################################

from math import prod, gcd

print('-----------------------------------------------')
# schedules = '7,13,x,x,59,x,31,19'.split(',')
schedules = lines[1].split(',')
schedules_in_service = [int(schedule) for schedule in schedules if schedule != 'x' ]
schedules_in_service_delta = [(len(schedules) - schedules.index(schedule)) % int(schedule) - 1 for schedule in schedules if schedule != 'x' ]

# schedules_in_service = [7, 13, 59, 31, 19]
# schedules_in_service_delta = [0, 6, 3, 1, 0]
# print(schedules_in_service_delta)

schedules_multipliers = []

lcm = schedules_in_service[0]
for i in schedules_in_service[1:]:
    lcm = int(lcm * i / gcd(lcm, i))

total = 0
for num in schedules_in_service:
    m = int(lcm/num)
    k = 1
    while k*m % num != 1:
        k += 1
    schedules_multipliers.append(k*m)

print(f'{schedules_multipliers}')

num_very_big = 0
for index, num in enumerate(schedules_in_service_delta):
    num_very_big += num * schedules_multipliers[index]

total = num_very_big % prod(schedules_in_service)

print(f'Answer = {total-len(schedules)+1}')
