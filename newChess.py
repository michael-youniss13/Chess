from enum import Enum

#### Methods for chess ####
class Color(Enum):
    BLACK = -1
    WHITE = 1

class Pawn:
    enPessant = False;
    opening = True;

    def __init__(self, color, x_pos, y_pos, board):
        self.color = color
        self.x_pos = x_pos
        self.y_pos = y_pos
        board.setSquare(x_pos, y_pos, self)

    def possibleMoves(self, board):
        possibleMoves = []

        moveSquare_x = self.x_pos
        moveSquare_y = self.y_pos - (self.color)
        if board.isValidSquare(moveSquare_x, moveSquare_y) and board.squareValue(moveSquare_x, moveSquare_y) == 0:
            possibleMoves.append((moveSquare_x, moveSquare_y))

        moveSquare_y = self.y_pos - (self.color*2)
        if board.isValidSquare(moveSquare_x, moveSquare_y) and board.squareValue(moveSquare_x, moveSquare_y) == 0 and self.opening:
            possibleMoves.append((moveSquare_x, moveSquare_y))

        return possibleMoves

    def move(self, board, move):
        # board.move(move)
        return 0

    def getValue(self):
        return 1

class King:
    queenSideCastleAvailable = True
    kingSideCastleAvailable = True
    inCheck = False

    def __init__(self, color, x_pos, y_pos, board):
        self.color = color
        self.x_pos = x_pos
        self.y_pos = y_pos
        board.setSquare(x_pos, y_pos, self)

    def getValue(self):
        return 10

    def possibleMoves(self, board):
        possibleMoves = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if board.isValidSquare(self.x_pos + i, self.y_pos + j) and board.squareValue(self.x_pos + i, self.y_pos + j) == 0:
                    possibleMoves.append((self.x_pos + i, self.y_pos + j))
        return possibleMoves

class ChessBoard:
    board = []
    innerList = []

    def __init__(self):
        for i in range(0,8):
            for j in range(0,8):
                self.innerList.append(0)
            self.board.append(self.innerList)
            self.innerList = []

        # Add pawns
        for i in range(0,8):
            blackPawn = Pawn(Color.BLACK.value, i, 1, self)
            whitePawn = Pawn(Color.WHITE.value, i, 6, self)

        # Add Kings
        blackKing = King(Color.BLACK.value, 3, 0, self)
        whiteKing = King(Color.WHITE.value, 3, 7, self)

        # Add Knights

        # Add Bishops

        # Add Kings

        # Add Queens

    def isValidSquare(self, x, y):
        if x <= 7 and x >= 0 and y <= 7 and y >= 0:
            return True
        else:
            return False

    def squareValue(self, x, y):
        return self.board[y][x]

    def getPiece(self, x, y):
        return self.board[y][x]

    def printBoard(self):
        for row in self.board:
            for piece in row:
                if piece == 0:
                    print(0, end='\t')
                else:
                    print(piece.getValue() * piece.color, end='\t')
            print()

    def setSquare(self,x,y,val):
        self.board[y][x] = val

def main():
    board = ChessBoard()

    print(board.getPiece(3,7).possibleMoves(board))

    board.printBoard()



if __name__:
    main()
