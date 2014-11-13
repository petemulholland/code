"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

from TPCard import *

class Hist(dict):
    """A map from each item (x) to its frequency."""

    def __init__(self, seq=[]):
        "Creates a new histogram starting with the items in seq."
        for x in seq:
            self.count(x)

    def count(self, x, f=1):
        "Increments the counter associated with item x."
        self[x] = self.get(x, 0) + f
        if self[x] == 0:
            del self[x]


class PokerHand(Hand):

    def __init__(self, label=''):
        Hand.__init__(self, label)

    def __str__(self):
        """Returns a human-readable string representation."""
        return '%s: %s' % (self.label, Deck.__str__(self))


    def make_histograms(self):
        """Computes histograms for suits and hands.

        Creates attributes:

          suits: a histogram of the suits in the hand.
          ranks: a histogram of the ranks.
          sets: a sorted list of the rank sets in the hand.
        """
        self.suits = Hist()
        self.ranks = Hist()
        
        for c in self.cards:
            self.suits.count(c.suit)
            self.ranks.count(c.rank)

    def has_pair(self):
        self.make_histograms()
        for val in self.ranks.values():
            if val >= 2:
                return True
        return False

    def has_2_pair(self):
        self.make_histograms()
        pairs = 0
        for val in self.ranks.values():
            if val >= 2:
                pairs += 1
        
        if pairs >= 2:
            return True

        return False

    def has_3_of_a_kind(self):
        self.make_histograms()
        for val in self.ranks.values():
            if val >= 3:
                return True
        return False

    def has_straight(self):
        self.make_histograms()
        # make a copy of the rank histogram before we mess with it
        ranks = self.ranks.copy()
        ranks[14] = ranks.get(1, 0)

        # see if we have 5 in a row
        count = 0
        for i in range(1, 15):
            if ranks.get(i, 0):
                count += 1
                if count == 5: return True
            else:
                count = 0
        return False

    def has_flush(self):
        self.make_histograms()
        """Returns True if the hand has a flush, False otherwise.
        Note that this works correctly for hands with more than 5 cards.
        """
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def has_full_house(self):
        self.make_histograms()
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
        self.make_histograms()
        for val in self.ranks.values():
            if val >= 4:
                return True
        return False

    def has_straight_flush(self):
        self.make_histograms()
        # make a sorted list of (suit, rank) tuples
        cds = []
        for c in self.cards:
            cds.append((c.suit, c.rank))
            if c.rank == 1:
                cds.append((c.suit, 14))
        cds.sort()
        
        suit = -1
        rank = -1
        count = 0
        for s, r in cds:
            if s != suit:
                suit = s
                rank = r
                count = 1
                continue
            if r == rank + 1:
                count += 1
                if count == 5: return True
                rank = r
            else:
                count = 1
                rank = r
        return False

    def classify(self):
        self.labels = []
        self.labels.append('High card')
        self.label = 'High card'

        if self.has_pair(): 
            self.labels.append('Pair')
            self.label = 'Pair'
        if self.has_2_pair(): 
            self.labels.append('2 pair')
            self.label = '2 pair'
        if self.has_3_of_a_kind(): 
            self.labels.append('3 of a kind')
            self.label = '3 of a kind'
        if self.has_straight(): 
            self.labels.append('Straight')
            self.label = 'Straight'
        if self.has_flush(): 
            self.labels.append('Flush')
            self.label = 'Flush'
        if self.has_full_house(): 
            self.labels.append('Full house')
            self.label = 'Full house'
        if self.has_4_of_a_kind(): 
            self.labels.append('4 of a kind')
            self.label = '4 of a kind'
        if self.has_straight_flush(): 
            self.labels.append('Straight flush')
            self.label = 'Straight flush'


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
    clba = Card(0, 1)
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
    hands.append(create_hand('Pair', [clb2, dmd2, hrt8, spd9, clba]))
    hands.append(create_hand('2 Pair', [clb2, dmd2, hrt3, spd9, clb3]))
    hands.append(create_hand('3 of a kind', [clb2, dmd2, hrt2, spd9, clb3]))
    hands.append(create_hand('Straight', [clb5, clb6, dmd7, spd9, hrt8]))
    hands.append(create_hand('Flush', [clb2, clb3, clb5, clb6, clb9]))
    hands.append(create_hand('House', [clb2, dmd2, hrt2, dmd3, clb3]))
    hands.append(create_hand('Poker', [clb2, dmd2, hrt2, spd2, clb3]))
    hands.append(create_hand('Straight Flush', [clb2, clb3, clb4, clb5, clb6]))
    hands.append(create_hand('Not Straight Flush', [clb3, clb4, clb5, clb6, dmd7, clb9]))

    #for hand in hands:
    #    test_hand(hand)
#
#    print 

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

class PokerDeck(Deck):
    """Represents a deck of cards that can deal poker hands."""

    def deal_hands(deck, num_cards=5, num_hands=10):
        hands = []
        for i in range(num_hands):        
            hand = PokerHand()
            deck.move_cards(hand, num_cards)
            hand.classify()
            hands.append(hand)
        return hands


def hand_probabilities():
    # the label histogram: map from label to number of occurances
    lhist = Hist()

    # loop n times, dealing 7 hands per iteration, 7 cards each
    n = 100
    for i in range(n):
        if i%1000 == 0:
            print i
            
        deck = PokerDeck()
        deck.shuffle()

        hands = deck.deal_hands(7, 7)
        for hand in hands:
            for label in hand.labels:
                lhist.count(label)
            
    # print the results
    total = 7.0 * n
    print total, 'hands dealt:'

     for label, freq in lhist.items():
        p = total / freq
        print '%s happens one time in %.2f' % (label, p)


if __name__ == '__main__':
    #test_poker_hands()
    hand_probabilities()
