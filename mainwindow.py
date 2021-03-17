# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(0, 554))
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.centralwidget.setAutoFillBackground(False)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(9, -1, -1, -1)
        self.imageFrame = QFrame(self.centralwidget)
        self.imageFrame.setObjectName(u"imageFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.imageFrame.sizePolicy().hasHeightForWidth())
        self.imageFrame.setSizePolicy(sizePolicy1)
        self.imageFrame.setFrameShape(QFrame.StyledPanel)
        self.imageFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.imageFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.imagePreview = QLabel(self.imageFrame)
        self.imagePreview.setObjectName(u"imagePreview")
        sizePolicy1.setHeightForWidth(self.imagePreview.sizePolicy().hasHeightForWidth())
        self.imagePreview.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(22)
        self.imagePreview.setFont(font)
        self.imagePreview.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.imagePreview, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.imageFrame, 2, 0, 1, 1)

        self.scrollAreaDst = QScrollArea(self.centralwidget)
        self.scrollAreaDst.setObjectName(u"scrollAreaDst")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scrollAreaDst.sizePolicy().hasHeightForWidth())
        self.scrollAreaDst.setSizePolicy(sizePolicy2)
        self.scrollAreaDst.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollAreaDst.setWidgetResizable(True)
        self.scrollAreaWidgetContentsDst = QWidget()
        self.scrollAreaWidgetContentsDst.setObjectName(u"scrollAreaWidgetContentsDst")
        self.scrollAreaWidgetContentsDst.setGeometry(QRect(0, 0, 386, 247))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContentsDst)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollAreaDst.setWidget(self.scrollAreaWidgetContentsDst)

        self.gridLayout.addWidget(self.scrollAreaDst, 2, 6, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(6)
        self.buttonInputDir = QPushButton(self.centralwidget)
        self.buttonInputDir.setObjectName(u"buttonInputDir")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.buttonInputDir)

        self.buttonOutputDir = QPushButton(self.centralwidget)
        self.buttonOutputDir.setObjectName(u"buttonOutputDir")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.buttonOutputDir)

        self.labelInDir = QLabel(self.centralwidget)
        self.labelInDir.setObjectName(u"labelInDir")
        sizePolicy.setHeightForWidth(self.labelInDir.sizePolicy().hasHeightForWidth())
        self.labelInDir.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelInDir)

        self.labelOutDir = QLabel(self.centralwidget)
        self.labelOutDir.setObjectName(u"labelOutDir")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.labelOutDir.sizePolicy().hasHeightForWidth())
        self.labelOutDir.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.labelOutDir)

        self.labelClusterCount = QLabel(self.centralwidget)
        self.labelClusterCount.setObjectName(u"labelClusterCount")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.labelClusterCount)

        self.labelRunCount = QLabel(self.centralwidget)
        self.labelRunCount.setObjectName(u"labelRunCount")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.labelRunCount)

        self.runCount = QSpinBox(self.centralwidget)
        self.runCount.setObjectName(u"runCount")
        self.runCount.setValue(50)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.runCount)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label)

        self.maxIterCount = QSpinBox(self.centralwidget)
        self.maxIterCount.setObjectName(u"maxIterCount")
        self.maxIterCount.setMaximum(10000)
        self.maxIterCount.setValue(100)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.maxIterCount)

        self.buttonGenerate = QPushButton(self.centralwidget)
        self.buttonGenerate.setObjectName(u"buttonGenerate")
        self.buttonGenerate.setEnabled(False)
        self.buttonGenerate.setCheckable(False)
        self.buttonGenerate.setChecked(False)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.buttonGenerate)

        self.clusterCount = QSpinBox(self.centralwidget)
        self.clusterCount.setObjectName(u"clusterCount")
        self.clusterCount.setValue(4)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.clusterCount)


        self.gridLayout.addLayout(self.formLayout, 11, 6, 1, 1)

        self.scrollAreaSrc = QScrollArea(self.centralwidget)
        self.scrollAreaSrc.setObjectName(u"scrollAreaSrc")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.scrollAreaSrc.sizePolicy().hasHeightForWidth())
        self.scrollAreaSrc.setSizePolicy(sizePolicy4)
        self.scrollAreaSrc.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollAreaSrc.setWidgetResizable(True)
        self.scrollAreaWidgetContentsSrc = QWidget()
        self.scrollAreaWidgetContentsSrc.setObjectName(u"scrollAreaWidgetContentsSrc")
        self.scrollAreaWidgetContentsSrc.setGeometry(QRect(0, 0, 386, 247))
        self.horizontalLayout = QHBoxLayout(self.scrollAreaWidgetContentsSrc)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.scrollAreaSrc.setWidget(self.scrollAreaWidgetContentsSrc)

        self.gridLayout.addWidget(self.scrollAreaSrc, 11, 0, 1, 1)

        self.buttonCheckUncheck = QPushButton(self.centralwidget)
        self.buttonCheckUncheck.setObjectName(u"buttonCheckUncheck")

        self.gridLayout.addWidget(self.buttonCheckUncheck, 5, 0, 1, 1)

        self.buttonClearGenerated = QPushButton(self.centralwidget)
        self.buttonClearGenerated.setObjectName(u"buttonClearGenerated")

        self.gridLayout.addWidget(self.buttonClearGenerated, 5, 6, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.imagePreview.setText(QCoreApplication.translate("MainWindow", u"Preview", None))
        self.buttonInputDir.setText(QCoreApplication.translate("MainWindow", u"Load input directory", None))
        self.buttonOutputDir.setText(QCoreApplication.translate("MainWindow", u"Load output directory", None))
        self.labelInDir.setText("")
        self.labelOutDir.setText("")
        self.labelClusterCount.setText(QCoreApplication.translate("MainWindow", u"Cluster Count", None))
        self.labelRunCount.setText(QCoreApplication.translate("MainWindow", u"Run count", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Max iterations", None))
        self.buttonGenerate.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.clusterCount.setSuffix("")
        self.clusterCount.setPrefix("")
        self.buttonCheckUncheck.setText(QCoreApplication.translate("MainWindow", u"Select/Deselect all", None))
        self.buttonClearGenerated.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
    # retranslateUi

