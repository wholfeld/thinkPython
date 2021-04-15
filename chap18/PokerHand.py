"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

from Card import Hand, Deck, Card
from poker_enums import RANK_NAMES, POKER_RANKED_HANDS, SUIT_NAMES


class PokerHand(Hand):
    """Represents a poker hand."""

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def __str__(self):
        cards_str = []
        for card in self.cards:
            cards_str.append(f'{RANK_NAMES[card.rank][0]}{SUIT_NAMES[card.suit][0]}')
        return " ".join(cards_str)


    def has_four_of_a_kind(self, rank_counts:dict):
        for count in rank_counts.values():
            if count == 4:
                return True
        return False

    def has_three_of_a_kind(self, rank_counts):
        for count in rank_counts.values():
            if count == 3:
                return True
        return False

    def has_pair(self, rank_counts):
        for count in rank_counts.values():
            if count == 2:
                return True
        return False

    def has_two_pair(self, rank_counts):
        pair_counts = 0
        for count in rank_counts.values():
            if count == 2:
                pair_counts += 1
                if pair_counts == 2:
                    return True
        return False

    def has_full_house(self, rank_counts):
        return self.has_three_of_a_kind(rank_counts) and self.has_pair(rank_counts)
        # has_trips = False
        # has_pair = False
        # for count in rank_counts.values:
        #     if count == 3:
        #         has_trips = True
        #     if count == 2:
        #         has_pair = True
        # return has_trips and has_pair
    
    def has_straight(self, rank_counts):
        last_rank = None
        row_count = 0
        has_ace = False
        for i in range(1, 14):
            if rank_counts[i] > 0:
                if not last_rank:
                    if i == 1:
                        has_ace = True
                elif last_rank + 1 == i:
                    row_count += 1
                    if row_count == 5:
                        return True
                else:
                    row_count = 1
                last_rank = i
        return row_count == 4 and has_ace


    
    def has_straight_flush(self):
        cards_in_row = 0
        ace_in_suit = None
        last_card = None
        for card in self.cards:
            if not last_card:
                last_card = card
                cards_in_row = 1
            if card.rank == 1:
                ace_in_suit = card.suit
            elif card.rank == 13 and cards_in_row == 4:
                if card.suit == ace_in_suit:
                    return True
            elif last_card.rank + 1 == card.rank and\
                last_card.suit == card.suit:
                cards_in_row += 1
                if cards_in_row == 5:
                    return True
                if cards_in_row == 4 and card.rank == 13:
                    if card.suit == ace_in_suit:
                        return True
                    return False
            else:
                cards_in_row = 1
            last_card = card
        return False

    def create_rank_counts(self):
        ranks_dictionary = {}
        for i in range(14):
            ranks_dictionary[i] = 0
        for card in self.cards:
            ranks_dictionary[card.rank] += 1
        return ranks_dictionary
    
def classify(poker_hand:PokerHand, classifier_dict:dict)->str:
    if poker_hand.has_straight_flush():
        classifier_dict[POKER_RANKED_HANDS[7]] += 1
        print(poker_hand)
        return POKER_RANKED_HANDS[7]

    ranked_counts = poker_hand.create_rank_counts()
    if poker_hand.has_four_of_a_kind(ranked_counts):
        classifier_dict[POKER_RANKED_HANDS[6]] += 1
        # print(poker_hand)
        return POKER_RANKED_HANDS[6]
    elif poker_hand.has_full_house(ranked_counts):
        classifier_dict[POKER_RANKED_HANDS[5]] += 1
        return POKER_RANKED_HANDS[5]
    elif poker_hand.has_flush():
        classifier_dict[POKER_RANKED_HANDS[4]] += 1
        return POKER_RANKED_HANDS[4]
    elif poker_hand.has_straight(ranked_counts):
        classifier_dict[POKER_RANKED_HANDS[3]] += 1
        return POKER_RANKED_HANDS[3]
    elif poker_hand.has_three_of_a_kind(ranked_counts):
        classifier_dict[POKER_RANKED_HANDS[2]] += 1
        return POKER_RANKED_HANDS[2]
    elif poker_hand.has_two_pair(ranked_counts):
        classifier_dict[POKER_RANKED_HANDS[1]] += 1
        return POKER_RANKED_HANDS[1]
    elif poker_hand.has_pair(ranked_counts):
        classifier_dict[POKER_RANKED_HANDS[0]] += 1
        return POKER_RANKED_HANDS[0]
    else: 
        return None

def check_statistics(hand_counts:int=1000)->dict:
    classifier_count = create_classifier_counts()
    for i in range(hand_counts // 7):
        deck = Deck()
        deck.shuffle()
        for j in range(7):
            hand = PokerHand()
            deck.move_cards(hand, 7)
            hand.cards.sort()
            classify(hand, classifier_count)
    for key in classifier_count:
        print(f'{key} happens one time in {hand_counts / classifier_count[key]}')
    return classifier_count


def create_classifier_counts():
    classifier_counts = {}
    for ranked_hands in POKER_RANKED_HANDS:
        classifier_counts[ranked_hands] = 0
    return classifier_counts


if __name__ == '__main__':
    stats = check_statistics(70000)
    print(stats)
    # make a deck
    # deck = Deck()
    # deck.shuffle()

    # deal the cards and classify the hands
    # for i in range(7):
    #     hand = PokerHand()
    #     deck.move_cards(hand, 7)
    #     hand.sort()
    #     print(hand)
    #     print(hand.has_flush())
    #     print('')

