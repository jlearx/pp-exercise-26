'''
Created on Sep 20, 2017

@author: jlearx
'''
NOWINNER = "No winner yet. Game not over."
PLAYER1WON = "Game over! Player 1 Won!"
PLAYER2WON = "Game over! Player 2 Won!"
DRAW = "Game over! Draw!"



def checkWinner(gameBoard):
    return DRAW

if __name__ == '__main__':
    # Run tests
    winner_is_2 = [[2, 2, 0],[2, 1, 0],[2, 1, 1]]
    winner_is_1 = [[1, 2, 0],[2, 1, 0],[2, 1, 1]]
    winner_is_also_1 = [[0, 1, 0],[2, 1, 0],[2, 1, 1]]
    no_winner = [[1, 2, 0],[2, 1, 0],[2, 1, 2]]
    also_no_winner = [[1, 2, 0],[2, 1, 0],[2, 1, 0]]
    
    print(checkWinner(winner_is_2))
    print(checkWinner(winner_is_1))
    print(checkWinner(winner_is_also_1))
    print(checkWinner(no_winner))
    print(checkWinner(also_no_winner))
    