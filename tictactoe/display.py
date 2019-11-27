import time
import structure
import graphics.graphics as g

steps = 3
h_w = 400
time = 0.0001
m = h_w * 0.0075
black = "#000000"
white = "#FFFFFF"
title = "Tic Tac Toe"
nums = ["1", "2", "3", "4", "5"]
xo_colors = {"X": "#33CC66", "O": "#F95B5B", "1": "#FFFFFF", "2": "#FFFFFF",
            "3": "#FFFFFF", "4": "#FFFFFF", "5": "#FFFFFF"}

class GameView():
    def __init__(self, h_w):
        self.h_w = h_w
        self.win = g.GraphWin(title, h_w, h_w)

    def get_key(self):
        return self.win.getKey()


class GridView(structure.GameListener):
    def __init__(self, game, grid_size):
        self.game = game
        self.win = game.win
        self.bg = g.Rectangle(g.Point(0, 0), g.Point(game.h_w, game.h_w))
        self.bg.setFill(black)
        self.bg.draw(self.win)
        self.cell_h_w = (game.h_w - m) / grid_size
        self.tile_h_w = self.cell_h_w - m
        self.tiles = []
        for r in range(grid_size):
            row_tiles = []
            for c in range(grid_size):
                left, right = self.tile_corners(r, c)
                tile_bg = g.Rectangle(left, right)
                tile_bg.setFill(white)
                tile_bg.draw(self.win)
                row_tiles.append(tile_bg)
            self.tiles.append(row_tiles)

    def tile_corners(self, r, c):
        top_left = m + c * self.cell_h_w
        top_right = top_left + self.tile_h_w
        bottom_left = m + r * self.cell_h_w
        bottom_right = bottom_left + self.tile_h_w
        left = g.Point(top_left, bottom_left)
        right = g.Point(top_right, bottom_right)
        return left, right

    def notify(self, evt):
        if evt.k == structure.EventKind.tile_c:
            view = TileView(self, evt.t)
            evt.t.add_listener(view)


class TileView():
    def __init__(self, grid, t):
        self.grid = grid
        self.win = grid.win
        self.r = t.r
        self.c = t.c
        self.val = t.val
        left, right = grid.tile_corners(self.r, self.c)
        white = g.Rectangle(left, right)
        white.setFill(xo_colors[self.val])
        self.bg = white
        x = (left.getX() + right.getX()) / 2
        y = (left.getY() + right.getY()) / 2
        center = g.Point(x, y)
        label = g.Text(center, self.val)
        label.setSize(36)
        if self.val in nums:
            label.setFill("white")
        self.label = label
        white.draw(self.win)
        label.draw(self.win)
        self.x = x
        self.y = y

    def notify(self, evt):
        if evt.kind == structure.EventKind.tile_updated:
            r, c = evt.tile.r, evt.tile.c
            if self.val != evt.t.val:
                self.val = evt.t.val
                tile_color = xo_colors[evt.t.val]
                self.bg.setFill(tile_color)
                self.label.setText(str(evt.t.val))
