class TicTacToe:
    # set starting variables and board
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False

    # display the board in ASCII
    def print_board(self):
        print("-------------")
        for row in self.board:
            print("|", " | ".join(row), "|")
            print("-------------")

    # check for winning player
    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return self.board[i][0]
            elif self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return self.board[0][i]
            elif self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
                return self.board[0][0]
            elif self.board[2][0] == self.board[1][1] == self.board[0][2] != ' ':
                return self.board[2][0]
        return None

    # player will enter move and move will be played
    def make_move(self, row, col):
        # check against max and min value
        if (row < 3 and col < 3) and (row >= 0 and col >= 0):

            # dont make move if game over or space full
            if not self.game_over and self.board[row][col] == ' ':
                self.board[row][col] = self.current_player
                winner = self.check_winner()
                # winner states
                if winner:
                    self.print_board()
                    print(f"Congratulations! {winner} wins!")
                    self.game_over = True
                elif all([self.board[i][j] != ' ' for i in range(3) for j in range(3)]):
                    self.print_board()
                    print("It's a tie!")
                    self.game_over = True
                else:
                    self.switch_player()
            elif self.board[row][col] != ' ':
                print("That position is already taken. Please choose another.")
        else:
            print("Invalid values entered enter Again.")

    # change current player
    def switch_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    # main game code
    def play_game(self):
        print("Welcome to Tic Tac Toe!")
        while not self.game_over:
            self.print_board()
            move = input(f"{self.current_player}, please enter your move (row,col): ")
            row, col = move.split(',')
            row = int(row)
            col = int(col)
            self.make_move(row, col)


# intiailise game and start main function
if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
