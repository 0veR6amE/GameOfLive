import json
import sys
from typing import NoReturn, Tuple

from PyQt5.QtCore import QCoreApplication, QSize, QMetaObject, Qt, QRect
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtWidgets import QWidget, QColorDialog, QLabel, QFormLayout, \
    QComboBox, QPushButton, QSizePolicy, QGridLayout

from PY.CONS import ROOT_DIR
from error import WrongValueIn_hex2rgb, WrongLenIn_hex2rgb


# noinspection PyTypeChecker
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


# noinspection PyTypeChecker,PyPep8Naming,PyUnresolvedReferences
class SettingMenu(QWidget):
    """Class of Setting window"""

    def __init__(self):
        """Initialization of class"""
        super().__init__()
        self.page_now = 0
        self.pages = {0: 'gui'}

        self.font = QFont()
        self.font.setFamily('Arial')

    # noinspection PyAttributeOutsideInit
    def SettingMenu_setupUi(self) -> NoReturn:
        """Setup UI"""
        colors = json.load(open('Files/json_files/colors.json'))
        self.Empty_color_rgb = hex2rgb(colors['empty'])
        self.Live_color_rgb = hex2rgb(colors['live'])
        self.Line_color_rgb = hex2rgb(colors['line'])
        self.Empty_color_hex = colors['empty']
        self.Live_color_hex = colors['live']
        self.Line_color_hex = colors['line']

        self.MainAspectsofWindow()

        if self.page_now == 0:
            self.GUI()
        QMetaObject.connectSlotsByName(self)

    def MainAspectsofWindow(self) -> NoReturn:
        """Window"""
        self.setObjectName("SettingW")
        self.resize(190, 145)

        sizePolicy = QSizePolicy(QSizePolicy.Fixed,
                                 QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(190)
        sizePolicy.setVerticalStretch(145)
        sizePolicy.setHeightForWidth(
            self.sizePolicy().hasHeightForWidth())

        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QSize(190, 145))
        self.setMaximumSize(QSize(190, 145))
        self.setSizeIncrement(QSize(190, 145))
        self.setBaseSize(QSize(190, 145))

        self.setFont(self.font)

    def GUI(self) -> NoReturn:
        def create_Layots() -> NoReturn:
            """Create Layouts"""
            self.formLayoutWidget = QWidget(self)
            self.formLayoutWidget.setGeometry(QRect(0, 0, 190, 150))
            self.formLayoutWidget.setObjectName("formLayoutWidget")

            self.main_form = QFormLayout(self.formLayoutWidget)
            self.main_form.setContentsMargins(5, 5, 5, 5)
            self.main_form.setObjectName("main_form")

            self.GUI_up_menu = QGridLayout()
            self.GUI_up_menu.setObjectName("GUI_up_menu")
            self.main_form.setLayout(0, QFormLayout.LabelRole,
                                     self.GUI_up_menu)

            self.GUI_down_menu = QFormLayout()
            self.GUI_down_menu.setObjectName("GUI_down_menu")
            self.main_form.setLayout(1, QFormLayout.LabelRole,
                                     self.GUI_down_menu)

        def createUi() -> NoReturn:
            """Crete UI"""
            self.GUI_up_name = QLabel(self)
            self.GUI_up_name.setObjectName("GUI_up_name")
            self.GUI_up_menu.addWidget(self.GUI_up_name, 0, 1, 1, 1)

            self.GUI_up_right_btn = QPushButton(self)
            self.GUI_up_right_btn.setObjectName("GUI_up_right_btn")
            self.GUI_up_menu.addWidget(self.GUI_up_right_btn, 0, 2, 1, 1)

            self.GUI_up_left_btn = QPushButton(self)
            self.GUI_up_left_btn.setObjectName("GUI_up_left_btn")
            self.GUI_up_menu.addWidget(self.GUI_up_left_btn, 0, 0, 1, 1)

            self.GUI_down_lang_lbl = QLabel(self)
            self.GUI_down_lang_lbl.setObjectName("GUI_down_lang_lbl")
            self.GUI_down_menu.setWidget(1, QFormLayout.LabelRole,
                                         self.GUI_down_lang_lbl)
            self.GUI_down_languages_box = QComboBox(self)
            self.GUI_down_languages_box.setObjectName("GUI_down_languages_box")
            self.GUI_down_menu.setWidget(1, QFormLayout.FieldRole,
                                         self.GUI_down_languages_box)
            self.GUI_down_Live_color_lbl = QLabel(self)
            self.GUI_down_Live_color_lbl.setObjectName(
                "GUI_down_Live_color_lbl")
            self.GUI_down_menu.setWidget(2, QFormLayout.LabelRole,
                                         self.GUI_down_Live_color_lbl)
            self.GUI_down_Line_color_lbl = QLabel(self)
            self.GUI_down_Line_color_lbl.setObjectName(
                "GUI_down_Line_color_lbl")
            self.GUI_down_menu.setWidget(4, QFormLayout.LabelRole,
                                         self.GUI_down_Line_color_lbl)
            self.GUI_down_Line_color_btn = QPushButton(self)
            self.GUI_down_Line_color_btn.setObjectName(
                "GUI_down_Line_color_btn")
            self.GUI_down_menu.setWidget(4, QFormLayout.FieldRole,
                                         self.GUI_down_Line_color_btn)
            self.GUI_down_Empty_color_lbl = QLabel(self)
            self.GUI_down_Empty_color_lbl.setObjectName(
                "GUI_down_Empty_color_lbl")
            self.GUI_down_menu.setWidget(3, QFormLayout.LabelRole,
                                         self.GUI_down_Empty_color_lbl)

            self.GUI_down_Empty_color_btn = QPushButton(self)
            self.GUI_down_Empty_color_btn.setObjectName(
                "GUI_down_Empty_color_btn")
            self.GUI_down_menu.setWidget(3, QFormLayout.FieldRole,
                                         self.GUI_down_Empty_color_btn)

            self.GUI_down_Live_color_btn = QPushButton(self)
            self.GUI_down_Live_color_btn.setObjectName(
                "GUI_down_Live_color_btn")
            self.GUI_down_menu.setWidget(2, QFormLayout.FieldRole,
                                         self.GUI_down_Live_color_btn)

        def repositionUi() -> NoReturn:
            """Reposition UI"""
            self.GUI_up_name.setMinimumSize(QSize(115, 20))

            self.GUI_up_right_btn.setMaximumSize(QSize(25, 25))

            self.GUI_up_left_btn.setMaximumSize(QSize(25, 25))

            self.GUI_down_lang_lbl.setMinimumSize(QSize(56, 0))

            self.GUI_down_languages_box.setMinimumSize(QSize(115, 22))
            self.GUI_down_languages_box.setMaximumSize(QSize(115, 22))

            self.GUI_down_Live_color_lbl.setMinimumSize(QSize(56, 0))

            self.GUI_down_Line_color_lbl.setMinimumSize(QSize(56, 0))

            self.GUI_down_Line_color_btn.setMaximumSize(QSize(20, 20))

            self.GUI_down_Empty_color_lbl.setMinimumSize(QSize(56, 0))

            self.GUI_down_Empty_color_btn.setMaximumSize(QSize(20, 20))

            self.GUI_down_Live_color_btn.setMaximumSize(QSize(20, 20))

        def give_cssUI() -> NoReturn:
            """Give SCC UI"""
            self.font.setPointSize(13)
            self.GUI_up_name.setFont(self.font)
            self.GUI_up_name.setAlignment(Qt.AlignCenter)

            self.font.setPointSize(15)
            self.GUI_up_right_btn.setFont(self.font)

            self.font.setPointSize(15)
            self.GUI_up_left_btn.setFont(self.font)

            self.font.setPointSize(10)
            self.GUI_down_lang_lbl.setFont(self.font)
            self.GUI_down_lang_lbl.setAlignment(Qt.AlignCenter)

            self.font.setPointSize(12)
            self.GUI_down_Live_color_lbl.setFont(self.font)
            self.GUI_down_Live_color_lbl.setAlignment(Qt.AlignCenter)

            self.font.setPointSize(12)
            self.GUI_down_Line_color_lbl.setFont(self.font)
            self.GUI_down_Line_color_lbl.setAlignment(Qt.AlignCenter)

            self.font.setPointSize(11)
            self.GUI_down_Empty_color_lbl.setFont(self.font)
            self.GUI_down_Empty_color_lbl.setLayoutDirection(Qt.LeftToRight)
            self.GUI_down_Empty_color_lbl.setLineWidth(100)
            self.GUI_down_Empty_color_lbl.setAlignment(Qt.AlignCenter)
            self.GUI_down_Empty_color_btn.setStyleSheet(
                f'background-color:  rgb{self.Empty_color_rgb}')
            self.GUI_down_Live_color_btn.setStyleSheet(
                f'background-color:  rgb{self.Live_color_rgb}')
            self.GUI_down_Line_color_btn.setStyleSheet(
                f'background-color:  rgb{self.Line_color_rgb}')

        def give_connectUi() -> NoReturn:
            """Give connect UI"""
            languages = {'Russian': ''}
            self.GUI_down_languages_box.addItems(languages.keys())
            self.GUI_down_languages_box.setCurrentText('English')

            self.GUI_down_Empty_color_btn.clicked.connect(change_color_empty)
            self.GUI_down_Live_color_btn.clicked.connect(change_color_live)
            self.GUI_down_Line_color_btn.clicked.connect(change_color_line)

        def change_color_empty() -> NoReturn:
            """Change color for empty color"""
            _color = self.Empty_color_hex
            dlg = QColorDialog(self)
            if _color:
                dlg.setCurrentColor(QColor(_color))
            if dlg.exec_():
                setColorEmpty(dlg.currentColor().name(), _color)

        def setColorEmpty(color, _color) -> NoReturn:
            """Set color"""
            if color != _color:
                _color = color
            if _color:
                self.sender().setStyleSheet("background-color: %s;" % _color)
                self.Empty_color_hex = _color
                colors_dict = {
                    'empty': self.Empty_color_hex,
                    'live': self.Live_color_hex,
                    'line': self.Line_color_hex}
                json.dump(colors_dict,
                          open(r'Files/json_files/colors.json', 'w+'))

        def change_color_live() -> NoReturn:
            """Change color for live color"""
            _color = self.Live_color_hex
            dlg = QColorDialog(self)
            if _color:
                dlg.setCurrentColor(QColor(_color))
            if dlg.exec_():
                setColorLive(dlg.currentColor().name(), _color)

        def setColorLive(color, _color) -> NoReturn:
            """Set color"""
            if color != _color:
                _color = color
            if _color:
                self.sender().setStyleSheet("background-color: %s;" % _color)
                self.Live_color_hex = _color
                colors_dict = {'empty': self.Empty_color_hex,
                               'live': self.Live_color_hex,
                               'line': self.Line_color_hex}
                json.dump(colors_dict,
                          open(r'Files/json_files/colors.json', 'w+'))

        def change_color_line() -> NoReturn:
            """Change color for line color"""
            _color = self.Line_color_hex
            dlg = QColorDialog(self)
            if _color:
                dlg.setCurrentColor(QColor(_color))
            if dlg.exec_():
                setColorLine(dlg.currentColor().name(), _color)

        def setColorLine(color, _color) -> NoReturn:
            """Set color"""
            if color != _color:
                _color = color
            if _color:
                self.sender().setStyleSheet("background-color: %s;" % _color)
                self.Line_color_hex = _color
                colors_dict = {'empty': self.Empty_color_hex,
                               'live': self.Live_color_hex,
                               'line': self.Line_color_hex}
                json.dump(colors_dict,
                          open(r'Files/json_files/colors.json', 'w+'))

        def retranslateUi() -> NoReturn:
            """Retranslate UI"""
            _translate = QCoreApplication.translate
            self.setWindowTitle(_translate("SettingW_form", "Setting"))
            self.GUI_up_left_btn.setText(_translate("SettingW_form", "<"))
            self.GUI_up_right_btn.setText(_translate("SettingW_form", ">"))
            self.GUI_up_name.setText(_translate("SettingW_form", "gui"))
            self.GUI_down_lang_lbl.setText(
                _translate("SettingW_form", "Language"))
            self.GUI_down_Live_color_lbl.setText(
                _translate("SettingW_form", "Live"))
            self.GUI_down_Empty_color_lbl.setText(
                _translate("SettingW_form", "Empty"))
            self.GUI_down_Line_color_lbl.setText(
                _translate("SettingW_form", "Line"))

        create_Layots()
        createUi()
        repositionUi()
        give_cssUI()
        give_connectUi()
        retranslateUi()
