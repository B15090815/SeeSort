# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'showGround.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(786, 548)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(widget.sizePolicy().hasHeightForWidth())
        widget.setSizePolicy(sizePolicy)
        widget.setMinimumSize(QtCore.QSize(786, 548))
        widget.setMaximumSize(QtCore.QSize(786, 548))
        widget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.show_place = QtWidgets.QGraphicsView(widget)
        self.show_place.setGeometry(QtCore.QRect(20, 110, 741, 421))
        self.show_place.setObjectName("show_place")
        self.start = QtWidgets.QPushButton(widget)
        self.start.setGeometry(QtCore.QRect(40, 30, 81, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(14)
        self.start.setFont(font)
        self.start.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start.setObjectName("start")
        self.sort_name = QtWidgets.QLabel(widget)
        self.sort_name.setGeometry(QtCore.QRect(290, 30, 171, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(22)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.sort_name.setFont(font)
        self.sort_name.setAlignment(QtCore.Qt.AlignCenter)
        self.sort_name.setObjectName("sort_name")
        self.stop = QtWidgets.QPushButton(widget)
        self.stop.setGeometry(QtCore.QRect(160, 30, 81, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(14)
        self.stop.setFont(font)
        self.stop.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stop.setObjectName("stop")

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "排序过程"))
        self.start.setText(_translate("widget", "开始"))
        self.sort_name.setText(_translate("widget", "选择排序"))
        self.stop.setText(_translate("widget", "停止"))
