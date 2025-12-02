class Cell:
    def __init__(self, row, col, color, rect):
        self.row = row
        self.col = col
        self.color = color
        self.rect = rect

    def GetRow(self):
        return self.row

    def GetCol(self):
        return self.col

    def GetColor(self):
        return self.color

    def GetRect(self):
        return self.rect
