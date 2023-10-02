grid = []
for rowNumber in range(6):
    grid.append(["-", "-", "-", "-", "-", "-", "-"])


# function to print the grid out
def printGrid():
    # iterates through each row and each character in each row
    for rowToPrint in grid:
        stringToPrint = ""
        for symbolToPrint in rowToPrint:
            stringToPrint = stringToPrint + symbolToPrint + " "
        print(stringToPrint)


# function to check if the board has a winner
def checkGameContinue(inputtedColumn, inputtedRow):
    return True


def checkValidColumn(columnToCheck):
    if columnToCheck.isdigit():
        if 0 < int(columnToCheck) < 8:
            return True
    else:
        return False


def checkRow(turnColumn):
    # sets correct row to 10, which means that the tile is not placed
    correctRow = 6
    for rowToCheck in range(5, -1, -1):
        if grid[rowToCheck][turnColumn] == "-" and correctRow == 6:
            correctRow = rowToCheck
    return correctRow


def rotateTurn(previousTurn):
    if previousTurn == "X":
        newTurn = "O"
    else:
        newTurn = "X"
    return newTurn


# gives welcome text and prints the initial board
print("Welcome to Connect 4!")
printGrid()
# sets the starting players turn
playerTurn = "X"
# starts the game and keeps iterating till board is checked and a winner is recognised
gameRunning = True
while gameRunning:
    # gets the column from the user
    columnInput = input("Input a column: ")
    # first checks that the input is a number 1-7 and formats the input accordingly
    if checkValidColumn(columnInput):
        columnInput = int(columnInput) - 1
        # checks what row the tile will fall into, with 6 being that a tile cannot fit into the grid
        selectedRow = checkRow(columnInput)
        if selectedRow != 6:
            # sets the spot to the player's character, switches the turn,
            # checks if the game should continue and prints the grid
            grid[selectedRow][columnInput] = playerTurn
            playerTurn = rotateTurn(playerTurn)
            gameRunning = checkGameContinue(columnInput, selectedRow)
            printGrid()
        else:
            # outputs if the column is full
            print("Column is full")
    else:
        # outputs if the column is not a number or an invalid number
        print("Not a valid column number!")
