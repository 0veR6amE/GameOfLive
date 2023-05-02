import json
import sqlite3
import sys
from typing import NoReturn

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication

from PY.CONS import ROOT_DIR
from PY.mainMenu import MainMenu

try:
    colors = json.load(
        open(r'Files/json_files/colors.json'))
except FileNotFoundError:
    colors_dict = {'empty': '#000000',
                   'live': '#ffffff',
                   'line': 'ff00ff'}
    json.dump(colors_dict,
              open(r'Files/json_files/colors.json', 'w+'))

try:
    f = json.load(
        open(r'Files/json_files/PreStart_config.json',
             'r'))
except FileNotFoundError:
    setting = {'SizeOfField': 50, 'SizeOfWindow': 840, 'speed': 15}
    json.dump(setting, open(
        r'Files/json_files/PreStart_config.json', 'w+'))

try:
    f = json.load(
        open(r'Files/json_files/config.json', 'r'))
except FileNotFoundError:
    setting = {'SizeOfField': 50, 'SizeOfWindow': 840, 'speed': 15}
    json.dump(setting,
              open(r'Files/json_files/config.json', 'w+'))

conn = sqlite3.connect(r'Files/databases/matrixes.sqllite')
cur = conn.cursor()
try:
    cur.execute("""Select * from main""")
except sqlite3.OperationalError:
    cur.executescript("""
    PRAGMA foreign_keys = off;
    BEGIN TRANSACTION;
    
    -- Таблица: main
    DROP TABLE IF EXISTS main;
    CREATE TABLE main 
    (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, 
    name STRING NOT NULL UNIQUE, 
    matrixes INT REFERENCES mat (id) UNIQUE);
    
    -- Таблица: mat
    DROP TABLE IF EXISTS mat;
    CREATE TABLE mat 
    (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, 
    size INT NOT NULL, 
    "where" STRING NOT NULL UNIQUE,
    image   STRING  UNIQUE
                NOT NULL);
    
    COMMIT TRANSACTION;
    PRAGMA foreign_keys = on;
    
    """)
conn.commit()
cur.close()

conn = sqlite3.connect(r'Files/databases/config.sqllite')
cur = conn.cursor()
try:
    cur.execute("""Select * from config""")
except sqlite3.OperationalError:
    cur.executescript("""
    PRAGMA foreign_keys = off;
    BEGIN TRANSACTION;
    
    -- Таблица: config1
    DROP TABLE IF EXISTS config;
    CREATE TABLE config (
        id       INTEGER PRIMARY KEY
                         UNIQUE
                         NOT NULL,
        name     TEXT    UNIQUE
                         NOT NULL,
        field    INTEGER NOT NULL,
        [window] INTEGER NOT NULL,
        speed    INTEGER NOT NULL
    );
    
    COMMIT TRANSACTION;
    PRAGMA foreign_keys = on;""")

conn.commit()
cur.close()


class Window(QMainWindow, MainMenu):
    """Window of my app"""
    def __init__(self) -> NoReturn:
        """Initialization of class"""
        super().__init__()
        self.setupUi(self)

    def closeEvent(self, event) -> NoReturn:
        """When window close"""
        for window in QApplication.topLevelWidgets():
            window.close()

    def keyPressEvent(self, event) -> NoReturn:
        """When was press key"""
        key = event.key()
        mode = event.modifiers()
        if int(mode) == Qt.AltModifier:
            if key == Qt.Key_F4:
                sys.exit()


def except_hook(cls, exception, traceback) -> NoReturn:
    """Except_hook"""
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = Window()
    ex.show()
    sys.exit(app.exec())
