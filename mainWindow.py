# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLCDNumber,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 381, 213))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_client = QLabel(self.layoutWidget)
        self.lbl_client.setObjectName(u"lbl_client")
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(14)
        self.lbl_client.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_client)

        self.txt_client = QLineEdit(self.layoutWidget)
        self.txt_client.setObjectName(u"txt_client")
        font1 = QFont()
        font1.setPointSize(12)
        self.txt_client.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.txt_client)

        self.lbl_description = QLabel(self.layoutWidget)
        self.lbl_description.setObjectName(u"lbl_description")
        self.lbl_description.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_description)

        self.txt_description = QLineEdit(self.layoutWidget)
        self.txt_description.setObjectName(u"txt_description")
        self.txt_description.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.txt_description)

        self.lbl_hardware = QLabel(self.layoutWidget)
        self.lbl_hardware.setObjectName(u"lbl_hardware")
        self.lbl_hardware.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lbl_hardware)

        self.txt_hardware = QLineEdit(self.layoutWidget)
        self.txt_hardware.setObjectName(u"txt_hardware")
        self.txt_hardware.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.txt_hardware)

        self.lbl_tickeNo = QLabel(self.layoutWidget)
        self.lbl_tickeNo.setObjectName(u"lbl_tickeNo")
        self.lbl_tickeNo.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lbl_tickeNo)

        self.txt_ticketNo = QLineEdit(self.layoutWidget)
        self.txt_ticketNo.setObjectName(u"txt_ticketNo")
        self.txt_ticketNo.setFont(font1)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.txt_ticketNo)

        self.lbl_startTime = QLabel(self.layoutWidget)
        self.lbl_startTime.setObjectName(u"lbl_startTime")
        self.lbl_startTime.setFont(font)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.lbl_startTime)

        self.txt_startTime = QLineEdit(self.layoutWidget)
        self.txt_startTime.setObjectName(u"txt_startTime")
        self.txt_startTime.setFont(font1)
        self.txt_startTime.setReadOnly(True)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.txt_startTime)

        self.lbl_endTime = QLabel(self.layoutWidget)
        self.lbl_endTime.setObjectName(u"lbl_endTime")
        self.lbl_endTime.setFont(font)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.lbl_endTime)

        self.txt_endTime = QLineEdit(self.layoutWidget)
        self.txt_endTime.setObjectName(u"txt_endTime")
        self.txt_endTime.setFont(font1)
        self.txt_endTime.setReadOnly(True)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.txt_endTime)

        self.lbl_duration = QLabel(self.layoutWidget)
        self.lbl_duration.setObjectName(u"lbl_duration")
        self.lbl_duration.setFont(font)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.lbl_duration)

        self.txt_duration = QLineEdit(self.layoutWidget)
        self.txt_duration.setObjectName(u"txt_duration")
        self.txt_duration.setFont(font1)
        self.txt_duration.setReadOnly(True)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.txt_duration)

        self.layoutWidget1 = QWidget(Form)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 250, 221, 29))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_start = QPushButton(self.layoutWidget1)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setFont(font1)

        self.horizontalLayout.addWidget(self.btn_start)

        self.btn_stop = QPushButton(self.layoutWidget1)
        self.btn_stop.setObjectName(u"btn_stop")
        self.btn_stop.setFont(font1)

        self.horizontalLayout.addWidget(self.btn_stop)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(250, 250, 125, 31))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lcdHours = QLCDNumber(self.widget)
        self.lcdHours.setObjectName(u"lcdHours")
        font2 = QFont()
        font2.setPointSize(14)
        self.lcdHours.setFont(font2)
        self.lcdHours.setSmallDecimalPoint(False)
        self.lcdHours.setDigitCount(2)
        self.lcdHours.setSegmentStyle(QLCDNumber.Filled)
        self.lcdHours.setProperty("value", 0.000000000000000)
        self.lcdHours.setProperty("intValue", 0)

        self.horizontalLayout_2.addWidget(self.lcdHours)

        self.lcdMinutes = QLCDNumber(self.widget)
        self.lcdMinutes.setObjectName(u"lcdMinutes")
        self.lcdMinutes.setFont(font2)
        self.lcdMinutes.setSmallDecimalPoint(False)
        self.lcdMinutes.setDigitCount(2)
        self.lcdMinutes.setSegmentStyle(QLCDNumber.Filled)
        self.lcdMinutes.setProperty("value", 0.000000000000000)

        self.horizontalLayout_2.addWidget(self.lcdMinutes)

        self.lcdSeconds = QLCDNumber(self.widget)
        self.lcdSeconds.setObjectName(u"lcdSeconds")
        self.lcdSeconds.setFont(font2)
        self.lcdSeconds.setSmallDecimalPoint(False)
        self.lcdSeconds.setDigitCount(2)
        self.lcdSeconds.setSegmentStyle(QLCDNumber.Filled)
        self.lcdSeconds.setProperty("value", 0.000000000000000)

        self.horizontalLayout_2.addWidget(self.lcdSeconds)

        QWidget.setTabOrder(self.txt_client, self.txt_description)
        QWidget.setTabOrder(self.txt_description, self.txt_hardware)
        QWidget.setTabOrder(self.txt_hardware, self.txt_ticketNo)
        QWidget.setTabOrder(self.txt_ticketNo, self.txt_startTime)
        QWidget.setTabOrder(self.txt_startTime, self.txt_endTime)
        QWidget.setTabOrder(self.txt_endTime, self.txt_duration)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Ticket Timer", None))
        self.lbl_client.setText(QCoreApplication.translate("Form", u"Client", None))
        self.lbl_description.setText(QCoreApplication.translate("Form", u"Description", None))
        self.lbl_hardware.setText(QCoreApplication.translate("Form", u"Hardware", None))
        self.lbl_tickeNo.setText(QCoreApplication.translate("Form", u"Ticket No.", None))
        self.lbl_startTime.setText(QCoreApplication.translate("Form", u"Start time", None))
        self.txt_startTime.setInputMask("")
        self.lbl_endTime.setText(QCoreApplication.translate("Form", u"End time", None))
        self.lbl_duration.setText(QCoreApplication.translate("Form", u"Duration", None))
        self.btn_start.setText(QCoreApplication.translate("Form", u"Start time", None))
        self.btn_stop.setText(QCoreApplication.translate("Form", u"Stop time", None))
    # retranslateUi

