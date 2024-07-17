
#Ben Hawkins
#Batleship, High School Interns, Stage 1.0

import random

# Print the game board
def print_board(board):
    for row in board:
        print(" ".join(row))

#Generate random number based on the column length (how many columns there are. aka how many indices are in the list of lists)
def generate_location(board):
    return random.randint(1, len(board)), random.randint(1, len(board[0]))

#Input validation that checks to make sure its an int and on the board. 
def collect_input(board_size):
    while(True):
        try:
            guess_row = eval(input("\nGuess Row: "))
            guess_col = eval(input("Guess Col: "))
            
            if guess_col <= board_size and guess_row <= board_size:
                return guess_row-1, guess_col-1
            else:
                print("That is not on the board. Please do better next time.\n")
        except: 
            print("Please type an integer that correlates to an index on the board.\n")
        
############################################ Actual Game code below this #######################################################

board_size = 5

# Set up the game board
board = []
for i in range(board_size):
    board.append(["O"] * board_size)


print("Let's play Battleship!\n")


ship_row, ship_col = generate_location(board) 
print(ship_row, ship_col)

#Range of 4 because there will be 3 turns and then another turn if they didn't win which will then break. 
for turn in range(4):

    #This is done to check to see if they lost. If they won, they would have exited the loop before turn is equal to 3
    if turn == 3:
        print("Game Over")
        board[guess_row][guess_col] = "X"
        break
    
    #Humans don't think of a 0th turn. So turn + 1 = 1-4
    print("Turn", turn + 1)
    print_board(board)
    
    guess_row, guess_col = collect_input(board_size)

    #We can classify the objective into 2 cases. They either hit it or they didn't.
    if guess_row + 1 == ship_row and guess_col + 1 == ship_col:
        print("\nGreat Shot, you sunk my ship")
        board[guess_row][guess_col] = "X"
        print_board(board)
        print("")
        break
    
    #Because of the input validation, we know they missed because 1 of 2 reasons. They either already guessed it or it isn't the battleship. 
    else:
        if board[guess_row][guess_col] == "M":
            print("\nYou guessed that one already.")
            print(" ")
        else:
            print("\nYou missed my battleship!")
            board[guess_row][guess_col] = "M"