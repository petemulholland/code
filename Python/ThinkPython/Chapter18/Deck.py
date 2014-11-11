from Card import Card

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
            
        return '\n'.join(res)


if __name__ == '__main__':
    deck = Deck()
    print deck