import sqlite3
from typing import NoReturn

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QLabel

from PY.CONS import ROOT_DIR


# noinspection PyAttributeOutsideInit
class SeeGrid(QWidget):
    """Class for see grid Image"""

    def __init__(self, size: int, name: bool = None) -> NoReturn:
        """Initialization of class"""
        super().__init__()
        self.setGeometry(300, 300, size - 40, size - 40)
        self.setWindowTitle('Просмотр темы')
        self.size = size - 40
        self.name = name

    def setupUi(self) -> NoReturn:
        """Setup UI"""
        self.label = QLabel(self)
        self.label.setText("")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.move(0, 0)
        self.label.resize(QSize(self.size, self.size))
        path = r'Files/databases/matrixes.sqllite'
        conn = sqlite3.connect(path)
        cur = conn.cursor()
        image_where = cur.execute(
            """select image from mat 
            where id=(select matrixes from main where name=?)""",
            (self.name,)).fetchone()[0]
        img = QImage(image_where)
        self.label.setPixmap(QPixmap(img))
