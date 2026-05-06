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

GameInfo = {
    "Round": 1,
    "PlayerTotal": 0,
    "DealerTotal": 0,
    "Win": False,

}



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
            RandomCardIndex = randint(0, len(CreatedCards[i]))
            print(len(CreatedCards[i]), RandomCardIndex)
            RandomCardValue = CreatedCards[i][RandomCardIndex]
            CreatedCards[i].pop(RandomCardIndex)
            return RandomCardValue, suit


def ReturnHands(CreatedCards):
    CreateableHands = {
        "Player": [],
        "Dealer": []
    }
    PlayerDealt = 0
    DealerDealt = 0

    print("Lifeline")

    while PlayerDealt <= 2 and DealerDealt <= 2:
        if DealerDealt < PlayerDealt:
            DealerDealt += 1
            DealerCard, DealerSuit = ReturnRandomSuit(CreatedCards)
            print(DealerCard, DealerSuit, DealerDealt)
            print(f"Line {inspect.currentframe().f_lineno}: something happened")
        else:
            if PlayerDealt == 2:
                continue
            PlayerDealt += 1
            PlayerCard, PlayerSuit = ReturnRandomSuit(CreatedCards)
            print(f"Line {inspect.currentframe().f_lineno}: something happened")
            print(PlayerCard, PlayerSuit, PlayerDealt)
    return None


def Deal():
    print("Sending First Hand")


def Hit():
    print("Sending Hit")

def BlackJackMainGameLoop():
    Cards = CreateCards()
    Hands = ReturnHands(Cards)


def main():
    print("Starting BlackJack Main Game Loop")
    BlackJackMainGameLoop()


# Testing Purposes
if __name__ == "__main__":
    main()
