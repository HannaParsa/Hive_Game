from Piece import Piece
class Beetle(Piece):
   def get_neighbors(self, x, y ):
      neighbors = []
      n = self.Board.ground[x - 2][y]
      s = self.Board.ground[x + 2][y]
      n_w = self.Board.ground[x - 1][y - 1]
      n_e = self.Board.ground[x - 1][y + 1]
      s_w = self.Board.ground[x + 1][y - 1]
      s_e = self.Board.ground[x + 1][y + 1]
      neighbors.append((x - 2, y))
      neighbors.append((x + 2, y))
      neighbors.append((x - 1, y - 1))
      neighbors.append((x - 1, y + 1))
      neighbors.append((x + 1, y - 1))
      neighbors.append((x + 1, y + 1))
      return neighbors