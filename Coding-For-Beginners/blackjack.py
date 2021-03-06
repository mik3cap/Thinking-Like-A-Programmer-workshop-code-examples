#!/usr/bin/env python
"""This code plays a blackjack game with the user. It follows all the basic
rules of the blackjack card game. An external game library with an object
oriented card implementation is imported."""

import random
import sys

from termcolor import colored
from game_library.card import create_deck, deal, calculate_points


# First create the deck
deck = create_deck()

# Shuffle the deck
random.shuffle(deck)

dealer_hand = []
player_hand = []

dealer_total = 0
player_total = 0

bool_player_done = False

# Print a welcome message
print(colored("Welcome to blackjack! Highest to 21 wins. Dealing for you...",
              'green'))

# Deal two cards to the player
player_card = deal(deck)
player_hand.append(player_card)
player_total = calculate_points(player_hand)

print(colored("You have: " + player_card.get_card(), 'cyan'))

player_card = deal(deck)
player_hand.append(player_card)
player_total = calculate_points(player_hand)

print(colored("You have: " + player_card.get_card() + " , total of " +
              str(player_total), 'cyan'))

# It's possible the player can be dealt 21, if so don't give dealer cards
player_total = calculate_points(player_hand)

if player_total == 21:
    # Exit the program if 21 is dealt on the first hand
    print(colored("Player wins with %s!!" % (str(player_total), ), 'green'))

    sys.exit()
else:
    # Else deal two cards to the dealer
    print(colored("Now dealing for the dealer...", 'cyan'))

    dealer_card = deal(deck)
    dealer_hand.append(dealer_card)
    dealer_total = calculate_points(dealer_hand)

    print(colored("Dealer deals one card up, dealer has: " +
                  dealer_card.get_card() + " , total of " +
                  str(dealer_total), 'cyan'))

    dealer_card = deal(deck)
    dealer_hand.append(dealer_card)
    dealer_total = calculate_points(dealer_hand)

    print(colored("Dealer deals another card down.", 'cyan'))

# Play the game until the player or dealer finish
while True:
    if not bool_player_done:
        player_action = input("\nDo you want to hit or stand? (h or s): ")
    else:
        player_action = "s"

    # Check to see if input is hit or stand
    if player_action == "h" and not bool_player_done:
        # If hit, deal a card
        player_card = deal(deck)
        player_hand.append(player_card)
        player_total = calculate_points(player_hand)

        print(colored("Player dealt: " + player_card.get_card() +
                      " , total of " + str(player_total), 'cyan'))

        if player_total > 21:
            # Check to see if player busts
            print(colored("Busted! Game over.", 'red'))

            break
        elif player_total == 21:
            # Check to see if player wins
            print(colored("Player has 21!", 'green'))
            bool_player_done = True
    elif player_action == "s":
        # If stand, player is done, deal dealer's cards
        string_dealer = "Dealer reveals his cards: "

        for each_card in dealer_hand:
            string_dealer += each_card.get_card() + " , "

        dealer_total = calculate_points(dealer_hand)
        string_dealer += "total of " + str(dealer_total)

        print(colored(string_dealer, 'cyan'))

        while True:
            # Dealer must hit if points are <= 16 must stand on > 16
            if dealer_total <= 16:
                # Dealer must hit
                print(colored("Dealer hits...", 'cyan'))

                dealer_card = deal(deck)
                dealer_hand.append(dealer_card)
                dealer_total = calculate_points(dealer_hand)

                print(colored("Dealer has: " + dealer_card.get_card() +
                              " , total of " + str(dealer_total), 'cyan'))

                if dealer_total > 21:
                    # Check to see if dealer busts
                    print(colored("Dealer busted! Player wins!!", 'green'))

                    break
                elif dealer_total == 21:
                    # If dealer gets 21, house wins
                    print(colored("Dealer wins! Game over.", 'red'))

                    break
            else:
                # Dealer has to stand, check to see who wins
                print(colored("Dealer stands.", 'cyan'))

                if player_total > dealer_total:
                    # Player wins with more points
                    print(colored("Player wins with %s!!" %
                                  (str(player_total), ), 'green'))
                elif player_total == dealer_total:
                    # Or there is a tie
                    print(colored("Push! Looks like a tie - Game over.",
                                  'cyan'))
                else:
                    # Or the dealer wins with more points
                    print(colored("Dealer wins with %s! Game over." %
                                  (str(dealer_total), ), 'red'))

                break

        break
    else:
        # Or maybe there is bad input
        print(colored("Bad input! Must be h or s to hit or stand.", 'red'))

        continue
