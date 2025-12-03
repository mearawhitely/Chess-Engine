class Cell:
    def __init__(self, row, col, color, rect, occupied, piece):
        self.row = row
        self.col = col
        self.color = color
        self.rect = rect
        self.occupied = occupied
        self.piece = piece
        self.highlight = False  

    # ----------------- GETTERS -----------------
    def GetRow(self):
        return self.row

    def GetCol(self):
        return self.col

    def GetColor(self):
        # Return green if highlighted, otherwise the normal color
        if self.highlight:
            return (0, 255, 0)  # Bright green for highlight
        return self.color

    def GetRect(self):
        return self.rect

    def GetOccupied(self):
        return self.occupied

    def GetPiece(self):
        return self.piece

    def GetHighlight(self):
        return self.highlight  # NEW

    # ----------------- SETTERS -----------------
    def SetColor(self, color):
        self.color = color

    def SetOccupied(self, occupied):
        self.occupied = occupied

    def SetPiece(self, piece):
        self.piece = piece

    def SetHighlight(self, value):
        self.highlight = value  
