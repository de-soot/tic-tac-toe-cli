def display_board(board_):
    for i in range(3):
        print("  " + board_[i][0] + "  │  " + board_[i][1] + "  │  " + board_[i][2])
        print("─────┼─────┼─────")
    
    print("\n")
 
 
def plot(board_, input_position_, X_or_O_):
    if input_position_ < 1 or input_position_ > 9:
        print("Out of bounds, try again\n")
        return 1
 
    y = (input_position_ - 1) // 3
    x = (input_position_ % 3) - 1
 
    if (board_[y][x] == 'X') or (board_[y][x] == 'O'):
        print("Already taken, try again\n")
        return 1
 
    board_[y][x] = X_or_O_
 
    return 0
 
 
def win(board_, X_or_O_):
    # 8 total checks for 3 horizontal, 3 vertical, and 2 diagonal rows
    return (board_[0][0] == X_or_O_ and board_[0][1] == X_or_O_ and board_[0][2] == X_or_O_) or\
           (board_[1][0] == X_or_O_ and board_[1][1] == X_or_O_ and board_[1][2] == X_or_O_) or\
           (board_[2][0] == X_or_O_ and board_[2][1] == X_or_O_ and board_[2][2] == X_or_O_) or\
           (board_[0][0] == X_or_O_ and board_[1][0] == X_or_O_ and board_[2][0] == X_or_O_) or\
           (board_[0][1] == X_or_O_ and board_[1][1] == X_or_O_ and board_[2][1] == X_or_O_) or\
           (board_[0][2] == X_or_O_ and board_[1][2] == X_or_O_ and board_[2][2] == X_or_O_) or\
           (board_[0][0] == X_or_O_ and board_[1][1] == X_or_O_ and board_[2][2] == X_or_O_) or\
           (board_[2][0] == X_or_O_ and board_[1][1] == X_or_O_ and board_[0][2] == X_or_O_)


def main():
    user_input = input("Press enter to play a game of tic-tac-toe / noughts-and-crosses or type 'quit' to exit the program : ").lower()

    if user_input == "quit":
        return

    # initialise variables
    board = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9']
            ]

    count = 0
    x_turn = False
    X_or_O = 'X'
    
    # game start
    while not win(board, X_or_O) and (count < 9):
        count += 1
        display_board(board)
        x_turn = (count % 2 == 1)
        X_or_O = ( 'X' * (x_turn) ) + ( 'O' * (not x_turn) )
 
        print(X_or_O + "'s turn")
        input_position = int( input("Position : ") )
        count -= plot(board, input_position, X_or_O)
    # game end

    # display results
    display_board(board)
    has_winner = win(board, X_or_O)
    print( (X_or_O + " is the winner !\n") * ( has_winner ) + ("It's a tie !\n") * ( not has_winner ) )
    main()

if __name__ == "__main__":
    main()
