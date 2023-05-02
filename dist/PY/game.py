import json
import sys
from typing import NoReturn, Union, Tuple

import pygame

from PY.CONS import *
from PY.cell import CellGrid, Cell
from error import WrongValueIn_hex2rgb, WrongLenIn_hex2rgb


def hex2rgb(value: str) -> Tuple[int, int, int]:
    """Function of change hex to rgb. \n
       Value must be view as (#......), where every point is one of element
       from the list of symbols '0123456789ABCDEF'"""
    sys.tracebacklimit = 0
    try:
        value = value.lower().lstrip('#')
        lv = len(value)
        if lv == 6:
            rgb = tuple([int(value[i:i + lv // 3], 16)
                         for i in range(0, lv, lv // 3)])
            sys.tracebacklimit = 1000
            return rgb
        else:
            raise WrongLenIn_hex2rgb("\n \t Len of input value must be 6(six)")
    except TypeError as e:
        print(f"error was = {e}")
        raise WrongValueIn_hex2rgb(
            "Wrong type of input value. \n Value must be view "
            "as (#......), where point is one of element from "
            "the list of symbols '0123456789ABCDEF'")


class Game:
    """Class of create and rendering Game"""
    screen: Union[pygame.Surface] = None
    width: Union[int] = None
    height: Union[int] = None
    x_rate: Union[int] = None
    y_rate: Union[int] = None
    cells: Union[CellGrid] = None
    random_data: Union[bytes] = None
    config_data: Union[bytes] = None

    # noinspection PyTypeChecker
    def __init__(self, width: int, height: int, x: int, y) -> NoReturn:
        """initialization of class"""
        self.width = Game.width = width
        self.height = Game.height = height
        self.x_rate = Game.x_rate = int(
            (width - 2 * EDGE_WIDTH) / x)  # Cell width
        self.y_rate = Game.y_rate = int(
            (height - 2 * EDGE_WIDTH) / y)  # Cell height
        self.screen = Game.screen = pygame.display.set_mode([width, height])
        self.cells = Game.cells = CellGrid(x, y)
        self.random_data = Game.random_data = None
        self.config_data = Game.config_data = None

    def re__init__(self) -> NoReturn:
        """reinitialization of class. Use for scheme redactor"""
        self.width = Game.width - 40
        self.height = Game.height - 40
        self.screen = Game.screen = pygame.display.set_mode(
            [self.width, self.height])

    @staticmethod
    def hide():
        pygame.display.set_mode(flags=pygame.HIDDEN)

    def create_random_Grid(self) -> NoReturn:
        """Transit function. Create random grid in class CellGrid"""
        self.cells.create_random_Grid()

    def create_empty_Grid(self) -> NoReturn:
        """Transit function. Create empty grid in class CellGrid"""
        if self.cells.cells:
            self.cells.reset()
        self.cells.create_empty_Grid()
        self.cells.cells = self.cells.return_Grid()

    def create_squares_grid(self):
        """Rendering of squares grid on window. Use for random grid"""
        colors: dict = json.load(open('Files/json_files/colors.json'))
        color_of_line: tuple = hex2rgb(colors['line'])

        for i in range(self.cells.x + 1):
            pygame.draw.line(self.screen, color_of_line,
                             (START_POSX, START_POSY + i * self.y_rate),
                             (START_POSX + self.cells.x * self.x_rate,
                              START_POSY + i * self.y_rate),
                             LINE_WIDTH)
            pygame.draw.line(self.screen, color_of_line,
                             (START_POSX + i * self.x_rate, START_POSY),
                             (START_POSX + i * self.x_rate,
                              START_POSY + self.cells.x * self.y_rate),
                             LINE_WIDTH)
        self.random_data = self.screen.get_buffer().raw

    def create_config_squares_grid(self):
        """Rendering of squares grid on window. Use for config grid"""
        colors: dict = json.load(open('Files/json_files/colors.json'))
        color_of_line: tuple = hex2rgb(colors['line'])

        for i in range(self.cells.x + 1):
            pygame.draw.line(self.screen, color_of_line,
                             (0, i * self.y_rate),
                             (self.cells.x * self.x_rate,
                              i * self.y_rate),
                             LINE_WIDTH)
            pygame.draw.line(self.screen, color_of_line,
                             (i * self.x_rate, 0),
                             (i * self.x_rate,
                              self.cells.x * self.y_rate),
                             LINE_WIDTH)
        self.config_data = Game.config_data = self.screen.get_buffer().raw

    def show_random_life(self):
        """Show life on the screen. Use for random grid"""
        colors: dict = json.load(open('Files/json_files/colors.json'))
        color_of_life: tuple = hex2rgb(colors['live'])

        for cell_list in self.cells.cells:
            for item in cell_list:
                x: int = item.x
                y: int = item.y
                if item.is_alive:
                    pygame.draw.rect(self.screen, color_of_life,
                                     [START_POSX + x * self.x_rate + (
                                             LINE_WIDTH - 1),
                                      START_POSY + y * self.y_rate + (
                                              LINE_WIDTH - 1),
                                      self.x_rate - LINE_WIDTH,
                                      self.y_rate - LINE_WIDTH])
        self.random_data = self.screen.get_buffer().raw

    def create_config_life(self):
        """Rendering config grid"""
        colors: dict = json.load(open('Files/json_files/colors.json'))
        bg: tuple = hex2rgb(colors['empty'])

        for row in range(self.width // self.x_rate):
            for col in range(self.height // self.y_rate):
                pygame.draw.rect(self.screen, bg,
                                 [col * self.x_rate + (
                                         LINE_WIDTH - 1),
                                  row * self.y_rate + (
                                          LINE_WIDTH - 1),
                                  self.x_rate - LINE_WIDTH,
                                  self.y_rate - LINE_WIDTH])
        self.config_data = Game.config_data = self.screen.get_buffer().raw

    def unload_config_life(self, a: list):
        """Unload config life from scv file"""
        self.reset()
        for cell_list_i in a:
            cell_list = []
            for cell_list_j in cell_list_i:
                x, y, alive = cell_list_j
                cell = Cell(x, y, alive)
                cell_list.append(cell)
            CellGrid.cells.append(cell_list)

    def show_config_life(self, row: int, col: int):
        """Rendering Cell when open Redactor with config grid"""
        colors: dict = json.load(open('Files/json_files/colors.json'))
        color_of_life: tuple = hex2rgb(colors['live'])
        bg: tuple = hex2rgb(colors['empty'])
        if self.cells.cells[row][col].is_alive:
            pygame.draw.rect(self.screen, color_of_life,
                             [col * self.x_rate + (
                                     LINE_WIDTH - 1),
                              row * self.y_rate + (
                                      LINE_WIDTH - 1),
                              self.x_rate - LINE_WIDTH,
                              self.y_rate - LINE_WIDTH])
        else:
            pygame.draw.rect(self.screen, bg,
                             [col * self.x_rate + (
                                     LINE_WIDTH - 1),
                              row * self.y_rate + (
                                      LINE_WIDTH - 1),
                              self.x_rate - LINE_WIDTH,
                              self.y_rate - LINE_WIDTH])
        self.config_data = Game.config_data = self.screen.get_buffer().raw

    def reset(self):
        """Update the CellGrid"""
        self.cells.reset()
