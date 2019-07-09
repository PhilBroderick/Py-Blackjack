from random import randrange

class CardHand(object):

    def __init__(self):
        self.cards = []
        self.cards.append(randrange(1,11))
        self.cards.append(randrange(1,11))

    def getCards(self):
        return (str(self.cards))

    def addCard(self):
        self.cards.append(randrange(11))
        return self.getCards()

    def cardTotal(self):
        return sum(self.cards)

def startGame():

## start user hand
    userHand = CardHand()
    print("Users cards: " + userHand.getCards())
    userChoice = input("Would you like to (s)tick or (h)it?");
    choiceLower = userChoice.lower()
    while(choiceLower == "s" or choiceLower == "h"):
        if(choiceLower == "s"):
            print("Okay you stick - let's see what the dealer will do...")
            break;
        elif(choiceLower == "h"):
            print("Okay you decided to hit, will it pay off..")
            print("Hand: " + userHand.addCard())
            if(userHand.cardTotal() > 21):
                print("Aww you bust! Hard luck")
                break;
            else:
                choiceLower = input("What would you like to do now? (S)tick or (h)it?")

## start dealers hand
    dealerHand = CardHand()
    print("Dealers hand: " + dealerHand.getCards())
    dealerTotal = dealerHand.cardTotal()
    while(dealerTotal < 21):
        if(dealerTotal < 15):
            dealerHand.addCard()
            dealerTotal = dealerHand.cardTotal()
            print("Dealer's hand: " + dealerHand.getCards())
        elif(dealerTotal >= 15 and dealerTotal <= 21):
            print("Dealer sticks!")
            break;
        else:
            print("Dealer breaks")

## see who won
    if(userHand.cardTotal() > dealerHand.cardTotal()):
        print("You won!!")
    elif(userHand.cardTotal() == dealerHand.cardTotal()):
        print("Draw - dealer wins")
    else:
        print("Dealer wins - hard luck")
            
            
## start game
print("--------------------------------")
inputStr = input("Welcome to Blackjack, press 'Y' to begin or 'N' to exit: ")
if(inputStr == "Y" or inputStr == "y"):
    print("Let's start!")
    startGame()
    input()
elif(inputStr == "N"):
    print("Alright - goodbye!")
    

