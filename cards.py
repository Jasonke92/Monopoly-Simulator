import random

Comm_Cards = list(range(1,17))
random.shuffle(Comm_Cards)

class cards:
    def __init__(self,flag) -> None:
        self.flag = flag
        pass

    def draw(self, deck):
        draw = deck[0]
        deck.append(deck.pop(deck.index(draw)))
        return draw
# class commcards