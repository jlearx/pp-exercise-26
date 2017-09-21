'''
Created on Sep 20, 2017

@author: jlearx
'''
NOWINNER = "No winner yet. Game not over."
PLAYER1WON = "Game over! Player 1 Won!"
PLAYER2WON = "Game over! Player 2 Won!"
DRAW = "Game over! Draw!"

def checkInARow(row):
    # Can't win if there is a 0 in the row
    if (0 in row):
        return NOWINNER
    elif (row.count(1) == 3):
        return PLAYER1WON
    elif (row.count(2) == 3):
        return PLAYER2WON
    else:
        return DRAW    

def checkHorizontal(gameBoard):
    finalResult = DRAW
    result = DRAW
    rowIdx = 0
    
    while (((result == NOWINNER) or (result == DRAW)) and (rowIdx < 3)):
        row = gameBoard[rowIdx]
        result = checkInARow(row)
        
        if (result == NOWINNER):
            finalResult = NOWINNER
        elif ((result == PLAYER1WON) or (result == PLAYER2WON)):
            return result
        
        rowIdx += 1

    return finalResult

def checkVertical(gameBoard):
    finalResult = DRAW
    result = DRAW
    colIdx = 0
    
    while (((result == NOWINNER) or (result == DRAW)) and (colIdx < 3)):
        row = []
        
        for rowIdx in range(0,3):
            row.append(gameBoard[rowIdx][colIdx])
        
        result = checkInARow(row)
        
        if (result == NOWINNER):
            finalResult = NOWINNER
        elif ((result == PLAYER1WON) or (result == PLAYER2WON)):
            return result
        
        colIdx += 1

    return finalResult

def checkDiagonal(gameBoard):
    finalResult = DRAW
    
    # Check first diagonal
    row = [gameBoard[0][0], gameBoard[1][1], gameBoard[2][2]]
    result = checkInARow(row)
    
    if (result == NOWINNER):
        finalResult = NOWINNER
    elif ((result == PLAYER1WON) or (result == PLAYER2WON)):
        return result    
    
    # Check second diagonal    
    row = [gameBoard[0][2], gameBoard[1][1], gameBoard[2][0]]
    result = checkInARow(row)        
        
    if (result == NOWINNER):
        finalResult = NOWINNER
    elif ((result == PLAYER1WON) or (result == PLAYER2WON)):
        return result

    return finalResult    

def checkWinner(gameBoard):
    finalResult = DRAW
    
    # Check for horizontal wins
    result = checkHorizontal(gameBoard)
    
    if (result == NOWINNER):
        finalResult = NOWINNER
    elif ((result == PLAYER1WON) or (result == PLAYER2WON)):
        return result    
    
    # Check for vertical wins
    result = checkVertical(gameBoard)
    
    if (result == NOWINNER):
        finalResult = NOWINNER
    elif ((result == PLAYER1WON) or (result == PLAYER2WON)):
        return result
    
    # Check for diagonal wins
    result = checkDiagonal(gameBoard)
    
    if (result == NOWINNER):
        finalResult = NOWINNER
    elif ((result == PLAYER1WON) or (result == PLAYER2WON)):
        return result
        
    return finalResult

if __name__ == '__main__':
    # Run tests
    winner_is_2 = [[2, 2, 0],[2, 1, 0],[2, 1, 1]]
    winner_is_1 = [[1, 2, 0],[2, 1, 0],[2, 1, 1]]
    winner_is_also_1 = [[0, 1, 0],[2, 1, 0],[2, 1, 1]]
    no_winner = [[1, 2, 0],[2, 1, 0],[2, 1, 2]]
    also_no_winner = [[1, 2, 0],[2, 1, 0],[2, 1, 0]]
    winner_is_2_also = [[1, 2, 1],[1, 1, 0],[2, 2, 2]]
    draw_no_winner = [[1, 2, 1],[1, 2, 2],[2, 1, 1]]
    
    print(checkWinner(winner_is_2))
    print(checkWinner(winner_is_1))
    print(checkWinner(winner_is_also_1))
    print(checkWinner(no_winner))
    print(checkWinner(also_no_winner))
    print(checkWinner(winner_is_2_also))
    print(checkWinner(draw_no_winner))
    