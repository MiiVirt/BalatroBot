
def cards():
    card_dict = {
        "two" : 2,
        "three" : 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9,
        "ten" : 10,
        "jack" : 10,
        "queen" : 10,
        "king" : 10,
        "ace" : 11
    }
    #card_dict.update({"ace" : 1})
    #print(card_dict["ace"])
    return card_dict

def poker_hands():
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

def hand():
    print("2-10, jack = j, queen = q, king = k, ace = a")
    print("Hearts = h, diamonds = d, clubs = c, spades = s")
    print("example answer: qh = queen of hearts, 5d = five of diamonds ")
    print("x = no card")
    card1 = input("Card 1: ")
    rank1, suit1 = card_type(card1)
    card2 = input("Card 2: ")
    rank2, suit2 = card_type(card2)
    card3 = input("Card 3: ")
    rank3, suit3 = card_type(card3)
    card4 = input("Card 4: ")
    rank4, suit4 = card_type(card4)
    card5 = input("Card 5: ")
    rank5, suit5 = card_type(card5)

    ranks = [rank1, rank2, rank3, rank4, rank5]
    suits = [suit1, suit2, suit3, suit4, suit5]

    if suit1 == suit2 and suit2 == suit3 and suit3 == suit4 and suit4 == suit5:
        print("flush!")

    for i
def card_type(card):
    rank = card[0]
    suit = card[1]
    # check if correct values
    return rank, suit


if __name__ == '__main__':
    hand()