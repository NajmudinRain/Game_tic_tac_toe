from collections import deque
from Model.Board import  Board
from Model.PieceType import PieceType
from Model.Player import Player
from Model.PlayingPieceO import PlayingPieceO
from Model.PlayingPieceX import PlayingPieceX

class TicTacToeGame:
    def __init__(self):
        self.players = deque()
        self.game_board = None

    def initialize_game(self):
        # Creating 2 Players
        cross_piece = PlayingPieceX()
        player1 = Player("Player1", cross_piece)

        noughts_piece = PlayingPieceO()
        player2 = Player("Player2", noughts_piece)

        self.players.append(player1)
        self.players.append(player2)

        # Initialize Board
        self.game_board = Board(3)

    def start_game(self):
        no_winner = True
        while no_winner:
            # Take out the player whose turn it is
            player_turn = self.players.popleft()

            # Print board and get free spaces
            self.game_board.print_board()
            free_spaces = self.game_board.get_free_cells()
            if not free_spaces:
                return "tie"

            # Read user input
            row, col = map(int, input(f"Player {player_turn.name}, enter row,column: ").split(","))

            # Place the piece
            if not self.game_board.add_piece(row, col, player_turn.playing_piece):
                print("Incorrect position chosen, try again")
                self.players.appendleft(player_turn)
                continue

            self.players.append(player_turn)

            if self.is_there_winner(row, col, player_turn.playing_piece.piece_type):
                return player_turn.name

        return "tie"

    def is_there_winner(self, row, col, piece_type):
        size = self.game_board.size

        row_match = all(self.game_board.board[row][i] and self.game_board.board[row][i].piece_type == piece_type for i in range(size))
        col_match = all(self.game_board.board[i][col] and self.game_board.board[i][col].piece_type == piece_type for i in range(size))
        diagonal_match = all(self.game_board.board[i][i] and self.game_board.board[i][i].piece_type == piece_type for i in range(size))
        anti_diagonal_match = all(self.game_board.board[i][size - 1 - i] and self.game_board.board[i][size - 1 - i].piece_type == piece_type for i in range(size))

        return row_match or col_match or diagonal_match or anti_diagonal_match
