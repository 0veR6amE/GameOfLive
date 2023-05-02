import json
import sqlite3
from typing import NoReturn

from PyQt5.QtCore import QCoreApplication, QSize, QRect, QMetaObject, Qt
from PyQt5.QtGui import QFont, QPixmap, QImage
from PyQt5.QtWidgets import QGridLayout, QHBoxLayout, QVBoxLayout, QLayout
from PyQt5.QtWidgets import QLabel, QPushButton, QSpinBox, QCheckBox
from PyQt5.QtWidgets import QLineEdit, QSlider, QRadioButton
from PyQt5.QtWidgets import QWidget, QSizePolicy, QApplication, QInputDialog

from PY.CONS import ROOT_DIR
from bdWindow import Schemes_BaseDate, Config_BaseDate
from schmesMenu import SchemesWindow
from startGame import StartGame
from error import Error


# noinspection PyTypeChecker,PyPep8Naming,PyUnresolvedReferences
class PreStart(QWidget):
    """Class of show Pre Start window"""

    def __init__(self) -> NoReturn:
        self.slider_speed = 0
        """initialization of class"""

        super().__init__()

        USER_WINDOW = QApplication.desktop()
        WINDOW_WIDTH = USER_WINDOW.screenGeometry().width()
        WINDOW_HEIGHT = USER_WINDOW.screenGeometry().height()

        if WINDOW_HEIGHT > WINDOW_WIDTH:
            self.small = WINDOW_WIDTH
        else:
            self.small = WINDOW_HEIGHT

        self.config_json = json.load(
            open(r'Files/json_files/PreStart_config.json'))

        self.startGame: StartGame = None
        self.scheme: SchemesWindow = None
        self.bd_bd: Schemes_BaseDate = None
        self.bd_config: Config_BaseDate = None
        self.errors: Error = Error()
        self.load_from_config = PreStart.load_from_config = False
        self.font = QFont()
        self.font.setFamily('Arial')

        self.widget: QWidget = None
        self.gridLayout: QGridLayout = None
        self.Random_config_layout: QGridLayout = None

        self.UP_Choose_way_Layout: QHBoxLayout = None
        self.UP_Choose_way_Random_Layout: QHBoxLayout = None
        self.UP_Choose_way_Config_layout: QHBoxLayout = None
        self.UP_Choose_way_Scheme_layout: QHBoxLayout = None
        self.Down_Choose_way_Layout: QHBoxLayout = None
        self.Down_Random_helper_layout: QHBoxLayout = None
        self.sys_btns_layout: QHBoxLayout = None

        self.Random_layout: QVBoxLayout = None
        self.Down_Choose_way_Scheme_layout: QVBoxLayout = None
        self.Down_Choose_way_Config_layout: QVBoxLayout = None

        self.Random_config_Speed_question_lbl: QLabel = None
        self.Random_config_SizeOfField_question_lbl: QLabel = None
        self.Random_config_SizeOfCell_question_lbl: QLabel = None
        self.Pre_Scheme_field_view_lbl: QLabel = None
        self.UP_Choose_way_Scheme_question_lbl: QLabel = None
        self.UP_Choose_way_Config_question_lbl: QLabel = None
        self.UP_Choose_way_Void_lbl_2: QLabel = None
        self.UP_Choose_way_Void_lbl: QLabel = None
        self.UP_Choose_way_Random_question_lbl: QLabel = None
        self.Random_Void_lbl: QLabel = None
        self.Random_config_SizeOfWindow_question_lbl: QLabel = None

        self.Down_Choose_way_Scheme_choose_Scheme_btn: QPushButton = None
        self.Down_Choose_way_Scheme_open_SchemeMenu_btn: QPushButton = None
        self.Down_Choose_way_Config_Download_btn: QPushButton = None
        self.Down_Choose_way_Config_Save_btn: QPushButton = None
        self.Down_Random_helper_clear_btn: QPushButton = None
        self.PreStart_easter_egg_btn: QPushButton = None
        self.sys_btns_Resume_btn: QPushButton = None
        self.sys_btns_newGame_btn: QPushButton = None
        self.sys_btns_Cancel_btn: QPushButton = None
        self.Down_Random_helper_ets: QPushButton = None

        self.UP_Choose_way_Config_radiobtn: QRadioButton = None
        self.UP_Choose_way_Scheme_radiobtn: QRadioButton = None
        self.UP_Choose_way_Random_radiobtn: QRadioButton = None

        self.Random_config_SizeOfField_checkbox: QCheckBox = None
        self.Random_config_Speed_checkbox: QCheckBox = None
        self.Random_config_SizeOfWindow_checkbox: QCheckBox = None

        self.Random_config_SizeOfField_choose_spinbox: QSpinBox = None
        self.Random_config_SizeOfWindow_choose_spinbox: QSpinBox = None

        self.Random_config_Speed_num_lineEdit: QLineEdit = None
        self.Random_progressBar: QLabel = None
        self.Random_config_Speed_slider: QSlider = None

    def PreStart_setupUi(self) -> NoReturn:
        """Setup UI of class"""
        self.startGame: StartGame = StartGame()
        self.scheme: SchemesWindow = SchemesWindow(self)
        self.bd_bd: Schemes_BaseDate = Schemes_BaseDate(
            self.scheme.unload_from_csv, self.scheme.start_csv_game)
        self.bd_config: Config_BaseDate = Config_BaseDate()

        self.MainAspectsOfWindow()
        self.createLayouts()
        self.createUi()
        self.repositionUi()
        self.give_cssUI()
        self.give_connectUi()
        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)

    def MainAspectsOfWindow(self) -> NoReturn:
        """Create window"""
        self.setObjectName("PreStart")
        self.resize(520, 430)

        sizePolicy = QSizePolicy(QSizePolicy.Preferred,
                                 QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())

        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QSize(520, 430))
        self.setMaximumSize(QSize(520, 430))
        self.widget = QWidget(self)
        self.widget.setGeometry(QRect(0, 0, 520, 430))
        self.widget.setObjectName("widget")

    def createLayouts(self) -> NoReturn:
        """Create Layouts"""
        # func_createLayot_gridLayout
        # Begin
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        # End
        # -----------------------------------------
        # func_createLayot_UP_Choose_way_Layout
        # Begin
        self.UP_Choose_way_Layout = QHBoxLayout()
        self.UP_Choose_way_Layout.setSizeConstraint(
            QLayout.SetMinimumSize)
        self.UP_Choose_way_Layout.setContentsMargins(0, 0, -1, -1)
        self.UP_Choose_way_Layout.setSpacing(10)
        self.UP_Choose_way_Layout.setObjectName("UP_Choose_way_Layout")
        self.gridLayout.addLayout(self.UP_Choose_way_Layout, 0, 0, 1, 3)

        # func_createLayot_UP_Choose_way_Random_Layout
        self.UP_Choose_way_Random_Layout = QHBoxLayout()
        self.UP_Choose_way_Random_Layout.setSpacing(0)
        self.UP_Choose_way_Random_Layout.setObjectName(
            "UP_Choose_way_Random_Layout")
        self.UP_Choose_way_Layout.addLayout(
            self.UP_Choose_way_Random_Layout)

        # func_createLayot_UP_Choose_way_Voids
        self.UP_Choose_way_Void_lbl = QLabel(self)
        self.UP_Choose_way_Void_lbl.setMinimumSize(QSize(5, 78))
        self.UP_Choose_way_Void_lbl.setMaximumSize(
            QSize(115, 16777215))
        font = QFont()
        font.setFamily("Arial")
        self.UP_Choose_way_Void_lbl.setFont(font)
        self.UP_Choose_way_Void_lbl.setObjectName(
            "UP_Choose_way_Void_lbl")
        self.UP_Choose_way_Layout.addWidget(
            self.UP_Choose_way_Void_lbl)

        self.UP_Choose_way_Void_lbl_2 = QLabel(self)
        self.UP_Choose_way_Void_lbl_2.setMinimumSize(QSize(5, 78))
        self.UP_Choose_way_Void_lbl_2.setMaximumSize(
            QSize(15, 16777215))
        font = QFont()
        font.setFamily("Arial")
        self.UP_Choose_way_Void_lbl_2.setFont(font)
        self.UP_Choose_way_Void_lbl_2.setObjectName(
            "UP_Choose_way_Void_lbl_2")
        self.UP_Choose_way_Layout.addWidget(
            self.UP_Choose_way_Void_lbl_2)

        # func_createLayot_UP_Choose_way_Config_layout
        self.UP_Choose_way_Config_layout = QHBoxLayout()
        self.UP_Choose_way_Config_layout.setContentsMargins(30, -1, -1,
                                                            -1)
        self.UP_Choose_way_Config_layout.setSpacing(0)
        self.UP_Choose_way_Config_layout.setObjectName(
            "UP_Choose_way_Config_layout")
        self.UP_Choose_way_Layout.addLayout(
            self.UP_Choose_way_Config_layout)

        # func_createLayot_UP_Choose_way_Scheme_layout
        self.UP_Choose_way_Scheme_layout = QHBoxLayout()
        self.UP_Choose_way_Scheme_layout.setContentsMargins(22, -1, -1,
                                                            -1)
        self.UP_Choose_way_Scheme_layout.setSpacing(0)
        self.UP_Choose_way_Scheme_layout.setObjectName(
            "UP_Choose_way_Scheme_layout")
        self.UP_Choose_way_Layout.addLayout(
            self.UP_Choose_way_Scheme_layout)
        # End
        # -----------------------------------------
        # func_createLayot_Down_Choose_way_Layout
        # Begin
        self.Down_Choose_way_Layout = QHBoxLayout()
        self.Down_Choose_way_Layout.setSpacing(9)
        self.Down_Choose_way_Layout.setObjectName("Down_Choose_way_Layout")
        self.gridLayout.addLayout(self.Down_Choose_way_Layout, 1, 2, 2, 1)

        # func_createLayot_Down_Choose_way_Config_layout
        self.Down_Choose_way_Config_layout = QVBoxLayout()
        self.Down_Choose_way_Config_layout.setObjectName(
            "Down_Choose_way_Config_layout")
        self.Down_Choose_way_Layout.addLayout(
            self.Down_Choose_way_Config_layout)

        # func_createLayot_Down_Choose_way_Scheme_layout
        self.Down_Choose_way_Scheme_layout = QVBoxLayout()
        self.Down_Choose_way_Scheme_layout.setObjectName(
            "Down_Choose_way_Scheme_layout")
        self.Down_Choose_way_Layout.addLayout(
            self.Down_Choose_way_Scheme_layout)
        # End
        # -----------------------------------------
        # func_createLayot_Down_Random_helper_layout
        # Begin
        self.Down_Random_helper_layout = QHBoxLayout()
        self.Down_Random_helper_layout.setObjectName(
            "Down_Random_helper_layout")
        self.gridLayout.addLayout(self.Down_Random_helper_layout, 1, 0, 1,
                                  1)
        # End
        # -----------------------------------------
        # func_createLayot_Random_layout
        # Begin
        self.Random_layout = QVBoxLayout()
        self.Random_layout.setObjectName("Random_layout")
        self.gridLayout.addLayout(self.Random_layout, 2, 0, 2, 1)

        # func_createLayot_Random_config_layout
        self.Random_config_layout = QGridLayout()
        self.Random_config_layout.setObjectName("Random_config_layout")
        self.Random_layout.addLayout(self.Random_config_layout)

        # func_createUi_other
        self.Random_config_Speed_slider = QSlider(self)
        self.Random_config_Speed_slider.setObjectName(
            "Random_config_Speed_slider")
        self.Random_layout.addWidget(self.Random_config_Speed_slider)

        self.Random_Void_lbl = QLabel(self)
        self.Random_Void_lbl.setMaximumSize(QSize(16777215, 70))
        self.Random_Void_lbl.setObjectName("Random_Void_lbl")
        self.Random_layout.addWidget(self.Random_Void_lbl)

        self.Random_progressBar = QLabel(self)
        self.Random_progressBar.setProperty("value", 24)
        self.Random_progressBar.setObjectName("Random_progressBar")
        self.Random_layout.addWidget(self.Random_progressBar)

        # func_createLayot_sys_btns_layout
        self.sys_btns_layout = QHBoxLayout()
        self.sys_btns_layout.setObjectName("sys_btns_layout")
        self.Random_layout.addLayout(self.sys_btns_layout)
        # End

    def createUi(self) -> NoReturn:
        """Create UI"""
        # createUi_gridLayout
        # Begin
        self.PreStart_easter_egg_btn = QPushButton(self)
        self.PreStart_easter_egg_btn.setObjectName(
            "PreStart_easter_egg_btn")
        self.gridLayout.addWidget(self.PreStart_easter_egg_btn, 2, 1, 1,
                                  1)

        self.Pre_Scheme_field_view_lbl = QLabel(self)
        self.Pre_Scheme_field_view_lbl.setMinimumSize(QSize(261, 261))
        self.Pre_Scheme_field_view_lbl.setMaximumSize(QSize(261, 261))
        self.Pre_Scheme_field_view_lbl.setStyleSheet(
            "background-color: rgb(85, 255, 0);")
        self.Pre_Scheme_field_view_lbl.setObjectName(
            "Pre_Scheme_field_view_lbl")
        self.gridLayout.addWidget(self.Pre_Scheme_field_view_lbl, 3, 1, 1, 2)
        # End
        # -----------------------------------------
        # func_createUi_UP_Choose_way_Layout
        # Begin

        # func_createUi_UP_Choose_way_Random_Layout
        self.UP_Choose_way_Random_radiobtn = QRadioButton(
            self)

        sizePolicy = QSizePolicy(QSizePolicy.Preferred,
                                 QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.UP_Choose_way_Random_radiobtn.sizePolicy().hasHeightForWidth()
        )
        self.UP_Choose_way_Random_radiobtn.setSizePolicy(sizePolicy)
        self.UP_Choose_way_Random_radiobtn.setMinimumSize(
            QSize(85, 76))
        self.UP_Choose_way_Random_radiobtn.setMaximumSize(
            QSize(85, 111111))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.UP_Choose_way_Random_radiobtn.setFont(font)
        self.UP_Choose_way_Random_radiobtn.setObjectName(
            "UP_Choose_way_Random_radiobtn")
        self.UP_Choose_way_Random_Layout.addWidget(
            self.UP_Choose_way_Random_radiobtn)

        self.UP_Choose_way_Random_question_lbl = QLabel(self)
        self.UP_Choose_way_Random_question_lbl.setMinimumSize(
            QSize(15, 76))
        self.UP_Choose_way_Random_question_lbl.setMaximumSize(
            QSize(15, 111111))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.UP_Choose_way_Random_question_lbl.setFont(font)
        self.UP_Choose_way_Random_question_lbl.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.UP_Choose_way_Random_question_lbl.setObjectName(
            "UP_Choose_way_Random_question_lbl")
        self.UP_Choose_way_Random_Layout.addWidget(
            self.UP_Choose_way_Random_question_lbl)

        # func_createUi_UP_Choose_way_Config_layout
        self.UP_Choose_way_Config_radiobtn = QRadioButton(self)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.UP_Choose_way_Config_radiobtn.setFont(font)
        self.UP_Choose_way_Config_radiobtn.setObjectName(
            "UP_Choose_way_Config_radiobtn")
        self.UP_Choose_way_Config_layout.addWidget(
            self.UP_Choose_way_Config_radiobtn)

        self.UP_Choose_way_Config_question_lbl = QLabel(self)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.UP_Choose_way_Config_question_lbl.setFont(font)
        self.UP_Choose_way_Config_question_lbl.setObjectName(
            "UP_Choose_way_Config_question_lbl")
        self.UP_Choose_way_Config_layout.addWidget(
            self.UP_Choose_way_Config_question_lbl)

        # func_createUi_UP_Choose_way_Scheme_layout
        self.UP_Choose_way_Scheme_radiobtn = QRadioButton(self)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.UP_Choose_way_Scheme_radiobtn.setFont(font)
        self.UP_Choose_way_Scheme_radiobtn.setObjectName(
            "UP_Choose_way_Scheme_radiobtn")
        self.UP_Choose_way_Scheme_layout.addWidget(
            self.UP_Choose_way_Scheme_radiobtn)

        self.UP_Choose_way_Scheme_question_lbl = QLabel(self)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.UP_Choose_way_Scheme_question_lbl.setFont(font)
        self.UP_Choose_way_Scheme_question_lbl.setObjectName(
            "UP_Choose_way_Scheme_question_lbl")
        self.UP_Choose_way_Scheme_layout.addWidget(
            self.UP_Choose_way_Scheme_question_lbl)
        # End
        # -----------------------------------------
        # func_createUi_Down_Choose_way_Layout
        # Begin

        # func_createUi_Down_Choose_way_Config_layout
        self.Down_Choose_way_Config_Save_btn = QPushButton(
            self)
        self.Down_Choose_way_Config_Save_btn.setObjectName(
            "Down_Choose_way_Config_Save_btn")
        self.Down_Choose_way_Config_layout.addWidget(
            self.Down_Choose_way_Config_Save_btn)

        self.Down_Choose_way_Config_Download_btn = QPushButton(
            self)
        self.Down_Choose_way_Config_Download_btn.setObjectName(
            "Down_Choose_way_Config_Download_btn")
        self.Down_Choose_way_Config_layout.addWidget(
            self.Down_Choose_way_Config_Download_btn)

        # func_createUi_Down_Choose_way_Scheme_layout
        self.Down_Choose_way_Scheme_open_SchemeMenu_btn = QPushButton(
            self)
        self.Down_Choose_way_Scheme_open_SchemeMenu_btn.setObjectName(
            "Down_Choose_way_Scheme_open_SchemeMenu_btn")
        self.Down_Choose_way_Scheme_layout.addWidget(
            self.Down_Choose_way_Scheme_open_SchemeMenu_btn)

        self.Down_Choose_way_Scheme_choose_Scheme_btn = QPushButton(
            self)
        self.Down_Choose_way_Scheme_choose_Scheme_btn.setObjectName(
            "Down_Choose_way_Scheme_choose_Scheme_btn")
        self.Down_Choose_way_Scheme_layout.addWidget(
            self.Down_Choose_way_Scheme_choose_Scheme_btn)

        # func_createUi_Down_Random_helper_layout
        self.Down_Random_helper_clear_btn = QPushButton(self)
        self.Down_Random_helper_clear_btn.setObjectName(
            "Down_Random_helper_clear_btn")
        self.Down_Random_helper_layout.addWidget(
            self.Down_Random_helper_clear_btn)

        self.Down_Random_helper_ets = QPushButton(self)
        self.Down_Random_helper_ets.setObjectName("Down_Random_helper_ets")
        self.Down_Random_helper_layout.addWidget(
            self.Down_Random_helper_ets)
        # End
        # -----------------------------------------
        # func_createUi_Random_layout
        # Begin

        # func_createUi_Random_config_layout
        self.Random_config_SizeOfWindow_choose_spinbox = QSpinBox(
            self)
        self.Random_config_SizeOfWindow_choose_spinbox.setMaximum(
            self.small)
        self.Random_config_SizeOfWindow_choose_spinbox.setObjectName(
            "Random_config_SizeOfWindow_choose_spinbox")
        self.Random_config_layout.addWidget(
            self.Random_config_SizeOfWindow_choose_spinbox, 1, 2, 1, 1)

        self.Random_config_Speed_question_lbl = QLabel(self)
        self.Random_config_Speed_question_lbl.setObjectName(
            "Random_config_Speed_question_lbl")
        self.Random_config_layout.addWidget(
            self.Random_config_Speed_question_lbl, 2, 1, 1, 1)

        self.Random_config_SizeOfField_choose_spinbox = QSpinBox(self)
        self.Random_config_SizeOfField_choose_spinbox.setMaximum(150)
        self.Random_config_SizeOfField_choose_spinbox.setObjectName(
            "Random_config_SizeOfField_choose_spinbox")
        self.Random_config_layout.addWidget(
            self.Random_config_SizeOfField_choose_spinbox, 0, 2, 1, 1)

        self.Random_config_SizeOfWindow_checkbox = QCheckBox(
            self)
        self.Random_config_SizeOfWindow_checkbox.setObjectName(
            "Random_config_SizeOfWindow_checkbox")
        self.Random_config_layout.addWidget(
            self.Random_config_SizeOfWindow_checkbox, 1, 0, 1, 1)

        self.Random_config_Speed_checkbox = QCheckBox(self)
        self.Random_config_Speed_checkbox.setObjectName(
            "Random_config_Speed_checkbox")
        self.Random_config_layout.addWidget(
            self.Random_config_Speed_checkbox, 2, 0, 1, 1)

        self.Random_config_SizeOfField_question_lbl = QLabel(
            self)
        self.Random_config_SizeOfField_question_lbl.setObjectName(
            "Random_config_SizeOfField_question_lbl")
        self.Random_config_layout.addWidget(
            self.Random_config_SizeOfField_question_lbl, 0, 1, 1, 1)

        self.Random_config_SizeOfField_checkbox = QCheckBox(
            self)
        self.Random_config_SizeOfField_checkbox.setObjectName(
            "Random_config_SizeOfField_checkbox")
        self.Random_config_layout.addWidget(
            self.Random_config_SizeOfField_checkbox, 0, 0, 1, 1)

        self.Random_config_SizeOfWindow_question_lbl = QLabel(
            self)
        self.Random_config_SizeOfWindow_question_lbl.setObjectName(
            "Random_config_SizeOfWindow_question_lbl")
        self.Random_config_layout.addWidget(
            self.Random_config_SizeOfWindow_question_lbl, 1, 1, 1, 1)

        self.Random_config_Speed_num_lineEdit = QLineEdit(
            self)
        self.Random_config_Speed_num_lineEdit.setMaximumSize(QSize(64, 16777))
        self.Random_config_Speed_num_lineEdit.setObjectName(
            "lRandom_config_Speed_num_lineEdit")
        self.Random_config_layout.addWidget(
            self.Random_config_Speed_num_lineEdit, 2, 2, 1, 1)
        # End
        # -----------------------------------------
        # func_createUi_sys_btns_layout
        # Begin
        self.sys_btns_Cancel_btn = QPushButton(self)
        self.sys_btns_Cancel_btn.setObjectName("sys_btns_Cancel_btn")
        self.sys_btns_layout.addWidget(self.sys_btns_Cancel_btn)

        self.sys_btns_newGame_btn = QPushButton(self)
        self.sys_btns_newGame_btn.setObjectName("sys_btns_newGame_btn")
        self.sys_btns_layout.addWidget(self.sys_btns_newGame_btn)

        self.sys_btns_Resume_btn = QPushButton(self)
        self.sys_btns_Resume_btn.setObjectName("sys_btns_Resume_btn")
        self.sys_btns_layout.addWidget(self.sys_btns_Resume_btn)
        # End
        self.Random_config_Speed_slider.setValue(self.config_json['speed'])
        self.slider_speed = 200 * self.Random_config_Speed_slider.value() // 60

    def update_field_view_lbl(self) -> NoReturn:
        """Update field label for random"""
        image = QImage(StartGame.random_data, self.config_json['SizeOfWindow'],
                       self.config_json['SizeOfWindow'], QImage.Format_RGB32)
        image = QPixmap(image)
        image_new = image.scaledToHeight(
            self.Pre_Scheme_field_view_lbl.size().height())
        self.Pre_Scheme_field_view_lbl.setPixmap(image_new)

    def update_field_view(self, name):
        """Update field label for config"""
        path = r'Files/databases/matrixes.sqllite'
        conn = sqlite3.connect(path)
        cur = conn.cursor()
        image_where = cur.execute(
            """select image from mat 
            where id=(select matrixes from main where name=?)""",
            (name,)).fetchone()[0]
        img = QPixmap(QImage(image_where))
        image_new = img.scaledToHeight(
            self.Pre_Scheme_field_view_lbl.size().height())
        self.Pre_Scheme_field_view_lbl.setPixmap(image_new)

    def start(self) -> NoReturn:
        """Start Game"""
        for window in QApplication.topLevelWidgets():
            window.hide()
        self.Random_config_SizeOfWindow_checkbox.setChecked(False)
        self.Random_config_SizeOfField_checkbox.setChecked(False)
        self.Random_config_Speed_checkbox.setChecked(False)
        self.checkboxes()
        print(self.bd_config.load_from_config)
        if not self.bd_config.load_from_config:
            json.dump(self.config_json,
                      open(r'Files/json_files/PreStart_config.json', 'w'))
            if not self.scheme.choose:
                if not StartGame.was:
                    StartGame.was = True
                    self.startGame.new_game()
                self.startGame.start_game(config_file=self.config_json)
                self.startGame.StartGame_setupUi(config_file=self.config_json)
                self.update_field_view_lbl()
                self.show()
            else:
                name = self.scheme.return_name()
                print(name)
                self.startGame.StartGame_setupUi(schemes=True, name=name)
                self.scheme.choose = False
        else:
            if not StartGame.was:
                StartGame.was = True
                self.startGame.new_game()
            config_json = self.bd_config.config_json
            self.startGame.start_game(config_file=config_json)
            self.startGame.StartGame_setupUi(config_file=config_json)
            self.show()

    def resume(self) -> NoReturn:
        """Resume Game"""
        if StartGame.was and StartGame.is_pause:

            json.dump(self.config_json,
                      open('Files/json_files/PreStart_config.json', 'w'))
            StartGame.play = True
            StartGame.is_pause = True
            self.hide()
            if not self.bd_config.load_from_config:
                self.startGame.StartGame_setupUi(config_file=self.config_json)
                self.update_field_view_lbl()
            else:
                config_json = self.bd_config.config_json
                self.startGame.StartGame_setupUi(config_file=config_json)
            self.show()

    def clear(self) -> NoReturn:
        """Clear pre config Game"""
        self.config_json = {"SizeOfField": 25, "SizeOfWindow": 880,
                            "speed": 9}
        self.Random_config_SizeOfWindow_checkbox.setChecked(False)
        self.Random_config_SizeOfField_checkbox.setChecked(False)
        self.Random_config_Speed_checkbox.setChecked(False)
        self.Random_config_Speed_slider.setValue(9)
        self.slider_speed = 200 * self.Random_config_Speed_slider.value() // 60
        self.update_config()

    def scheme_open(self) -> NoReturn:
        """Open Schemes"""
        self.scheme.show()

    def scheme_choose(self) -> NoReturn:
        """When Schemes was chosen"""
        self.bd_bd.setupUi(all_func=False)
        self.bd_bd.create_bd()
        self.bd_bd.show()

    def SizeOfField_spinbox_update(self) -> NoReturn:
        """Update spinbox"""
        val = self.Random_config_SizeOfField_choose_spinbox.value()
        if val < 10:
            self.Random_config_SizeOfField_choose_spinbox.setValue(10)
        elif val > 150:
            self.Random_config_SizeOfField_choose_spinbox.setValue(150)
        val = self.Random_config_SizeOfField_choose_spinbox.value()
        self.config_json['SizeOfField'] = val
        json.dump(self.config_json,
                  open(r'{Files/json_files/PreStart_config.json', 'w'))

    def SizeOfWindow_spinbox_update(self) -> NoReturn:
        """Update spinbox"""
        val = self.Random_config_SizeOfWindow_choose_spinbox.value()
        if val < 150:
            self.Random_config_SizeOfWindow_choose_spinbox.setValue(150)
        elif val > self.small:
            self.Random_config_SizeOfWindow_choose_spinbox.setValue(
                self.small)
        val = self.Random_config_SizeOfWindow_choose_spinbox.value()
        self.config_json['SizeOfWindow'] = val
        json.dump(self.config_json,
                  open(r'Files/json_files/PreStart_config.json', 'w'))

    def speed_update(self) -> NoReturn:
        """Speed update"""
        self.Random_config_Speed_num_lineEdit.setText(f'{self.slider_speed}')

    def unload_config(self, text: str) -> NoReturn:
        """Unload config file"""
        sw = self.Random_config_SizeOfWindow_choose_spinbox.value()
        sf = self.Random_config_SizeOfField_choose_spinbox.value()
        sp = int(self.Random_config_Speed_num_lineEdit.text())
        conn = sqlite3.connect(
            r'Files/databases/config.sqllite')
        cur = conn.cursor()
        cur.execute(
            """INSERT INTO config(name, field, [window], speed) 
            VALUES (?, ? ,? ,?);""",
            (text, sf, sw, sp,))
        conn.commit()
        cur.close()

    def showDialog(self) -> NoReturn:
        """Show Dialog"""
        text, ok = QInputDialog.getText(self, 'Input Dialog',
                                        'Enter name:')
        if ok:
            self.unload_config(text)

    def show_config(self) -> NoReturn:
        """Show Config"""
        self.errors.config()
        self.bd_config.show()
        self.bd_config.createUi()
        conf = self.bd_config.config_json
        self.Random_config_SizeOfWindow_choose_spinbox.setValue(
            conf['SizeOfWindow'])
        self.Random_config_SizeOfField_choose_spinbox.setValue(
            conf['SizeOfField'])
        self.Random_config_Speed_slider.setValue(conf['speed'])
        self.slider_speed = 200 * self.Random_config_Speed_slider.value() // 60
        self.Random_config_Speed_num_lineEdit.setText(
            str(self.slider_speed))

    def give_connectUi(self) -> NoReturn:
        """Give Connect UI"""
        self.sys_btns_newGame_btn.clicked.connect(self.start)
        self.sys_btns_Resume_btn.clicked.connect(self.resume)
        self.Down_Random_helper_clear_btn.clicked.connect(self.clear)

        self.UP_Choose_way_Config_radiobtn.clicked.connect(self.UP_Choose_way)
        self.UP_Choose_way_Random_radiobtn.clicked.connect(self.UP_Choose_way)
        self.UP_Choose_way_Scheme_radiobtn.clicked.connect(self.UP_Choose_way)

        self.Random_config_SizeOfWindow_checkbox.clicked.connect(
            self.checkboxes)
        self.Random_config_SizeOfField_checkbox.clicked.connect(
            self.checkboxes)
        self.Random_config_Speed_checkbox.clicked.connect(
            self.checkboxes)

        self.Random_config_SizeOfField_choose_spinbox.valueChanged.connect(
            self.SizeOfField_spinbox_update)
        self.Random_config_SizeOfWindow_choose_spinbox.valueChanged.connect(
            self.SizeOfWindow_spinbox_update)
        self.Random_config_Speed_num_lineEdit.textChanged.connect(
            self.speed_update)
        self.Random_config_Speed_slider.valueChanged.connect(
            self.change_value_slider)

        self.Down_Choose_way_Scheme_open_SchemeMenu_btn.clicked.connect(
            self.scheme_open)
        self.Down_Choose_way_Scheme_choose_Scheme_btn.clicked.connect(
            self.scheme_choose)
        self.Down_Choose_way_Config_Download_btn.clicked.connect(
            self.show_config)

        self.Down_Choose_way_Config_Save_btn.clicked.connect(self.showDialog)

    def repositionUi(self) -> NoReturn:
        """Reposition UI"""
        self.PreStart_easter_egg_btn.setMinimumSize(QSize(20, 20))
        self.PreStart_easter_egg_btn.setMaximumSize(QSize(20, 20))

    def checkboxes(self) -> NoReturn:
        """When checkbox change state"""
        StartGame.was = False
        if self.Random_config_SizeOfWindow_checkbox.isChecked():
            self.Random_config_SizeOfWindow_choose_spinbox.setEnabled(True)
            self.Random_config_SizeOfWindow_question_lbl.setEnabled(True)
        else:
            self.Random_config_SizeOfWindow_choose_spinbox.setEnabled(False)
            self.Random_config_SizeOfWindow_question_lbl.setEnabled(False)

        if self.Random_config_SizeOfField_checkbox.isChecked():
            self.Random_config_SizeOfField_choose_spinbox.setEnabled(True)
            self.Random_config_SizeOfField_question_lbl.setEnabled(True)
        else:
            self.Random_config_SizeOfField_choose_spinbox.setEnabled(False)
            self.Random_config_SizeOfField_question_lbl.setEnabled(False)

        if self.Random_config_Speed_checkbox.isChecked():
            self.Random_config_Speed_num_lineEdit.setEnabled(True)
            self.Random_config_Speed_question_lbl.setEnabled(True)
            self.Random_config_Speed_slider.setEnabled(True)
        else:
            self.Random_config_Speed_num_lineEdit.setEnabled(False)
            self.Random_config_Speed_question_lbl.setEnabled(False)
            self.Random_config_Speed_slider.setEnabled(False)

    def setDisable_Random_config_layout(self) -> NoReturn:
        """Disable_Random_config_layout"""
        self.Random_config_SizeOfWindow_checkbox.setEnabled(False)
        self.Random_config_SizeOfWindow_checkbox.setChecked(False)
        self.Random_config_SizeOfWindow_choose_spinbox.setEnabled(False)
        self.Random_config_SizeOfWindow_question_lbl.setEnabled(False)
        self.Random_config_SizeOfField_checkbox.setEnabled(False)
        self.Random_config_SizeOfField_checkbox.setChecked(False)
        self.Random_config_SizeOfField_choose_spinbox.setEnabled(False)
        self.Random_config_SizeOfField_question_lbl.setEnabled(False)
        self.Random_config_Speed_checkbox.setEnabled(False)
        self.Random_config_Speed_question_lbl.setEnabled(False)
        self.Random_config_Speed_num_lineEdit.setEnabled(False)
        self.Random_config_Speed_slider.setEnabled(False)
        self.Down_Random_helper_clear_btn.setEnabled(False)
        self.Down_Random_helper_ets.setEnabled(False)

    def setEnable_Random_config_layout(self) -> NoReturn:
        """Enable_Random_config_layout"""
        self.Random_config_SizeOfWindow_checkbox.setEnabled(True)
        self.Random_config_SizeOfWindow_question_lbl.setEnabled(True)
        self.Random_config_SizeOfField_checkbox.setEnabled(True)
        self.Random_config_SizeOfField_question_lbl.setEnabled(True)
        self.Random_config_Speed_checkbox.setEnabled(True)
        self.Random_config_Speed_question_lbl.setEnabled(True)
        self.Random_config_Speed_slider.setEnabled(True)
        self.Down_Random_helper_clear_btn.setEnabled(True)
        self.Down_Random_helper_ets.setEnabled(True)

    def UP_Choose_way(self) -> NoReturn:
        """When change radiobutons state"""
        if self.UP_Choose_way_Scheme_radiobtn.isChecked():
            self.Down_Choose_way_Scheme_choose_Scheme_btn.setEnabled(True)
            self.Down_Choose_way_Scheme_open_SchemeMenu_btn.setEnabled(True)
            self.Down_Choose_way_Config_Download_btn.setEnabled(False)
            self.Down_Choose_way_Config_Save_btn.setEnabled(False)
            self.setDisable_Random_config_layout()
            self.Random_config_Speed_checkbox.setEnabled(True)

        if self.UP_Choose_way_Config_radiobtn.isChecked():
            self.Down_Choose_way_Config_Download_btn.setEnabled(True)
            self.Down_Choose_way_Config_Save_btn.setEnabled(True)
            self.bd_config.load_from_config = True
            self.Down_Choose_way_Scheme_choose_Scheme_btn.setEnabled(False)
            self.Down_Choose_way_Scheme_open_SchemeMenu_btn.setEnabled(False)
            self.setDisable_Random_config_layout()

        if self.UP_Choose_way_Random_radiobtn.isChecked():
            self.setEnable_Random_config_layout()
            self.checkboxes()
            self.bd_config.load_from_config = False
            self.Down_Choose_way_Config_Download_btn.setEnabled(False)
            self.Down_Choose_way_Config_Save_btn.setEnabled(False)
            self.Down_Choose_way_Scheme_choose_Scheme_btn.setEnabled(False)
            self.Down_Choose_way_Scheme_open_SchemeMenu_btn.setEnabled(False)

    def change_value_slider(self, value):
        """Change value slider"""
        self.slider_speed = 200 * value // 60
        self.Random_config_Speed_num_lineEdit.setText(f'{self.slider_speed}')
        self.config_json['speed'] = value
        json.dump(self.config_json,
                  open(r'{}/Files/json_files/PreStart_config.json'.format(
                      ROOT_DIR), 'w'))

    def give_cssUI(self) -> NoReturn:
        """Give CSS UI"""
        self.Random_config_SizeOfWindow_choose_spinbox.setEnabled(False)
        self.Random_config_SizeOfWindow_question_lbl.setEnabled(False)
        self.Random_config_SizeOfField_choose_spinbox.setEnabled(False)
        self.Random_config_SizeOfField_question_lbl.setEnabled(False)
        self.Random_config_Speed_question_lbl.setEnabled(False)
        self.Random_config_Speed_num_lineEdit.setEnabled(False)
        self.Random_config_Speed_slider.setEnabled(False)

        self.Random_config_Speed_slider.setMinimum(1)
        self.Random_config_Speed_slider.setMaximum(60)
        self.UP_Choose_way_Random_radiobtn.setChecked(True)
        self.UP_Choose_way()
        self.Random_config_Speed_slider.setOrientation(Qt.Horizontal)
        self.Pre_Scheme_field_view_lbl.setAlignment(Qt.AlignCenter)
        self.Random_config_SizeOfWindow_choose_spinbox.setSingleStep(10)
        self.Random_config_SizeOfField_choose_spinbox.setSingleStep(1)
        self.update_config()

    def update_config(self) -> NoReturn:
        """Update config"""
        self.Random_config_SizeOfWindow_choose_spinbox.setValue(
            self.config_json['SizeOfWindow'])
        self.Random_config_SizeOfField_choose_spinbox.setValue(
            self.config_json['SizeOfField'])
        self.Random_config_Speed_num_lineEdit.setText(
            str(self.slider_speed))

    def retranslateUi(self) -> NoReturn:
        """Retranslate Ui"""
        self.PreStart_easter_egg_btn.setText("")
        _translate = QCoreApplication.translate

        self.setWindowTitle(_translate("PreStart", "PreStart"))
        self.Down_Random_helper_clear_btn.setText(
            _translate("PreStart", "Очистить"))
        self.Down_Random_helper_ets.setText(_translate("PreStart", "ETs"))
        self.Random_config_Speed_question_lbl.setText(
            _translate("PreStart", "?"))
        self.Random_config_SizeOfWindow_checkbox.setText(
            _translate("PreStart", "Размер окна"))
        self.Random_config_Speed_checkbox.setText(
            _translate("PreStart", "Скорость"))
        self.Random_config_SizeOfField_question_lbl.setText(
            _translate("PreStart", "?"))
        self.Random_config_SizeOfField_checkbox.setText(
            _translate("PreStart", "Размер поля"))
        self.Random_config_SizeOfWindow_question_lbl.setText(
            _translate("PreStart", "?"))
        self.Random_Void_lbl.setText(_translate("PreStart", ""))
        self.sys_btns_Cancel_btn.setText(_translate("PreStart", "Отмена"))
        self.sys_btns_newGame_btn.setText(_translate("PreStart", "Сначала"))
        self.sys_btns_Resume_btn.setText(_translate("PreStart", "Продолжить"))
        self.Down_Choose_way_Config_Save_btn.setText(
            _translate("PreStart", "Сохранить"))
        self.Down_Choose_way_Config_Download_btn.setText(
            _translate("PreStart", "Открыть"))
        self.Down_Choose_way_Scheme_open_SchemeMenu_btn.setText(
            _translate("PreStart", "В меню тем"))
        self.Down_Choose_way_Scheme_choose_Scheme_btn.setText(
            _translate("PreStart", "Выбрать тему"))
        self.UP_Choose_way_Random_radiobtn.setText(
            _translate("PreStart", "Рандомно"))
        self.UP_Choose_way_Random_question_lbl.setText(
            _translate("PreStart", "?"))
        self.UP_Choose_way_Void_lbl.setText(_translate("PreStart", ""))
        self.UP_Choose_way_Void_lbl_2.setText(
            _translate("PreStart", ""))
        self.UP_Choose_way_Config_radiobtn.setText(
            _translate("PreStart", "Конфиг"))
        self.UP_Choose_way_Config_question_lbl.setText(
            _translate("PreStart", "?"))
        self.UP_Choose_way_Scheme_radiobtn.setText(
            _translate("PreStart", "Схемы"))
        self.UP_Choose_way_Scheme_question_lbl.setText(
            _translate("PreStart", "?"))
        self.Pre_Scheme_field_view_lbl.setText(
            _translate("PreStart", "Последняя Игра"))

    def closeEvent(self, event) -> NoReturn:
        """When window was close"""
        for window in QApplication.topLevelWidgets():
            if window.__class__.__name__ == 'Window':
                window.show()
        self.close()
