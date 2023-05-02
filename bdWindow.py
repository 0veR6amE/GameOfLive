import json
import os
import shutil
import sqlite3
from typing import NoReturn

from PyQt5.QtCore import QRect, QMetaObject, QCoreApplication, QSize
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QVBoxLayout, QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QHeaderView, QAbstractItemView, QInputDialog
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QMessageBox

from PY.CONS import ROOT_DIR
from error import Error
from seeGrid import SeeGrid


# noinspection PyTypeChecker,PyPep8Naming,PyUnresolvedReferences
class Schemes_BaseDate(QWidget):
    """class to display and editing my DataBase for schemes"""
    bd_is_exist = False

    def __init__(self, scheme_func_unload_from_csv,
                 scheme_func_start_csv_game) -> NoReturn:
        """initialization of class"""
        super().__init__()
        self.count: int = None
        self.row: int = None
        self.scheme_func_unload_from_csv = scheme_func_unload_from_csv
        self.scheme_func_start_csv_game = scheme_func_start_csv_game
        self.errors: Error = Error()
        self.see_grid = SeeGrid(840)
        # Resize window
        self.setObjectName("Form")
        self.resize(325, 425)
        self.setMaximumSize(QSize(325, 425))
        self.setMinimumSize(QSize(325, 425))

        # Initialization variables
        self.widget: QWidget = None
        self.main_layout: QVBoxLayout = None
        self.btns_layout: QHBoxLayout = None
        self.table: QTableWidget = None
        # -----------------------------------------
        self.change_name_btn: QPushButton = None
        self.see_grid_btn: QPushButton = None
        self.delete_btn: QPushButton = None
        self.choose_btn: QPushButton = None

    def setupUi(self, all_func: bool = True) -> NoReturn:
        """Create UI on the window"""

        self.widget = QWidget(self)
        self.widget.setGeometry(QRect(0, 0, 325, 425))
        self.widget.setObjectName("widget")
        self.row = 0
        self.count = 0

        self.main_layout = QVBoxLayout(self.widget)
        self.main_layout.setContentsMargins(5, 5, 5, 5)
        self.main_layout.setObjectName("main_layout")
        self.table: QTableWidget = None
        self.createTable_without_bd()
        # -----------------------------------------
        self.btns_layout = QHBoxLayout()
        self.btns_layout.setObjectName("btns_layout")
        self.main_layout.addLayout(self.btns_layout)

        if all_func:
            self.all_functional()
            self.retranslateUi()
            self.connectUi()
        else:
            self.part_functional()
            self.retranslateUi(all_func=False)
            self.connectUi(all_func=False)

        QMetaObject.connectSlotsByName(self)

    def createTable_without_bd(self) -> NoReturn:
        """Create table on a window"""
        self.table = QTableWidget(self.widget)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setObjectName("table")
        self.table.setColumnCount(2)
        self.table.setRowCount(0)
        self.main_layout.addWidget(self.table)
        # -----------------------------------------
        item = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)

    def all_functional(self) -> NoReturn:
        """Help class function to get all functional"""

        self.change_name_btn = QPushButton(self.widget)
        self.change_name_btn.setObjectName("change_name_btn")
        self.btns_layout.addWidget(self.change_name_btn)

        self.see_grid_btn = QPushButton(self.widget)
        self.see_grid_btn.setObjectName("see_grid_btn")
        self.btns_layout.addWidget(self.see_grid_btn)

        self.delete_btn = QPushButton(self.widget)
        self.delete_btn.setObjectName("delete_btn")
        self.btns_layout.addWidget(self.delete_btn)

        self.main_layout.addLayout(self.btns_layout)

    def part_functional(self) -> NoReturn:
        """Help class function to get part of functional"""
        self.choose_btn = QPushButton(self)
        self.choose_btn.setObjectName("choose_btn")
        self.btns_layout.addWidget(self.choose_btn)

        self.see_grid_btn = QPushButton(self)
        self.see_grid_btn.setObjectName("see_grid_btn")
        self.btns_layout.addWidget(self.see_grid_btn)
        self.main_layout.addLayout(self.btns_layout)

    def create_bd(self) -> NoReturn:
        """Func of by display DateBase"""
        try:
            print('qwerty')
            # Connect into DateBase
            path = r'Files/databases/matrixes.sqllite'
            conn = sqlite3.connect(path)
            cur = conn.cursor()

            # Set count of row use count of elements in DateBase
            self.table.setRowCount(
                cur.execute("""SELECT max(id) from main""").fetchone()[0])

            # Add all names into TableWidget
            for i, a in enumerate(cur.execute("""SELECT name FROM main""")):
                for j, b in enumerate(a):
                    self.table.setItem(i, 0, QTableWidgetItem(str(b)))

            # Add all sizes into TableWidget
            for i, a in enumerate(cur.execute("""SELECT size FROM mat""")):
                for j, b in enumerate(a):
                    self.table.setItem(i, 1, QTableWidgetItem(str(b)))

            # Close DataBase
            conn.commit()
            cur.close()
            Schemes_BaseDate.bd_is_exist = True
            self.errors.scheme_bd_is_exist = Schemes_BaseDate.bd_is_exist

        except TypeError:
            Schemes_BaseDate.bd_is_exist = False
            self.errors.scheme_bd_is_exist = Schemes_BaseDate.bd_is_exist

    def clicked_table(self, row: int, count: int) -> NoReturn:
        """When someone clicked to the database"""
        self.row = row
        self.count = count
        print(row, count)

    def createTable(self, text: str, row: int, column: int) -> NoReturn:
        """Update name on the table and database"""
        item = self.table.item(row, column)
        last_text = item.text()
        item.setText(text)
        path = r'Files/databases/matrixes.sqllite'
        conn = sqlite3.connect(path)
        cur = conn.cursor()
        cur.execute("""Update main SET name=? where name=?""",
                    (text, last_text,))
        cur.close()
        conn.commit()
        self.create_bd()

    def showDialogChangeName(self) -> NoReturn:
        """Dialog doe change name"""
        text, ok = QInputDialog.getText(self, 'Change Name',
                                        'Enter name:')
        text = str(text).capitalize()
        if text != '' and text.isalpha():
            if ok:
                self.createTable(text, self.row, self.count)
        else:
            self.errors.scheme_ChangeName(_is='notStr')

    def change_name(self) -> NoReturn:
        """Helper function for change name"""
        if (self.row is None) or (self.count is None):
            self.errors.scheme_ChangeName()
        elif self.count == 0:
            self.showDialogChangeName()

        else:
            self.errors.scheme_ChangeName(_is='notNull')

    def func_see_grid_btn(self, row: int, column: int) -> NoReturn:
        """Function for see grid"""
        name = self.table.item(row, column).text()
        self.see_grid = SeeGrid(840, name=name)
        self.see_grid.setupUi()
        self.see_grid.show()

    def Pre_seeGrid(self) -> NoReturn:
        """Pre function for see grid"""
        if (self.row is None) or (self.count is None):
            self.errors.scheme_ChangeName()
        else:
            self.func_see_grid_btn(self.row, 0)

    def showDialogDelete(self) -> NoReturn:
        """Show Dialog delete"""
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Are you sure?")
        dlg.setText("Delete this scheme?\n"
                    "P.S. Can work incorrectly and delete all your schemes")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Question)
        button = dlg.exec()

        if button == QMessageBox.Yes:
            self.delete()
        else:
            dlg.close()

    def delete(self) -> NoReturn:
        """Delete function"""
        path = r'Files/databases/matrixes.sqllite'
        conn = sqlite3.connect(path)
        cur = conn.cursor()
        cur.execute("""DROP TABLE mat""")
        cur.execute("""DROP TABLE main""")
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
        shutil.rmtree(r"Files\matrixes")
        os.mkdir(r"Files\matrixes")
        os.mkdir(r"Files\matrixes\csv")
        os.mkdir(r"Files\matrixes\images")
        cur.close()
        conn.commit()
        self.table.setRowCount(0)

    def choose(self) -> NoReturn:
        """When we choose that we will be play"""
        text = self.table.item(self.row, 0).text().capitalize()
        self.scheme_func_unload_from_csv(text)
        self.scheme_func_start_csv_game(text)
        self.hide()

    def return_name(self) -> str:
        """Return the name of selected item"""
        return self.table.item(self.row, 0).text().capitalize()

    def PreChoose(self) -> NoReturn:
        """Pre choose function"""
        if (self.row is None) or (self.count is None):
            self.errors.scheme_ChangeName()
        else:
            self.choose()

    def connectUi(self, all_func: bool = True) -> NoReturn:
        """Connection UI"""
        self.table.cellClicked.connect(self.clicked_table)
        self.see_grid_btn.clicked.connect(self.Pre_seeGrid)
        if all_func:
            self.change_name_btn.clicked.connect(self.change_name)
            self.delete_btn.clicked.connect(self.showDialogDelete)
        else:
            self.choose_btn.clicked.connect(self.PreChoose)

    def retranslateUi(self, all_func: bool = True) -> NoReturn:
        """Func of retranslate UI"""
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Schemes"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("Form", "name"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("Form", "size"))
        # -----------------------------------------
        if all_func:
            self.change_name_btn.setText(_translate("Form", "Изменить"))
            self.see_grid_btn.setText(_translate("Form", "Посмотреть"))
            self.delete_btn.setText(_translate("Form", "Удалить"))
        else:
            self.choose_btn.setText(_translate("Form", "Использовать"))
            self.see_grid_btn.setText(_translate("Form", "Посмотреть"))


# noinspection PyUnresolvedReferences,PyTypeChecker,PyAttributeOutsideInit
class Config_BaseDate(QWidget):
    """class to display and editing my DataBase for config"""

    config_json = {"SizeOfField": 25, "SizeOfWindow": 840,
                   "speed": 9}
    load_from_config = False

    def __init__(self) -> NoReturn:
        """initialization of Class"""
        super().__init__()
        self.font = QFont()
        self.font.setFamily("Arial")

        self.row: int = None
        self.count: int = None

        self.setObjectName("Form")
        self.resize(420, 465)
        self.setFont(self.font)
        self.config_json = Config_BaseDate.config_json = {"SizeOfField": 25,
                                                          "SizeOfWindow": 880,
                                                          "speed": 10}

    def createUi(self) -> NoReturn:
        """Create UI"""
        self.widget = QWidget(self)
        self.widget.setGeometry(QRect(0, 0, 440, 465))
        self.widget.setObjectName("widget")

        self.mainLayout = QVBoxLayout(self)
        self.mainLayout.setContentsMargins(5, 5, 5, 5)
        self.mainLayout.setObjectName("mainLayout")

        self.tableWidget = QTableWidget(self)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        # -----------------------------------------
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        # -----------------------------------------
        self.mainLayout.addWidget(self.tableWidget)
        self.create_bd()
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.layout = QHBoxLayout()
        self.layout.setObjectName("layout")

        self.change_button = QPushButton(self)
        self.change_button.setObjectName("change_button")
        self.layout.addWidget(self.change_button)

        self.choose_btn = QPushButton(self)
        self.choose_btn.setObjectName("choose_btn")
        self.layout.addWidget(self.choose_btn)

        self.delete_btn = QPushButton(self)
        self.delete_btn.setObjectName("delete_btn")
        self.layout.addWidget(self.delete_btn)

        self.mainLayout.addLayout(self.layout)

        self.retranslateUi()
        self.connectUi()
        QMetaObject.connectSlotsByName(self)

    def create_CSS(self) -> NoReturn:
        """Create CSS"""
        self.font.setPointSize(10)
        self.choose_btn.setFont(self.font)

        self.font.setPointSize(10)
        self.change_button.setFont(self.font)

        self.font.setPointSize(10)
        self.delete_btn.setFont(self.font)

    def create_bd(self) -> NoReturn:
        """Func of by display DateBase"""
        try:
            print('qwerty')
            # Connect into DateBase
            path = r'Files/databases/config.sqllite'
            conn = sqlite3.connect(path)
            cur = conn.cursor()

            # Set count of row use count of elements in DateBase
            self.tableWidget.setRowCount(
                cur.execute("""SELECT max(id) from config""").fetchone()[0])

            # Add all names into TableWidget
            for i, a in enumerate(cur.execute("""SELECT name FROM config""")):
                for j, b in enumerate(a):
                    self.tableWidget.setItem(i, 0, QTableWidgetItem(str(b)))

            # Add all sizes into TableWidget
            for i, a in enumerate(cur.execute("""SELECT field FROM config""")):
                for j, b in enumerate(a):
                    self.tableWidget.setItem(i, 1, QTableWidgetItem(str(b)))

            for i, a in enumerate(
                    cur.execute("""SELECT window FROM config""")):
                for j, b in enumerate(a):
                    self.tableWidget.setItem(i, 2, QTableWidgetItem(str(b)))

            for i, a in enumerate(cur.execute("""SELECT speed FROM config""")):
                for j, b in enumerate(a):
                    self.tableWidget.setItem(i, 3, QTableWidgetItem(str(b)))

            # Close DataBase
            conn.commit()
            cur.close()

        except TypeError:
            pass

    def clicked_table(self, row: int, count: int) -> NoReturn:
        """When someone clicked to the database"""
        self.row = row
        self.count = count

    def choose_config(self) -> NoReturn:
        """When we choose config"""
        path = r'Files/databases/config.sqllite'
        conn = sqlite3.connect(path)
        cur = conn.cursor()
        item = self.tableWidget.item(self.row, 0).text()
        data = cur.execute("""select * from config where name=?""",
                           (item,)).fetchall()[0]
        print(data)
        size_of_field = data[2]
        size_of_window = data[3]
        speed = data[-1]
        config_json = Config_BaseDate.config_json = {
            "SizeOfField": size_of_field, "SizeOfWindow": size_of_window,
            "speed": speed}
        json.dump(config_json, open(r'Files/json_files/config.json', 'w+'))
        Config_BaseDate.load_from_config = True
        self.hide()

    def connectUi(self) -> NoReturn:
        """Connect UI"""
        self.tableWidget.cellClicked.connect(self.clicked_table)
        self.choose_btn.clicked.connect(self.choose_config)

    def retranslateUi(self) -> NoReturn:
        """Retranslate UI"""
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Config_window"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "size"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "window"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "speed"))
        self.change_button.setText(_translate("Form", "Изменить"))
        self.choose_btn.setText(_translate("Form", "Выбрать"))
        self.delete_btn.setText(_translate("Form", "Удалить"))
