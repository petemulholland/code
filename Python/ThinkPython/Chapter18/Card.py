class Card(object):
    """ Represents a playing card"""

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    # class variables
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', 
                   '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    # for this implementation suit is more important than rank,
    # so all Spaces outrank all diamonds etc.
    def __cmp__(self, other):
        c1 = self.suit, self.rank
        c2 = other.suit, other.rank
        return cmp(c1, c2)

def cmp_to_string(res):
    if res > 0:
        return ">"
    if res < 0:
        return "<"
    return "="

if __name__ == '__main__':
    card1 = Card(1, 11)
    card2 = Card(1, 11)
    card3 = Card(2, 8)

    print card1, cmp_to_string(cmp(card1, card2)), card2
    print card1, cmp_to_string(cmp(card1, card3)), card3
    print card3, cmp_to_string(cmp(card3, card2)), card2

    print card1