
class Card:
    def __init__(self, name, value, type, short):
        self.name = name
        self.value = value
        self.type = type
        self.short = short
    def __str__(self):
        return f"{self.name}{self.value}{self.type}"


c1 = Card("ace", 11, 1, "a")
c2 = Card("two", 2, 2, "2")
c3 = Card("three", 3, 3, "3")
c4 = Card("four", 4, 4, "4")
c5 = Card("five", 5, 5, "5")
c6 = Card("six", 6, 6, "6")
c7 = Card("seven", 7, 7, "7")
c8 = Card("eight", 8, 8, "8")
c9 = Card("nine", 9, 9, "9")
c10 = Card("ten", 10, 10, "10")
c11 = Card("jack", 10, 11, "j")
c12 = Card("queen", 10, 12, "q")
c13 = Card("king", 10, 13, "k")

cards = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13]

def hand_values():
    # base chip amount, base mult, + chips, + mult
    high_card = [5, 1, 0, 0]
    pair = [10, 2, 0, 0]
    two_pair = [20, 2, 0, 0]
    three_kind = [30, 3, 0, 0]
    straight = [30, 4, 0, 0]
    flush = [35, 4, 0, 0]
    four_kind = [60, 7, 0, 0]
    straight_flush = [100, 8, 0, 0]
    five_kind = [120, 12, 0, 0]
    flush_house = [140, 14, 0, 0]
    flush_five = [160, 16, 0, 0]

def hand(ranks, suits):
    if suits[0] == suits[1] and suits[1] == suits[2] and suits[2] == suits[3] and suits[3] == suits[4]:
        print("flush!")


def card_type(card):
    rank = card[0]
    suit = card[1]
    # check if correct values
    return rank, suit

def main():
    print("2-10, jack = j, queen = q, king = k, ace = a")
    print("Hearts = h, diamonds = d, clubs = c, spades = s")
    print("example answer: qh = queen of hearts, 5d = five of diamonds ")
    print("xx = no card")
    card1 = input("Card 1: ").lower()
    rank1, suit1 = card_type(card1)
    card2 = input("Card 2: ").lower()
    rank2, suit2 = card_type(card2)
    card3 = input("Card 3: ").lower()
    rank3, suit3 = card_type(card3)
    card4 = input("Card 4: ").lower()
    rank4, suit4 = card_type(card4)
    card5 = input("Card 5: ").lower()
    rank5, suit5 = card_type(card5)

    ranks = [rank1, rank2, rank3, rank4, rank5]
    suits = [suit1, suit2, suit3, suit4, suit5]
    hand(ranks, suits)

    for i in ranks:
        for c in cards:
            if c.short == i:
                print(c.name)



if __name__ == '__main__':
    main()