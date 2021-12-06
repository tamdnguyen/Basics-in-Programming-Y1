from box import Box


class DotsAndBoxesGame:
    TIE = "tie"
    PLAYER1 = "A"
    PLAYER2 = "B"

    def __init__(self, grid_width, grid_height, player_name_1, player_name_2):
        self.__grid_width = grid_width
        self.__grid_height = grid_height
        self.__player_name_1 = player_name_1
        self.__player_name_2 = player_name_2
        self.__grid = self.create_grid()

    def create_grid(self):
        game_grid = []
        for i in range(self.__grid_height):
            row_grid = []
            for j in range(self.__grid_width):
                box = Box()
                row_grid.append(box)
            game_grid.append(row_grid)

        return game_grid

    def add_line(self, x, y, side, player):
        # create boolean for return info
        success_add_line = False
        four_line_added = False

        # The numbering of the box coordinates is started from 1 (NOT from 0 as list indices).
        box_row = x - 1
        box_column = y - 1

        # add line to the box
        box = self.__grid[box_row][box_column]
        if box.add_line(side):
            # If the line is added successfully, the method
            # also adds a line to the neighbour box on this side
            self.update_neighbour_of_box(box_row, box_column, side)
            # find the recently updated box as neighbour_box
            neighbour_box = self.get_neighbour_on_side(side, box_row, box_column)
            success_add_line = True

            # If a fourth line is added to the |box or its neighbour box|
            # the method adds a letter (A or B) corresponding to
            # the player given as a parameter to be the owner of the completed box.
            if box.four_lines_placed():
                four_line_added = True
                if player == self.__player_name_1:
                    box.add_owner(DotsAndBoxesGame.PLAYER1)
                else:
                    box.add_owner(DotsAndBoxesGame.PLAYER2)
                # check and add owner of the neighbour box - JUST IN CASE neighbour not None
                if neighbour_box != None:
                    if neighbour_box.four_lines_placed():
                        if player == self.__player_name_1:
                            neighbour_box.add_owner(DotsAndBoxesGame.PLAYER1)
                        else:
                            neighbour_box.add_owner(DotsAndBoxesGame.PLAYER2)

        if not success_add_line:
            return False, False
        else:
            if four_line_added:
                return True, True
            else:
                return True, False

    def update_neighbour_of_box(self, row_index, column_index, side):
        neighbour = self.get_neighbour_on_side(side, row_index, column_index)

        # add to the neighbour on one side
        if neighbour is not None:
            if side == 0:
                neighbour.add_line(2)
            elif side == 1:
                neighbour.add_line(3)
            elif side == 2:
                neighbour.add_line(0)
            else:
                neighbour.add_line(1)

    def get_neighbour_on_side(self, side, row, column):
        # find the edges and if they are outside of the game_grid then return None
        # there are four cases:
        #   first row and find the up side => row = 0 and side = 1
        #   last row and find the bottom side => row = height - 1 (Index from 0) and side = 3
        #   first column and find the left side => column = 0 and side = 0
        #   last column and find the right side => column = width - 1 (Index from 0) and side = 2
        if row == 0 and side == 1:
            return None
        elif row == self.__grid_height - 1 and side == 3:
            return None
        elif column == 0 and side == 0:
            return None
        elif column == self.__grid_width - 1 and side == 2:
            return None
        else:
            if side == 0:
                neighbour = self.__grid[row][column - 1]
                return neighbour
            elif side == 1:
                neighbour = self.__grid[row - 1][column]
                return neighbour
            elif side == 2:
                neighbour = self.__grid[row][column + 1]
                return neighbour
            else:
                neighbour = self.__grid[row + 1][column]
                return neighbour

    def calculate_points_of_player(self, player):
        point = 0

        for i in range(self.__grid_height):
            for j in range(self.__grid_width):
                if self.__grid[i][j].get_owner() == player:
                    point += 1

        return point

    def is_ended(self):
        for i in range(self.__grid_height):
            for j in range(self.__grid_width):
                if not self.__grid[i][j].four_lines_placed():
                    return False

        return True

    def winner(self):
        point_A = self.calculate_points_of_player("A")
        point_B = self.calculate_points_of_player("B")

        if point_A > point_B:
            return self.__player_name_1
        elif point_B > point_A:
            return self.__player_name_2
        else:
            return DotsAndBoxesGame.TIE

    def give_score(self):
        table_1 = "{:<15s} | {:<15s}".format(self.__player_name_1 + " (A)", self.__player_name_2 + " (B)")
        table_2 = "-" * 37
        table_3 = "{:<15d} | {:<15d}".format(self.calculate_points_of_player("A"), self.calculate_points_of_player("B"))
        score_string = "\n{:s}:\n\n{:s}\n{:s}\n{:s}\n".format("Score", table_1, table_2, table_3)

        return score_string

    def one_row_of_grid(self, row_index):
        # first, we need to check if the row_index is odd or even
        # if even, then it contain dots and space and possibly line ——
        if row_index % 2 == 0:
            row = "   o"
            # the last row has the number as self.__grid_height * 2 + 1
            # but its index should be minus 1, therefore
            if row_index == self.__grid_height * 2:
                box_row_index = int(row_index / 2 - 1)
                for i in range(self.__grid_width):
                    box = self.__grid[box_row_index][i]
                    if box.has_line_on_side(3):
                        box_print = "{:^4s}o".format("——")
                    else:
                        box_print = "{:^4s}o".format(" " * 4)
                    row += box_print

            # for every row except for the last row, we check the top side of the box to add the —— or not
            else:
                box_row_index = int(row_index / 2)
                for i in range(self.__grid_width):
                    box = self.__grid[box_row_index][i]
                    if box.has_line_on_side(1):
                        box_print = "{:^4s}o".format("——")
                    else:
                        box_print = "{:^4s}o".format(" " * 4)
                    row += box_print
        else:
            row = ""
            box_row_index = int((row_index + 1) / 2 - 1)
            for i in range(self.__grid_width):
                box = self.__grid[box_row_index][i]
                if box.has_line_on_side(0):
                    if box.four_lines_placed():
                        box_print = "| {:s}  ".format(box.get_owner())
                    else:
                        box_print = "|    "
                else:
                    box_print = " " * 5
                row += box_print
                if i == self.__grid_width - 1:
                    if box.has_line_on_side(2):
                        row += "|"
        row += "\n"
        return row

    def __str__(self):
        # create row 1 consists of number
        row_1 = "   "
        for i in range(self.__grid_width):
            row_1 += "   {:d} ".format(i + 1)

        # create the grid table
        grid_row = ""
        for i in range(self.__grid_height * 2 + 1):
            if i % 2 == 0:
                grid_row += self.one_row_of_grid(i)
            else:
                grid_row += "{:d}  {:s}".format((i + 1) // 2, self.one_row_of_grid(i))

        # the main string need to return
        current = "{:s}\n{:s}{:s}".format(row_1, grid_row, self.give_score())

        return current

