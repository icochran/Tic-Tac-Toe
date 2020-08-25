# Issy Cochran
# Hw 10
# 12/10/18
# TIC TAC TOE
# Has some design issues but the game is functional and it prints out instructions in the shell 

from pyprocessing import *

"""
To play the game click the run current script button and follow the instructions that are printed out. The heart symbol takes a little longer to load
so you need to wait a little to see it pop up. You will need to download the three files I also turned in. You can replay the game by pressing the
y button or you can click the stop button and press the run button again. When you play again the pyprocessing window is put behind the thonny window,
so after you enter the players names you will have to first click on the pyprocessing window and then click to make the first move.
"""

class Player:
    """
    Attributes: symbol- is the player a heart or rainbow symbol?
    Methods: changeSymbol- call when you need to switch out the current players symbol
    This class contains player objects to be used in the tictactoe game.
    """
    
    def __init__(self, symbol):
        """
        Initializes the player class with 1 argument
        """
        self.symbol = symbol
    
    def changeSymbol(self, symbol):
        """
        Sets the given players symbol to the new one given
        """
        self.symbol = symbol
    
class TicTacToe:
    """
    Attributes: player1, player2, dict
    The dict starts empty but when the TicTacToe class is initialized it adds two players.
    The names are the keys and the values are player objects.
    Methods:
    addPlayer- adds player objects into the dictionary when given a name and symbol.
    getSymbolImage- given a symbol, either heart or rainbow, the method will load an image of that symbol
    """
    def __init__(self, player1, player2, dict = {}):
        """
        Initializes the TicTacToe class and adds two players to the dict, and calls the playGame function
        """
        self.dict = dict
        self.player1 = player1
        self.player2 = player2
        
        # add the players to the dict
        self.addPlayer(player1, "heart")
        self.addPlayer(player2, "rainbow")
            
        # call the playGame function
        playGame(player1, player2)
    
    def addPlayer(self, name, symbol):
        """
        Adds players to the classes dict when given a name and symbol.
        """
        # if the dict is empty it will be the first player who is always the heart symbol
        if self.dict == {}:
            # create a player object and store it in the dict for the key, name
            player = Player(symbol)
            self.dict[name] = player
        # this will be the second player who is always the rainbow symbol
        else:
            # create a player object and store it in the dict for the key, name
            player = Player(symbol)
            self.dict[name] = player
        
        # print out information about the player so the users know their symbols
        str = name + " will be the " + symbol + " symbol"
        print(str)
    
    def getSymbolImage(symbol):
        """
        Given a symbol, this method returns a loaded image of that symbol
        """
        if symbol == "heart":
            return loadImage("heart.jpg")
        elif symbol == "rainbow":
            return loadImage("rainbow.jpg")

def setup():
    """
    This function initializes the PyProcessing library. It runs once at beginning of the program. This function sets the window size, changes
    background color to black, and draws the outline of the tictactoe game. It also starts the beggining of the game.
    """
    # these can be accessed by other functions
    global squareWidth, squareHeight, game, currentPlayer, moves, heartList, rainbowList, player1, player2
    
    # create the window size
    size(500, 500)
    # set background to black
    background(0,0,0)
    
    # display an image of an empty tictactoe game
    img = loadImage("TicTacToe.png")
    image(img, 0, 0)
    
    # set variables = to the width and height of a square in the game
    squareWidth = (img.width) / 3
    squareHeight = (img.height) / 3
    
    # ask the users for their names
    player1 = input("Please enter player1's name: ")
    player2 = input("Please enter player2's name: ")
    
    # create an instance of the tictactoe class which will create player objects and call the playGame function
    game = TicTacToe(player1, player2)
    # keep track of how many times the board has been clicked on
    moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # these lists store which squares have been taken by player1 or 2
    rainbowList = []
    heartList = []
    # this is used to switch off which player is taking their turn
    currentPlayer = game.dict[game.player1]
    
def mousePressed():
    """
    This function is called every time the mouse is pressed. It will display a symbol on the tictactoe board based off of where the user clicked.
    """
    global squareWidth, squareHeight, game, currentPlayer, moves, heartList, rainbowList
    
    # when the mouse is in the upper left square
    if mouse.x < 73 and mouse.y < 340:
        # if the current player is a heart and this square is not in the rainbowList or heartList
        if currentPlayer.symbol == "heart" and ("1" not in rainbowList) and ("1" not in heartList):
            # display the heart image in the square the user clicked on
            img = TicTacToe.getSymbolImage("heart")
            image(img, 0, 0, squareWidth-25, squareHeight-20)
            # change the symbol to rainbow
            currentPlayer.changeSymbol("rainbow")
            # take away a move
            moves.pop()
            # add this location to the heartList 
            heartList.append("1")
            # check to see if someone has won
            winGame()
        # if the current player is a rainbow and this square is not in the heartList or rainbowList
        if currentPlayer.symbol == "rainbow" and ("1" not in heartList) and ("1" not in rainbowList):
            # display the rainbow image in the square the user clicked on
            img = TicTacToe.getSymbolImage("rainbow")
            image(img, 0, 0, squareWidth-25, squareHeight-20)
            # change the symbol to heart
            currentPlayer.changeSymbol("heart")
            # take away a move
            moves.pop()
            # add this location to the rainbowList
            rainbowList.append("1")
            # check to see if someone has one
            winGame()
            
    # the rest of the code is the same, but the location of where the mouse is pressed is different
    
    # middle left square
    elif mouse.x < 73 and mouse.y < 425:
        if currentPlayer.symbol == "heart" and ("4" not in rainbowList) and ("4" not in heartList):
            img = TicTacToe.getSymbolImage("heart")
            image(img, 0, 175, squareWidth-25, squareHeight-20)
            currentPlayer.changeSymbol("rainbow")
            moves.pop()
            heartList.append("4")
            winGame()
        if currentPlayer.symbol == "rainbow" and ("4" not in heartList) and ("4" not in rainbowList):
            img = TicTacToe.getSymbolImage("rainbow")
            image(img, 0, 175, squareWidth-25, squareHeight-20)
            currentPlayer.changeSymbol("heart")
            moves.pop()
            rainbowList.append("4")
            winGame()
    # bottom left square
    elif mouse.x < 73 and mouse.y < 500:
        if currentPlayer.symbol == "heart" and ("7" not in rainbowList) and ("7" not in heartList):
            img = TicTacToe.getSymbolImage("heart")
            image(img, 0, 358, squareWidth-25, squareHeight-20)
            currentPlayer.changeSymbol("rainbow")
            moves.pop()
            heartList.append("7")
            winGame()
        if currentPlayer.symbol == "rainbow" and ("7" not in heartList) and ("7" not in rainbowList):
            img = TicTacToe.getSymbolImage("rainbow")
            image(img, 0, 358, squareWidth-25, squareHeight-20)
            currentPlayer.changeSymbol("heart")
            moves.pop()
            rainbowList.append("7")
            winGame()
    # upper middle square           
    elif mouse.x < 170 and mouse.y < 340:
        if currentPlayer.symbol == "heart" and ("2" not in rainbowList) and ("2" not in heartList):
            img = TicTacToe.getSymbolImage("heart")
            image(img, 171, 0, squareWidth-25, squareHeight-20)
            currentPlayer.changeSymbol("rainbow")
            moves.pop()
            heartList.append("2")
            winGame()
        if currentPlayer.symbol == "rainbow" and ("2" not in heartList) and ("2" not in rainbowList):
            img = TicTacToe.getSymbolImage("rainbow")
            image(img, 171, 0, squareWidth-25, squareHeight-20)
            currentPlayer.changeSymbol("heart")
            moves.pop()
            rainbowList.append("2")
            winGame()
    # middle middle square
    elif mouse.x < 170 and mouse.y < 425:
        if currentPlayer.symbol == "heart" and ("5" not in rainbowList) and ("5" not in heartList):
            img = TicTacToe.getSymbolImage("heart")
            image(img, 171, 175, squareWidth-25, squareHeight-20)
            currentPlayer.changeSymbol("rainbow")
            moves.pop()
            heartList.append("5")
            winGame()
        if currentPlayer.symbol == "rainbow" and ("5" not in heartList) and ("5" not in rainbowList):
            img = TicTacToe.getSymbolImage("rainbow")
            image(img, 171, 175, squareWidth-25, squareHeight-20)
            currentPlayer.changeSymbol("heart")
            moves.pop()
            rainbowList.append("5")
            winGame()
    # bottom middle square
    elif mouse.x < 170 and mouse.y < 500:
        if currentPlayer.symbol == "heart" and ("8" not in rainbowList) and ("8" not in heartList):
            img = TicTacToe.getSymbolImage("heart")
            image(img, 171, 358, squareWidth-25, squareHeight-20)
            currentPlayer.changeSymbol("rainbow")
            moves.pop()
            heartList.append("8")
            winGame()
        if currentPlayer.symbol == "rainbow" and ("8" not in heartList) and ("8" not in rainbowList):
            img = TicTacToe.getSymbolImage("rainbow")
            image(img, 171, 358, squareWidth-25, squareHeight-20)
            currentPlayer.changeSymbol("heart")
            moves.pop()
            rainbowList.append("8")
            winGame()
    # upper right square
    elif mouse.x < 250 and mouse.y < 340:
        if currentPlayer.symbol == "heart" and ("3" not in rainbowList) and ("3" not in heartList):
            img = TicTacToe.getSymbolImage("heart")
            image(img, 352, 0, squareWidth-25, squareHeight-20)
            currentPlayer.changeSymbol("rainbow")
            moves.pop()
            heartList.append("3")
            winGame()
        if currentPlayer.symbol == "rainbow" and ("3" not in heartList) and ("3" not in rainbowList):
            img = TicTacToe.getSymbolImage("rainbow")
            image(img, 352, 0, squareWidth-25, squareHeight-20)
            currentPlayer.changeSymbol("heart")
            moves.pop()
            rainbowList.append("3")
            winGame()
    # middle right square
    elif mouse.x < 250 and mouse.y < 425:
        if currentPlayer.symbol == "heart" and ("6" not in rainbowList) and ("6" not in heartList):
            img = TicTacToe.getSymbolImage("heart")
            image(img, 352, 175, squareWidth-25, squareHeight-20)
            currentPlayer.changeSymbol("rainbow")
            moves.pop()
            heartList.append("6")
            winGame()
        if currentPlayer.symbol == "rainbow" and ("6" not in heartList) and ("6" not in rainbowList):
            img = TicTacToe.getSymbolImage("rainbow")
            image(img, 352, 175, squareWidth-25, squareHeight-20)
            currentPlayer.changeSymbol("heart")
            moves.pop()
            rainbowList.append("6")
            winGame()
    # bottom right square
    elif mouse.x < 250 and mouse.y < 500:
        if currentPlayer.symbol == "heart" and ("9" not in rainbowList) and ("9" not in heartList):
            img = TicTacToe.getSymbolImage("heart")
            image(img, 352, 358, squareWidth-25, squareHeight-20)
            currentPlayer.changeSymbol("rainbow")
            moves.pop()
            heartList.append("9")
            winGame()
        if currentPlayer.symbol == "rainbow" and ("9" not in heartList) and ("9" not in rainbowList):
            img = TicTacToe.getSymbolImage("rainbow")
            image(img, 352, 358, squareWidth-25, squareHeight-20)
            currentPlayer.changeSymbol("heart")
            moves.pop()
            rainbowList.append("9")
            winGame()
            
    # if all the 9 spots have been played on tell the users they tied
    if len(moves) == 0:
        print("It looks like you tied!) Look above for instructions on what to do next!")
        
def keyReleased():
    """
    This function is run when the user presses a key. The user is told to press the y key if they want to play again, so the playAgain function is called.
    """
    # reset the game
    playAgain()
        
def winGame():
    """
    This function checks to see if either player has won the game and outputs who the winner is if someone won.
    """
    global player1, player2
    
    # these keep track of how many squares for each way to win the game player1 has
    upperRow1 = 0
    middleRow1 = 0
    lowerRow1 = 0
    leftColumn1 = 0
    middleColumn1 = 0
    rightColumn1 = 0
    diagonalUp1 = 0
    diagonalDown1 = 0
    
    # these keep track of how many squares for each way to win the game player2 has
    upperRow2 = 0
    middleRow2 = 0
    lowerRow2 = 0
    leftColumn2 = 0
    middleColumn2 = 0
    rightColumn2 = 0
    diagonalUp2 = 0
    diagonalDown2 = 0
    
    # for each elem in player1's list
    for elem in heartList:
        str = "Congratulations " + player1 + "! You won the game with the hearts! Look above for instructions on what to do next!"
        # if the have all three in the upperRow, tell them they won
        if elem == "1" or elem == "2" or elem == "3":
            upperRow1 += 1
            if upperRow1 == 3:
                print(str)
        # if they have all 3 in the middleRow, tell them they won
        if elem == "4" or elem == "5" or elem == "6":
            middleRow1 += 1
            if middleRow1 == 3:
                print(str)
        # if they have all 3 in the lowerRow, tell them they won
        if elem == "7" or elem == "8" or elem == "9":
            lowerRow1 += 1
            if lowerRow1 == 3:
                print(str)
        # if they have all 3 in the leftColumn, tell them they won
        if elem == "1" or elem == "4" or elem == "7":
            leftColumn1 += 1
            if leftColumn1 == 3:
                print(str)
        # if they have all 3 in the middleColumn, tell them they won
        if elem == "2" or elem == "5" or elem == "8":
            middleColumn1 += 1
            if middleColumn1 == 3:
                print(str)
        # if they have all 3 in the rightColumn, tell them they won
        if elem == "3" or elem == "6" or elem == "9":
            rightColumn1 += 1
            if rightColumn1 == 3:
                print(str)
        # if they have all 3 in the diagonalDown, tell them they won
        if elem == "1" or elem == "5" or elem == "9":
            diagonalDown1 += 1
            if diagonalDown1 == 3:
                print(str)
        # if they have all 3 in the diagonalUp, tell them they won
        if elem == "7" or elem == "5" or elem == "3":
            diagonalUp1 += 1
            if diagonalUp1 == 3:
                print(str)
                
    # for each elem in player2's list do the exact same thing              
    for elem in rainbowList:
        str = "Congratulations " + player2 + "! You won the game with the rainbows! Look above for instructions on what to do next!"
        if elem == "1" or elem == "2" or elem == "3":
            upperRow2 += 1
            if upperRow2 == 3:
                print(str)               
        if elem == "4" or elem == "5" or elem == "6":
            middleRow2 += 1
            if middleRow2 == 3:
                print(str)               
        if elem == "7" or elem == "8" or elem == "9":
            lowerRow2 += 1
            if lowerRow2 == 3:
                print(str)
        if elem == "1" or elem == "4" or elem == "7":
            leftColumn2 += 1
            if leftColumn2 == 3:
                print(str)
        if elem == "2" or elem == "5" or elem == "8":
            middleColumn2 += 1
            if middleColumn2 == 3:
                print(str)
        if elem == "3" or elem == "6" or elem == "9":
            rightColumn2 += 1
            if rightColumn2 == 3:
                print(str)
        if elem == "1" or elem == "5" or elem == "9":
            diagonalDown2 += 1
            if diagonalDown2 == 3:
                print(str)
        if elem == "7" or elem == "5" or elem == "3":
            diagonalUp2 += 1
            if diagonalUp2 == 3:
                print(str)
                       
def playAgain():
    """
    This function is called when the user presses the y key to restart the game board and play again
    """
    # these also need to be shared between functions
    global squareWidth, squareHeight, moves, rainbowList, heartList, currentPlayer, player1, player2
    
    print("Lets play again! The same rules apply.")
    # set the background to black
    background(0,0,0)
    # display the blank tictactoe board 
    img = loadImage("TicTacToe.png")
    image(img, 0, 0)
    # assign variables to measure the width and height of the squares
    squareWidth = (img.width) / 3
    squareHeight = (img.height) / 3
    
    # ask the users for their names
    player1 = input("Please enter player1's name: ")
    player2 = input("Please enter player2's name: ")
    
    # create an instance of the tictactoe class which will create player objects and call the playGame function
    game = TicTacToe(player1, player2)
    # keep track of how many times the board has been clicked on
    moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # these lists store which squares have been taken by player1 or 2
    rainbowList = []
    heartList = []
    # this is used to switch off which player is taking their turn
    currentPlayer = game.dict[game.player1]
                           
def playGame(player1, player2): 
    """
    This function tells the users the rules of the game and what to do if they want to stop the game.
    It also says to press the y key if they want to play again and to press the red stop button to quit the program.
    """
    print("Here are the rules:")
    print(player1 + " will go first. You must pick a spot on the board to place your symbol. Then, it is " + player2 + "'s turn!")
    print("The goal of the game is to have your symbols all on either 1. the same row 2. the same column or 3. a diagonal.")
    print("But do not get so caught up in trying to win that you forget to stop the other person from winning!")
    print("The game will end either when one of you wins, or when all the spots are taken and neither has won.")
    print("When the game ends, enter y if you would like to play again.")
    print("If you would like to stop playing press the red stop button.")
    
# This will start the game by running the setup function    
run()
