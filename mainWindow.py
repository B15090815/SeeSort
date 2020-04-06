# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(630, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(630, 300))
        MainWindow.setMaximumSize(QtCore.QSize(630, 300))
        MainWindow.setSizeIncrement(QtCore.QSize(5, 5))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(11)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ensure = QtWidgets.QPushButton(self.centralwidget)
        self.ensure.setGeometry(QtCore.QRect(360, 130, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ensure.setFont(font)
        self.ensure.setObjectName("ensure")
        self.sort_combo = QtWidgets.QComboBox(self.centralwidget)
        self.sort_combo.setGeometry(QtCore.QRect(160, 130, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sort_combo.setFont(font)
        self.sort_combo.setObjectName("sort_combo")
        self.sort_combo.addItem("")
        self.sort_combo.addItem("")
        self.sort_combo.addItem("")
        self.sort_combo.addItem("")
        self.sort_combo.addItem("")
        self.sort_combo.addItem("")
        self.sort_range = QtWidgets.QLineEdit(self.centralwidget)
        self.sort_range.setGeometry(QtCore.QRect(240, 80, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.sort_range.setFont(font)
        self.sort_range.setAlignment(QtCore.Qt.AlignCenter)
        self.sort_range.setObjectName("sort_range")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 80, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "排序可视化"))
        MainWindow.setToolTip(_translate("MainWindow", "数值大于0"))
        self.ensure.setText(_translate("MainWindow", "确定"))
        self.sort_combo.setItemText(0, _translate("MainWindow", "选择排序"))
        self.sort_combo.setItemText(1, _translate("MainWindow", "插入排序"))
        self.sort_combo.setItemText(2, _translate("MainWindow", "冒泡排序"))
        self.sort_combo.setItemText(3, _translate("MainWindow", "堆排序"))
        self.sort_combo.setItemText(4, _translate("MainWindow", "归并排序"))
        self.sort_combo.setItemText(5, _translate("MainWindow", "快速排序"))
        self.sort_range.setText(_translate("MainWindow", "50"))
        self.label.setText(_translate("MainWindow", "数组大小"))
