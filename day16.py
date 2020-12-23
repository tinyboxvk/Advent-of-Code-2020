# --- Day 16: Ticket Translation ---
#
# As you're walking to yet another connecting flight, you realize that one of the legs of your re-routed trip coming up is on a high-speed train. However, the train ticket you were given is in a language you don't understand. You should probably figure out what it says before you get to the train station after the next flight.
#
# Unfortunately, you can't actually read the words on the ticket. You can, however, read the numbers, and so you figure out the fields these tickets must have and the valid ranges for values in those fields.
#
# You collect the rules for ticket fields, the numbers on your ticket, and the numbers on other nearby tickets for the same train service (via the airport security cameras) together into a single document you can reference (your puzzle input).
#
# The rules for ticket fields specify a list of fields that exist somewhere on the ticket and the valid ranges of values for each field. For example, a rule like class: 1-3 or 5-7 means that one of the fields in every ticket is named class and can be any value in the ranges 1-3 or 5-7 (inclusive, such that 3 and 5 are both valid in this field, but 4 is not).
#
# Each ticket is represented by a single line of comma-separated values. The values are the numbers on the ticket in the order they appear; every ticket has the same format. For example, consider this ticket:
#
# .--------------------------------------------------------.
# | ????: 101    ?????: 102   ??????????: 103     ???: 104 |
# |                                                        |
# | ??: 301  ??: 302             ???????: 303      ??????? |
# | ??: 401  ??: 402           ???? ????: 403    ????????? |
# '--------------------------------------------------------'
#
# Here, ? represents text in a language you don't understand. This ticket might be represented as 101,102,103,104,301,302,303,401,402,403; of course, the actual train tickets you're looking at are much more complicated. In any case, you've extracted just the numbers in such a way that the first number is always the same specific field, the second number is always a different specific field, and so on - you just don't know what each position actually means!
#
# Start by determining which tickets are completely invalid; these are tickets that contain values which aren't valid for any field. Ignore your ticket for now.
#
# For example, suppose you have the following notes:
#
# class: 1-3 or 5-7
# row: 6-11 or 33-44
# seat: 13-40 or 45-50
#
# your ticket:
# 7,1,14
#
# nearby tickets:
# 7,3,47
# 40,4,50
# 55,2,20
# 38,6,12
#
# It doesn't matter which position corresponds to which field; you can identify invalid nearby tickets by considering only whether tickets contain values that are not valid for any field. In this example, the values on the first nearby ticket are all valid for at least one field. This is not true of the other three nearby tickets: the values 4, 55, and 12 are are not valid for any field. Adding together all of the invalid values produces your ticket scanning error rate: 4 + 55 + 12 = 71.
#
# Consider the validity of the nearby tickets you scanned. What is your ticket scanning error rate?


lines = []
with open('day16input.txt') as input_file:
    lines = input_file.read().splitlines()

lines_rules = lines[:20]
my_ticket = lines[22].split(',')
lines_nearby_tickets = lines[25:]

# lines = [
#     'class: 1-3 or 5-7',
#     'row: 6-11 or 33-44',
#     'seat: 13-40 or 45-50',
#     '',
#     'your ticket:',
#     '7,1,14',
#     '',
#     'nearby tickets:',
#     '7,3,47',
#     '40,4,50',
#     '55,2,20',
#     '38,6,12'
# ]

# lines_rules = lines[:3]
# my_ticket = lines[5].split(',')
# lines_nearby_tickets = lines[8:]

# lines = [
#     'class: 0-1 or 4-19',
#     'row: 0-5 or 8-19',
#     'seat: 0-13 or 16-19',
#     '',
#     'your ticket:',
#     '11,12,13',
#     '',
#     'nearby tickets:',
#     '3,9,18',
#     '15,1,5',
#     '5,14,9'
# ]

# lines_rules = lines[:3]
# my_ticket = lines[5].split(',')
# lines_nearby_tickets = lines[8:]

# print(lines_rules)
# print(my_ticket)
# print(lines_nearby_tickets)

rules = {}

for line in lines_rules:
    rule = line.split(': ')
    rules[rule[0]] = rule[1].split(' or ')

def check_valid(ticket, rules):
    valid = False
    sum_invalid_field = 0
    for field in ticket:
        found_field_valid = False
        for rule_limits_pair in rules.values():
            for rule_limits in rule_limits_pair:
                rule_limit_lower, rule_limit_upper = rule_limits.split('-')
                rule_limit_lower, rule_limit_upper = int(rule_limit_lower), int(rule_limit_upper)
                if field >= rule_limit_lower and field <= rule_limit_upper:
                    found_field_valid = True
                    break
        if not found_field_valid:
            sum_invalid_field += field
            break
    else:
        valid = True
    return valid, sum_invalid_field

sum_invalid_total = 0
list_nearby_tickets_valid = []

for line in lines_nearby_tickets:
    ticket = [int(ticket_field) for ticket_field in line.split(',')]
    valid, sum_invalid = check_valid(ticket, rules)
    if valid:
        list_nearby_tickets_valid.append(ticket)
    sum_invalid_total += sum_invalid

print(f'Ticket scanning error rate: {sum_invalid_total}')


# --- Part Two ---
#
# Now that you've identified which tickets contain invalid values, discard those tickets entirely. Use the remaining valid tickets to determine which field is which.
#
# Using the valid ranges for each field, determine what order the fields appear on the tickets. The order is consistent between all tickets: if seat is the third field, it is the third field on every ticket, including your ticket.
#
# For example, suppose you have the following notes:
#
# class: 0-1 or 4-19
# row: 0-5 or 8-19
# seat: 0-13 or 16-19
#
# your ticket:
# 11,12,13
#
# nearby tickets:
# 3,9,18
# 15,1,5
# 5,14,9
#
# Based on the nearby tickets in the above example, the first position must be row, the second position must be class, and the third position must be seat; you can conclude that in your ticket, class is 12, row is 11, and seat is 13.
#
# Once you work out which field is which, look for the six fields on your ticket that start with the word departure. What do you get if you multiply those six values together?


from copy import deepcopy
from math import prod

def check_field(list_field_numbers, rules, list_rule_names_avail):
    list_rule_names = deepcopy(list_rule_names_avail)
    for field in list_field_numbers:
        for rule_name in list_rule_names:
            rule_limits_pair = rules[rule_name]
            for rule_limits in rule_limits_pair:
                rule_limit_lower, rule_limit_upper = rule_limits.split('-')
                rule_limit_lower, rule_limit_upper = int(rule_limit_lower), int(rule_limit_upper)
                if field >= rule_limit_lower and field <= rule_limit_upper:
                    break
            else:
                # print(f'Removing \'{rule_name}\' from {list_rule_names}')
                list_rule_names.remove(rule_name)
    if len(list_rule_names) == 1:
        list_rule_names_avail.remove(list_rule_names[0])
        return list_rule_names[0]
    else:
        return None

list_rule_names = [str(rule_name) for rule_name in rules.keys()]
list_departure_index = []

while True:
    for index in range(len(my_ticket)):
        list_field_numbers = [ticket[index] for ticket in list_nearby_tickets_valid]
        field = check_field(list_field_numbers, rules, list_rule_names)
        if field is not None and 'departure' in field:
            # print(f'Index of \'{field}\' is {index}')
            list_departure_index.append(index)
    if len(list_rule_names) == 0:
        break

list_departure_value = [int(my_ticket[index]) for index in list_departure_index]

print(f'Prod of departure fields: {prod(list_departure_value)}')
