board = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']
        ]
 
 
def display_board():
    for i in range(3):
        print("  " + board[i][0] + "  │  " + board[i][1] + "  │  " + board[i][2])
        print("─────┼─────┼─────")
 
 
def X_O():
    if input_position < 1 or input_position > 9:
        print("Out of bounds, try again")
        return 1
 
    y = (input_position - 1) // 3
    x = input_position % 3 - 1
 
    if board[y][x] == 'X' or board[y][x] == 'O':
        print("Already taken, try again")
        return 1
 
    board[y][x] = X_or_O
 
    return 0
 
 
 
def win():
    # 9 total checks for 3 horizontal, vertical, and diagonal rows
    if (board[0][0] == X_or_O and board[0][1] == X_or_O and board[0][2] == X_or_O) or\
       (board[1][0] == X_or_O and board[1][1] == X_or_O and board[1][2] == X_or_O) or\
       (board[2][0] == X_or_O and board[2][1] == X_or_O and board[2][2] == X_or_O) or\
       (board[0][0] == X_or_O and board[1][0] == X_or_O and board[2][0] == X_or_O) or\
       (board[0][1] == X_or_O and board[1][1] == X_or_O and board[2][1] == X_or_O) or\
       (board[0][2] == X_or_O and board[1][2] == X_or_O and board[2][2] == X_or_O) or\
       (board[0][0] == X_or_O and board[1][1] == X_or_O and board[2][2] == X_or_O) or\
       (board[2][0] == X_or_O and board[1][1] == X_or_O and board[0][2] == X_or_O):
        return True
 
    return False
 
 
user_input = input("Press enter to play a game of tic-tac-toe / noughts-and-crosses or type 'quit' to exit the program : ").lower()
 
while user_input != "quit":
    input_position = 0
    count = 0
    x_turn = False
    X_or_O = ''
 
    while not win() and count < 9:
        count += 1
        display_board()
        x_turn = (count % 2 == 1)
        X_or_O = 'X' * (x_turn) + 'O' * (not x_turn)
 
        print(X_or_O + "'s turn")
        input_position = int(input("Position : "))
        count -= X_O()
   
    display_board()
    print((X_or_O + " is the winner !") * (win()) + ("It's a tie !") * (not win()))
    user_input = input("Press enter to play another game of tic-tac-toe/noughts-and-crosses or type 'quit' to exit the program : ").lower()
