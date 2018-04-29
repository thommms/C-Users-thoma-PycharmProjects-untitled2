#from Ipython.display import clear_output
#Global variables
import os
def clear():
    os.system('cls')

board=[' ']*10
game_state=True
announce=''

#Note: game will ignore 0 index
def reset_board():
    global board,game_state
    board=[' ']*10
    game_state=True

def display_board():
    '''This function prints out the board so the nunpad can be used as a reference'''
    #clear current cell output
    clear()
    #print board
    print (" "+board[7]+" |"+board[8]+" |"+board[9]+" ")
    print ("-----------")
    print (" "+board[4]+" |"+board[5]+" |"+board[6]+" ")
    print ("-----------")
    print (" "+board[1]+" |"+board[2]+" |"+board[3]+" ")

def win_check (board,player):
    '''check Horizontals, verticals and diagonals for win'''
    if (board[7]==board[8]==board[9]==player) or \
        (board[7]==board[5]==board[3]==player) or \
        (board[7]==board[4]==board[1]==player) or \
        (board[7]==board[8]==board[9]==player) or \
        (board[4]==board[5]==board[6]==player) or \
        (board[1]==board[2]==board[3]==player) or \
        (board[8]==board[5]==board[2]==player) or \
        (board[9]==board[6]==board[3]==player) or \
        (board[9]==board[5]==board[1]==player):
        return True
    else:
        return False

def full_board_check(board):
    '''Function to check if any remaining blanks are in the board'''
    if (" " in board[1:]):
        return False
    else:
        return True

def ask_player(mark):
    '''Asks player where to place X or O mark, checks validity'''
    global board
    req='Choose where to place your %s: ' % mark
    while True:
        try:
            choice =int(input(req))
        except ValueError:
            print ("sorry, please input a number between 1-9")
            continue
        if board[choice]==" ":
            board[choice]=mark
            break
        else:
            print ("That space isn't empty!")
            continue

def player_choice(mark):
    global board,game_state,announce
    #set # blank game announcement
    announce=''
    #Get player input
    mark =str(mark)
    #validate input
    ask_player(mark)

    #check for player win
    if win_check(board,mark):
        clear()
        display_board()
        announce=mark+" wins! Congratulations"
        game_state=False
    #show board
    clear()
    display_board()

    #check for a tie
    if full_board_check(board):
        announce='Tie!'
        game_state=False
    return game_state,announce

def play_game():
    reset_board()
    global announce

    #set marks
    X='X'
    O='O'
    while True:
        #show board
        clear()
        display_board()

        #player X turn
        game_state,announce=player_choice(X)
        print (announce)
        if game_state==False:
            break

        #player O turn
        game_state,announce=player_choice(O)
        print(announce)
        if game_state==False:
            break
    #ask player for a rematch
    rematch=input('would you like a to play again? y/n').lower()
    if rematch=='y':
        play_game()
    else:
        print ("Thanks for playing!")
play_game()