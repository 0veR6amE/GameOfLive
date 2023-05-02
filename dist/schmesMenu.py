import json
import sqlite3
from typing import NoReturn, Union, Dict

from PyQt5.QtCore import QMetaObject, QCoreApplication, QSize, QRect, Qt
from PyQt5.QtGui import QFont, QImage
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QSpinBox

from PY.CONS import ROOT_DIR
from PY.cell import CellGrid
from bdWindow import Schemes_BaseDate
from error import Error
from startGame import StartGame


# noinspection PyTypeChecker,PyPep8Naming,PyUnresolvedReferences
class SchemesWindow(QWidget):
    """Class of Schemes window"""
    text = None
    choose = False

    def __init__(self, PreStart_window) -> NoReturn:
        """Initialization of class"""
        super().__init__()

        self.settings = json.load(
            open(r'Files/json_files/PreStart_config.json',
                 'r'))

        self.font = QFont()
        self.font.setFamily("Arial")

        self.PreStart_window = PreStart_window
        self.start_game: StartGame = StartGame()
        self.bd_bd: Schemes_BaseDate = Schemes_BaseDate(self.unload_from_csv,
                                                        self.start_csv_game)
        self.errors = Error()

        self.Schem_layout: QVBoxLayout = None
        self.Set_name_layout: QHBoxLayout = None
        self.SizeOfMap_layout: QHBoxLayout = None
        self.Create_Scheme_layout: QHBoxLayout = None

        self.see_db_btn: QPushButton = None
        self.Create_Scheme_Create_btn: QPushButton = None
        self.Create_Scheme_Save_btn: QPushButton = None
        self.Create_Scheme_resume: QPushButton = None
        self.see_db_btn: QPushButton = None
        self.name_question_lbl: QLabel = None
        self.SizeOfField_lbl: QLabel = None
        self.msg_lbl: QLabel = None
        self.SizeOfField_spinbox: QSpinBox = None
        self.Set_name_line: QLineEdit = None

        self.setObjectName("Scheme")
        self.resize(190, 160)
        self.setFont(self.font)
        self.widget = QWidget(self)
        self.widget.setGeometry(QRect(0, 0, 190, 160))
        self.widget.setObjectName("widget")

        self.create_layouts()
        self.createUi()
        self.give_CSS()
        self.connectUi()
        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

    def new(self) -> NoReturn:
        """Open Redactor"""
        self.start_game.Schemes_startGame(self.SizeOfField_spinbox.value())
        self.start_game.SchemesMenu_setupUi()

    @staticmethod
    def save_into_csv(name: str) -> NoReturn:
        """Save file into csv"""
        text = ''
        a = []
        for i in CellGrid.cells:
            txt = []
            for j in range(CellGrid.x):
                txt.append(i[j].__str__())
            a.append(txt)
        for f in a:
            rows = ''
            for i, j, k in f:
                rows += "{}, {}, {}".format(i, j, k) + ';'
            text += (str(rows)) + '\n'
        with open(name, 'w+') as f:
            f.write(text)

    def save_image(self, name: str,
                   config_file: Union[Dict[str, int]] = None) -> NoReturn:
        """Save image"""
        buffer = self.start_game.config_data
        img = QImage(buffer, config_file['SizeOfWindow'] - 40,
                     config_file['SizeOfWindow'] - 40, QImage.Format_RGB32)
        img.save(name)

    def see_bd(self) -> NoReturn:
        """see bd"""
        self.hide()
        self.bd_bd.setupUi()
        self.bd_bd.create_bd()
        self.bd_bd.show()

    def return_name(self) -> str:
        """Return name"""
        self.bd_bd.setupUi()
        self.bd_bd.create_bd()
        name = self.bd_bd.return_name()
        return name

    def save_into_db(self,
                     config_file: Union[Dict[str, int]] = None) -> NoReturn:
        """Save scheme into db"""
        name = self.Set_name_line.text()
        if name != '' and name.isalnum():
            where_csv = r'Files/matrixes/csv/{}.csv'.format(
                                                               name.capitalize())
            where_img = r'Files/matrixes/images/{}.png'.format(
                                                                  name.capitalize())
            path = r'Files/databases/matrixes.sqllite'
            conn = sqlite3.connect(path)
            cur = conn.cursor()
            self.save_into_csv(where_csv)
            if config_file is None:
                self.save_image(where_img, config_file=config_file)
            else:
                settings = json.load(
                    open(r'Files/json_files/PreStart_config.json', 'r'))
                self.save_image(where_img, config_file=settings)
            cur.execute(
                """INSERT INTO mat(size, "where", image) VALUES (?, ?, ?)""",
                (self.SizeOfField_spinbox.value(), where_csv, where_img,))
            cur.execute(
                """INSERT INTO main(name, matrixes) VALUES 
                (?, (select max(id) from mat))""",
                (name.capitalize(),))
            print(cur.execute("""select * from mat""").fetchall())
            conn.commit()
            cur.close()
        else:
            self.errors.scheme_ChangeName()

    def create_layouts(self) -> NoReturn:
        """Create Layouts"""
        self.Schem_layout = QVBoxLayout(self)
        self.Schem_layout.setContentsMargins(5, 5, 5, 5)
        self.Schem_layout.setObjectName("Schem_layout")

        self.Create_Scheme_layout = QHBoxLayout()
        self.Create_Scheme_layout.setObjectName("Create_Scheme_layout")
        self.Schem_layout.addLayout(self.Create_Scheme_layout)

        self.SizeOfMap_layout = QHBoxLayout()
        self.SizeOfMap_layout.setObjectName("SizeOfMap_layout")
        self.Schem_layout.addLayout(self.SizeOfMap_layout)

        self.Set_name_layout = QHBoxLayout()
        self.Set_name_layout.setObjectName("Set_name_layout")
        self.Schem_layout.addLayout(self.Set_name_layout)

    def unload_from_csv(self, name: str) -> NoReturn:
        """Unload from scv"""
        with open(r'Files/matrixes/csv/{}.csv'.format(name),
                  'r') as f:
            lines = [line.split('\n') for line in f]
            q = []
            for i in lines:
                w = []
                i = i[0].split(';')
                del i[-1]
                for j in i:
                    e = []
                    j = j.split(', ')
                    for k in range(len(j)):
                        if k != 2:
                            e.append(int(j[k]))
                        else:
                            e.append(eval(j[k]))
                    w.append(e)
                q.append(w)
            self.start_game.unload_config_life(q)

    def start_csv_game(self, name: str) -> NoReturn:
        """Start game from scv"""
        self.start_game.Schemes_start_configGame(name)
        self.start_game.game.hide()
        self.PreStart_window.update_field_view(name)
        SchemesWindow.choose = True

    def createUi(self) -> NoReturn:
        """Create UI"""
        self.Create_Scheme_Create_btn = QPushButton(self)
        self.Create_Scheme_Create_btn.setObjectName("Create_Scheme_Create_btn")
        self.Create_Scheme_layout.addWidget(self.Create_Scheme_Create_btn)

        self.Create_Scheme_resume = QPushButton(self)
        self.Create_Scheme_resume.setObjectName("Create_Scheme_resume")
        self.Create_Scheme_layout.addWidget(self.Create_Scheme_resume)

        self.Create_Scheme_Save_btn = QPushButton(self)
        self.Create_Scheme_Save_btn.setObjectName("Create_Scheme_Save")
        self.Create_Scheme_layout.addWidget(self.Create_Scheme_Save_btn)

        self.SizeOfField_lbl = QLabel(self)
        self.SizeOfField_lbl.setObjectName("SizeOfField_lbl")
        self.SizeOfMap_layout.addWidget(self.SizeOfField_lbl)

        self.SizeOfField_spinbox = QSpinBox(self)
        self.SizeOfField_spinbox.setObjectName("SizeOfField_spinbox")
        self.SizeOfMap_layout.addWidget(self.SizeOfField_spinbox)

        self.Set_name_line = QLineEdit(self)
        self.Set_name_line.setObjectName("Set_name_line")
        self.Set_name_layout.addWidget(self.Set_name_line)

        self.name_question_lbl = QLabel(self)
        self.name_question_lbl.setMinimumSize(QSize(10, 10))
        self.name_question_lbl.setMaximumSize(QSize(10, 10))
        self.name_question_lbl.setObjectName("name_question_lbl")
        self.Set_name_layout.addWidget(self.name_question_lbl)

        self.msg_lbl = QLabel(self)
        self.msg_lbl.setObjectName("msg_lbl")
        self.Schem_layout.addWidget(self.msg_lbl)

        self.see_db_btn = QPushButton(self)
        self.see_db_btn.setObjectName("see_db_btn")
        self.Schem_layout.addWidget(self.see_db_btn)

    def PreSave_into_db(self) -> NoReturn:
        """Pre save into db"""
        path = r'Files/databases/matrixes.sqllite'
        conn = sqlite3.connect(path)
        cur = conn.cursor()
        a = cur.execute("""Select name from main""").fetchall()
        next = True
        for i in range(len(a)):
            if Set_name_line.text() == a[i][0]:
                next = False
        if (self.Set_name_line.text().isalnum() and
                self.Set_name_line.text() != '' and next):
            self.save_into_db()

    def itDoesntDo(self):
        path = r'Files/databases/matrixes.sqllite'
        conn = sqlite3.connect(path)
        cur = conn.cursor()
        a = cur.execute("""Select name from main""").fetchall()
        print(a)
        for i in range(len(a)):
            print(a[i])
            if 'Fdsf' == a[i][0]:
                print('dsads')
        self.errors.scheme_itDoesnt_do()

    def connectUi(self) -> NoReturn:
        """Connect UI"""
        self.Create_Scheme_Create_btn.clicked.connect(self.new)
        self.Create_Scheme_Save_btn.clicked.connect(self.save_into_db)
        self.see_db_btn.clicked.connect(self.see_bd)
        self.Create_Scheme_resume.clicked.connect(self.itDoesntDo)

    def retranslateUi(self) -> NoReturn:
        """Retranslate UI"""
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("Scheme", "Form"))
        self.Create_Scheme_Create_btn.setText(
            _translate("Scheme", "Создать"))
        self.Create_Scheme_resume.setText(_translate("Scheme", "Продолжить"))
        self.Create_Scheme_Save_btn.setText(_translate("Scheme", "Сохранить"))
        self.SizeOfField_lbl.setText(_translate("Scheme", "Размер Поля"))
        self.name_question_lbl.setText(_translate("Scheme", "?"))
        self.see_db_btn.setText(_translate("Scheme", "Cозданные таблицы"))

    def changeSpinbox(self):
        val = self.SizeOfField_spinbox.value()
        if val < 10:
            self.SizeOfField_spinbox.setValue(10)
        elif val > 150:
            self.SizeOfField_spinbox.setValue(150)

    def give_CSS(self) -> NoReturn:
        """Give scc for UI"""
        self.font.setPointSize(9)
        self.Create_Scheme_Create_btn.setFont(self.font)

        self.font.setPointSize(9)
        self.Create_Scheme_resume.setFont(self.font)

        self.font.setPointSize(9)
        self.Create_Scheme_Save_btn.setFont(self.font)

        self.font.setPointSize(10)
        self.SizeOfField_lbl.setFont(self.font)
        self.SizeOfField_spinbox.setMaximum(10)
        self.SizeOfField_spinbox.setMaximum(150)
        self.SizeOfField_spinbox.setValue(25)
        self.SizeOfField_spinbox.valueChanged.connect(self.changeSpinbox)

        self.font.setPointSize(10)
        self.font.setBold(True)
        self.font.setWeight(75)
        self.name_question_lbl.setFont(self.font)

        self.font.setBold(False)
        self.font.setPointSize(9)
        self.see_db_btn.setFont(self.font)

        self.font.setPointSize(10)
        self.msg_lbl.setFont(self.font)
        self.msg_lbl.setText("")
        self.msg_lbl.setAlignment(Qt.AlignCenter)
