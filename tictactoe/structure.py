import random
from enum import Enum
import graphics.graphics as g

size = 3

class EventKind(Enum):
    tile_c = 1


class GameEvent(object):
    def __init__(self, k, t):
        self.k = k
        self.t = t

    def __repr__(self):
        return "GameEvent({}, {})".format(self.k, self.t)


class GameListener(object):
    def notify(self, event):
        raise NotImplementedError("")


class GameElement(object):
    def __init__(self):
        self._ls = []

    def add_listener(self, l):
        self._ls.append(l)

    def notify_all(self, evt):
        for l in self._ls:
            l.notify(evt)


class Grid(GameElement):
    def __init__(self):
        super().__init__()
        self.s = size
        self.tiles = []
        for r in range(self.s):
            columns = []
            for c in range(self.s):
                columns.append(None)
            self.tiles.append(columns)

    def in_bounds(self, r, col):
        return 0 <= r < self.rs and 0 <= c < self.cols

    def as_list(self):
        rep = []
        for r in self.tiles:
            value_list = []
            for tile in r:
                if tile is None:
                    value_list.append(0)
                else:
                    value_list.append(tile.value)
            rep.append(value_list)
        return rep

    def set_tiles(self, rep):
        self.tiles = []
        for r in range(self.rs):
            r_tiles = []
            for c in range(self.cols):
                if rep[r][col] == 0:
                    r_tiles.append(None)
                else:
                    val = rep[r][col]
                    tile = Tile(self, r, col, value=val)
                    r_tiles.append(tile)
                    self.notify_all(GameEvent(EventKind.tile_c, tile))
            self.tiles.append(r_tiles)

    def find_empty(self):
        candidates = []
        for r in range(self.s):
            for c in range(self.s):
                if self.tiles[r][c] is None:
                    pos = (r, c)
                    candidates.append(pos)
        if candidates == []:
            return None
        return random.choice(candidates)

    def place_tile(self, count):
        spot = self.find_empty()
        r, c = spot
        if count == 1 or count == 3:
            self.place_tile_spec("#33CC66", r, c, "X")
        elif count == 2 or count == 4:
            self.place_tile_spec("#FFFFFF", r, c, "O")
        else:
            self.place_tile_spec("#FFFFFF", r, c, str(count - 4))

    def place_tile_spec(self, color, r, c, val):
        tile = Tile(self, r, c, color, val)
        self.tiles[r][c] = tile
        self.notify_all(GameEvent(EventKind.tile_c, tile))

    def find_correct_tile(self):
        v = 0
        x_positions = []
        for r in range(self.s):
            for c in range(self.s):
                if self.tiles[r][c].val == "X":
                    x_positions.append(g.Point(r, c))
        p1 = x_positions[0]
        p2 = x_positions[1]
        if (p2.x - p1.x == 1 and p2.y == p1.y):
            if p2.x == 2:
                value = self.tiles[int(p2.x - 2)][int(p1.y)].val
                v = self.tiles[int(p2.x - 2)][int(p1.y)]
                if value == "O":
                    v = 0
            else:
                value = self.tiles[int(p2.x + 1)][int(p1.y)].val
                v = self.tiles[int(p2.x + 1)][int(p1.y)]
                if value == "O":
                  v = 0
        if (p2.y - p1.y == 1 and p2.x == p1.x):
            if p2.y == 2:
                value = self.tiles[int(p1.x)][int(p2.y - 2)].val
                v = self.tiles[int(p1.x)][int(p2.y - 2)]
                if value == "O":
                    v = 0
            else:
                value = self.tiles[int(p1.x)][int(p2.y + 1)].val
                v = self.tiles[int(p1.x)][int(p2.y + 1)]
                if value == "O":
                    v = 0
        if (p2.x - p1.x == 2 and p2.y == p1.y):
            if p2.x == 2:
                value = self.tiles[int(p2.x - 1)][int(p1.y)].val
                v = self.tiles[int(p2.x - 1)][int(p1.y)]
                if value == "O":
                    v = 0
        if (p2.y - p1.y == 2 and p2.x == p1.x):
            if p2.y == 2:
                value = self.tiles[int(p1.x)][int(p2.y - 1)].val
                v = self.tiles[int(p1.x)][int(p2.y - 1)]
                if value == "O":
                    v = 0

        # Diagonals
        if (p1.x == 0 and p1.y == 0):
            if (p2.x == 1 and p2.y == 1):
                value = self.tiles[2][2].val
                v = self.tiles[2][2]
                if value == "O":
                    v = 0
            if (p2.x == 2 and p2.y ==2):
                value = self.tiles[1][1].val
                v = self.tiles[1][1]
                if value == "O":
                    v = 0
        if (p1.x == 1 and p1.y == 1 and p2.x == 2 and p2.y ==2):
            value = self.tiles[0][0].val
            v = self.tiles[0][0]
            if value == "O":
                v = 0

        if (p2.x == 0 and p2.y == 0):
            if (p1.x == 1 and p1.y == 1):
                value = self.tiles[2][2].val
                v = self.tiles[2][2]
                if value == "O":
                    v = 0
            if (p1.x == 2 and p1.y ==2):
                value = self.tiles[1][1].val
                v = self.tiles[1][1]
                if value == "O":
                    v = 0
        if (p2.x == 1 and p2.y == 1 and p1.x == 2 and p1.y ==2):
            value = self.tiles[0][0].val
            v = self.tiles[0][0]
            if value == "O":
                v = 0

        if (p1.x == 0 and p1.y == 2):
            if (p2.x == 1 and p2.y == 1):
                value = self.tiles[2][0].val
                v = self.tiles[2][0]
                if value == "O":
                    v = 0
            if (p2.x == 2 and p2.y == 0):
                value = self.tiles[1][1].val
                v = self.tiles[1][1]
                if value == "O":
                    v = 0
        if (p1.x == 1 and p1.y == 1 and p2.x == 2 and p2.y == 0):
            value = self.tiles[0][2].val
            v = self.tiles[0][2]
            if value == "O":
                v = 0

        if (p2.x == 0 and p2.y == 2):
            if (p1.x == 1 and p1.y == 1):
                value = self.tiles[2][0].val
                v = self.tiles[2][0]
                if value == "O":
                    v = 0
            if (p1.x == 2 and p1.y == 0):
                value = self.tiles[1][1].val
                v = self.tiles[1][1]
                if value == "O":
                    v = 0
        if (p2.x == 1 and p2.y == 1 and p1.x == 2 and p1.y == 0):
            value = self.tiles[0][2].val
            v = self.tiles[0][2]
            if value == "O":
                v = 0

        return v


class Tile(GameElement):
    def __init__(self, grid, r, c, color, val):
        super().__init__()
        self.grid = grid
        self.r = r
        self.c = c
        self.color = color
        self.val = val
        self.pos = g.Point(r, c)

    def __repr__(self):
        return "Tile({}) at {},{}".format(self.val, self.r, self.c)

    def __str__(self):
        return str(self.val)
