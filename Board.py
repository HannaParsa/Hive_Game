from Player import Player
from Piece import Piece
from Bee import Bee
from Beetle import Beetle
from Grasshopper import Grasshopper
from Spider import Spider


class Cell:
    def __init__(self):
        self.bug = None


class Board:
    def __init__(self, rows, columns):
        self.ground = []
        self.full_positions_map = {}  # (x, y) -> Piece
        self.rows = rows
        self.columns = columns
        for _ in range(rows * 2):
            row = []
            for _ in range(columns * 2):
                row.append(Cell())
            self.ground.append(row)

    def __str__(self, **kwargs):
        res = " "
        for j in range(self.columns):
            res += 3 * "_" + 5 * " "
        res += "\n"

        for i in range(self.rows):
            for j in range(self.columns):
                piece_label = 3 * " "

                piece = self.ground[2 * i][2 * j]
                # if piece is None and (i, j) in selects.keys():
                #     color_name = selects.get((i, j))
                #     color = colors.get(color_name)
                #     piece_label = color + "NON" + colors.get('Normal')
                if not piece.bug:
                    piece_label = "   "
                else:
                    temp = len(piece.bug.piece)
                    piece_label = piece.bug.piece + piece.bug.player.color[0] + " " * (2 - temp)

                res += "/" + piece_label + "\\" + 3 * "_"

            res += "\n"

            for j in range(self.columns):

                piece = self.ground[2 * i + 1][2 * j + 1]
                if not piece.bug:
                    piece_label = "   "
                else:
                    temp = len(piece.bug.piece)
                    piece_label = piece.bug.piece + piece.bug.player.color[0] + " " * (2 - temp)
                res += "\\" + 3 * "_" + "/" + piece_label

            res += "\n"

        return res

    def add_piece_place(self, x, y, color, piece, player):
        self.ground[x][y].bug = Piece(color, piece, self.ground)
        self.ground[x][y].bug.pos = {
            'x': x,
            'y': y
        }
        self.ground[x][y].bug.player = player
        self.full_positions_map[(x, y)] = self.ground[x][y].bug

    def show_possible_places(self, color):
        output = set()
        # insert in the middle of the board
        if len(self.full_positions_map) == 0:
            output.add((self.rows - 1, self.columns - 1))
        elif len(self.full_positions_map) == 1:
            output.add((8, 10))
            output.add((12, 10))
            output.add((9, 9))
            output.add((11, 11))
            output.add((9, 11))
            output.add((11, 9))
        else:
            for et, piece in self.full_positions_map.items():
                neighbors = self.get_neighbors(piece.pos['x'], piece.pos['y'])
                for neighbor in neighbors:
                    x = neighbor[0]
                    y = neighbor[1]
                    if 0 <= x - 2 < self.columns * 2 and 0 <= y < self.rows * 2:
                        n = self.ground[x - 2][y]
                        if n.bug and n.bug.player.color != color:
                            continue
                    if 0 <= x + 2 < self.columns * 2 and 0 <= y < self.rows * 2:
                        s = self.ground[x + 2][y]
                        if s.bug and s.bug.player.color != color:
                            continue
                    if 0 <= x - 1 < self.columns * 2 and 0 <= y - 1 < self.rows * 2:
                        n_w = self.ground[x - 1][y - 1]
                        if n_w.bug and n_w.bug.player.color != color:
                            continue
                    if 0 <= x - 1 < self.columns * 2 and 0 <= y + 1 < self.rows * 2:
                        n_e = self.ground[x - 1][y + 1]
                        if n_e.bug and n_e.bug.player.color != color:
                            continue
                    if 0 <= x + 1 < self.columns * 2 and 0 <= y - 1 < self.rows * 2:
                        s_w = self.ground[x + 1][y - 1]
                        if s_w.bug and s_w.bug.player.color != color:
                            continue
                    if 0 <= x + 1 < self.columns * 2 and 0 <= y + 1 < self.rows * 2:
                        s_e = self.ground[x + 1][y + 1]
                        if s_e.bug and s_e.bug.player.color != color:
                            continue
                    output.add((x, y))

        return output

    def get_neighbors(self, x, y):
        neighbors = []
        n = self.ground[x - 2][y]
        s = self.ground[x + 2][y]
        n_w = self.ground[x - 1][y - 1]
        n_e = self.ground[x - 1][y + 1]
        s_w = self.ground[x + 1][y - 1]
        s_e = self.ground[x + 1][y + 1]
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

    # remove the chosen piece
    def move(self, x, y, x2, y2, color, pieceName, player):
        self.ground[x2][y2].bug = Piece(color, pieceName, self.ground)
        self.ground[x2][y2].bug.pos = {
            'x': x2,
            'y': y2
        }
        self.ground[x2][y2].bug.player = player
        self.full_positions_map[(x2, y2)] = self.ground[x2][y2].bug
        self.ground[x][y].bug = None

    def move_piece(self, x, y, x2, y2, color, pieceName, player,piece ):
        #self.ground[x][y] = piece.piece_buttom
        self.ground[x][y].bug = piece.piece_buttom
        if self.ground[x2][y2].bug is not None:
            piece.piece_buttom = self.ground[x2][y2]
        #add
        self.ground[x2][y2].bug = Piece(color, pieceName, self.ground)
        self.ground[x2][y2].bug.pos = {
            'x': x2,
            'y': y2
        }
        self.ground[x2][y2].bug.player = player
        self.full_positions_map[(x2, y2)] = self.ground[x2][y2].bug
        # error dare
        if self.ground[x][y].bug == None:
           self.ground[x][y].bug = None


# ------------------------------------------------------------------------------

if __name__ == '__main__':
    turn = 0
    P1 = Player("P1", "black")
    P2 = Player("P2", "red")
    b = Board(11, 11)
    QB_P1 = Bee(None, None, b)
    QB_P2 = Bee(None, None, b)
    while True:
        # show the board
        print(str(b))
        print("add or move")
        func = input()
        player_turn = P1 if turn % 2 == 0 else P2
        if player_turn == 0:
            player = P1
        else:
            player = P2
        # turn is even P1 else P2
        color = "black" if turn % 2 == 0 else "red"
        if func == "add":
            print("choose your piece: ")
            pieceName = input()
            print(b.show_possible_places(player_turn.color))
            print("enter the position: ")
            # 10, 10 for the first time
            num = input().split(" ")
            x = int(num[0])
            y = int(num[1])
            # pieces:QB S B G A
            b.add_piece_place(x, y, color, pieceName, player_turn)
            if pieceName == "QB" and color == "black":
                QB_P1 = Bee(P1, pieceName, b)
            if pieceName == "QB" and color == "red":
                QB_P2 = Bee(P2, pieceName, b)
        if func == "move":
            print("Enter source x y: ")
            x, y = map(int, input().split())
            print("enter piece: ")
            pp = input()
            if pp == "QB":
               piece = Piece(player , pp , b)
               qb = Bee(player_turn, piece, b)
               print(qb.get_neighbors(x, y))
               x2, y2 = map(int, input('enter destination: ').split())
               qb.pos = {
                   'x': x2,
                    'y': y2
                }
               b.move(x, y, x2, y2, color, pp, player_turn )
            if pp == "B":
                piece = Piece(player , pp , b)
                beetle  = Beetle(player_turn , pp , b)
                print(beetle.get_neighbors(x, y ))
                x2, y2 = map(int, input('enter destination: ').split())
                beetle.pos = {
                   'x': x2,
                    'y': y2
                }
                b.move_piece(x, y, x2, y2, color, pp, player_turn , piece)
            if pp =="G":
                piece = Piece(player , pp ,b)
                grasshooper = Grasshopper(player_turn , pp,b)
                print(grasshooper.movements(x, y))
                x2, y2 = map(int, input('enter destination: ').split())
                grasshooper.pos = {
                   'x': x2,
                    'y': y2
                }
                b.move(x, y, x2, y2, color, pp, player_turn)
            if pp == "S":
               piece = Piece(player , pp ,b) 
               spider = Spider(player_turn , pp , b)
               print(spider.movement_spider(x, y, piece))
               x2, y2 = map(int, input('enter destination: ').split())
               spider.pos = {
                   'x': x2,
                   'y': y2
                }
               b.move(x, y, x2, y2, color, pp, player_turn)
        # determine the winner
        if player_turn == P1:
            ans = b.get_neighbors(QB_P1.pos['x'], QB_P1.pos['y'])
            if len(ans) == 0:
                print("Player 1 won")
                break
        else:
            ans = b.get_neighbors(QB_P2.pos['x'], QB_P1.pos['y'])
            if len(ans) == 0:
                print("Player 2 won")
                break
        turn += 1
