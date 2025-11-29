class Piece:
    def __init__(self, row, col, color, image, type, rank):
        self.row = row
        self.row = col
        self.color = color
        self.image = image
        self.type = type

    def MovePiece(self, row, col):
        self.row = row
        self.col = col

    def GetRow(self):
        return self.row
    
    def GetCol(self):
        return self.col
    
    def GetColor(self):
        return self.color
    
    def GetImage(self):
        return self.image
    
    def GetType(self):
        return self.type

    def GetRank(self):
        return self.rank
    
    def GetPossibleMoves(self):
        if type == "Pawn":
            possible_moves = []
        elif type == "Bishop[]":
            possible_moves = []
        elif type == "Rook[]":
            possible_moves = []
        elif type == "Knight[]":
            possible_moves = []
        elif type == "Queen[]":
            possible_moves = []
        elif type == "King[]":
            possible_moves = []
        else:
            possible_moves = None
    


class Pawn(Piece):
    type = "Pawn"
    rank = 2

    def __init__(self, row, col, color, image):
        super().__init__(row, col, color, image, self.type, self.rank)



class Bishop(Piece):
    type = "Bishop"
    rank = 3

    def __init__(self, row, col, color, image):
        super().__init__(row, col, color, image, self.type, self.rank)



class Rook(Piece):
    type = "Rook"
    rank = 3

    def __init__(self, row, col, color, image):
        super().__init__(row, col, color, image, self.type, self.rank)



class Knight(Piece):
    type = "Knight"
    rank = 4

    def __init__(self, row, col, color, image):
        super().__init__(row, col, color, image, self.type, self.rank)



class Queen(Piece):
    type = "Queen"
    rank = 3

    def __init__(self, row, col, color, image):
        super().__init__(row, col, color, image, self.type, self.rank)



class King(Piece):
    type = "King"
    rank = 10

    def __init__(self, row, col, color, image):
        super().__init__(row, col, color, image, self.type, self.rank)
