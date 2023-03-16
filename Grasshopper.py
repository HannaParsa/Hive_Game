from Piece import Piece
class Grasshopper(Piece):
    def get_neighbors(self, x, y , piece):
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
    def movements(self , x , y ):
        output = set()
        n_e = self.get_ne()
        if n_e:
            destenation = n_e.get_ne()
            while destenation:
                n_e = destenation
                destenation = n_e.get_ne()
            if  n_e!= "ERROR":
                output.add(n_e.get_ne_pos())
        n_w = self.get_nw()
        if n_w:
            destenation = n_w.get_nw()
            while destenation:
                n_w = destenation
                destenation = n_w.get_nw()
            if  n_w!= "none":
                output.add(n_w.get_nw_pos())
        s_e = self.get_se()
        if s_e:
            destenation = s_e.get_se()
            while destenation:
                s_e = destenation
                destenation = s_e.get_se()
            if  s_e!= "none":
                output.add(n_e.get_se_pos())
        s_w = self.get_sw()
        if s_w:
            destenation = s_w.get_sw()
            while destenation:
                s_w = destenation
                destenation = s_w.get_sw()
            if  s_w!= "none":
                output.add(s_w.get_sw_pos())
        n = self.get_n()
        if n:
            destenation = n.get_n()
            while destenation:
                n = destenation
                destenation = n.get_n()
            if  n!= "none":
                output.add(n.get_n_pos())
        s = self.get_s()
        if s:
            destenation = s.get_s()
            while destenation:
                s = destenation
                destenation = s.get_s()
            if  s!= "none":
                output.add(s.get_s_pos())
        return output
    def get_n(self):
        if 0 <= self.pos['x'] - 2 < self.Board.columns * 2 and 0 <= self.pos['y'] < self.Board.rows * 2:
            return self.Board.ground[self.pos["x"] - 2][self.pos["y"]]
        return "none"

    def get_s(self):
        if 0 <= self.pos['x'] + 2 < self.Board.columns *+ 2 < self.Board.columns * 2 and 0 <= self.pos['y'] < self.Board.rows * 2 :
            return self.Board.ground[self.pos["x"] + 2][self.pos["y"]]
        return "none"

    def get_nw(self):
        if 0 <= self.pos['x']- 1 < self.Board.columns * 2 and 0 <= self.pos['y']-1 < self.Board.rows * 2:
            return self.Board.ground[self.pos["x"] - 1][self.pos["y"] - 1]
        return "none"

    def get_ne(self):
        if 0 <= self.pos['x']- 1 < self.Board.columns * 2 and 0 <= self.pos['y']+ 1 < self.Board.rows * 2 :
            return self.Board.ground[self.pos["x"] - 1][self.pos["y"] + 1]
        return "none"

    def get_sw(self):
        if 0 <= self.pos['x'] + 1 < self.Board.columns * 2 and 0 <= self.pos['y'] - 1 < self.Board.rows * 2 :
            return self.Board.ground[self.pos["x"] + 1][self.pos["y"] - 1]
        return "none"

    def get_se(self):
        if 0 <= self.pos['x']+ 1 < self.Board.columns * 2 and 0 <= self.pos['y'] + 1 < self.Board.rows * 2 :
            return self.Board.ground[self.pos["x"] + 1][self.pos["y"] + 1]
        return "none"
    def get_n_pos(self):
        return self.pos["x"] - 2, self.pos["y"]

    def get_s_pos(self):
        return self.pos["x"] + 2, self.pos["y"]

    def get_nw_pos(self):
        return self.pos["x"] - 1, self.pos["y"] - 1

    def get_ne_pos(self):
        return self.pos["x"] - 1, self.pos["y"] + 1

    def get_sw_pos(self):
        return self.pos["x"] + 1, self.pos["y"] - 1

    def get_se_pos(self):
        return self.pos["x"] + 1, self.pos["y"] + 1