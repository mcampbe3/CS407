import display
import structure

def main():
    grid = structure.Grid()
    game_v = display.GameView(400)
    grid_v = display.GridView(game_v, len(grid.tiles))
    grid.add_listener(grid_v)

    for i in range(1, 10):
        grid.place_tile(i)

    print("Pick the number on the board that gives X a tic tac toe")
    print("Please type type a number (1-5) from the board")
    print("or type 0 if it is not possible for X to get a tic tac toe\n")
    answer = grid.find_correct_tile()
    user_input = input("Choose a position: ")
    if user_input == answer:
        print("\nYou passed!")
    else:
        print("\nBot test failed :(")
    # if user_input == 1:
    # 	#
    # elif user_input == 2:
    # 	#
    # elif user_input == 3:
    # 	#
    # elif user_input == 4:
    # 	#
    # elif user_input == 5:
    # 	#
    # else:
    # 	#	

if __name__ == "__main__":
    main()
