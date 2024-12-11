
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

def hand_values(hand, card_values):

    score = 0
    card_score = sum(card_values)
    #print(card_score)

    # base chip amount, base mult, + chips, + mult
    high_card = [5, 1, 0, 0]
    pair = [10, 2, 0, 0]
    two_pair = [20, 2, 0, 0]
    three_kind = [30, 3, 0, 0]
    straight = [30, 4, 0, 0]
    flush = [35, 4, 0, 0]
    full_house = [40, 4, 0, 0]
    four_kind = [60, 7, 0, 0]
    straight_flush = [100, 8, 0, 0]
    five_kind = [120, 12, 0, 0]
    flush_house = [140, 14, 0, 0]
    flush_five = [160, 16, 0, 0]

    hands = {"high_card": high_card,
             "pair": pair,
             "two_pair": two_pair,
             "three_kind": three_kind,
             "straight": straight,
             "flush": flush,
             "full_house": full_house,
             "four_kind": four_kind,
             "straight_flush": straight_flush,
             "five_kind": five_kind,
             "flush_house": flush_house,
             "flush_five": flush_five}

    for i in hands:
        if i == hand:
            chips = hands.get(i)[0] + hands.get(i)[2]
            mult = hands.get(i)[1] + hands.get(i)[3]
            #print("Chips: ", chips,", Mult: ", mult)
            score = (chips+ card_score) * mult
    print("Score: ", score)
    return score

def score_evaluator(score1, score2):

    if score1 > score2:
        return score1
    elif score2 > score1:
        return score2
    else:
        print("Both scores are equal!")

def hand(ranks, suits):
    #high_card = False
    pair = False
    two_pair = False
    three_kind = False
    four_kind = False
    five_kind = False
    flush_five = False
    flush = False
    straight = False
    full_house = False
    flush_house = False
    straight_flush = False

    pairs = []
    pair_count = 0
    score = 0

    type_list = []
    value_list = []
    for i in ranks:
        for c in cards:
            if c.short == i:
                type_list.append(c.type)
                value_list.append(c.value)
    type_list.sort()

    #2-3-4-5 of a kind
    for i in type_list:
        if type_list.count(i) == 5:
            print("Five of a kind!")
            five_kind = True
            hand_values("five_kind", value_list)
            break
        elif type_list.count(i) == 4:
            print("Four of a kind!")
            four_kind = True
            hand_values("four_kind", value_list)
            break
        elif type_list.count(i) == 3 and three_kind == False:
            print("Three of a kind!")
            three_kind = True
            hand_values("three_kind", value_list)
            three_type = i
        elif type_list.count(i) == 2:
            print("a Pair!")
            pair = True
            hand_values("pair", value_list)
            if i not in pairs:
                pair_count += 1
                pairs.append(i)

    #2 pairs
    if len(pairs) > 1:
        print("Two pairs!")
        two_pair = True
        hand_values("two_pair", value_list)

    #Full house
    if pair == True and three_kind == True:
        print("Full house!")
        full_house == True
        hand_values("full_house", value_list)

    #Flush
    if suits[0] == suits[1] and suits[1] == suits[2] and suits[2] == suits[3] and suits[3] == suits[4]:
        print("flush!")
        flush = True
        hand_values("flush", value_list)

    #Straight
    if type_list == list(range(type_list[0], type_list[0] + len(type_list))):
        print("Straight!")
        straight = True
        hand_values("straight", value_list)
    elif type_list[0] == 1:
        type_list[0] = 14
        type_list.sort()
        #print(type_list)
        if type_list == list(range(type_list[0], type_list[0] + len(type_list))):
            print("Straight")
            straight = True
            hand_values("straight", value_list)
        type_list[-1] = 1
        type_list.sort()

    #Straigth Flush
    if flush == True and straight == True:
        print("Straight flush!")
        straight_flush = True
        hand_values("straight_flush", value_list)

    #Flush house
    if flush == True and full_house == True:
        print("Flush house!")
        flush_house == True
        hand_values("flush_house", value_list)

    #Flush five
    if flush == True and five_kind == True:
        print("Flush five!")
        flush_five == True
        hand_values("flush_five", value_list)

def card_type(card):
    if len(card) > 3:
        print("Too long card")

    elif len(card) == 3:
        rank = card[:2]
        suit = card[2]

    else:
        rank = card[0]
        suit = card[1]

    return rank, suit

def get_card(count):

    card_ranks = []
    card_suits = []
    while count > 0:
        card = input("Card: ").lower()
        rank, suit = card_type(card)
        card_ranks.append(rank)
        card_suits.append(suit)
        count -= 1
    return card_ranks, card_suits
def main():
    print("2-10, jack = j, queen = q, king = k, ace = a")
    print("Hearts = h, diamonds = d, clubs = c, spades = s")
    print("example answer: qh = queen of hearts, 5d = five of diamonds ")
    print("xx = no card")
    count = int(input("How many cards would you like to add? "))

    ranks, suits = get_card(count)
    hand(ranks, suits)

if __name__ == '__main__':
    main()