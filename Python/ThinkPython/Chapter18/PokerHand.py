"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

from TPCard import *


class PokerHand(Hand):

    def __init__(self, label=''):
        Hand.__init__(self, label)

    def __str__(self):
        """Returns a human-readable string representation."""
        return '%s: %s' % (self.label, Deck.__str__(self))


    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def rank_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_pair(self):
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 2:
                return True
        return False

    def has_2_pair(self):
        self.rank_hist()
        pairs = 0
        for val in self.ranks.values():
            if val >= 2:
                pairs += 1
        
        if pairs >= 2:
            return True

        return False

    def has_3_of_a_kind(self):
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 3:
                return True
        return False

    def has_straight(self):
        # TODO: implement has_straight
        return False

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def has_full_house(self):
        self.rank_hist()
        has_3k = False
        pairs = 0
        for val in self.ranks.values():
            if val >= 3:
                has_3k = True
            if val >= 2:
                pairs += 1

        # 3 of kind, will also count as a pair, need at least 2 pairs and 3 of a kind
        return has_3k and pairs >= 2

    def has_4_of_a_kind(self):
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 4:
                return True
        return False

    def has_straight_flush(self):
        # TODO: fwith more than 5 cards flush and straight could be different combinations here
        return self.has_flush() and self.has_straight()

    def classify(self):
        if self.has_straight_flush(): self.label = 'Straight flush'
        elif self.has_4_of_a_kind(): self.label = '4 of a kind'
        elif self.has_full_house(): self.label = 'Full house'
        elif self.has_flush(): self.label = 'Flush'
        elif self.has_straight(): self.label = 'Straight'
        elif self.has_3_of_a_kind(): self.label = '3 of a kind'
        elif self.has_2_pair(): self.label = '2 pair'
        elif self.has_pair(): self.label = 'Pair'
        else: self.label = 'Dross'


def test_classify(hand):
    old_label = hand.label
    hand.classify()
    print hand, 'was: ', old_label


def test_hand(hand):
    print hand,
    # TODO: 
    # for each method on hand:
    #   if method name starts with 'has_'
    #       call method & print name if returns true.    
    if hand.has_pair(): print 'has_pair', 
    if hand.has_2_pair(): print 'has_2_pair', 
    if hand.has_3_of_a_kind(): print 'has_3_of_a_kind', 
    if hand.has_straight(): print 'has_straight', 
    if hand.has_flush(): print 'has_flush', 
    if hand.has_full_house(): print 'has_full_house', 
    if hand.has_4_of_a_kind(): print 'has_4_of_a_kind', 
    if hand.has_straight_flush(): print 'has_straight_flush', 
    print


def create_hand(name, cards):
    hand = PokerHand(name)
    for card in cards:
        hand.add_card(card)

    return hand

def test_poker_hands():
    hands = []
    clb2 = Card(0, 2)
    clb3 = Card(0, 3)
    clb4 = Card(0, 4)
    clb5 = Card(0, 5)
    clb6 = Card(0, 6)
    clb9 = Card(0, 9)
    dmd2 = Card(1, 2)
    dmd3 = Card(1, 3)
    dmd7 = Card(1, 7)
    hrt2 = Card(2, 2)
    hrt3 = Card(2, 3)
    hrt8 = Card(2, 8)
    spd2 = Card(3, 2)
    spd9 = Card(3, 9)

    hands.append(create_hand('trash', [clb2, dmd3, hrt8, spd9, clb4]))
    hands.append(create_hand('Pair', [clb2, dmd2, hrt8, spd9, clb4]))
    hands.append(create_hand('2 Pair', [clb2, dmd2, hrt3, spd9, clb3]))
    hands.append(create_hand('3 of a kind', [clb2, dmd2, hrt2, spd9, clb3]))
    hands.append(create_hand('Straight', [clb5, clb6, dmd7, spd9, hrt8]))
    hands.append(create_hand('Flush', [clb2, clb3, clb5, clb6, clb9]))
    hands.append(create_hand('House', [clb2, dmd2, hrt2, dmd3, clb3]))
    hands.append(create_hand('Poker', [clb2, dmd2, hrt2, spd2, clb3]))
    hands.append(create_hand('Straight Flush', [clb2, clb3, clb4, clb5, clb6]))

    for hand in hands:
        test_hand(hand)

    print 

    for hand in hands:
        test_classify(hand)

    print

def old_main():    
    # make a deck
    deck = Deck()
    deck.shuffle()

    # deal the cards and classify the hands
    for i in range(7):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        print hand
        print hand.has_flush()
        print ''

if __name__ == '__main__':
    test_poker_hands()
