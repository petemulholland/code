from Card import *
from Deck import *
from Debug import *

if __name__ == '__main__':
    deck = Deck()

    deck.shuffle()

    hand = Hand('new hand')

    card = deck.pop_card()
    hand.add_card(card)

    deck.move_cards(hand, 4)

    print hand
    print find_defining_class(hand, 'shuffle')

    hands = deck.deal_hands(3, 5)
    for hand in hands:
        print hand 