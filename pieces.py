WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Piece:
    def __init__(self, row, col, color, image_url, type, rank, image, rect):
        self.row = row
        self.col = col
        self.color = color
        self.image_url = image_url
        self.type = type
        self.rank = rank
        self.image = image
        self.rect = rect

    def MovePiece(self, row, col):
        self.row = row
        self.col = col

    def GetRow(self): return self.row
    def GetCol(self): return self.col
    def GetColor(self): return self.color
    def GetImageURL(self): return self.image_url
    def GetType(self): return self.type
    def GetRank(self): return self.rank
    def GetImage(self): return self.image
    def GetRect(self): return self.rect
    def SetRow(self, row): self.row = row
    def SetCol(self, col): self.col = col

    def get_moves(self, cells):
        """Override in subclasses."""
        return []

def get_cell(cells, row, col):
    """Helper: return the cell at (row,col)"""
    for cell in cells:
        if cell.row == row and cell.col == col:
            return cell
    return None

# -------------------- PAWN --------------------
class Pawn(Piece):
    type = "Pawn"
    rank = 2

    def __init__(self, row, col, color, image_url, image, rect):
        super().__init__(row, col, color, image_url, self.type, self.rank, image, rect)

    def get_moves(self, cells):
        moves = []
        direction = -1 if self.color == WHITE else 1  # White moves up, Black moves down

       
        for dc in [-1, 1]:
            target_row = self.row + direction
            target_col = self.col + dc
            if 0 <= target_row < 8 and 0 <= target_col < 8:
                for cell in cells:
                    if cell.row == target_row and cell.col == target_col and not cell.GetOccupied():
                        moves.append(cell)

        
        target_row = self.row + direction
        target_col = self.col
        if 0 <= target_row < 8:
            for cell in cells:
                if cell.row == target_row and cell.col == target_col and cell.GetOccupied():
                    if cell.GetPiece().color != self.color:
                        moves.append(cell)

        return moves

# -------------------- KNIGHT --------------------
class Knight(Piece):
    type = "Knight"
    rank = 4

    def __init__(self, row, col, color, image_url, image, rect):
        super().__init__(row, col, color, image_url, self.type, self.rank, image, rect)

    def get_moves(self, cells):
        moves = []
        # Directions: up, down, left, right, skipping one cell
        directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]

        for dr, dc in directions:
            r, c = self.row + dr, self.col + dc
            if 0 <= r < 8 and 0 <= c < 8:
                for cell in cells:
                    if cell.row == r and cell.col == c:
                        # Can move if empty or contains enemy piece
                        if not cell.GetOccupied() or cell.GetPiece().color != self.color:
                            moves.append(cell)
        return moves

# -------------------- BISHOP --------------------
class Bishop(Piece):
    type = "Bishop"
    rank = 3

    def __init__(self, row, col, color, image_url, image, rect):
        super().__init__(row, col, color, image_url, self.type, self.rank, image, rect)

    def get_moves(self, cells):
        moves = []

        # Zig-zag patterns for all four directions
        zigzag_patterns = [
            [(-1, -1), (-1, 1)],  # Upward zig-zag
            [(1, -1), (1, 1)],    # Downward zig-zag
            [(-1, -1), (1, -1)],  # Leftward zig-zag
            [(-1, 1), (1, 1)],    # Rightward zig-zag
        ]

        for pattern in zigzag_patterns:
            r, c = self.row, self.col
            blocked = False
            step = 0
            while not blocked:
                dr, dc = pattern[step % 2]
                r += dr
                c += dc
                step += 1

                if not (0 <= r < 8 and 0 <= c < 8):
                    break

                for cell in cells:
                    if cell.row == r and cell.col == c:
                        if not cell.GetOccupied():
                            moves.append(cell)
                        elif cell.GetPiece().color != self.color:
                            moves.append(cell)
                            blocked = True
                        else:
                            blocked = True
                        break  # Found the cell, stop searching

        return moves

# -------------------- ROOK --------------------
class Rook(Piece):
    type = "Rook"
    rank = 3

    def __init__(self, row, col, color, image_url, image, rect):
        super().__init__(row, col, color, image_url, self.type, self.rank, image, rect)

    def get_moves(self, cells):
        moves = []

        # Step 1: Diagonal 1-square move
        diagonal_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        diagonal_moves = []
        for dr, dc in diagonal_directions:
            r1, c1 = self.row + dr, self.col + dc
            if 0 <= r1 < 8 and 0 <= c1 < 8:
                # Find the target diagonal cell
                target_cell = next((cell for cell in cells if cell.row == r1 and cell.col == c1), None)
                if target_cell and (not target_cell.GetOccupied() or target_cell.GetPiece().color != self.color):
                    diagonal_moves.append(target_cell)

        # Step 2: From each diagonal square, add normal rook moves
        for diag_cell in diagonal_moves:
            moves.append(diag_cell)  # Include the 1-diagonal step itself
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                r, c = diag_cell.row, diag_cell.col
                while True:
                    r += dr
                    c += dc
                    if not (0 <= r < 8 and 0 <= c < 8):
                        break
                    target_cell = next((cell for cell in cells if cell.row == r and cell.col == c), None)
                    if target_cell:
                        if not target_cell.GetOccupied():
                            moves.append(target_cell)
                        elif target_cell.GetPiece().color != self.color:
                            moves.append(target_cell)
                            break
                        else:
                            break
        return moves

# -------------------- QUEEN --------------------
class Queen(Piece):
    type = "Queen"
    rank = 9

    def __init__(self, row, col, color, image_url, image, rect):
        super().__init__(row, col, color, image_url, self.type, self.rank, image, rect)

    def get_moves(self, cells):
        moves = []
        max_range = 2  # limit teleport to 2 spaces in any direction

        for r in range(self.row - max_range, self.row + max_range + 1):
            for c in range(self.col - max_range, self.col + max_range + 1):
                if 0 <= r < 8 and 0 <= c < 8:
                    if r == self.row and c == self.col:
                        continue  # skip current position
                    for cell in cells:
                        if cell.row == r and cell.col == c:
                            if not cell.GetOccupied() or cell.GetPiece().color != self.color:
                                moves.append(cell)
        return moves

# -------------------- KING --------------------
class King(Piece):
    type = "King"
    rank = 10

    def __init__(self,row,col,color,image_url,image,rect):
        super().__init__(row,col,color,image_url,self.type,self.rank,image,rect)

    def get_moves(self,cells):
        moves = []
        for dr in [-1,0,1]:
            for dc in [-1,0,1]:
                if dr==0 and dc==0: continue
                r,c = self.row+dr,self.col+dc
                if 0 <= r < 8 and 0 <= c < 8:
                    target = get_cell(cells,r,c)
                    if not target.GetOccupied() or target.GetPiece().color != self.color:
                        moves.append(target)
        return moves

