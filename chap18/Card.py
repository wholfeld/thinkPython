from __future__ import annotations
import poker_enums
import random

class Card:
    '''Represents a standard playing card.'''
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King',]

    def __init__(self, suit:int=0, rank:int=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{Card.rank_names[self.rank]} of {Card.suit_names[self.suit]}'

    def __lt__(self, other:Card) -> bool:
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2

class Deck:
    '''Represents a deck of cards'''

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def add_card(self, card:Card):
        self.cards.append(card)

    def pop_card(self):
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())
    
    def deal_hands(self, hands:int, cards_per_hand:int):
        hands_list = []
        for i in range(hands):
            hand = Hand()
            for j in range(cards_per_hand):
                card = self.pop_card()
                hand.add_card(card)
            hands_list.append(hand)
        return hands_list

def find_defining_class(obj, meth_name):
    # MRO is method resolution order
    for ty in type(obj).mro():
        if meth_name in ty.__dict__:
            return ty

class Hand(Deck):
    '''Represents a hand of playing cards'''
    def __init__(self, label=''):
        self.cards = []
        self.label = label
    


if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()
    hands = deck.deal_hands(4, 5)
    for hand in hands:
        print(hand)
        print('')
    # print(deck)
    # hand = Hand()
    # print(find_defining_class(hand, 'shuffle'))
