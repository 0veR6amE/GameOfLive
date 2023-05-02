from random import random
from typing import NoReturn, Optional


class Cell:
    """
    Class of one cell
    """

    def __init__(self, x: int, y: int, is_alive: bool) -> NoReturn:
        """initialization of class"""
        self.x = x
        self.y = y
        self.is_alive = is_alive
        self.neighbour_count = 0

    def __repr__(self) -> str:
        return "[{},{},{:5}]".format(self.x, self.y, str(self.is_alive))

    def __str__(self) -> list:
        return [self.x, self.y, self.is_alive]

    def calc_neighbour_count(self) -> int:
        """Func of counting the number of living neighbors around"""
        count, pre_x, pre_y = 0, 0, 0
        if self.x > 0:
            pre_x = self.x - 1
        for x in range(pre_x,
                       self.x + 1 + 1):
            if self.y > 0:
                pre_y = self.y - 1
            for y in range(pre_y,
                           self.y + 1 + 1):
                if x == self.x and y == self.y:
                    continue
                if self.invalidate(x, y):
                    continue
                count += int(CellGrid.cells[x][y].is_alive)
        self.neighbour_count = count
        return count

    @staticmethod
    def invalidate(x: int, y: int) -> bool:
        """Checking for the correct coords of the cell"""
        if x >= CellGrid.x or y >= CellGrid.y:
            return True
        if x < 0 or y < 0:
            return True
        return False

    # noinspection PyTypeChecker
    def rule(self) -> Optional[bool]:
        """Rules of the GoL"""
        if self.neighbour_count > 3 or self.neighbour_count < 2:
            self.is_alive = False
        elif self.neighbour_count == 3:
            self.is_alive = True
        elif self.neighbour_count == 2:
            pass


class CellGrid:
    """
         Cell grid type, all cells are in a grid of length x and width y
    """
    cells = []
    x = 0
    y = 0

    def __init__(self, x: int, y: int) -> NoReturn:
        """Initialization of class"""
        CellGrid.x = x
        CellGrid.y = y

    def create_random_Grid(self) -> NoReturn:
        """Crate random grid of Cells"""
        self.reset()
        for i in range(CellGrid.x):
            cell_list = []
            for j in range(CellGrid.y):
                cell = Cell(i, j, random() > 0.5)
                cell_list.append(cell)
            CellGrid.cells.append(cell_list)

    @staticmethod
    def create_empty_Grid() -> NoReturn:
        """Crate empty grid of Cells"""
        for i in range(CellGrid.x):
            cell_list = []
            for j in range(CellGrid.y):
                cell = Cell(j, i, False)
                cell_list.append(cell)
            CellGrid.cells.append(cell_list)

    @staticmethod
    def circulate_rule() -> NoReturn:
        """Scroll through each cell to determine its vital state"""
        for cell_list in CellGrid.cells:
            for item in cell_list:
                item.rule()

    @staticmethod
    def circulate_neighbour_count() -> NoReturn:
        """Scroll through each cell to calculate the number of
         living neighbors"""
        for cell_list in CellGrid.cells:
            for item in cell_list:
                item.calc_neighbour_count()

    @staticmethod
    def reset() -> NoReturn:
        """Update the CellGrid"""
        CellGrid.cells = []

    @staticmethod
    def return_Grid() -> list:
        """Return grid of cells"""
        return CellGrid.cells
