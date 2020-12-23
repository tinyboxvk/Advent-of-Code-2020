# --- Day 18: Operation Order ---
#
# As you look out the window and notice a heavily-forested continent slowly appear over the horizon, you are interrupted by the child sitting next to you. They're curious if you could help them with their math homework.
#
# Unfortunately, it seems like this "math" follows different rules than you remember.
#
# The homework (your puzzle input) consists of a series of expressions that consist of addition (+), multiplication (*), and parentheses ((...)). Just like normal math, parentheses indicate that the expression inside must be evaluated before it can be used by the surrounding expression. Addition still finds the sum of the numbers on both sides of the operator, and multiplication still finds the product.
#
# However, the rules of operator precedence have changed. Rather than evaluating multiplication before addition, the operators have the same precedence, and are evaluated left-to-right regardless of the order in which they appear.
#
# For example, the steps to evaluate the expression 1 + 2 * 3 + 4 * 5 + 6 are as follows:
#
# 1 + 2 * 3 + 4 * 5 + 6
#   3   * 3 + 4 * 5 + 6
#       9   + 4 * 5 + 6
#          13   * 5 + 6
#              65   + 6
#                  71
#
# Parentheses can override this order; for example, here is what happens if parentheses are added to form 1 + (2 * 3) + (4 * (5 + 6)):
#
# 1 + (2 * 3) + (4 * (5 + 6))
# 1 +    6    + (4 * (5 + 6))
#      7      + (4 * (5 + 6))
#      7      + (4 *   11   )
#      7      +     44
#             51
#
# Here are a few more examples:
#
#     2 * 3 + (4 * 5) becomes 26.
#     5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 437.
#     5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 12240.
#     ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 13632.
#
# Before you can help with the homework, you need to understand it yourself. Evaluate the expression on each line of the homework; what is the sum of the resulting values?


lines = []
with open('day18input.txt') as input_file:
    lines = input_file.read().splitlines()

# lines = [
#     '1 + (2 * 3) + (4 * (5 + 6))',
#     '2 * 3 + (4 * 5)',
#     '5 + (8 * 3 + 9 + 3 * 4 * 3)',
#     '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))',
#     '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'
# ]

def eval_new(math_string_list):
    # print(math_string_list)
    while '(' in math_string_list[0]:
        math_string_list[0] = math_string_list[0][1:]
    # print(f'First num: {math_string_list[0]}')
    while ')' in math_string_list[-1]:
        math_string_list[-1] = math_string_list[-1][:-1]
    # print(f'Last num: {math_string_list[-1]}')
    num_1 = math_string_list[0]
    for index in range(1, len(math_string_list)-1, 2):
        num_1 = eval(str(num_1)+''.join(math_string_list[index:index+2]))
    # print(f'Returning {num_1}')
    return str(num_1)

def eval_alt(math_string):
    while '(' in math_string:
        math_string_list = math_string.split(' ')
        # print(f'Operating on {math_string} (Length: {len(math_string_list)})')
        index_l = 0
        index_r = 0
        index = 0
        while ')' not in math_string_list[index]:
            index += 1
            if '(' in math_string_list[index]:
                index_l = index
            elif ')' in math_string_list[index]:
                index_r = index
        # print(f'Replacing {" ".join(math_string_list[index_l:index_r+1])} in {math_string}')
        math_string = math_string.replace('(' + math_string_list[index_l].replace('(', '') + ' ' + ' '.join(math_string_list[index_l+1:index_r]) + ' ' + math_string_list[index_r].replace(')', '') + ')', eval_new(math_string_list[index_l:index_r+1]))
        # print(f'math_string is now {math_string}')
    return eval_new(math_string.split(' '))

sum_weird_math = 0

for line in lines:
    result_weird_math = eval_alt(line)
    sum_weird_math += int(result_weird_math)
    # print('---------------------------------')

print(f'Sum: {sum_weird_math}')
print('---------------------------------')

# --- Part Two ---
#
# You manage to answer the child's questions and they finish part 1 of their homework, but get stuck when they reach the next section: advanced math.
#
# Now, addition and multiplication have different precedence levels, but they're not the ones you're familiar with. Instead, addition is evaluated before multiplication.
#
# For example, the steps to evaluate the expression 1 + 2 * 3 + 4 * 5 + 6 are now as follows:
#
# 1 + 2 * 3 + 4 * 5 + 6
#   3   * 3 + 4 * 5 + 6
#   3   *   7   * 5 + 6
#   3   *   7   *  11
#      21       *  11
#          231
#
# Here are the other examples from above:
#
#     1 + (2 * 3) + (4 * (5 + 6)) still becomes 51.
#     2 * 3 + (4 * 5) becomes 46.
#     5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 1445.
#     5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 669060.
#     ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 23340.
#
# What do you get if you add up the results of evaluating the homework problems using these new rules?


def eval_new_2(math_string_list):
    while '(' in math_string_list[0]:
        math_string_list[0] = math_string_list[0][1:]
    while ')' in math_string_list[-1]:
        math_string_list[-1] = math_string_list[-1][:-1]
    while '+' in math_string_list and len(math_string_list) > 3:
        index = 0
        while '+' != math_string_list[index]:
            index += 1
        # print(f'Replacing {" ".join(math_string_list[index-1:index+2])} in {math_string} with {eval("".join(math_string_list[index-1:index+2]))}')
        math_string_list = math_string_list[:index-1] + [str(eval(''.join(math_string_list[index-1:index+2])))] + math_string_list[index+2:]
    num_1 = math_string_list[0]
    for index in range(1, len(math_string_list)-1, 2):
        num_1 = eval(str(num_1)+''.join(math_string_list[index:index+2]))
    # print(f'Returning {num_1}')
    return int(num_1)

def eval_alt_2(math_string):
    print(math_string)
    while '(' in math_string:
        math_string_list = math_string.split(' ')
        # print(f'Operating on {math_string} (Length: {len(math_string_list)})')
        index_l = 0
        index_r = 0
        index = 0
        while ')' not in math_string_list[index]:
            index += 1
            if '(' in math_string_list[index]:
                index_l = index
            elif ')' in math_string_list[index]:
                index_r = index
        # print(f'Replacing {" ".join(math_string_list[index_l:index_r+1])} in {math_string}')
        math_string = math_string.replace('(' + math_string_list[index_l].replace('(', '') + ' ' + ' '.join(math_string_list[index_l+1:index_r]) + ' ' + math_string_list[index_r].replace(')', '') + ')', str(eval_new_2(math_string_list[index_l:index_r+1])))
        # print(f'math_string is now {math_string}')
        # print(math_string)
    return eval_new_2(math_string.split(' '))

sum_weird_math_2 = 0

# lines = ['5 * 7 + 2 + 7 + (4 + 7 * 4 * 6)']

for line in lines:
    print(result_weird_math := eval_alt_2(line))
    sum_weird_math_2 += result_weird_math
    # print(f'Sum: {sum_weird_math_2}')
    # print(f'{sum_weird_math_2}')
    print('---------------------------------')

print(f'Sum: {sum_weird_math_2}')
