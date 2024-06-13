def main() -> None:
    if input("Press enter to play a game of Tic-Tac-Toe (A.K.A Noughts-and-Crosses) \
or type 'quit' to exit the program : ").lower() == "quit": return

    # initialise board
    board_length = int(input("Enter the side length of the board : "))

    while board_length < 1:
        board_length = int(input("Enter the side length of the board (must be larger than 0) : "))

    board_square = board_length * board_length
    board_digit = len(str(board_square)) # maximum number of digits on the board
    board = create_board(board_length)
    
    count = 0
    X_or_O = 'X'
    has_winner = False
    
    # game loop start
    while not has_winner and count < board_square:
        count += 1
        display_board(board, board_length, board_square, board_digit)
        x_turn = (count % 2 == 1)
        X_or_O = ('X' * x_turn) + ('O' * (not x_turn))

        print(X_or_O + "'s Turn\n->\t", end = '')
        user_input = int(input("Position : "))

        count -= plot(board, user_input, X_or_O , board_length, board_square) # uncount invalid moves
        has_winner = win(board, X_or_O, board_length) # check for winning moves
    # game loop end

    # display results
    display_board(board, board_length, board_square, board_digit)
    print((X_or_O + " is the winner !\n") * has_winner + ("It's a tie !\n") * (not has_winner))
    main()


def create_board(board_length: int) -> list[list]:
    return [[str(x + y * board_length) for x in range(1, board_length + 1)] for y in range(board_length)]
    

def display_board(board: list[list], board_length: int, board_square: int, board_digit: int) -> None:
    print("\n")
    
    for y in range(board_length):
        for x in range(board_length):
            board_plot = board[y][x]
            # adjust the spacing / padding around the current number displayed
            # according to the number of digits in the current number displayed
            print(" │ " + board_plot, end = (' ' * (board_digit - len(board_plot))))

        # scale the board display according to the maximum number of digits of a number on the board
        print(("\n ┼──" + '─' * board_digit) + ("┼──" + '─' * board_digit) * (board_length - 1))

    print("\n")
 
 
def plot(board: list[list], input_position: int, X_or_O: str, board_length: int, board_square: int) -> int:
    if input_position < 1 or input_position > board_square:
        print("Out of bounds, try again\n")
        return 1 # uncount move
 
    y = (input_position - 1) // board_length
    x = (input_position % board_length) - 1

    board_plot = board[y][x]
 
    if (board_plot == 'X') or (board_plot == 'O'):
        print("Already taken, try again\n")
        return 1 # uncount move
 
    board[y][x] = X_or_O
 
    return 0 # do not uncount move
 
 
def win(board: list[list], X_or_O: str, board_length: int) -> bool:
    # check for horizontal win condition
    for y in range(board_length):
        for x in range(board_length):
            win_condition = (board[y][x] == X_or_O)
            if not win_condition: break # do not continue checking if impossible
        if win_condition: return True # return True if row is complete

    # check for vertical win condition
    for x in range(board_length):
        for y in range(board_length):
            win_condition = (board[y][x] == X_or_O)
            if not win_condition: break
        if win_condition: return True

    # check for diagonal win condition
    for x in range(board_length): # top left to bottom right (y = x)
        win_condition = (board[x][x] == X_or_O)
        if not win_condition: break
    if win_condition: return True

    for x in range(board_length): # bottom left to top right (y = -x)
        win_condition = (board[x][board_length - x - 1] == X_or_O)
        if not win_condition: break
    if win_condition: return True

    # return False if no win conditions are met
    return False


if __name__ == "__main__": main()
