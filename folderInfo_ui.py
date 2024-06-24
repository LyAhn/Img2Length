# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'folderInfo.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QSizePolicy, QWidget)

class Ui_InfoDialog(object):
    def setupUi(self, InfoDialog):
        if not InfoDialog.objectName():
            InfoDialog.setObjectName(u"InfoDialog")
        InfoDialog.resize(400, 227)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(InfoDialog.sizePolicy().hasHeightForWidth())
        InfoDialog.setSizePolicy(sizePolicy)
        InfoDialog.setMinimumSize(QSize(400, 227))
        InfoDialog.setSizeGripEnabled(False)
        self.ttlImgLabel = QLabel(InfoDialog)
        self.ttlImgLabel.setObjectName(u"ttlImgLabel")
        self.ttlImgLabel.setGeometry(QRect(150, 50, 81, 16))
        self.ttFileSizeLabel = QLabel(InfoDialog)
        self.ttFileSizeLabel.setObjectName(u"ttFileSizeLabel")
        self.ttFileSizeLabel.setGeometry(QRect(150, 70, 81, 16))
        self.uniqueDimLabel = QLabel(InfoDialog)
        self.uniqueDimLabel.setObjectName(u"uniqueDimLabel")
        self.uniqueDimLabel.setGeometry(QRect(170, 90, 71, 16))
        self.smallResLabel = QLabel(InfoDialog)
        self.smallResLabel.setObjectName(u"smallResLabel")
        self.smallResLabel.setGeometry(QRect(170, 110, 81, 16))
        self.highResLabel = QLabel(InfoDialog)
        self.highResLabel.setObjectName(u"highResLabel")
        self.highResLabel.setGeometry(QRect(160, 130, 151, 16))
        self.widget = QWidget(InfoDialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 371, 201))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.widget.setAutoFillBackground(False)
        self.ttlCountUILabel = QLabel(self.widget)
        self.ttlCountUILabel.setObjectName(u"ttlCountUILabel")
        self.ttlCountUILabel.setGeometry(QRect(20, 40, 111, 16))
        self.ttlFileSizeUILabel = QLabel(self.widget)
        self.ttlFileSizeUILabel.setObjectName(u"ttlFileSizeUILabel")
        self.ttlFileSizeUILabel.setGeometry(QRect(20, 60, 101, 16))
        self.highResUILabel = QLabel(self.widget)
        self.highResUILabel.setObjectName(u"highResUILabel")
        self.highResUILabel.setGeometry(QRect(20, 120, 131, 16))
        self.smallResUILabel = QLabel(self.widget)
        self.smallResUILabel.setObjectName(u"smallResUILabel")
        self.smallResUILabel.setGeometry(QRect(20, 100, 141, 16))
        self.ttlUniqueUILabel = QLabel(self.widget)
        self.ttlUniqueUILabel.setObjectName(u"ttlUniqueUILabel")
        self.ttlUniqueUILabel.setGeometry(QRect(20, 80, 141, 16))
        self.buttonBox = QDialogButtonBox(self.widget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(20, 160, 341, 32))
        self.buttonBox.setMaximumSize(QSize(341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)

        self.retranslateUi(InfoDialog)
        self.buttonBox.accepted.connect(InfoDialog.accept)
        self.buttonBox.rejected.connect(InfoDialog.reject)

        QMetaObject.connectSlotsByName(InfoDialog)
    # setupUi

    def retranslateUi(self, InfoDialog):
        InfoDialog.setWindowTitle(QCoreApplication.translate("InfoDialog", u"Folder Stats", None))
        self.ttlCountUILabel.setText(QCoreApplication.translate("InfoDialog", u"Total # Images:", None))
        self.ttlFileSizeUILabel.setText(QCoreApplication.translate("InfoDialog", u"Total File Size:", None))
        self.highResUILabel.setText(QCoreApplication.translate("InfoDialog", u"Highest Resolution", None))
        self.smallResUILabel.setText(QCoreApplication.translate("InfoDialog", u"Smallest Resolution:", None))
        self.ttlUniqueUILabel.setText(QCoreApplication.translate("InfoDialog", u"Unique Dimensions:", None))
    # retranslateUi

