import random
import inspect
from random import randint

Properties = {
    "Decks": 1,
    "Cards": 52,
    "Suits": {
       "Spades": 1,
        "Clubs":  2,
        "Diamonds": 3,
        "Hearts": 4,
    },
    "MaxNumberOfCardsPerSuit": 4,
    "Players": {},
    "CardTypes": [1,2,3,4,5,6,7,8,9,10,"Q","K","A"]
}

CardValues = {
    10: ["Q", "K", "A"],
    "Joker": "Any",
    "Ace": "A"
}


CreateableHands = {
    "Player": {
        "Card": [],
        "Suit": [],
        "PlayerTotal": 0,
        "Win": False,
        "MoneyOnTheLine": 0
    },
    "Dealer": {
        "Card": [],
        "Suit": [],
        "DealerTotal": 0,
        "Win": False,
    }
}



def ReturnValue(Value):
    for i in CardValues:
        if Value == CardValues[i]:
            return CardValues[i]
        else:
            return Value



def CreateCards():
    CreatedCards = {}
    for i in Properties["Suits"]:
        CreatedCards[i] = Properties["CardTypes"]
    return CreatedCards


def ReturnRandomSuit(CreatedCards):
    suitvalue = random.randint(1, 4)
    suit = False
    for i in Properties["Suits"]:
        if Properties["Suits"][i] == suitvalue and len(CreatedCards[i]) > 0:
            suit = i
            RandomCardIndex = randint(0, len(CreatedCards[i]) - 1)
            print(len(CreatedCards[i]), RandomCardIndex)
            RandomCardValue = CreatedCards[i][RandomCardIndex]
            CreatedCards[i].pop(RandomCardIndex)
            return RandomCardValue, suit


def ReturnHands(CreatedCards):
    PlayerDealt = 0
    DealerDealt = 0

    print("Lifeline")

    while PlayerDealt <= 2 and DealerDealt <= 2:
        if DealerDealt < PlayerDealt:
            DealerDealt += 1
            DealerCard, DealerSuit = ReturnRandomSuit(CreatedCards)
            print(DealerCard, DealerSuit, DealerDealt)
            print(f"Line {inspect.currentframe().f_lineno}: something happened")
            CreateableHands["Dealer"]["Card"].append(DealerCard)
            CreateableHands["Dealer"]["DealerTotal"] += DealerDealt
            CreateableHands["Dealer"]["Suit"].append(DealerSuit)
        else:
            if PlayerDealt == 2:
                break
            PlayerDealt += 1
            PlayerCard, PlayerSuit = ReturnRandomSuit(CreatedCards)
            print(f"Line {inspect.currentframe().f_lineno}: something happened")
            print(PlayerCard, PlayerSuit, PlayerDealt)
            CreateableHands["Player"]["Card"].append(PlayerCard)
            CreateableHands["Player"]["PlayerTotal"] += PlayerDealt
            CreateableHands["Player"]["Suit"].append(PlayerSuit)

    return CreateableHands





def Hit():
    print("Sending Hit")

def BlackJackMainGameLoop(money):
    if not money:
        money += 1
    else:
        CreateableHands["Player"]["MoneyOnTheLine"] += money
    Cards = CreateCards()
    Hands = ReturnHands(Cards)
    print(Hands)

def main():
    print("Starting BlackJack Main Game Loop")
    BlackJackMainGameLoop(200)


# Testing Purposes
if __name__ == "__main__":
    main()
