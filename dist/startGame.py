import json
import sqlite3
import sys
from typing import NoReturn, Union, Tuple, Dict

import pygame

from PY.CONS import ROOT_DIR
from PY.game import Game
from error import WrongValueIn_hex2rgb, WrongLenIn_hex2rgb

sys.tracebacklimit = 0


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
            # noinspection PyTypeChecker
            return rgb
        else:
            raise WrongLenIn_hex2rgb("\n \t Len of input value must be 6(six)")
    except TypeError as e:
        print(f"error was = {e}")
        raise WrongValueIn_hex2rgb(
            "Wrong type of input value. \n Value must be view "
            "as (#......), where point is one of element from "
            "the list of symbols '0123456789ABCDEF'")


# noinspection PyPep8Naming
class StartGame:
    """Class responsible for create and rendering Game"""

    was: bool = False
    is_pause: bool = False
    play: bool = False
    random_data: Union[bytes] = None
    config_data: Union[bytes] = None

    # noinspection PyTypeChecker
    def __init__(self) -> NoReturn:
        """initialization of class"""
        self.empty_cells = None
        self.settings = json.load(
            open(r'Files/json_files/PreStart_config.json',
                 'r'))
        self.game: Game = None

    @staticmethod
    def new_game() -> NoReturn:
        """New game"""
        if StartGame.was:
            pygame.quit()
            StartGame.was = False
            StartGame.is_pause = False

    def createGame(self, resume: bool = False,
                   config_file: Union[Dict[str, int]] = None,
                   size: Union[int] = None) -> NoReturn:
        """Create class Game"""
        if not resume:
            if config_file is None:
                if size is None:
                    self.game = Game(self.settings['SizeOfWindow'],
                                     self.settings['SizeOfWindow'],
                                     self.settings['SizeOfField'],
                                     self.settings['SizeOfField'])
                else:
                    self.game = Game(self.settings['SizeOfWindow'],
                                     self.settings['SizeOfWindow'],
                                     size, size)
            else:
                if size is None:
                    self.game = Game(config_file['SizeOfWindow'],
                                     config_file['SizeOfWindow'],
                                     config_file['SizeOfField'],
                                     config_file['SizeOfField'])
                else:
                    self.game = Game(config_file['SizeOfWindow'],
                                     config_file['SizeOfWindow'],
                                     size, size)

    def start_game(self, random_game: bool = True,
                   resume: bool = False,
                   schemes: bool = False,
                   name: Union[str] = None,
                   config_file: Union[Dict[str, int]] = None) -> NoReturn:
        """Helper function for start game"""
        if not schemes:
            if config_file is None:
                if not resume:
                    self.createGame()
                else:
                    self.createGame(resume=True)
            else:
                if not resume:
                    self.createGame(config_file=config_file)
                else:
                    self.createGame(resume=True, config_file=config_file)
        else:
            self.Schemes_start_configGame(name)

        if random_game and not resume:
            self.game.create_random_Grid()

        StartGame.play = True
        StartGame.was = True

    def unload_config_life(self, a: list) -> NoReturn:
        """transit function"""
        self.createGame()
        self.game.unload_config_life(a)

    def Schemes_startGame(self, size_of_map: int) -> NoReturn:
        """Helper function for start Schemes window of game"""
        self.createGame(size=size_of_map)
        self.game.re__init__()
        self.game.create_empty_Grid()

    def Schemes_start_configGame(self, name: str) -> NoReturn:
        """Helper function for start game use one of scheme"""
        path = r'Files/databases/matrixes.sqllite'
        conn = sqlite3.connect(path)
        cur = conn.cursor()
        size: int = cur.execute(
            """SELECT size FROM mat 
            WHERE id=(SELECT id FROM main WHERE name=?)""",
            (name,)).fetchone()[0]
        self.createGame(size=size)
        StartGame.play = True
        StartGame.was = True
        conn.commit()
        cur.close()

    def SchemesMenu_setupUi(self) -> NoReturn:
        """Game when open redactor scheme"""
        pygame.init()
        pygame.display.set_caption('Redactor')
        clock = pygame.time.Clock()
        self.empty_cells = Game.cells.cells
        self.game.create_config_squares_grid()
        self.play = True
        self.game.create_config_life()
        self.game.create_config_squares_grid()
        while self.play:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Game.cells.cells = self.empty_cells
                    StartGame.config_data = self.game.config_data
                    self.play = False
                    StartGame.was = True
                    pygame.display.set_mode(flags=pygame.HIDDEN)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x_mouse, y_mouse = pygame.mouse.get_pos()
                    col = x_mouse // Game.x_rate
                    row = y_mouse // Game.y_rate
                    if self.empty_cells[row][col].is_alive:
                        self.empty_cells[row][col].is_alive = False
                        self.game.show_config_life(row, col)
                    else:
                        self.empty_cells[row][col].is_alive = True
                        print(self.empty_cells[row][col].is_alive)
                        self.game.show_config_life(row, col)

            pygame.display.flip()

    def StartGame_setupUi(self, schemes=False, name=None,
                          config_file: Union[
                              Dict[str, int]] = None) -> NoReturn:
        """Start Game"""
        super().__init__()
        pygame.init()
        pygame.display.set_caption("GoL")
        pygame.display.set_mode([Game.width, Game.height], flags=pygame.SHOWN)
        pygame.display.update()
        clock = pygame.time.Clock()
        colors = json.load(
            open(r'Files/json_files/colors.json'))
        BG = hex2rgb(colors['empty'])
        if schemes:
            self.start_game(random_game=False, schemes=True, name=name)
        else:
            if config_file is None:
                if StartGame.is_pause:
                    self.start_game(resume=True)
                else:
                    self.start_game()
            else:
                if StartGame.is_pause:
                    self.start_game(resume=True, config_file=config_file)
                else:
                    self.start_game(config_file=config_file)
        a = []
        for i in self.game.cells.cells:
            a.append(i[0])
        while StartGame.play:
            self.game.screen.fill(BG)
            if config_file is None:
                clock.tick(self.settings['speed'])
            else:
                clock.tick(config_file['speed'])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    StartGame.random_data = self.game.random_data
                    StartGame.play = False
                    StartGame.is_pause = True
            self.game.cells.circulate_neighbour_count()
            self.game.cells.circulate_rule()
            self.game.create_squares_grid()
            self.game.show_random_life()
            pygame.display.flip()
        if StartGame.is_pause:
            pygame.display.set_mode(flags=pygame.HIDDEN)
        else:
            pygame.quit()
            self.game.reset()
            StartGame.was = False
            StartGame.is_pause = False
