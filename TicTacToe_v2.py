# Author: aqeelanwar
# Created: 12 March 2020, 7:06 PM
# Email: aqeel.anwar@gatech.edu

from tkinter import *
import numpy as np
import random

# initialise game variables
size_of_board = 600
symbol_size = (size_of_board / 3 - size_of_board / 8) / 2
symbol_thickness = 50
symbol_X_color = '#FF3333'
symbol_O_color = '#060000'
Green_color = '#7BC043'


class Tic_Tac_Toe():
    # ------------------------------------------------------------------
    # Initialization Functions:
    # ------------------------------------------------------------------
    def __init__(self):
        self.window = Tk()
        self.window.title('Tic-Tac-Toe')
        self.canvas = Canvas(self.window, width=size_of_board, height=size_of_board)
        self.canvas.pack()
        # Input from user in form of clicks
        self.window.bind('<Button-1>', self.click)

        self.initialize_board()
        self.player_X_turns = True
        self.board_status = np.zeros(shape=(3, 3))

        self.player_X_starts = True
        self.reset_board = False
        self.gameover = False
        self.tie = False
        self.X_wins = False
        self.O_wins = False

        self.X_score = 0
        self.O_score = 0
        self.tie_score = 0

    def mainloop(self):
        self.window.mainloop()

    # draw board lines
    def initialize_board(self):
        for i in range(2):
            self.canvas.create_line((i + 1) * size_of_board / 3, 0, (i + 1) * size_of_board / 3, size_of_board)

        for i in range(2):
            self.canvas.create_line(0, (i + 1) * size_of_board / 3, size_of_board, (i + 1) * size_of_board / 3)

    # reset the board for game start
    def play_again(self):
        self.initialize_board()
        self.player_X_starts = not self.player_X_starts
        self.player_X_turns = self.player_X_starts
        self.board_status = np.zeros(shape=(3, 3))

    # ------------------------------------------------------------------
    # Drawing Functions:
    # The modules required to draw required game based object on canvas
    # ------------------------------------------------------------------

    # make the 0 symbol
    def draw_O(self, logical_position):
        logical_position = np.array(logical_position)
        # logical_position = grid value on the board
        # grid_position = actual pixel values of the center of the grid
        grid_position = self.convert_logical_to_grid_position(logical_position)
        self.canvas.create_oval(grid_position[0] - symbol_size, grid_position[1] - symbol_size,
                                grid_position[0] + symbol_size, grid_position[1] + symbol_size, width=symbol_thickness,
                                outline=symbol_O_color)

    # make the X symbol
    def draw_X(self, logical_position):
        grid_position = self.convert_logical_to_grid_position(logical_position)
        self.canvas.create_line(grid_position[0] - symbol_size, grid_position[1] - symbol_size,
                                grid_position[0] + symbol_size, grid_position[1] + symbol_size, width=symbol_thickness,
                                fill=symbol_X_color)
        self.canvas.create_line(grid_position[0] - symbol_size, grid_position[1] + symbol_size,
                                grid_position[0] + symbol_size, grid_position[1] - symbol_size, width=symbol_thickness,
                                fill=symbol_X_color)

    # display the game over screen and define text
    def display_gameover(self):

        if self.X_wins:
            self.X_score += 1
            text = 'Winner: Player 1 (X)'
            color = symbol_X_color
        elif self.O_wins:
            self.O_score += 1
            text = 'Winner: Player 2 (O)'
            color = symbol_O_color
        else:
            self.tie_score += 1
            text = 'Its a tie'
            color = 'gray'

        self.canvas.delete("all")
        self.canvas.create_text(size_of_board / 2, size_of_board / 3, font="cmr 40 bold", fill=color, text=text)

        score_text = 'Scores \n'
        self.canvas.create_text(size_of_board / 2, 5 * size_of_board / 8, font="cmr 40 bold", fill=Green_color,
                                text=score_text)

        score_text = 'Player 1 (X) : ' + str(self.X_score) + '\n'
        score_text += 'Player 2 (O): ' + str(self.O_score) + '\n'
        score_text += 'Tie                    : ' + str(self.tie_score)
        self.canvas.create_text(size_of_board / 2, 3 * size_of_board / 4, font="cmr 30 bold", fill=Green_color,
                                text=score_text)
        self.reset_board = True

        score_text = 'Click to play again \n'
        self.canvas.create_text(size_of_board / 2, 15 * size_of_board / 16, font="cmr 20 bold", fill="gray",
                                text=score_text)

    # ------------------------------------------------------------------
    # Logical Functions:
    # The modules required to carry out game logic
    # ------------------------------------------------------------------

    def convert_logical_to_grid_position(self, logical_position):
        logical_position = np.array(logical_position, dtype=int)
        return (size_of_board / 3) * logical_position + size_of_board / 6

    def convert_grid_to_logical_position(self, grid_position):
        grid_position = np.array(grid_position)
        return np.array(grid_position // (size_of_board / 3), dtype=int)

    def is_grid_occupied(self, logical_position):
        if self.board_status[logical_position[0]][logical_position[1]] == 0:
            return False
        else:
            return True

    # decide player to check and check if winner
    def is_winner(self, player):

        player = -1 if player == 'X' else 1

        # Three in a row
        for i in range(3):
            if self.board_status[i][0] == self.board_status[i][1] == self.board_status[i][2] == player:
                return True
            if self.board_status[0][i] == self.board_status[1][i] == self.board_status[2][i] == player:
                return True

        # Diagonals
        if self.board_status[0][0] == self.board_status[1][1] == self.board_status[2][2] == player:
            return True

        if self.board_status[0][2] == self.board_status[1][1] == self.board_status[2][0] == player:
            return True

        return False

    # check if board is full
    def is_tie(self):

        r, c = np.where(self.board_status == 0)
        tie = False
        if len(r) == 0:
            tie = True

        return tie

    # check if game is over
    def is_gameover(self):
        # Either someone wins or all grid occupied
        self.X_wins = self.is_winner('X')
        if not self.X_wins:
            self.O_wins = self.is_winner('O')

        if not self.O_wins:
            self.tie = self.is_tie()

        gameover = self.X_wins or self.O_wins or self.tie

        if self.X_wins:
            print('X wins')
        if self.O_wins:
            print('O wins')
        if self.tie:
            print('Its a tie')

        return gameover

    # computer player makes a move
    def computer_move(self):

        # record empty slots
        moves_scores = {}
        for i in range(0, 3):
            for j in range(0, 3):
                # reverse i , j due to nature of board
                if self.board_status[j][i] == 0:
                    moves_scores[(j, i)] = 0

        # random player - make random move if first turn
        if len(moves_scores) == 9 or len(moves_scores) == 8:
            while True:
                move = [random.randint(0, 2), random.randint(0, 2)]
                if self.is_grid_occupied(move) is False:
                    moves_scores.pop(tuple(move))
                    return move

        # smart player - check if move and evaluate a score based
        # on proximity to existing 1's.

        # update dictionary keys with scores
        for key, val in moves_scores.items():
            if key in moves_scores:
                moves_scores[key] = self.score_move(key)

        # select random best move
        if 1 not in moves_scores.values():
            # if no best moves make random
            while True:
                move = [random.randint(0, 2), random.randint(0, 2)]
                if self.is_grid_occupied(move) is False:
                    break
        else:
            # select random option from list of best moves
            while True:
                move = random.choice(tuple(moves_scores.keys()))
                # check if score >=1 and pos not already filled
                if moves_scores[move] >= 0 and self.is_grid_occupied(move) is False:
                    break

        # return move to main driver
        print("computer: making move to: ", move)
        return move

    # make a move in the test board and score it
    def score_move(self, move):
        score = int()  # store move score

        # get copy of board for simulations
        board_status_copy = self.board_status.copy()

        # check x and y axis
        for i in range(3):
            if board_status_copy[i][0] and board_status_copy[i][1]\
                    or board_status_copy[i][1] and board_status_copy[i][2] == 1:
                score += 1
            if board_status_copy[0][i] and board_status_copy[1][i]\
                    or board_status_copy[1][i] or board_status_copy[2][i] == 1:
                score += 1

        # Diagonals
        if board_status_copy[0][0] and board_status_copy[1][1]\
                or board_status_copy[1][1] and board_status_copy[2][2] == 1:
            score += 1

        if board_status_copy[0][2] and board_status_copy[1][1]\
                or board_status_copy[1][1] and board_status_copy[2][0] == 1:
            score += 1

        # computer player = 1
        return score

    # get user click and convert it to array (main driver)
    def click(self, event):
        grid_position = [event.x, event.y]
        logical_position = self.convert_grid_to_logical_position(grid_position)

        # check if board is full or not before turn
        if not self.reset_board:
            if self.player_X_turns:  # users turn
                if not self.is_grid_occupied(logical_position):
                    self.draw_X(logical_position)
                    self.board_status[logical_position[0]][logical_position[1]] = -1
                    self.player_X_turns = not self.player_X_turns
            else:
                if not self.is_grid_occupied(logical_position):  # computer players turn
                    temp = self.computer_move()  # click to trigger the computer move
                    self.draw_O(temp)
                    self.board_status[temp[0]][temp[1]] = 1
                    self.player_X_turns = not self.player_X_turns

            # Check if game is concluded
            if self.is_gameover():
                self.display_gameover()
                # print('Done')
        else:  # Play Again
            self.canvas.delete("all")
            self.play_again()
            self.reset_board = False


game_instance = Tic_Tac_Toe()
game_instance.mainloop()
