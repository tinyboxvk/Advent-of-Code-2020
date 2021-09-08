# --- Day 22: Crab Combat ---
#
# It only takes a few hours of sailing the ocean on a raft for boredom to sink in. Fortunately, you brought a small deck of space cards! You'd like to play a game of Combat, and there's even an opponent available: a small crab that climbed aboard your raft before you left.
#
# Fortunately, it doesn't take long to teach the crab the rules.
#
# Before the game starts, split the cards so each player has their own deck (your puzzle input). Then, the game consists of a series of rounds: both players draw their top card, and the player with the higher-valued card wins the round. The winner keeps both cards, placing them on the bottom of their own deck so that the winner's card is above the other card. If this causes a player to have all of the cards, they win, and the game ends.
#
# For example, consider the following starting decks:
#
# Player 1:
# 9
# 2
# 6
# 3
# 1
#
# Player 2:
# 5
# 8
# 4
# 7
# 10
#
# This arrangement means that player 1's deck contains 5 cards, with 9 on top and 1 on the bottom; player 2's deck also contains 5 cards, with 5 on top and 10 on the bottom.
#
# The first round begins with both players drawing the top card of their decks: 9 and 5. Player 1 has the higher card, so both cards move to the bottom of player 1's deck such that 9 is above 5. In total, it takes 29 rounds before a player has all of the cards:
#
# -- Round 1 --
# Player 1's deck: 9, 2, 6, 3, 1
# Player 2's deck: 5, 8, 4, 7, 10
# Player 1 plays: 9
# Player 2 plays: 5
# Player 1 wins the round!
#
# -- Round 2 --
# Player 1's deck: 2, 6, 3, 1, 9, 5
# Player 2's deck: 8, 4, 7, 10
# Player 1 plays: 2
# Player 2 plays: 8
# Player 2 wins the round!
#
# -- Round 3 --
# Player 1's deck: 6, 3, 1, 9, 5
# Player 2's deck: 4, 7, 10, 8, 2
# Player 1 plays: 6
# Player 2 plays: 4
# Player 1 wins the round!
#
# -- Round 4 --
# Player 1's deck: 3, 1, 9, 5, 6, 4
# Player 2's deck: 7, 10, 8, 2
# Player 1 plays: 3
# Player 2 plays: 7
# Player 2 wins the round!
#
# -- Round 5 --
# Player 1's deck: 1, 9, 5, 6, 4
# Player 2's deck: 10, 8, 2, 7, 3
# Player 1 plays: 1
# Player 2 plays: 10
# Player 2 wins the round!
#
# ...several more rounds pass...
#
# -- Round 27 --
# Player 1's deck: 5, 4, 1
# Player 2's deck: 8, 9, 7, 3, 2, 10, 6
# Player 1 plays: 5
# Player 2 plays: 8
# Player 2 wins the round!
#
# -- Round 28 --
# Player 1's deck: 4, 1
# Player 2's deck: 9, 7, 3, 2, 10, 6, 8, 5
# Player 1 plays: 4
# Player 2 plays: 9
# Player 2 wins the round!
#
# -- Round 29 --
# Player 1's deck: 1
# Player 2's deck: 7, 3, 2, 10, 6, 8, 5, 9, 4
# Player 1 plays: 1
# Player 2 plays: 7
# Player 2 wins the round!
#
#
# == Post-game results ==
# Player 1's deck:
# Player 2's deck: 3, 2, 10, 6, 8, 5, 9, 4, 7, 1
#
# Once the game ends, you can calculate the winning player's score. The bottom card in their deck is worth the value of the card multiplied by 1, the second-from-the-bottom card is worth the value of the card multiplied by 2, and so on. With 10 cards, the top card is worth the value on the card multiplied by 10. In this example, the winning player's score is:
#
#    3 * 10
# +  2 *  9
# + 10 *  8
# +  6 *  7
# +  8 *  6
# +  5 *  5
# +  9 *  4
# +  4 *  3
# +  7 *  2
# +  1 *  1
# = 306
#
# So, once the game ends, the winning player's score is 306.
#
# Play the small crab in a game of Combat using the two decks you just dealt. What is the winning player's score?


from copy import deepcopy
from collections import deque

with open('day22input.txt') as input_file:
    lines = input_file.read().splitlines()

# lines = [
#     'Player 1:',
#     '9',
#     '2',
#     '6',
#     '3',
#     '1',
#     '',
#     'Player 2:',
#     '5',
#     '8',
#     '4',
#     '7',
#     '10'
# ]

# lines = [
#     'Player 1:',
#     '43',
#     '19',
#     '',
#     'Player 2:',
#     '2',
#     '29',
#     '14'
# ]


def print_decks(deck_1, deck_2):
    print(f"Player 1's deck: {', '.join([str(num) for num in deck_1])}")
    print(f"Player 2's deck: {', '.join([str(num) for num in deck_2])}")


def print_cards(card_1, card_2):
    print(f"Player 1 plays: {card_1}")
    print(f"Player 2 plays: {card_2}")


def calculate_score(deck):
    score = 0
    deck.reverse()
    for index, num in enumerate(deck):
        score += num * (index + 1)
    return score


def play(deck_1, deck_2):
    round_index = 0
    winner_game = None
    while deck_1 and deck_2:
        round_index += 1
        winner_round = None
        # print(f'-- Round {round_index} --')
        # print_decks(deck_1, deck_2)
        card_1 = deck_1.popleft()
        card_2 = deck_2.popleft()
        # print_cards(card_1, card_2)
        if card_1 > card_2:
            winner_round = 1
            deck_1.append(card_1)
            deck_1.append(card_2)
        else:
            winner_round = 2
            deck_2.append(card_2)
            deck_2.append(card_1)
        # print(f'Player {winner_round} wins the round!')
        # print()
    winner_game = 1 if len(deck_2) == 0 else 2
    return winner_game


def print_result(deck_1, deck_2, winner):
    print('== Post-game results ==')
    # print_decks(deck_1, deck_2)
    # print()
    if winner == 1:
        print(f"Player 1's score: {calculate_score(deck_1)}")
    else:
        print(f"Player 2's score: {calculate_score(deck_2)}")


index_sep = lines.index('')
deck_1 = deque([int(num) for num in lines[1:index_sep]])
deck_2 = deque([int(num) for num in lines[index_sep+2:]])
winner = play(deck_1, deck_2)
print_result(deck_1, deck_2, winner)
print('-----------------------')


# --- Part Two ---
#
# You lost to the small crab! Fortunately, crabs aren't very good at recursion. To defend your honor as a Raft Captain, you challenge the small crab to a game of Recursive Combat.
#
# Recursive Combat still starts by splitting the cards into two decks (you offer to play with the same starting decks as before - it's only fair). Then, the game consists of a series of rounds with a few changes:
#
#     Before either player deals a card, if there was a previous round in this game that had exactly the same cards in the same order in the same players' decks, the game instantly ends in a win for player 1. Previous rounds from other games are not considered. (This prevents infinite games of Recursive Combat, which everyone agrees is a bad idea.)
#     Otherwise, this round's cards must be in a new configuration; the players begin the round by each drawing the top card of their deck as normal.
#     If both players have at least as many cards remaining in their deck as the value of the card they just drew, the winner of the round is determined by playing a new game of Recursive Combat (see below).
#     Otherwise, at least one player must not have enough cards left in their deck to recurse; the winner of the round is the player with the higher-value card.
#
# As in regular Combat, the winner of the round (even if they won the round by winning a sub-game) takes the two cards dealt at the beginning of the round and places them on the bottom of their own deck (again so that the winner's card is above the other card). Note that the winner's card might be the lower-valued of the two cards if they won the round due to winning a sub-game. If collecting cards by winning the round causes a player to have all of the cards, they win, and the game ends.
#
# Here is an example of a small game that would loop forever without the infinite game prevention rule:
#
# Player 1:
# 43
# 19
#
# Player 2:
# 2
# 29
# 14
#
# During a round of Recursive Combat, if both players have at least as many cards in their own decks as the number on the card they just dealt, the winner of the round is determined by recursing into a sub-game of Recursive Combat. (For example, if player 1 draws the 3 card, and player 2 draws the 7 card, this would occur if player 1 has at least 3 cards left and player 2 has at least 7 cards left, not counting the 3 and 7 cards that were drawn.)
#
# To play a sub-game of Recursive Combat, each player creates a new deck by making a copy of the next cards in their deck (the quantity of cards copied is equal to the number on the card they drew to trigger the sub-game). During this sub-game, the game that triggered it is on hold and completely unaffected; no cards are removed from players' decks to form the sub-game. (For example, if player 1 drew the 3 card, their deck in the sub-game would be copies of the next three cards in their deck.)
#
# Here is a complete example of gameplay, where Game 1 is the primary game of Recursive Combat:
#
# === Game 1 ===
#
# -- Round 1 (Game 1) --
# Player 1's deck: 9, 2, 6, 3, 1
# Player 2's deck: 5, 8, 4, 7, 10
# Player 1 plays: 9
# Player 2 plays: 5
# Player 1 wins round 1 of game 1!
#
# -- Round 2 (Game 1) --
# Player 1's deck: 2, 6, 3, 1, 9, 5
# Player 2's deck: 8, 4, 7, 10
# Player 1 plays: 2
# Player 2 plays: 8
# Player 2 wins round 2 of game 1!
#
# -- Round 3 (Game 1) --
# Player 1's deck: 6, 3, 1, 9, 5
# Player 2's deck: 4, 7, 10, 8, 2
# Player 1 plays: 6
# Player 2 plays: 4
# Player 1 wins round 3 of game 1!
#
# -- Round 4 (Game 1) --
# Player 1's deck: 3, 1, 9, 5, 6, 4
# Player 2's deck: 7, 10, 8, 2
# Player 1 plays: 3
# Player 2 plays: 7
# Player 2 wins round 4 of game 1!
#
# -- Round 5 (Game 1) --
# Player 1's deck: 1, 9, 5, 6, 4
# Player 2's deck: 10, 8, 2, 7, 3
# Player 1 plays: 1
# Player 2 plays: 10
# Player 2 wins round 5 of game 1!
#
# -- Round 6 (Game 1) --
# Player 1's deck: 9, 5, 6, 4
# Player 2's deck: 8, 2, 7, 3, 10, 1
# Player 1 plays: 9
# Player 2 plays: 8
# Player 1 wins round 6 of game 1!
#
# -- Round 7 (Game 1) --
# Player 1's deck: 5, 6, 4, 9, 8
# Player 2's deck: 2, 7, 3, 10, 1
# Player 1 plays: 5
# Player 2 plays: 2
# Player 1 wins round 7 of game 1!
#
# -- Round 8 (Game 1) --
# Player 1's deck: 6, 4, 9, 8, 5, 2
# Player 2's deck: 7, 3, 10, 1
# Player 1 plays: 6
# Player 2 plays: 7
# Player 2 wins round 8 of game 1!
#
# -- Round 9 (Game 1) --
# Player 1's deck: 4, 9, 8, 5, 2
# Player 2's deck: 3, 10, 1, 7, 6
# Player 1 plays: 4
# Player 2 plays: 3
# Playing a sub-game to determine the winner...
#
# === Game 2 ===
#
# -- Round 1 (Game 2) --
# Player 1's deck: 9, 8, 5, 2
# Player 2's deck: 10, 1, 7
# Player 1 plays: 9
# Player 2 plays: 10
# Player 2 wins round 1 of game 2!
#
# -- Round 2 (Game 2) --
# Player 1's deck: 8, 5, 2
# Player 2's deck: 1, 7, 10, 9
# Player 1 plays: 8
# Player 2 plays: 1
# Player 1 wins round 2 of game 2!
#
# -- Round 3 (Game 2) --
# Player 1's deck: 5, 2, 8, 1
# Player 2's deck: 7, 10, 9
# Player 1 plays: 5
# Player 2 plays: 7
# Player 2 wins round 3 of game 2!
#
# -- Round 4 (Game 2) --
# Player 1's deck: 2, 8, 1
# Player 2's deck: 10, 9, 7, 5
# Player 1 plays: 2
# Player 2 plays: 10
# Player 2 wins round 4 of game 2!
#
# -- Round 5 (Game 2) --
# Player 1's deck: 8, 1
# Player 2's deck: 9, 7, 5, 10, 2
# Player 1 plays: 8
# Player 2 plays: 9
# Player 2 wins round 5 of game 2!
#
# -- Round 6 (Game 2) --
# Player 1's deck: 1
# Player 2's deck: 7, 5, 10, 2, 9, 8
# Player 1 plays: 1
# Player 2 plays: 7
# Player 2 wins round 6 of game 2!
# The winner of game 2 is player 2!
#
# ...anyway, back to game 1.
# Player 2 wins round 9 of game 1!
#
# -- Round 10 (Game 1) --
# Player 1's deck: 9, 8, 5, 2
# Player 2's deck: 10, 1, 7, 6, 3, 4
# Player 1 plays: 9
# Player 2 plays: 10
# Player 2 wins round 10 of game 1!
#
# -- Round 11 (Game 1) --
# Player 1's deck: 8, 5, 2
# Player 2's deck: 1, 7, 6, 3, 4, 10, 9
# Player 1 plays: 8
# Player 2 plays: 1
# Player 1 wins round 11 of game 1!
#
# -- Round 12 (Game 1) --
# Player 1's deck: 5, 2, 8, 1
# Player 2's deck: 7, 6, 3, 4, 10, 9
# Player 1 plays: 5
# Player 2 plays: 7
# Player 2 wins round 12 of game 1!
#
# -- Round 13 (Game 1) --
# Player 1's deck: 2, 8, 1
# Player 2's deck: 6, 3, 4, 10, 9, 7, 5
# Player 1 plays: 2
# Player 2 plays: 6
# Playing a sub-game to determine the winner...
#
# === Game 3 ===
#
# -- Round 1 (Game 3) --
# Player 1's deck: 8, 1
# Player 2's deck: 3, 4, 10, 9, 7, 5
# Player 1 plays: 8
# Player 2 plays: 3
# Player 1 wins round 1 of game 3!
#
# -- Round 2 (Game 3) --
# Player 1's deck: 1, 8, 3
# Player 2's deck: 4, 10, 9, 7, 5
# Player 1 plays: 1
# Player 2 plays: 4
# Playing a sub-game to determine the winner...
#
# === Game 4 ===
#
# -- Round 1 (Game 4) --
# Player 1's deck: 8
# Player 2's deck: 10, 9, 7, 5
# Player 1 plays: 8
# Player 2 plays: 10
# Player 2 wins round 1 of game 4!
# The winner of game 4 is player 2!
#
# ...anyway, back to game 3.
# Player 2 wins round 2 of game 3!
#
# -- Round 3 (Game 3) --
# Player 1's deck: 8, 3
# Player 2's deck: 10, 9, 7, 5, 4, 1
# Player 1 plays: 8
# Player 2 plays: 10
# Player 2 wins round 3 of game 3!
#
# -- Round 4 (Game 3) --
# Player 1's deck: 3
# Player 2's deck: 9, 7, 5, 4, 1, 10, 8
# Player 1 plays: 3
# Player 2 plays: 9
# Player 2 wins round 4 of game 3!
# The winner of game 3 is player 2!
#
# ...anyway, back to game 1.
# Player 2 wins round 13 of game 1!
#
# -- Round 14 (Game 1) --
# Player 1's deck: 8, 1
# Player 2's deck: 3, 4, 10, 9, 7, 5, 6, 2
# Player 1 plays: 8
# Player 2 plays: 3
# Player 1 wins round 14 of game 1!
#
# -- Round 15 (Game 1) --
# Player 1's deck: 1, 8, 3
# Player 2's deck: 4, 10, 9, 7, 5, 6, 2
# Player 1 plays: 1
# Player 2 plays: 4
# Playing a sub-game to determine the winner...
#
# === Game 5 ===
#
# -- Round 1 (Game 5) --
# Player 1's deck: 8
# Player 2's deck: 10, 9, 7, 5
# Player 1 plays: 8
# Player 2 plays: 10
# Player 2 wins round 1 of game 5!
# The winner of game 5 is player 2!
#
# ...anyway, back to game 1.
# Player 2 wins round 15 of game 1!
#
# -- Round 16 (Game 1) --
# Player 1's deck: 8, 3
# Player 2's deck: 10, 9, 7, 5, 6, 2, 4, 1
# Player 1 plays: 8
# Player 2 plays: 10
# Player 2 wins round 16 of game 1!
#
# -- Round 17 (Game 1) --
# Player 1's deck: 3
# Player 2's deck: 9, 7, 5, 6, 2, 4, 1, 10, 8
# Player 1 plays: 3
# Player 2 plays: 9
# Player 2 wins round 17 of game 1!
# The winner of game 1 is player 2!
#
#
# == Post-game results ==
# Player 1's deck:
# Player 2's deck: 7, 5, 6, 2, 4, 1, 10, 8, 9, 3
#
# After the game, the winning player's score is calculated from the cards they have in their original deck using the same rules as regular Combat. In the above game, the winning player's score is 291.
#
# Defend your honor as Raft Captain by playing the small crab in a game of Recursive Combat using the same two decks as before. What is the winning player's score?


game_counter = 0


def play_2(deck_1_orig, deck_2_orig, game_id):
    global game_counter
    game_counter += 1
    game_id += 1
    winner_game = None
    # print(f'=== Game {game_counter} ===')
    deck_1 = deepcopy(deck_1_orig)
    deck_2 = deepcopy(deck_2_orig)
    deck_1_seen = deque()
    deck_2_seen = deque()
    round_index = 0
    if winner_game != None:
        return winner_game, deck_1, deck_2
    while deck_1 and deck_2:
        if list(deck_1) in deck_1_seen or list(deck_2) in deck_2_seen:
            # print(list(deck_1), deck_1_seen)
            # print(list(deck_2), deck_2_seen)
            winner_game = 1
            break
        else:
            deck_1_seen.append(list(deck_1))
            deck_2_seen.append(list(deck_2))
        round_index += 1
        winner_round = None
        # print()
        # print(f'-- Round {round_index} (Game {game_id}) --')
        # print_decks(deck_1, deck_2)
        card_1 = deck_1.popleft()
        card_2 = deck_2.popleft()
        # print_cards(card_1, card_2)
        len_deck_1 = len(deck_1)
        len_deck_2 = len(deck_2)
        if len_deck_1 >= card_1 and len_deck_2 >= card_2:
            # print('Playing a sub-game to determine the winner...')
            # print()
            game_counter_current = game_counter
            winner_round, card_winner, card_loser = play_2(deque([deck_1[i] for i in range(card_1)]), deque([
                                                           deck_2[i] for i in range(card_2)]), game_counter)
            # print(f'The winner of game {game_counter_current+1} is player {winner_round}!')
            # print()
            # print(f'...anyway, back to game {game_id}.')
            # print(f'Player {winner_round} wins round {round_index} of game {game_id}!')
            if winner_round == 1:
                deck_1.append(card_1)
                deck_1.append(card_2)
            else:
                deck_2.append(card_2)
                deck_2.append(card_1)
        else:
            if card_1 > card_2:
                winner_round = 1
                card_winner, card_loser = card_1, card_2
                deck_1.append(card_winner)
                deck_1.append(card_loser)
            else:
                winner_round = 2
                card_winner, card_loser = card_2, card_1
                deck_2.append(card_winner)
                deck_2.append(card_loser)
            # print(f'Player {winner_round} wins round {round_index} of game {game_id}!')
    else:
        card_winner, card_loser = (card_1, card_2) if len(deck_2) == 0 else (card_2, card_1)
        winner_game = 1 if len(deck_2) == 0 else 2
    if game_id == 1:
        # print(f'The winner of game 1 is player {winner_game}!')
        # print()
        return winner_game, deck_1, deck_2
    else:
        return winner_game, card_winner, card_loser


deck_1 = deque([int(num) for num in lines[1:index_sep]])
deck_2 = deque([int(num) for num in lines[index_sep+2:]])

winner, deck_1_now, deck_2_now = play_2(deck_1, deck_2, 0)
print_result(deck_1_now, deck_2_now, winner)
