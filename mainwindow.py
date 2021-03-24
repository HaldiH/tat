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
        MainWindow.resize(800, 700)
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
        self.scrollAreaDst = QScrollArea(self.centralwidget)
        self.scrollAreaDst.setObjectName(u"scrollAreaDst")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollAreaDst.sizePolicy().hasHeightForWidth())
        self.scrollAreaDst.setSizePolicy(sizePolicy1)
        self.scrollAreaDst.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollAreaDst.setWidgetResizable(True)
        self.scrollAreaWidgetContentsDst = QWidget()
        self.scrollAreaWidgetContentsDst.setObjectName(u"scrollAreaWidgetContentsDst")
        self.scrollAreaWidgetContentsDst.setGeometry(QRect(0, 0, 386, 265))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContentsDst)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollAreaDst.setWidget(self.scrollAreaWidgetContentsDst)

        self.gridLayout.addWidget(self.scrollAreaDst, 2, 6, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(6)
        self.labelClusterCount = QLabel(self.centralwidget)
        self.labelClusterCount.setObjectName(u"labelClusterCount")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.labelClusterCount.sizePolicy().hasHeightForWidth())
        self.labelClusterCount.setSizePolicy(sizePolicy2)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelClusterCount)

        self.clusterCount = QSpinBox(self.centralwidget)
        self.clusterCount.setObjectName(u"clusterCount")
        self.clusterCount.setValue(4)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.clusterCount)

        self.labelRunCount = QLabel(self.centralwidget)
        self.labelRunCount.setObjectName(u"labelRunCount")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelRunCount)

        self.runCount = QSpinBox(self.centralwidget)
        self.runCount.setObjectName(u"runCount")
        self.runCount.setValue(50)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.runCount)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label)

        self.maxIterCount = QSpinBox(self.centralwidget)
        self.maxIterCount.setObjectName(u"maxIterCount")
        self.maxIterCount.setMaximum(10000)
        self.maxIterCount.setValue(100)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.maxIterCount)

        self.buttonGenerate = QPushButton(self.centralwidget)
        self.buttonGenerate.setObjectName(u"buttonGenerate")
        self.buttonGenerate.setEnabled(False)
        self.buttonGenerate.setCheckable(False)
        self.buttonGenerate.setChecked(False)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.buttonGenerate)


        self.gridLayout.addLayout(self.formLayout, 11, 6, 1, 1)

        self.scrollAreaSrc = QScrollArea(self.centralwidget)
        self.scrollAreaSrc.setObjectName(u"scrollAreaSrc")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.scrollAreaSrc.sizePolicy().hasHeightForWidth())
        self.scrollAreaSrc.setSizePolicy(sizePolicy4)
        self.scrollAreaSrc.setMinimumSize(QSize(0, 100))
        self.scrollAreaSrc.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollAreaSrc.setWidgetResizable(True)
        self.scrollAreaWidgetContentsSrc = QWidget()
        self.scrollAreaWidgetContentsSrc.setObjectName(u"scrollAreaWidgetContentsSrc")
        self.scrollAreaWidgetContentsSrc.setGeometry(QRect(0, 0, 386, 265))
        self.horizontalLayout = QHBoxLayout(self.scrollAreaWidgetContentsSrc)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.scrollAreaSrc.setWidget(self.scrollAreaWidgetContentsSrc)

        self.gridLayout.addWidget(self.scrollAreaSrc, 11, 0, 1, 1)

        self.buttonCheckUncheck = QPushButton(self.centralwidget)
        self.buttonCheckUncheck.setObjectName(u"buttonCheckUncheck")

        self.gridLayout.addWidget(self.buttonCheckUncheck, 5, 0, 1, 1)

        self.buttonClearGenerated = QPushButton(self.centralwidget)
        self.buttonClearGenerated.setObjectName(u"buttonClearGenerated")
        self.buttonClearGenerated.setMinimumSize(QSize(20, 0))

        self.gridLayout.addWidget(self.buttonClearGenerated, 5, 6, 1, 1)

        self.buttonInputDir = QPushButton(self.centralwidget)
        self.buttonInputDir.setObjectName(u"buttonInputDir")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.buttonInputDir.sizePolicy().hasHeightForWidth())
        self.buttonInputDir.setSizePolicy(sizePolicy5)

        self.gridLayout.addWidget(self.buttonInputDir, 3, 6, 1, 1)

        self.buttonOutputDir = QPushButton(self.centralwidget)
        self.buttonOutputDir.setObjectName(u"buttonOutputDir")
        sizePolicy5.setHeightForWidth(self.buttonOutputDir.sizePolicy().hasHeightForWidth())
        self.buttonOutputDir.setSizePolicy(sizePolicy5)

        self.gridLayout.addWidget(self.buttonOutputDir, 4, 6, 1, 1)

        self.imageFrame = QFrame(self.centralwidget)
        self.imageFrame.setObjectName(u"imageFrame")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.imageFrame.sizePolicy().hasHeightForWidth())
        self.imageFrame.setSizePolicy(sizePolicy6)
        self.imageFrame.setFrameShape(QFrame.StyledPanel)
        self.imageFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.imageFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.imagePreview = QLabel(self.imageFrame)
        self.imagePreview.setObjectName(u"imagePreview")
        sizePolicy.setHeightForWidth(self.imagePreview.sizePolicy().hasHeightForWidth())
        self.imagePreview.setSizePolicy(sizePolicy)
        self.imagePreview.setMinimumSize(QSize(300, 300))
        font = QFont()
        font.setPointSize(22)
        self.imagePreview.setFont(font)
        self.imagePreview.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.imagePreview, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.imageFrame, 2, 0, 3, 1)

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
        self.labelClusterCount.setText(QCoreApplication.translate("MainWindow", u"Cluster Count", None))
        self.clusterCount.setSuffix("")
        self.clusterCount.setPrefix("")
        self.labelRunCount.setText(QCoreApplication.translate("MainWindow", u"Run count", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Max iterations", None))
        self.buttonGenerate.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.buttonCheckUncheck.setText(QCoreApplication.translate("MainWindow", u"Select/Deselect all", None))
        self.buttonClearGenerated.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.buttonInputDir.setText(QCoreApplication.translate("MainWindow", u"Load input directory", None))
        self.buttonOutputDir.setText(QCoreApplication.translate("MainWindow", u"Load output directory", None))
        self.imagePreview.setText(QCoreApplication.translate("MainWindow", u"Preview", None))
    # retranslateUi

