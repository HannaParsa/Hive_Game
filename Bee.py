from Piece import Piece
class Bee(Piece):
    def get_neighbors(self, x, y):
     neighbors = []
     n = self.Board.ground[x - 2][y]
     s = self.Board.ground[x + 2][y]
     n_w = self.Board.ground[x - 1][y - 1]
     n_e = self.Board.ground[x - 1][y + 1]
     s_w = self.Board.ground[x + 1][y - 1]
     s_e = self.Board.ground[x + 1][y + 1]
     if n.bug is None:
        neighbors.append((x - 2, y))
     if s.bug is None:
        neighbors.append((x + 2, y))
     if n_w.bug is None:
        neighbors.append((x - 1, y - 1))
     if n_e.bug is None:
        neighbors.append((x - 1, y + 1))
     if s_w.bug is None:
        neighbors.append((x + 1, y - 1))
     if s_e.bug is None:
        neighbors.append((x + 1, y + 1))
     return neighbors

