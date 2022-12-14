from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(447, 623)
        MainWindow.setStyleSheet("background-color: rgb(29, 29, 29);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.push_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(14)
        sizePolicy.setHeightForWidth(self.push_7.sizePolicy().hasHeightForWidth())
        self.push_7.setSizePolicy(sizePolicy)
        self.push_7.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(157, 246, 255);\n"
"border-radius:35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"background-color: rgb(238, 238, 238);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(255, 112, 93);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.push_7.setObjectName("push_7")
        self.gridLayout.addWidget(self.push_7, 4, 0, 1, 1)
        self.push_div = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(14)
        sizePolicy.setHeightForWidth(self.push_div.sizePolicy().hasHeightForWidth())
        self.push_div.setSizePolicy(sizePolicy)
        self.push_div.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(157, 246, 255);\n"
"border-radius:35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"background-color: rgb(238, 238, 238);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(253, 255, 107);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.push_div.setObjectName("push_div")
        self.gridLayout.addWidget(self.push_div, 4, 3, 1, 1)
        self.push_0 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(14)
        sizePolicy.setHeightForWidth(self.push_0.sizePolicy().hasHeightForWidth())
        self.push_0.setSizePolicy(sizePolicy)
        self.push_0.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(157, 246, 255);\n"
"border-radius:35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"background-color: rgb(238, 238, 238);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(255, 112, 93);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.push_0.setObjectName("push_0")
        self.gridLayout.addWidget(self.push_0, 5, 0, 1, 2)
        self.push_point = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(14)
        sizePolicy.setHeightForWidth(self.push_point.sizePolicy().hasHeightForWidth())
        self.push_point.setSizePolicy(sizePolicy)
        self.push_point.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(157, 246, 255);\n"
"border-radius:35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"background-color: rgb(238, 238, 238);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(255, 112, 93);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.push_point.setObjectName("push_point")
        self.gridLayout.addWidget(self.push_point, 5, 2, 1, 1)
        self.push_equal = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(14)
        sizePolicy.setHeightForWidth(self.push_equal.sizePolicy().hasHeightForWidth())
        self.push_equal.setSizePolicy(sizePolicy)
        self.push_equal.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(157, 246, 255);\n"
"border-radius:35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"background-color: rgb(238, 238, 238);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(253, 255, 107);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.push_equal.setObjectName("push_equal")
        self.gridLayout.addWidget(self.push_equal, 5, 3, 1, 1)
        self.push_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(14)
        sizePolicy.setHeightForWidth(self.push_6.sizePolicy().hasHeightForWidth())
        self.push_6.setSizePolicy(sizePolicy)
        self.push_6.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(157, 246, 255);\n"
"border-radius:35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"background-color: rgb(238, 238, 238);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(255, 112, 93);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.push_6.setObjectName("push_6")
        self.gridLayout.addWidget(self.push_6, 3, 2, 1, 1)
        self.push_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(14)
        sizePolicy.setHeightForWidth(self.push_3.sizePolicy().hasHeightForWidth())
        self.push_3.setSizePolicy(sizePolicy)
        self.push_3.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(157, 246, 255);\n"
"border-radius:35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"background-color: rgb(238, 238, 238);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(255, 112, 93);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.push_3.setObjectName("push_3")
        self.gridLayout.addWidget(self.push_3, 2, 2, 1, 1)
        self.push_add = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(14)
        sizePolicy.setHeightForWidth(self.push_add.sizePolicy().hasHeightForWidth())
        self.push_add.setSizePolicy(sizePolicy)
        self.push_add.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(157, 246, 255);\n"
"border-radius:35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"background-color: rgb(238, 238, 238);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(253, 255, 107);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.push_add.setObjectName("push_add")
        self.gridLayout.addWidget(self.push_add, 1, 3, 1, 1)
        self.push_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(14)
        sizePolicy.setHeightForWidth(self.push_4.sizePolicy().hasHeightForWidth())
        self.push_4.setSizePolicy(sizePolicy)
        self.push_4.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(157, 246, 255);\n"
"border-radius:35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"background-color: rgb(238, 238, 238);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(255, 112, 93);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.push_4.setObjectName("push_4")
        self.gridLayout.addWidget(self.push_4, 3, 0, 1, 1)
        self.push_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(14)
        sizePolicy.setHeightForWidth(self.push_5.sizePolicy().hasHeightForWidth())
        self.push_5.setSizePolicy(sizePolicy)
        self.push_5.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(157, 246, 255);\n"
"border-radius:35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"background-color: rgb(238, 238, 238);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(255, 112, 93);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.push_5.setObjectName("push_5")
        self.gridLayout.addWidget(self.push_5, 3, 1, 1, 1)
        self.push_mul = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(14)
        sizePolicy.setHeightForWidth(self.push_mul.sizePolicy().hasHeightForWidth())
        self.push_mul.setSizePolicy(sizePolicy)
        self.push_mul.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(157, 246, 255);\n"
"border-radius:35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"background-color: rgb(238, 238, 238);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(253, 255, 107);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.push_mul.setObjectName("push_mul")
        self.gridLayout.addWidget(self.push_mul, 3, 3, 1, 1)
        self.push_sub = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(14)
        sizePolicy.setHeightForWidth(self.push_sub.sizePolicy().hasHeightForWidth())
        self.push_sub.setSizePolicy(sizePolicy)
        self.push_sub.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(157, 246, 255);\n"
"border-radius:35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"background-color: rgb(238, 238, 238);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(253, 255, 107);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.push_sub.setObjectName("push_sub")
        self.gridLayout.addWidget(self.push_sub, 2, 3, 1, 1)
        self.push_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(14)
        sizePolicy.setHeightForWidth(self.push_8.sizePolicy().hasHeightForWidth())
        self.push_8.setSizePolicy(sizePolicy)
        self.push_8.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(157, 246, 255);\n"
"border-radius:35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"background-color: rgb(238, 238, 238);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(255, 112, 93);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.push_8.setObjectName("push_8")
        self.gridLayout.addWidget(self.push_8, 4, 1, 1, 1)
        self.push_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(14)
        sizePolicy.setHeightForWidth(self.push_9.sizePolicy().hasHeightForWidth())
        self.push_9.setSizePolicy(sizePolicy)
        self.push_9.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(157, 246, 255);\n"
"border-radius:35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"background-color: rgb(238, 238, 238);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(255, 112, 93);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.push_9.setObjectName("push_9")
        self.gridLayout.addWidget(self.push_9, 4, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(14)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)
        self.push_del = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(14)
        sizePolicy.setHeightForWidth(self.push_del.sizePolicy().hasHeightForWidth())
        self.push_del.setSizePolicy(sizePolicy)
        self.push_del.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(157, 246, 255);\n"
"border-radius:35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"background-color: rgb(238, 238, 238);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(255, 112, 93);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.push_del.setObjectName("push_del")
        self.gridLayout.addWidget(self.push_del, 1, 2, 1, 1)
        self.push_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(14)
        sizePolicy.setHeightForWidth(self.push_1.sizePolicy().hasHeightForWidth())
        self.push_1.setSizePolicy(sizePolicy)
        self.push_1.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(157, 246, 255);\n"
"border-radius:35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"background-color: rgb(238, 238, 238);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(255, 112, 93);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.push_1.setObjectName("push_1")
        self.gridLayout.addWidget(self.push_1, 2, 0, 1, 1)
        self.push_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(14)
        sizePolicy.setHeightForWidth(self.push_2.sizePolicy().hasHeightForWidth())
        self.push_2.setSizePolicy(sizePolicy)
        self.push_2.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(157, 246, 255);\n"
"border-radius:35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"background-color: rgb(238, 238, 238);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(255, 112, 93);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"")
        self.push_2.setObjectName("push_2")
        self.gridLayout.addWidget(self.push_2, 2, 1, 1, 1)
        self.push_clear = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(14)
        sizePolicy.setHeightForWidth(self.push_clear.sizePolicy().hasHeightForWidth())
        self.push_clear.setSizePolicy(sizePolicy)
        self.push_clear.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(157, 246, 255);\n"
"border-radius:35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"background-color: rgb(238, 238, 238);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(255, 112, 93);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.push_clear.setObjectName("push_clear")
        self.gridLayout.addWidget(self.push_clear, 1, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 447, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.push_1.clicked.connect(self.method_1)
        self.push_2.clicked.connect(self.method_2)
        self.push_3.clicked.connect(self.method_3)
        self.push_4.clicked.connect(self.method_4)
        self.push_5.clicked.connect(self.method_5)
        self.push_6.clicked.connect(self.method_6)
        self.push_7.clicked.connect(self.method_7)
        self.push_8.clicked.connect(self.method_8)
        self.push_9.clicked.connect(self.method_9)
        self.push_0.clicked.connect(self.method_0)
        self.push_point.clicked.connect(self.method_point)
        self.push_clear.clicked.connect(self.method_clear)
        self.push_del.clicked.connect(self.method_del)
        self.push_add.clicked.connect(self.method_add)
        self.push_sub.clicked.connect(self.method_sub)
        self.push_mul.clicked.connect(self.method_mul)
        self.push_div.clicked.connect(self.method_div)
        self.push_equal.clicked.connect(self.method_equal)

    def method_1(self):
        text=self.label.text()
        self.label.setText(text+"1")

    def method_2(self):
        text=self.label.text()
        self.label.setText(text+"2")

    def method_3(self):
        text=self.label.text()
        self.label.setText(text+"3")

    def method_4(self):
        text=self.label.text()
        self.label.setText(text+"4")

    def method_5(self):
        text=self.label.text()
        self.label.setText(text+"5")

    def method_6(self):
        text=self.label.text()
        self.label.setText(text+"6")

    def method_7(self):
        text=self.label.text()
        self.label.setText(text+"7")

    def method_8(self):
        text=self.label.text()
        self.label.setText(text+"8")

    def method_9(self):
        text=self.label.text()
        self.label.setText(text+"9")

    def method_0(self):
        text=self.label.text()
        self.label.setText(text+"0")

    def method_point(self):
        text=self.label.text()
        self.label.setText(text+".")

    def method_add(self):
        text=self.label.text()
        self.label.setText(text+"+")

    def method_sub(self):
        text=self.label.text()
        self.label.setText(text+"-")

    def method_mul(self):
        text=self.label.text()
        self.label.setText(text+"*")

    def method_div(self):
        text=self.label.text()
        self.label.setText(text+"/")

    def method_equal(self):
        text=self.label.text()

        try:
            ans=eval(text)
            self.label.setText(str(ans))
        except:
            self.label.setText("Wrong Input")

    def method_clear(self):
        text=self.label.text()
        self.label.setText("")

    def method_del(self):
        text=self.label.text()
        self.label.setText(text[:len(text)-1])


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.push_7.setText(_translate("MainWindow", "7"))
        self.push_7.setShortcut(_translate("MainWindow", "7"))
        self.push_div.setText(_translate("MainWindow", "%"))
        self.push_div.setShortcut(_translate("MainWindow", "%"))
        self.push_0.setText(_translate("MainWindow", "0"))
        self.push_0.setShortcut(_translate("MainWindow", "0"))
        self.push_point.setText(_translate("MainWindow", "."))
        self.push_point.setShortcut(_translate("MainWindow", "."))
        self.push_equal.setText(_translate("MainWindow", "="))
        self.push_equal.setShortcut(_translate("MainWindow", "="))
        self.push_6.setText(_translate("MainWindow", "6"))
        self.push_6.setShortcut(_translate("MainWindow", "6"))
        self.push_3.setText(_translate("MainWindow", "3"))
        self.push_3.setShortcut(_translate("MainWindow", "3"))
        self.push_add.setText(_translate("MainWindow", "+"))
        self.push_add.setShortcut(_translate("MainWindow", "+"))
        self.push_4.setText(_translate("MainWindow", "4"))
        self.push_4.setShortcut(_translate("MainWindow", "4"))
        self.push_5.setText(_translate("MainWindow", "5"))
        self.push_5.setShortcut(_translate("MainWindow", "5"))
        self.push_mul.setText(_translate("MainWindow", "x"))
        self.push_mul.setShortcut(_translate("MainWindow", "*"))
        self.push_sub.setText(_translate("MainWindow", "-"))
        self.push_sub.setShortcut(_translate("MainWindow", "-"))
        self.push_8.setText(_translate("MainWindow", "8"))
        self.push_8.setShortcut(_translate("MainWindow", "8"))
        self.push_9.setText(_translate("MainWindow", "9"))
        self.push_9.setShortcut(_translate("MainWindow", "9"))
        self.push_del.setText(_translate("MainWindow", "Del"))
        self.push_del.setShortcut(_translate("MainWindow", "Backspace"))
        self.push_1.setText(_translate("MainWindow", "1"))
        self.push_1.setShortcut(_translate("MainWindow", "1"))
        self.push_2.setText(_translate("MainWindow", "2"))
        self.push_2.setShortcut(_translate("MainWindow", "2"))
        self.push_clear.setText(_translate("MainWindow", "Clear"))
        self.push_clear.setShortcut(_translate("MainWindow", "Del"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
