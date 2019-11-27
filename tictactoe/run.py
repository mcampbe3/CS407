import display
import structure
import graphics.graphics as g
from PIL import Image as NewImage

def is_in(point, is_grid, is_tile):
    left, right = is_grid.tile_corners(is_tile.r, is_tile.c)
    white = g.Rectangle(left, right)
    ll = white.getP1()
    ur = white.getP2()
    return ll.getX() < point.getX() < ur.getX() and ll.getY() < point.getY() < ur.getY()

def main():
    print("Tic Tac Toe")
    print("------------")
    print("Please wait while your tic tac toe board is generated...")

    tr = 1
    while (tr):
        grid = structure.Grid()
        game_v = display.GameView(400)
        grid_v = display.GridView(game_v, len(grid.tiles))
        grid.add_listener(grid_v)

        for i in range(1, 10):
            grid.place_tile(i)

        answer = grid.find_correct_tile()
        if answer == 0:
            game_v.win.close()
        else:
            tr = 0

            print("\nTo prove you are not a bot:  Click the box that gives X a tic tac toe.")

            tile_v = display.TileView(grid_v, answer)
            answer = grid.find_correct_tile()
            clickPoint = game_v.win.getMouse()

            if is_in(clickPoint, grid_v, tile_v):
                print("\nYou passed!")
            else:
                print("\nBot test failed :(")

            game_v.win.close()
    return 1


if __name__ == "__main__":
    main()
