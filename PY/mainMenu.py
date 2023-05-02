from typing import NoReturn

from PyQt5.QtCore import Qt, QCoreApplication, QSize, QRect, QMetaObject
from PyQt5.QtGui import QPixmap, QFont, QCursor
from PyQt5.QtWidgets import QApplication, QSizePolicy, QFormLayout
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton

from PreStrart import PreStart
from schmesMenu import SchemesWindow
from settingMenu import SettingMenu


# noinspection PyTypeChecker,PyPep8Naming
class MainMenu(QWidget):
    """MainMenu of app"""
    def __init__(self) -> NoReturn:
        super().__init__()
        self.one = 0
        self.SettingW: SettingMenu = None
        self.SchemesW: SchemesWindow = None
        self.StartGame: PreStart = None

        self.centralwidget: QWidget = None
        self.formLayout: QFormLayout = None

        self.label: QLabel = None
        self.MW_lbl_of_creator: QLabel = None
        self.MW_setting_btn: QPushButton = None
        self.MW_schemes_btn: QPushButton = None
        self.MW_start_btn: QPushButton = None

        self.font: QFont = QFont()
        self.font.setFamily('Arial')

    def setupUi(self, MainWindow) -> NoReturn:
        """Create UI in window"""
        self.SettingW = SettingMenu()
        self.StartGame = PreStart()
        self.SchemesW = SchemesWindow(self.StartGame)

        self.MainAspectsOfWindow()
        self.createUi()
        self.repositionUi()
        self.give_cssUI()
        self.give_connectUi()
        self.retranslateUi()
        QMetaObject.connectSlotsByName(MainWindow)

    def MainAspectsOfWindow(self) -> NoReturn:
        """Create window such we need"""
        USER_WINDOW = QApplication.desktop()
        WINDOW_WIDTH = USER_WINDOW.screenGeometry().width()
        WINDOW_HEIGHT = USER_WINDOW.screenGeometry().height()

        self.setObjectName('MainWindow')
        self.setWindowTitle('GoL')
        WIDTH = 500
        HEIGHT = 500
        self.setGeometry((WINDOW_WIDTH // 2) - (WIDTH // 2),
                         (WINDOW_HEIGHT // 2) - (HEIGHT // 2), WIDTH,
                         HEIGHT)

        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.sizePolicy().hasHeightForWidth())

        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QSize(500, 500))
        self.setMaximumSize(QSize(500, 500))
        self.setSizeIncrement(QSize(500, 500))
        self.setBaseSize(QSize(500, 500))

        self.setFont(self.font)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName('centralwidget')
        self.setCentralWidget(self.centralwidget)

        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("MW_formLayout")

        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QRect(0, 0, 500, 500))
        self.label.setText('')
        self.label.setPixmap(QPixmap('Images/Squares.png'))
        self.label.setObjectName('label')
        self.formLayout.setWidget(0, QFormLayout.LabelRole,
                                  self.label)

    def createUi(self) -> NoReturn:
        """Create objects in window"""
        self.MW_start_btn = QPushButton('MW_start_btn', self.centralwidget)
        self.MW_start_btn.setObjectName('MW_start_btn')

        self.MW_setting_btn = QPushButton('MW_setting_btn', self.centralwidget)
        self.MW_setting_btn.setObjectName('MW_setting_btn')

        self.MW_schemes_btn = QPushButton('MW_schemes_btn', self.centralwidget)
        self.MW_schemes_btn.setObjectName('MW_schemes_btn')

        self.MW_lbl_of_creator = QLabel(self.centralwidget)
        self.MW_lbl_of_creator.setObjectName('MW_lbl_of_creator')

    def give_cssUI(self) -> NoReturn:
        """Do our window more nice"""

        color = 'rgb(255, 255, 255)'
        first_part = 'spread:pad, x1:0, y1:0, x2:1, y2:1'
        second_part = 'stop:0.130682 rgba(225, 0, 0, 255)'
        third_part = 'stop:1 rgba(255, 22, 255, 255)'

        self.font.setPointSize(25)
        self.MW_start_btn.setFont(self.font)
        self.MW_start_btn.setStyleSheet(
            f'background-color: qlineargradient({first_part}, {second_part},'
            f' {third_part});')
        self.MW_start_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.MW_start_btn.setMouseTracking(True)

        second_part = 'stop:0.130682 rgba(70, 0, 57, 255)'
        third_part = 'stop:1 rgba(225, 195, 255, 255)'

        self.font.setPointSize(12)
        self.MW_setting_btn.setFont(self.font)
        self.MW_setting_btn.setStyleSheet(
            f'background-color: qlineargradient({first_part}, {second_part},'
            f' {third_part});\n color: {color};')
        self.MW_setting_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.MW_setting_btn.setMouseTracking(True)

        self.font.setPointSize(12)
        self.MW_schemes_btn.setFont(self.font)
        self.MW_schemes_btn.setStyleSheet(
            f'background-color: qlineargradient({first_part}, {second_part},'
            f' {third_part});\n color: {color};')
        self.MW_schemes_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.MW_schemes_btn.setMouseTracking(True)

        self.font.setPointSize(10)
        self.MW_lbl_of_creator.setFont(self.font)
        self.MW_lbl_of_creator.setStyleSheet(
            f'background-color: rgb(0, 0, 0);\n color: {color};')

    def start(self) -> NoReturn:
        """Open PreStart window"""
        if self.one == 0:
            self.StartGame.PreStart_setupUi()
            self.one += 1
        self.StartGame.show()

    def setting(self) -> NoReturn:
        """Open Setting Window"""
        self.SettingW.SettingMenu_setupUi()
        self.SettingW.show()

    def schemes(self) -> NoReturn:
        """Open Schemes window"""
        self.SchemesW.show()

    def connected(self) -> NoReturn:
        """Helper func of connect UI"""
        name = self.sender().objectName()
        if name == 'MW_start_btn':
            self.start()
        elif name == 'MW_setting_btn':
            self.setting()
        elif name == 'MW_schemes_btn':
            self.schemes()

    # noinspection PyUnresolvedReferences
    def give_connectUi(self) -> NoReturn:
        """Connect UI"""
        self.MW_start_btn.clicked.connect(self.connected)
        self.MW_setting_btn.clicked.connect(self.connected)
        self.MW_schemes_btn.clicked.connect(self.connected)

    def reposition_MW_start_btn(self, sizePolicy: QSizePolicy) -> NoReturn:
        """Reposition UI"""
        self.MW_start_btn.setGeometry(QRect(290, 340, 200, 150))
        sizePolicy.setHeightForWidth(
            self.MW_start_btn.sizePolicy().hasHeightForWidth())
        self.MW_start_btn.setSizePolicy(sizePolicy)
        self.MW_start_btn.setMinimumSize(QSize(200, 150))
        self.MW_start_btn.setMaximumSize(QSize(200, 150))
        self.MW_start_btn.setSizeIncrement(QSize(150, 100))
        self.MW_start_btn.setBaseSize(QSize(150, 100))

    def reposition_MW_setting_btn(self, sizePolicy: QSizePolicy) -> NoReturn:
        """Reposition UI"""
        self.MW_setting_btn.setGeometry(QRect(290, 310, 200, 25))
        sizePolicy.setHeightForWidth(
            self.MW_setting_btn.sizePolicy().hasHeightForWidth())
        self.MW_setting_btn.setSizePolicy(sizePolicy)
        self.MW_setting_btn.setMinimumSize(QSize(200, 25))
        self.MW_setting_btn.setMaximumSize(QSize(200, 25))
        self.MW_setting_btn.setSizeIncrement(QSize(200, 25))
        self.MW_setting_btn.setBaseSize(QSize(200, 25))

    def reposition_MW_schemes_btn(self, sizePolicy: QSizePolicy) -> NoReturn:
        """Reposition UI"""
        self.MW_schemes_btn.setGeometry(QRect(290, 280, 200, 25))
        sizePolicy.setHeightForWidth(
            self.MW_schemes_btn.sizePolicy().hasHeightForWidth())
        self.MW_schemes_btn.setSizePolicy(sizePolicy)
        self.MW_schemes_btn.setMinimumSize(QSize(200, 25))
        self.MW_schemes_btn.setMaximumSize(QSize(200, 25))
        self.MW_schemes_btn.setSizeIncrement(QSize(200, 25))
        self.MW_schemes_btn.setBaseSize(QSize(200, 25))

    def reposition_MW_lbl_of_creator(self, sizePolicy: QSizePolicy) -> NoReturn:
        """Reposition UI"""
        self.MW_lbl_of_creator.setGeometry(QRect(6, 474, 100, 20))
        sizePolicy.setHeightForWidth(
            self.MW_lbl_of_creator.sizePolicy().hasHeightForWidth())
        self.MW_lbl_of_creator.setSizePolicy(sizePolicy)
        self.MW_lbl_of_creator.setMinimumSize(QSize(100, 20))
        self.MW_lbl_of_creator.setMaximumSize(QSize(100, 20))
        self.MW_lbl_of_creator.setSizeIncrement(QSize(101, 20))
        self.MW_lbl_of_creator.setBaseSize(QSize(100, 20))

    def repositionUi(self) -> NoReturn:
        """Reposition UI"""
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.reposition_MW_start_btn(sizePolicy)
        self.reposition_MW_setting_btn(sizePolicy)
        self.reposition_MW_schemes_btn(sizePolicy)
        self.reposition_MW_lbl_of_creator(sizePolicy)

    def retranslateUi(self) -> NoReturn:
        """Retranslate UI"""
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate('MainWindow', 'GoL'))
        self.MW_start_btn.setText(_translate('MainWindow', 'Start'))
        self.MW_setting_btn.setText(_translate('MainWindow', 'Settings'))
        self.MW_schemes_btn.setText(_translate('MainWindow', 'Schemes'))
        self.MW_lbl_of_creator.setText(
            _translate('MainWindow', 'Manannikov Oleg'))
