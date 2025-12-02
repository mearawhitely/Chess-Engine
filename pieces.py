class Piece:
    def __init__(self, row, col, color, image_url, type, rank, image, rect):
        self.row = row
        self.row = col
        self.color = color
        self.image_url = image_url
        self.type = type
        self.rank = rank
        self.image = image
        self.rect = rect

    def MovePiece(self, row, col):
        self.row = row
        self.col = col

    def GetRow(self):
        return self.row

    def GetCol(self):
        return self.col

    def GetColor(self):
        return self.color

    def GetImageURL(self):
        return self.image_url

    def GetType(self):
        return self.type

    def GetRank(self):
        return self.rank

    def GetImage(self):
        return self.image

    def GetRect(self):
        return self.rect

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

    def __init__(self, row, col, color, image_url, image, rect):
        super().__init__(row, col, color, image_url, self.type, self.rank, image, rect)


class Bishop(Piece):
    type = "Bishop"
    rank = 3

    def __init__(self, row, col, color, image_url, image, rect):
        super().__init__(row, col, color, image_url, self.type, self.rank, image, rect)


class Rook(Piece):
    type = "Rook"
    rank = 3

    def __init__(self, row, col, color, image_url, image, rect):
        super().__init__(row, col, color, image_url, self.type, self.rank, image, rect)


class Knight(Piece):
    type = "Knight"
    rank = 4

    def __init__(self, row, col, color, image_url, image, rect):
        super().__init__(row, col, color, image_url, self.type, self.rank, image, rect)


class Queen(Piece):
    type = "Queen"
    rank = 3

    def __init__(self, row, col, color, image_url, image, rect):
        super().__init__(row, col, color, image_url, self.type, self.rank, image, rect)


class King(Piece):
    type = "King"
    rank = 10

    def __init__(self, row, col, color, image_url, image, rect):
        super().__init__(row, col, color, image_url, self.type, self.rank, image, rect)
