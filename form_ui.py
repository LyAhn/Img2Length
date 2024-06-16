# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QLabel, QLayout, QMainWindow, QMenu,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QSplitter, QStatusBar, QWidget)

class Ui_Img2Length(object):
    def setupUi(self, Img2Length):
        if not Img2Length.objectName():
            Img2Length.setObjectName(u"Img2Length")
        Img2Length.resize(315, 219)
        Img2Length.setMinimumSize(QSize(315, 219))
        Img2Length.setMaximumSize(QSize(315, 219))
        Img2Length.setToolTipDuration(0)
        self.actionFolder_Info = QAction(Img2Length)
        self.actionFolder_Info.setObjectName(u"actionFolder_Info")
        self.actionFolder_Info.setIconVisibleInMenu(False)
        self.actionFolder_Info.setShortcutVisibleInContextMenu(False)
        self.centralwidget = QWidget(Img2Length)
        self.centralwidget.setObjectName(u"centralwidget")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(60, 140, 187, 16))
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(20, 10, 271, 92))
        self.splitter.setOrientation(Qt.Vertical)
        self.folder_label = QLabel(self.splitter)
        self.folder_label.setObjectName(u"folder_label")
        self.splitter.addWidget(self.folder_label)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout.setVerticalSpacing(8)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.unitComboBox = QComboBox(self.widget)
        self.unitComboBox.addItem("")
        self.unitComboBox.addItem("")
        self.unitComboBox.addItem("")
        self.unitComboBox.addItem("")
        self.unitComboBox.addItem("")
        self.unitComboBox.addItem("")
        self.unitComboBox.setObjectName(u"unitComboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.unitComboBox.sizePolicy().hasHeightForWidth())
        self.unitComboBox.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.unitComboBox, 0, 0, 1, 1)

        self.SubfoldersCheckBox = QCheckBox(self.widget)
        self.SubfoldersCheckBox.setObjectName(u"SubfoldersCheckBox")

        self.gridLayout.addWidget(self.SubfoldersCheckBox, 1, 0, 1, 2)

        self.converted_label = QLabel(self.widget)
        self.converted_label.setObjectName(u"converted_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.converted_label.sizePolicy().hasHeightForWidth())
        self.converted_label.setSizePolicy(sizePolicy1)
        self.converted_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.converted_label, 2, 0, 1, 2)

        self.browseButton = QPushButton(self.widget)
        self.browseButton.setObjectName(u"browseButton")
        sizePolicy.setHeightForWidth(self.browseButton.sizePolicy().hasHeightForWidth())
        self.browseButton.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.browseButton, 0, 1, 1, 1)

        self.splitter.addWidget(self.widget)
        Img2Length.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Img2Length)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 315, 21))
        self.menuInfo = QMenu(self.menubar)
        self.menuInfo.setObjectName(u"menuInfo")
        Img2Length.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Img2Length)
        self.statusbar.setObjectName(u"statusbar")
        Img2Length.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuInfo.menuAction())
        self.menuInfo.addAction(self.actionFolder_Info)

        self.retranslateUi(Img2Length)
        self.actionFolder_Info.triggered.connect(Img2Length.show)

        QMetaObject.connectSlotsByName(Img2Length)
    # setupUi

    def retranslateUi(self, Img2Length):
        Img2Length.setWindowTitle(QCoreApplication.translate("Img2Length", u"Img2Length", None))
        self.actionFolder_Info.setText(QCoreApplication.translate("Img2Length", u"Folder Info", None))
        self.folder_label.setText("")
        self.unitComboBox.setItemText(0, QCoreApplication.translate("Img2Length", u"mile", None))
        self.unitComboBox.setItemText(1, QCoreApplication.translate("Img2Length", u"meter", None))
        self.unitComboBox.setItemText(2, QCoreApplication.translate("Img2Length", u"yard", None))
        self.unitComboBox.setItemText(3, QCoreApplication.translate("Img2Length", u"km", None))
        self.unitComboBox.setItemText(4, QCoreApplication.translate("Img2Length", u"cm", None))
        self.unitComboBox.setItemText(5, QCoreApplication.translate("Img2Length", u"mm", None))

        self.unitComboBox.setCurrentText(QCoreApplication.translate("Img2Length", u"mile", None))
#if QT_CONFIG(tooltip)
        self.SubfoldersCheckBox.setToolTip(QCoreApplication.translate("Img2Length", u"*Slows down count on large number of sub-folders*", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.SubfoldersCheckBox.setStatusTip(QCoreApplication.translate("Img2Length", u"Not recommended for large subfolder counts", None))
#endif // QT_CONFIG(statustip)
        self.SubfoldersCheckBox.setText(QCoreApplication.translate("Img2Length", u"Include subfolders?", None))
        self.converted_label.setText(QCoreApplication.translate("Img2Length", u"Total Length:", None))
        self.browseButton.setText(QCoreApplication.translate("Img2Length", u"Browse", None))
        self.menuInfo.setTitle(QCoreApplication.translate("Img2Length", u"Info", None))
    # retranslateUi

