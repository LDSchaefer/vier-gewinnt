"""
This program implements a 'Connect Four' game.
"""

import os

__author__ = "6964771: Philip Reich"
__email__ = "philip.reich@stud.uni-frankfurt.de"

#
# if main:
# f1 start spiel (spielerx mensch/ ki?)
#
# while spiel:
# f2 zug spieler 1
# f3 gewonnen?
# f2 zug spieler 2
# f3 gewonnen?
# endergbnis
# f1:
# return bsp dictt = {"Spieler1": 0 (mensch), "Spieler2": 1 (ki)}
# f2a check spalte frei


def print_grid(to_print_grid):
    """Prints the grid to the console."""
    for row in to_print_grid:
        print(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])


def won_test(idn, grid_tt):
    """
    Tests if player has won who marks his fields with "idn" (1/2).
    Returns true or false.
    """

    idn = idn[1]
    flag = False
    # vert
    for rowx in range(len(grid_tt[0])-1):
        for coly in range(len(grid_tt)-2):
            vert_sum = 0
            for rind in range(2):
                for dind in range(3):
                    if grid_tt[dind + coly][rind + rowx] == idn:
                        vert_sum += 1
            if vert_sum == 4:
                flag = True
    # hori
    for rowx in range(len(grid_tt[0])-2):
        for coly in range(len(grid_tt)-1):
            hori_sum = 0
            for rind in range(3):
                for dind in range(2):
                    if grid_tt[dind + coly][rind + rowx] == idn:
                        hori_sum += 1
            if hori_sum == 4:
                flag = True
    return flag


def clear_console():
    """A call to this function clears the console."""

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def start_spiel():
    """Starts the game and returns player tupels and the grid."""

    players_start = []
    for i in range(2):
        temp = input("Spielername >>")
        temp1 = input("KI? (0 für KI)>>")
        while temp1 not in ["0", "1"]:
            temp1 = input("KI? (0 für KI)>>")
        players_start.append((temp, temp1))
    grid_start = [[0 for b in range(10)] for i in range(9)]
    return players_start, grid_start


def ai_turn(player_int, aiturn_grid):
    """Executes AI turn."""

    pass


def grid_move(player_symbol, mutate_grid, mutate_col):
    """Inserts value in grid for player."""

    print(mutate_col)
    for row in range(9):
        if mutate_grid[row][mutate_col] != 0:
            mutate_grid[row-1][mutate_col] = player_symbol
            break
        if row == 8:
            mutate_grid[row][mutate_col] = player_symbol

    return mutate_grid


def player_turn(player, turn_grid, playerlist):
    """Executes turn of player."""

    clear_console()
    zero_or_one = playerlist.index(player)
    print_grid(turn_grid)
    print(f"{player[0]}, your turn:")
    if player[1] == 0:
        ai_turn(zero_or_one, turn_grid)
    else:
        col = input("In welche Spalte soll eingeworfen werden? (1-10)")
        valid_cols = [i for i in range(1, 11) if turn_grid[0][i-1] == 0]
        valid_cols = [str(i) for i in valid_cols]
        while col not in valid_cols:
            print("Keine gültige Eingabe oder Spalte voll.")
            col = input("In welche Spalte soll eingeworfen werden? (1-10)")
        col = int(col)
        turn_grid = grid_move(zero_or_one+1, turn_grid, col-1)

    return turn_grid


def terminate_game():
    """Function that terminates the game."""

    print("spiel fertig bitches")


def main():
    """Is here to start the module from the console or shell."""

    players, grid = start_spiel()
    done = False

    while not done:

        for p in players:

            if not done:

                grid = player_turn(p, grid, players)

                done = won_test(p, grid)

    terminate_game()


if __name__ == "__main__":

    main()
