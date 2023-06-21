import random
# Create a deck of cards with a random order
class simulateGame():

    def generateDeck(self):
        randomDeck = []
        for num in range(1, 14):
            randomDeck.extend([num] * 4)
        # Shuffle the list
        random.shuffle(randomDeck)
        # Print the shuffled list
       # print(randomDeck)
        return randomDeck

    #returns the next card in the deck
    def getNextCard(self):
        self.nextCard+=1
        return self.deck[self.nextCard-1]

    #checks for centuries
    def century(self):
        for i in range(0,3):
            if(self.gameBoard[i]==self.gameBoard[i+1] and self.gameBoard[i+1]==self.gameBoard[i+2] and self.gameBoard[i]!=0):
                self.runs+=100
                if(self.nextCard<49):
                    self.gameBoard[i] = self.getNextCard()
                    self.gameBoard[i+1] = self.getNextCard()
                    self.gameBoard[i+2] = self.getNextCard()

                else:
                    self.runs+= 52-self.nextCard
                    for j in range(0,52-self.nextCard):
                       self.gameBoard[i+j] =self.getNextCard()
                   

                return True
            elif(self.gameBoard[i]==self.gameBoard[i+3] and self.gameBoard[i+3]==self.gameBoard[i+6] and self.gameBoard[i]!=0):
                self.runs+=100
                if(self.nextCard<49):
                    self.gameBoard[i] = self.getNextCard()
                    self.gameBoard[i+3] = self.getNextCard()
                    self.gameBoard[i+6] = self.getNextCard()
                else:
                    self.runs+= 52-self.nextCard
                    for j in range(0,52-self.nextCard):
                       self.gameBoard[i+(j*3)] =self.getNextCard()
                   
                    
                return True
        return False

    #checks for half centuries
    def halfCentury(self):
        if(self.gameBoard[0]==self.gameBoard[4] and self.gameBoard[4]==self.gameBoard[8]and self.gameBoard[4]!=0):
            self.runs+=50
            if(self.nextCard<49):
                self.gameBoard[0] = self.getNextCard()
                self.gameBoard[4] = self.getNextCard()
                self.gameBoard[8] = self.getNextCard()
            else:
                   self.runs+= 52-self.nextCard
                   for j in range(0,52-self.nextCard):
                       self.gameBoard[j*4] =self.getNextCard()
            return True
        
        elif(self.gameBoard[6]==self.gameBoard[5] and self.gameBoard[4]==self.gameBoard[2]and self.gameBoard[4]!=0):
            self.runs+=50
            if(self.nextCard<49):
                self.gameBoard[6] = self.getNextCard()
                self.gameBoard[4] = self.getNextCard()
                self.gameBoard[2] = self.getNextCard()
            else:
                   self.runs+= 52-self.nextCard
                   for j in range(0,52-self.nextCard):
                      self.gameBoard[(j+1)*2] =self.getNextCard()      
            return True
        
        return False
    
    def __init__(self):
        self.deck = self.generateDeck()
        self.nextCard = 0
        self.gameBoard = [0,0,0,0,0,0,0,0,0]
        self.nextSlot = 0 #keeps track of next available slot on gameboard
        self.gameEnded = False
        self.numCenturies = 0
        self.numHalfs = 0
        self.runs = 0

   # checks if a pair of cards is there on the game board 
    def pairAvailable(self, num1, num2):
        if (num1 in self.gameBoard) and (num2 in self.gameBoard):
            if(self.nextCard<50):
                self.runs+=2
                self.gameBoard[self.gameBoard.index(num1)] = self.getNextCard()
                self.gameBoard[self.gameBoard.index(num2)] = self.getNextCard()
            else:
                self.runs+=1
                self.gameBoard[self.gameBoard.index(num1)] = self.getNextCard()

            return True
        return False
    
    #checks if KQJ are there on the board
    def kqjAvailable(self):
        if (11 in self.gameBoard) and (12 in self.gameBoard) and (13 in self.gameBoard):
            if(self.nextCard<49):
                self.runs += 3
                self.gameBoard[self.gameBoard.index(13)] = self.getNextCard()
                self.gameBoard[self.gameBoard.index(12)] = self.getNextCard()
                self.gameBoard[self.gameBoard.index(11)] =self.getNextCard()
            else:
                self.runs+= 52-self.nextCard
                for i in range(11,11+52-self.nextCard):
                    self.gameBoard[self.gameBoard.index(i)] =self.getNextCard()
            return True
        return False
    
    #prints the game board for debugging purposes
    def printDeck(self):
        
        for i in range (0,3):
            for j in range(0,3):
                if(self.gameBoard[i*3 + j]< 11):
                    print("%2d"%self.gameBoard[i*3 + j], end = "  ")
                else:
                    if self.gameBoard[i*3 + j] == 11 :
                        print(" J",end = "  ")
                    elif self.gameBoard[i*3 + j] == 12 :
                        print(" Q",end = "  ")
                    else:
                        print(" K",end = "  ")

            
            print()
        print()
    # simulates the entire game for cricket

    def startGame(self):
        self.gameBoard[0] = self.getNextCard()
        self.gameBoard[1] = self.getNextCard()
        self.runs +=2
        self.nextSlot = 2
        while((self.nextSlot<9 or self.gameEnded == False) and self.nextCard < 52):
            #rule where centuries arent covered
            if self.century():
               # print("CENTURYYYY")
                self.numCenturies+=1
            elif self.halfCentury():
               # print("HALF CENTURYYYY")
                self.numHalfs+=1

            elif self.kqjAvailable():
                task = "DO SHIT"
            elif self.pairAvailable(10,1):
                task = "DO SHIT"
            elif self.pairAvailable(9,2):
                task = "DO SHIT"            
            elif self.pairAvailable(8,3):
                task = "DO SHIT"
            elif self.pairAvailable(7,4):
                task = "DO SHIT"
            elif self.pairAvailable(6,5):
                task = "DO SHIT"
            elif self.nextSlot<9:
                self.gameBoard[self.nextSlot] = self.getNextCard()
                self.runs+=1
                self.nextSlot+=1
            else:
                self.gameEnded = True
            #self.printDeck()
            
        
        if self.gameEnded == False:
            self.deck = self.generateDeck()
            self.nextCard = 0
            self.gameBoard = [0,0,0,0,0,0,0,0,0]
            self.nextSlot = 0 #keeps track of next available slot on gameboard
            self.startGame() #recursively calls startGame in case all cards are laid out

        """
        print(" RUNS  = ", self.runs)
        print(" CENTURIES  = ", self.numCenturies)
        print("HALF CENTURIES = ", self.numHalfs)
        """
        # The total runs are 0 in case only 9 cards are laid out
        if(self.runs ==9):
            self.runs = 0
        
        return[self.runs,self.numCenturies,self.numHalfs]


        

            



   
