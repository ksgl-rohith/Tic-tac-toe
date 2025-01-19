import os
import time

# Initialize the game board with 10 spaces (index 0 is unused for simplicity)
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# Player indicator (1 for Player 1, 2 for Player 2)
player = 1

# Game state flags
Win = 1  # Flag for when a player wins
Draw = -1  # Flag for when the game is a draw
Running = 0  # Flag for when the game is still running
Stop = 1  # Unused flag

# Initial state of the game
Game = Running
Mark = 'X'  # Default mark for Player 1


# Function to draw the game board
def DrawBoard():
    print(" %c | %c | %c " % (board[1], board[2], board[3]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[4], board[5], board[6]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[7], board[8], board[9]))
    print("   |   |   ")


# Function to check if a position on the board is available
def CheckPosition(x):
    if board[x] == ' ':
        return True
    else:
        return False


# Function to check if there is a win or draw
def CheckWin():
    global Game

    # Check horizontal win conditions
    if board[1] == board[2] and board[2] == board[3] and board[1] != ' ':
        Game = Win
    elif board[4] == board[5] and board[5] == board[6] and board[4] != ' ':
        Game = Win
    elif board[7] == board[8] and board[8] == board[9] and board[7] != ' ':
        Game = Win

    # Check vertical win conditions
    elif board[1] == board[4] and board[4] == board[7] and board[1] != ' ':
        Game = Win
    elif board[2] == board[5] and board[5] == board[8] and board[2] != ' ':
        Game = Win
    elif board[3] == board[6] and board[6] == board[9] and board[3] != ' ':
        Game = Win

    # Check diagonal win conditions
    elif board[1] == board[5] and board[5] == board[9] and board[5] != ' ':
        Game = Win
    elif board[3] == board[5] and board[5] == board[7] and board[5] != ' ':
        Game = Win

    # Check for a draw (all positions filled with no winner)
    elif all(space != ' ' for space in board[1:]):
        Game = Draw

    # Game is still running
    else:
        Game = Running


# Display game introduction
print("Tic-Tac-Toe Game Designed By Sourabh Somani")
print("Player 1 [X] --- Player 2 [O]\n")
print()
print("Please Wait...")
time.sleep(3)  # Pause for dramatic effect

# Main game loop
while Game == Running:
    os.system('cls')  # Clear the console (use 'clear' for macOS/Linux)
    DrawBoard()  # Display the board

    # Determine the current player and their mark
    if player % 2 != 0:
        print("Player 1's chance")
        Mark = 'X'
    else:
        print("Player 2's chance")
        Mark = 'O'

    # Prompt the player to choose a position
    choice = int(input("Enter the position between [1-9] where you want to mark: "))
    if CheckPosition(choice):  # Check if the chosen position is valid
        board[choice] = Mark  # Place the player's mark on the board
        player += 1  # Switch to the other player
        CheckWin()  # Check for a win or draw condition

    # Clear the console and display the updated board
    os.system('cls')
    DrawBoard()

    # Display the result if the game is over
    if Game == Draw:
        print("Game Draw")
    elif Game == Win:
        player -= 1  # Adjust player count for winner announcement
        if player % 2 != 0:
            print("Player 1 Won")
        else:
            print("Player 2 Won")
