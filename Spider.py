from Piece import Piece
class Spider(Piece):
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
    def movement_spider(self , x , y , piece):
        output = set()
        neighbors = piece.get_neighbors(piece.pos['x'], piece.pos['y'])
        for neighbor in neighbors:
            x = neighbor[0]
            y = neighbor[1]
            neighbor_second = neighbor.get_neighbors(x , y)
            for n in neighbor_second:
                x2 = n[0]
                y2 = n[1]
                neighbor_third = n.get_neighbors(x , y)
                output.add(x2 , y2)
        return output
                       