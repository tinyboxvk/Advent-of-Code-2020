# --- Day 21: Allergen Assessment ---
#
# You reach the train's last stop and the closest you can get to your vacation island without getting wet. There aren't even any boats here, but nothing can stop you now: you build a raft. You just need a few days' worth of food for your journey.
#
# You don't speak the local language, so you can't read any ingredients lists. However, sometimes, allergens are listed in a language you do understand. You should be able to use this information to determine which ingredient contains which allergen and work out which foods are safe to take with you on your trip.
#
# You start by compiling a list of foods (your puzzle input), one food per line. Each line includes that food's ingredients list followed by some or all of the allergens the food contains.
#
# Each allergen is found in exactly one ingredient. Each ingredient contains zero or one allergen. Allergens aren't always marked; when they're listed (as in (contains nuts, shellfish) after an ingredients list), the ingredient that contains each listed allergen will be somewhere in the corresponding ingredients list. However, even if an allergen isn't listed, the ingredient that contains that allergen could still be present: maybe they forgot to label it, or maybe it was labeled in a language you don't know.
#
# For example, consider the following list of foods:
#
# mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
# trh fvjkl sbzzf mxmxvkd (contains dairy)
# sqjhc fvjkl (contains soy)
# sqjhc mxmxvkd sbzzf (contains fish)
#
# The first food in the list has four ingredients (written in a language you don't understand): mxmxvkd, kfcds, sqjhc, and nhms. While the food might contain other allergens, a few allergens the food definitely contains are listed afterward: dairy and fish.
#
# The first step is to determine which ingredients can't possibly contain any of the allergens in any food in your list. In the above example, none of the ingredients kfcds, nhms, sbzzf, or trh can contain an allergen. Counting the number of times any of these ingredients appear in any ingredients list produces 5: they all appear once each except sbzzf, which appears twice.
#
# Determine which ingredients cannot possibly contain any of the allergens in your list. How many times do any of those ingredients appear?


from operator import itemgetter
from collections import defaultdict

with open('day21input.txt') as input_file:
    lines = input_file.read().splitlines()

# lines = [
#     'mxmxvkd kfcds sqjhc nhms (contains dairy, fish)',
#     'trh fvjkl sbzzf mxmxvkd (contains dairy)',
#     'sqjhc fvjkl (contains soy)',
#     'sqjhc mxmxvkd sbzzf (contains fish)'
# ]

dict_ingre_aller = defaultdict(list)

for line in lines:
    ingredients, allergens = line.split(' (contains ')
    ingredients = ingredients.split(' ')
    allergens = allergens.replace(')', '')
    allergens = allergens.split(', ')
    for ingredient in ingredients:
        for allergen in allergens:
            if allergen not in dict_ingre_aller[ingredient]:
                dict_ingre_aller[ingredient] = dict_ingre_aller[ingredient] + [allergen]

for line in lines:
    ingredients, allergens = line.split(' (contains ')
    ingredients = ingredients.split(' ')
    allergens = allergens.replace(')', '')
    allergens = allergens.split(', ')
    for allergen in allergens:
        for ingr, alle in dict_ingre_aller.items():
            if allergen in alle:
                if ingr not in ingredients:
                    dict_ingre_aller[ingr] = [
                        allergen_new for allergen_new in dict_ingre_aller[ingr] if allergen_new != allergen]

# print(dict_ingre_aller)

list_impossble_ingredients = []

for ingr, alle in dict_ingre_aller.items():
    if alle == []:
        list_impossble_ingredients.append(ingr)

# print(list_impossble_ingredients)

for impos_ingr in list_impossble_ingredients:
    dict_ingre_aller.pop(impos_ingr)

count_occurrence_impossble_ingredients = 0

for line in lines:
    ingredients, allergens = line.split(' (contains ')
    ingredients = ingredients.split(' ')
    allergens = allergens.replace(')', '')
    allergens = allergens.split(', ')
    for impos_ingr in list_impossble_ingredients:
        if impos_ingr in ingredients:
            count_occurrence_impossble_ingredients += 1

print(f'Appearances: {count_occurrence_impossble_ingredients}')
# print(dict_ingre_aller)


# --- Part Two ---
#
# Now that you've isolated the inert ingredients, you should have enough information to figure out which ingredient contains which allergen.
#
# In the above example:
#
#     mxmxvkd contains dairy.
#     sqjhc contains fish.
#     fvjkl contains soy.
#
# Arrange the ingredients alphabetically by their allergen and separate them by commas to produce your canonical dangerous ingredient list. (There should not be any spaces in your canonical dangerous ingredient list.) In the above example, this would be mxmxvkd,sqjhc,fvjkl.
#
# Time to stock your raft with supplies. What is your canonical dangerous ingredient list?


list_confirmed_pair = []

while len(dict_ingre_aller) != 0:
    list_to_remove = []
    for ingr, alle in dict_ingre_aller.items():
        if len(alle) == 1:
            list_confirmed_pair.append((ingr, alle[0]))
            list_to_remove.append(ingr)
            for i, a in dict_ingre_aller.items():
                if alle[0] in a:
                    dict_ingre_aller[i] = [
                        allergen_new for allergen_new in dict_ingre_aller[i] if allergen_new != alle[0]]
    for to_remove in list_to_remove:
        dict_ingre_aller.pop(to_remove)

list_confirmed_pair = sorted(list_confirmed_pair, key=itemgetter(1))
list_canonical_dangerous_ingredient = [di[0] for di in list_confirmed_pair]

print(f'Canonical dangerous ingredient list: {",".join(list_canonical_dangerous_ingredient)}')
