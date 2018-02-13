# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'banges.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1051, 746)
        MainWindow.setMaximumSize(QtCore.QSize(1366, 767))
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(".designer/backup/.designer/backup/Downloads/tal.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8("QToolTip\n"
"{\n"
"     border: 1px solid black;\n"
"     background-color: #ffa02f;\n"
"     padding: 1px;\n"
"     border-radius: 3px;\n"
"     opacity: 100;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background: #444;\n"
"    border: 1px solid #000;\n"
"    background-color: QLinearGradient(\n"
"        x1:0, y1:0,\n"
"        x2:0, y2:1,\n"
"        stop:1 #212121,\n"
"        stop:0.4 #343434/*,\n"
"        stop:0.2 #343434,\n"
"        stop:0.1 #ffaa00*/\n"
"    );\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #000;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 20px 2px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #404040;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);\n"
"}\n"
"\n"
"QWidget:focus\n"
"{\n"
"    /*border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);*/\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"\n"
"     border-left-width: 0px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"     image: url(:/down_arrow.png);\n"
"}\n"
"\n"
"QGroupBox:focus\n"
"{\n"
"border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QTextEdit:focus\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"     border: 1px solid #222222;\n"
"     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"     height: 7px;\n"
"     margin: 0px 16px 0 16px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"      width: 7px;\n"
"      margin: 16px 0 16px 0;\n"
"      border: 1px solid #222222;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      height: 14px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);\n"
"      height: 14px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"color: #414141;\n"
"}\n"
"\n"
"QDockWidget::title\n"
"{\n"
"    text-align: center;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button\n"
"{\n"
"    text-align: center;\n"
"    spacing: 1px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
"{\n"
"    background: #242424;\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed\n"
"{\n"
"    padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #4c4c4c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QToolBar::handle\n"
"{\n"
"     spacing: 3px; /* spacing between items in the tool bar */\n"
"     background: url(:/images/handle.png);\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 2px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QProgressBar\n"
"{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #d7801a;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #444;\n"
"    border-bottom-style: none;\n"
"    background-color: #323232;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: -1px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
" margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
"\n"
"\n"
"    border-top-left-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    margin-top: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    /*border-top: 2px solid #ffaa00;\n"
"    padding-bottom: 3px;*/\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #ffaa00,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    width: 9px;\n"
"    height: 9px;\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover, QCheckBox::indicator:hover\n"
"{\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(:/images/checkbox.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled, QRadioButton::indicator:disabled\n"
"{\n"
"    border: 1px solid #444;\n"
"}"))
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.labelmode = QtGui.QLabel(self.centralwidget)
        self.labelmode.setObjectName(_fromUtf8("labelmode"))
        self.gridLayout.addWidget(self.labelmode, 11, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 6, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 13, 3, 1, 1)
        self.ip = QtGui.QLineEdit(self.centralwidget)
        self.ip.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.ip.setObjectName(_fromUtf8("ip"))
        self.gridLayout.addWidget(self.ip, 5, 2, 1, 1)
        self.clamp = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clamp.sizePolicy().hasHeightForWidth())
        self.clamp.setSizePolicy(sizePolicy)
        self.clamp.setMinimumSize(QtCore.QSize(194, 160))
        self.clamp.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clamp.setObjectName(_fromUtf8("clamp"))
        self.clamp.setEnabled(False)
        self.gridLayout.addWidget(self.clamp, 12, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 19, 2, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 6, 2, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 5, 0, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 8, 2, 1, 1)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.ecx = QtGui.QPushButton(self.centralwidget)
        self.ecx.setEnabled(False)
        self.ecx.setMinimumSize(QtCore.QSize(0, 75))
        self.ecx.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ecx.setObjectName(_fromUtf8("ecx"))
        self.verticalLayout_5.addWidget(self.ecx)
        self.gridLayout.addLayout(self.verticalLayout_5, 7, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 13, 0, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem8, 13, 1, 1, 1)
        spacerItem9 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem9, 20, 2, 1, 1)
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.gridLayout.addWidget(self.line_4, 21, 2, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.dcx = QtGui.QPushButton(self.centralwidget)
        self.dcx.setEnabled(False)
        self.dcx.setMinimumSize(QtCore.QSize(0, 75))
        self.dcx.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dcx.setObjectName(_fromUtf8("dcx"))
        self.verticalLayout.addWidget(self.dcx)
        self.gridLayout.addLayout(self.verticalLayout, 7, 4, 1, 1)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.connect = QtGui.QPushButton(self.centralwidget)
        self.connect.setMinimumSize(QtCore.QSize(194, 60))
        self.connect.setFocusPolicy(QtCore.Qt.NoFocus)
        self.connect.setObjectName(_fromUtf8("connect"))
        self.verticalLayout_6.addWidget(self.connect)
        self.disconnect = QtGui.QPushButton(self.centralwidget)
        self.disconnect.setEnabled(False)
        self.disconnect.setMinimumSize(QtCore.QSize(194, 60))
        self.disconnect.setFocusPolicy(QtCore.Qt.NoFocus)
        self.disconnect.setObjectName(_fromUtf8("disconnect"))
        self.verticalLayout_6.addWidget(self.disconnect)
        self.gridLayout.addLayout(self.verticalLayout_6, 7, 2, 1, 1)
        self.dclamp = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dclamp.sizePolicy().hasHeightForWidth())
        self.dclamp.setEnabled(False)
        self.dclamp.setSizePolicy(sizePolicy)
        self.dclamp.setMinimumSize(QtCore.QSize(194, 100))
        self.dclamp.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dclamp.setObjectName(_fromUtf8("dclamp"))
        self.gridLayout.addWidget(self.dclamp, 12, 4, 1, 1)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 1, 0, 1, 1)
        self.line_5 = QtGui.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.gridLayout.addWidget(self.line_5, 10, 2, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem11 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem11)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setMinimumSize(QtCore.QSize(200, 0))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_2.addWidget(self.line)
        self.lb = QtGui.QRadioButton(self.centralwidget)
        self.lb.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lb.setObjectName(_fromUtf8("lb"))
        self.verticalLayout_2.addWidget(self.lb)
        self.jb = QtGui.QRadioButton(self.centralwidget)
        self.jb.setFocusPolicy(QtCore.Qt.NoFocus)
        self.jb.setObjectName(_fromUtf8("jb"))
        self.verticalLayout_2.addWidget(self.jb)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.sl = QtGui.QSlider(self.centralwidget)
        self.sl.setFocusPolicy(QtCore.Qt.NoFocus)
        self.sl.setMaximum(100)
        self.sl.setOrientation(QtCore.Qt.Horizontal)
        self.sl.setTickPosition(QtGui.QSlider.TicksBelow)
        self.sl.setTickInterval(5)
        self.sl.setObjectName(_fromUtf8("sl"))
        self.verticalLayout_2.addWidget(self.sl)
        self.gridLayout.addLayout(self.verticalLayout_2, 30, 0, 1, 1)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.rld = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rld.sizePolicy().hasHeightForWidth())
        self.rld.setSizePolicy(sizePolicy)
        self.rld.setMinimumSize(QtCore.QSize(0, 40))
        self.rld.setFocusPolicy(QtCore.Qt.NoFocus)
        self.rld.setObjectName(_fromUtf8("rld"))
        self.horizontalLayout.addWidget(self.rld)
        self.slcp = QtGui.QPushButton(self.centralwidget)
        self.slcp.setMinimumSize(QtCore.QSize(0, 40))
        self.slcp.setFocusPolicy(QtCore.Qt.NoFocus)
        self.slcp.setObjectName(_fromUtf8("slcp"))
        self.horizontalLayout.addWidget(self.slcp)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout_3.addWidget(self.line_3)
        self.exitB = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitB.sizePolicy().hasHeightForWidth())
        self.exitB.setSizePolicy(sizePolicy)
        self.exitB.setMinimumSize(QtCore.QSize(0, 50))
        self.exitB.setFocusPolicy(QtCore.Qt.NoFocus)
        self.exitB.setObjectName(_fromUtf8("exitB"))
        self.verticalLayout_3.addWidget(self.exitB)
        self.gridLayout.addLayout(self.verticalLayout_3, 30, 2, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.gridLayout.addLayout(self.horizontalLayout_3, 13, 2, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.labela1 = QtGui.QLabel(self.centralwidget)
        self.labela1.setObjectName(_fromUtf8("labela1"))
        self.verticalLayout_7.addWidget(self.labela1)
        self.labela2 = QtGui.QLabel(self.centralwidget)
        self.labela2.setObjectName(_fromUtf8("labela2"))
        self.verticalLayout_7.addWidget(self.labela2)
        self.labela3 = QtGui.QLabel(self.centralwidget)
        self.labela3.setObjectName(_fromUtf8("labela3"))
        self.verticalLayout_7.addWidget(self.labela3)
        self.labela4 = QtGui.QLabel(self.centralwidget)
        self.labela4.setObjectName(_fromUtf8("labela4"))
        self.verticalLayout_7.addWidget(self.labela4)
        self.labela5 = QtGui.QLabel(self.centralwidget)
        self.labela5.setObjectName(_fromUtf8("labela5"))
        self.verticalLayout_7.addWidget(self.labela5)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.lcdNumbera1 = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumbera1.setObjectName(_fromUtf8("lcdNumbera1"))
        self.verticalLayout_9.addWidget(self.lcdNumbera1)
        self.lcdNumbera2 = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumbera2.setObjectName(_fromUtf8("lcdNumbera2"))
        self.verticalLayout_9.addWidget(self.lcdNumbera2)
        self.lcdNumbera3 = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumbera3.setObjectName(_fromUtf8("lcdNumbera3"))
        self.verticalLayout_9.addWidget(self.lcdNumbera3)
        self.lcdNumbera4 = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumbera4.setObjectName(_fromUtf8("lcdNumbera4"))
        self.verticalLayout_9.addWidget(self.lcdNumbera4)
        self.lcdNumbera5 = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumbera5.setObjectName(_fromUtf8("lcdNumbera5"))
        self.verticalLayout_9.addWidget(self.lcdNumbera5)
        self.horizontalLayout_2.addLayout(self.verticalLayout_9)
        self.gridLayout.addLayout(self.horizontalLayout_2, 12, 2, 1, 1)
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem12, 13, 4, 1, 1)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.labela2m = QtGui.QLabel(self.centralwidget)
        self.labela2m.setObjectName(_fromUtf8("labela2m"))
        self.horizontalLayout_5.addWidget(self.labela2m)
        self.lcdNumbera2m = QtGui.QLCDNumber(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumbera2m.sizePolicy().hasHeightForWidth())
        self.lcdNumbera2m.setSizePolicy(sizePolicy)
        self.lcdNumbera2m.setMinimumSize(QtCore.QSize(0, 45))
        self.lcdNumbera2m.setObjectName(_fromUtf8("lcdNumbera2m"))
        self.horizontalLayout_5.addWidget(self.lcdNumbera2m)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        spacerItem13 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem13)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(200, 50))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_4.addWidget(self.label_2)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_4.addWidget(self.label_5)
        self.gridLayout.addLayout(self.verticalLayout_4, 30, 4, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1051, 25))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)
        """QtCore.QObject.connect(self.sl, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.label.setNum)
        QtCore.QObject.connect(self.exitB, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QObject.connect(self.ecx, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.dcx.setDisabled)
        QtCore.QObject.connect(self.ecx, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.ecx.setEnabled)
        QtCore.QObject.connect(self.dcx, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.ecx.setDisabled)
        QtCore.QObject.connect(self.dcx, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.dcx.setEnabled)
        QtCore.QObject.connect(self.connect, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.connect.setEnabled)
        QtCore.QObject.connect(self.connect, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.ip.setEnabled)
        QtCore.QObject.connect(self.connect, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.ecx.setDisabled)
        QtCore.QObject.connect(self.disconnect, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.connect.setDisabled)
        QtCore.QObject.connect(self.connect, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.disconnect.setDisabled)
        QtCore.QObject.connect(self.disconnect, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.disconnect.setEnabled)
        QtCore.QObject.connect(self.disconnect, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.ip.setDisabled)
        QtCore.QObject.connect(self.disconnect, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.ecx.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)"""
	      #a = 0
        #QtCore.QObject.connect(self.axistracker, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.lcd.update)
        QtCore.QObject.connect(self.sl, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.label.setNum)
        #QtCore.QObject.connect(self.sl, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.a)
        #QtCore.QObject.connect(self.exitB, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QObject.connect(self.ecx, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.dcx.setDisabled)
        #>>QtCore.QObject.connect(self.ecx, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.ecx_2.setEnabled)
        QtCore.QObject.connect(self.ecx, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.ecx.setEnabled)
        QtCore.QObject.connect(self.dcx, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.ecx.setDisabled)
        #>>QtCore.QObject.connect(self.dcx, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.ecx_2.setDisabled)
        QtCore.QObject.connect(self.dcx, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.dcx.setEnabled)
        #>>QtCore.QObject.connect(self.ecx_2, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.ecx_2.setEnabled)
        #>>QtCore.QObject.connect(self.ecx_2, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.ecx.setEnabled)
        #>>QtCore.QObject.connect(self.dcx_2, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.dcx_2.setEnabled)
        #>>QtCore.QObject.connect(self.dcx_2, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.ecx.setDisabled)
        #>>QtCore.QObject.connect(self.dcx_2, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.ecx_2.setDisabled)
        #>>QtCore.QObject.connect(self.ecx_2, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.dcx_2.setDisabled)

        ###code for connecting radio button to ecx
        #>>QtCore.QObject.connect(self.ecx_2, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.lb.setEnabled)
        #>>QtCore.QObject.connect(self.ecx_2, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.jb.setEnabled)
        #>>QtCore.QObject.connect(self.dcx_2, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.lb.setDisabled)
        #>>QtCore.QObject.connect(self.dcx_2, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.jb.setDisabled)
        #==========================================================================================================#
        #QtCore.QObject.connect(self.disconnect, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.lb.setDisabled)
        #QtCore.QObject.connect(self.disconnect, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.jb.setDisabled)
        #QtCore.QObject.connect(self.connect, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.connect.setEnabled)
        #QtCore.QObject.connect(self.connect, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.ip.setEnabled)
        #QtCore.QObject.connect(self.connect, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.ecx.setDisabled)
        #QtCore.QObject.connect(self.connect, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.ecx_2.setDisabled)
        #QtCore.QObject.connect(self.disconnect, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.connect.setDisabled)
        #QtCore.QObject.connect(self.disconnect, QtCore.SIGNAL(_fromUtf8("clicked(bool)")),
        #QtCore.QObject.connect(self.connect, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.disconnect.setDisabled)
        #Q#tCore.QObject.connect(self.disconnect, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.disconnect.setEnabled)
        #QtCore.QObject.connect(self.disconnect, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.ip.setDisabled)
        ##QtCore.QObject.connect(self.connect, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.clamp.setDisabled)
        ##QtCore.QObject.connect(self.clamp, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.dclamp.setDisabled)
        ##QtCore.QObject.connect(self.clamp, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.clamp.setEnabled)
        ##QtCore.QObject.connect(self.dclamp, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.dclamp.setEnabled)
        ##QtCore.QObject.connect(self.dclamp, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.clamp.setDisabled)
        #>>QtCore.QObject.connect(self.disconnect, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.ecx_2.setEnabled)
        #QtCore.QObject.connect(self.disconnect, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.ecx.setEnabled)
        #>>QtCore.QObject.connect(self.disconnect, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.dcx_2.setEnabled)
        #QtCore.QObject.connect(self.disconnect, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.dcx.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #self.connect.clicked.connect(lambda: self.th_st(self.ip.text()))
        #self.connect.clicked.connect(lambda: self.cont())
        #self.disconnect.clicked.connect(lambda: self.dist())
        #self.sl.valueChanged.connect(lambda: self.th_st(self.sl.value()))
        #thread.start_new_thread(print_slider, ("thread-1",self.sl.value()))
#==========================================================================================================#

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "ControlX", None))
        self.labelmode.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Linear mode</p></body></html>", None))
        self.ip.setText(_translate("MainWindow", "192.168.0.250", None))
        self.clamp.setText(_translate("MainWindow", "Clamp", None))
        self.ecx.setText(_translate("MainWindow", "Enable GestureX", None))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">CONNECT I.P.</p></body></html>", None))
        self.dcx.setText(_translate("MainWindow", "Disable GestureX", None))
        self.connect.setText(_translate("MainWindow", "Connect", None))
        self.disconnect.setText(_translate("MainWindow", "Disconnect", None))
        self.dclamp.setText(_translate("MainWindow", "Declamp", None))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; color:#ffffff;\">Motion Parameters</span></p></body></html>", None))
        self.lb.setText(_translate("MainWindow", "Linear Mode", None))
        self.jb.setText(_translate("MainWindow", "Joint Mode", None))
        self.label.setText(_translate("MainWindow", "0", None))
        self.rld.setText(_translate("MainWindow", "Restart leapd", None))
        self.slcp.setText(_translate("MainWindow", "Start LCP", None))
        self.exitB.setText(_translate("MainWindow", "EXIT", None))
        self.labela1.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Axis 1:</p></body></html>", None))
        self.labela2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Axis 2:</p></body></html>", None))
        self.labela3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Axis 3:</p></body></html>", None))
        self.labela4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Axis 4:</p></body></html>", None))
        self.labela5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Axis 5:</p></body></html>", None))
        self.labela2m.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Axis to move:</p></body></html>", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><br/><span style=\" font-size:8pt; color:#a5a5a5;\">ver 1.01</span></p><p align=\"right\"><img src=\":/newPrefix/image.jpg\"/></p><p align=\"right\"><br/></p></body></html>", None))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:6pt;\">GreSoft</span></p></body></html>", None))

import test_rc
