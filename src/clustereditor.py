# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clustereditor.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_EditorWindow(object):
    def setupUi(self, EditorWindow):
        if not EditorWindow.objectName():
            EditorWindow.setObjectName(u"EditorWindow")
        EditorWindow.resize(800, 600)
        self.centralwidget = QWidget(EditorWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.scrollAreaLayers = QScrollArea(self.centralwidget)
        self.scrollAreaLayers.setObjectName(u"scrollAreaLayers")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaLayers.sizePolicy().hasHeightForWidth())
        self.scrollAreaLayers.setSizePolicy(sizePolicy)
        self.scrollAreaLayers.setMinimumSize(QSize(150, 0))
        self.scrollAreaLayers.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollAreaLayers.setWidgetResizable(True)
        self.scrollAreaLayersContents = QWidget()
        self.scrollAreaLayersContents.setObjectName(u"scrollAreaLayersContents")
        self.scrollAreaLayersContents.setGeometry(QRect(0, 0, 148, 548))
        self.verticalLayout = QVBoxLayout(self.scrollAreaLayersContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollAreaLayers.setWidget(self.scrollAreaLayersContents)

        self.gridLayout_2.addWidget(self.scrollAreaLayers, 1, 1, 1, 1)

        self.mergeButton = QPushButton(self.centralwidget)
        self.mergeButton.setObjectName(u"mergeButton")

        self.gridLayout_2.addWidget(self.mergeButton, 0, 1, 1, 1)

        self.imageFrame = QFrame(self.centralwidget)
        self.imageFrame.setObjectName(u"imageFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.imageFrame.sizePolicy().hasHeightForWidth())
        self.imageFrame.setSizePolicy(sizePolicy1)
        self.imageFrame.setFrameShape(QFrame.StyledPanel)
        self.imageFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.imageFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.imageLabel = QLabel(self.imageFrame)
        self.imageLabel.setObjectName(u"imageLabel")
        self.imageLabel.setMinimumSize(QSize(300, 300))
        self.imageLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.imageLabel, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.imageFrame, 0, 0, 2, 1)

        EditorWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(EditorWindow)

        QMetaObject.connectSlotsByName(EditorWindow)
    # setupUi

    def retranslateUi(self, EditorWindow):
        EditorWindow.setWindowTitle(QCoreApplication.translate("EditorWindow", u"Cluster Editor", None))
        self.mergeButton.setText(QCoreApplication.translate("EditorWindow", u"Merge", None))
        self.imageLabel.setText(QCoreApplication.translate("EditorWindow", u"Layer", None))
    # retranslateUi

