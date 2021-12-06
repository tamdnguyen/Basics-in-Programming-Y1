class Box:
    LEFT = 0
    UP = 1
    RIGHT = 2
    DOWN = 3

    def __init__(self):
        self.__owner = None
        self.__left_side = False
        self.__right_side = False
        self.__up_side = False
        self.__down_side = False

    def get_owner(self):
        return self.__owner

    def add_owner(self, owner):
        self.__owner = owner

    def has_line_on_side(self, side):
        if side == Box.LEFT:
            if self.__left_side:
                return True
            else:
                return False
        elif side == Box.UP:
            if self.__up_side:
                return True
            else:
                return False
        elif side == Box.RIGHT:
            if self.__right_side:
                return True
            else:
                return False
        else:
            if self.__down_side:
                return True
            else:
                return False

    def add_line(self, side):
        if side == Box.LEFT:
            if self.__left_side:
                return False
            else:
                self.__left_side = True
                return True
        elif side == Box.UP:
            if self.__up_side:
                return False
            else:
                self.__up_side = True
                return True
        elif side == Box.RIGHT:
            if self.__right_side:
                return False
            else:
                self.__right_side = True
                return True
        else:
            if self.__down_side:
                return False
            else:
                self.__down_side = True
                return True

    def four_lines_placed(self):
        if self.__left_side is True and self.__up_side is True and \
                self.__right_side is True and self.__down_side is True:
            return True
        else:
            return False
