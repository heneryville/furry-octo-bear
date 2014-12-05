import random
def generateNewDeck():
        deckBase=[1,2,3,4,5,6,7,8,9,10,11,12,13]
        cardsSpades=deckBase
        cardsClubs=[i+14 for i in range (13)]
        cardsDiamonds=[i+27 for i in range (13)]
        cardsHearts=[i+40 for i in range(13)]
        cardsFullDeck=cardsSpades+cardsClubs+cardsDiamonds+cardsHearts
        random.shuffle(cardsFullDeck)
        return cardsFullDeck

def dealTopCard(currentDeck):
        cardSuit=""
        cardFaceValue=""
        cardValue=0
        if currentDeck[0]<14:
                cardSuit="Spades"
                cardValue=currentDeck[0]
        elif currentDeck[0]>13 and currentDeck[0]<27:
                cardSuit="Clubs"
                cardValue=currentDeck[0]-13
        elif currentDeck[0]>26 and currentDeck[0]<40:
                cardSuit="Diamomds"
                cardValue=currentDeck[0]-26
        else:
                cardSuit="Hearts"
                cardValue=currentDeck[0]-39
        if cardValue==1:
                cardFaceValue=="Ace"
        elif cardValue==2:
                cardFaceValue=="Two"
        elif cardValue==3:
                cardFaceValue=="Three"
        elif cardValue==4:
                cardFaceValue=="Four"
        elif cardValue==5:
                cardFaceValue=="Five"
        elif cardValue==6:
                cardFaceValue=="Six"
        elif cardValue==7:
                cardFaceValue=="Seven"
        elif cardValue==8:
                cardFaceValue=="Eight"
        elif cardValue==9:
                cardFaceValue=="Nine"
        elif cardValue==10:
                cardFaceValue=="Ten"
        elif cardValue==11:
                cardFaceValue=="Jack"       
        elif cardValue==12:
                cardFaceValue=="Queen"    
        elif cardValue==13:
                cardFaceValue=="King"
        print cardFaceValue+" of " + cardSuit
        print cardFaceValue, cardValue
        copyDeck=[]
        for i in range (1, len(currentDeck)):
                copyDeck.append(currentDeck[i])
        return copyDeck

currentDeck=generateNewDeck()
numberOfCards=int(raw_input("Number of cards to deal? "))
for i in range(0,numberOfCards):
        currentDeck=dealTopCard(currentDeck)
        
