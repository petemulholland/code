from Card import Card
import random

class Deck(object):
    """Represents a deck of playing cards"""

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
            
        return ', '.join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()

    def move_cards(self, deck, num):
        for i in range(num):
            deck.add_card(self.pop_card())

    # this crappy design creates a circular ref between Deck & Hand
    def deal_hands(self, num_hands, cards_per_hand):
        hands = []
        for i in range(num_hands):
            hand = Hand('%d' % (i))
            self.move_cards(hand, cards_per_hand)
            hands.append(hand)

        return hands


class Hand(Deck):
    """represent a hand of cards"""

    def __init__(self, label=''):
        self.cards = []
        self.label = label



if __name__ == '__main__':
    deck = Deck()

    deck.shuffle()
    print deck

    deck.sort()
    print deck
