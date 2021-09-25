
from random import shuffle

def createDeck(): 
    Deck = []
    
    faceValues = ["A","J","Q","K"]
    for i in range(4):
        for card in range(2,11):
            Deck.append(str(card))
            
        for card in faceValues:
            Deck.append(card)
            
    shuffle(Deck)
    return(Deck)
    
cardDeck = createDeck()

print(cardDeck)

class Player:
    def __init__(self,hand = [],money = 100):
        self.hand = hand
        self.score = self.setScore()
        print(self.score)
        self.money = money
        #self.bet = bet # Initial bet of player
    
    def __str__(self):
        currentHand = ""
        
        for card in self.hand:
            currentHand += str(card) + " "
        finalStatus = currentHand + "score: " + str(self.score)
        return finalStatus
        
    def setScore(self):
        self.score = 0
        print(self.score)
        faceCardsDicts = {"A":11,"J":10,"Q":10,"K":10,"2":2,"3":3,
                         "4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10}
                         
        aceCounter = 0
        for card in self.hand:
            self.score += faceCardsDicts[card]
            if card == "A":
                aceCounter +=1
            if self.score > 21 and aceCounter !=0:
                self.score -= 10
                aceCounter -= 1
        return self.score
    def hit(self,card):  # Player can pick a card
        self.hand.append(card)
        self.score = self.setScore()
    
    def play(self,newHand):   # player can initiate a new round
        self.hand = newHand
        self.score = self.setScore()
        
    def pay(self,amount):   # player deals
        self.money  -= amount
        
    def win(self,amount): # player wins
        self.money += amount
                
Player1 = Player(["3","7","5"])
print(Player1)
Player1.hit("K")
Player1.hit("A")
print(Player1)

Player1.play(["A","K"])
print(Player1)

Player1.pay(20)
print(Player1.money)
Player1.win(40)
print(Player1.money)