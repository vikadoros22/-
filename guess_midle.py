# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guess_midle.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindowmidle(object):
    def setupUi(self, MainWindowmidle):
        MainWindowmidle.setObjectName("MainWindowmidle")
        MainWindowmidle.resize(440, 670)
        MainWindowmidle.setMinimumSize(QtCore.QSize(420, 670))
        MainWindowmidle.setMaximumSize(QtCore.QSize(440, 670))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Дорошкевич/S_C1kah0oVtA_t.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindowmidle.setWindowIcon(icon)
        MainWindowmidle.setStyleSheet("background-color: rgb(5, 151, 242);")
        self.centralwidget = QtWidgets.QWidget(MainWindowmidle)
        self.centralwidget.setObjectName("centralwidget")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 110, 411, 41))
        self.label_5.setMaximumSize(QtCore.QSize(440, 16777215))
        self.label_5.setStyleSheet("font: 22pt \"Matura MT Script Capitals\";")
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 10, 201, 81))
        self.label_2.setStyleSheet("font: 25pt \"Matura MT Script Capitals\";\n"
"")
        self.label_2.setObjectName("label_2")
        self.i_chislo = QtWidgets.QLabel(self.centralwidget)
        self.i_chislo.setGeometry(QtCore.QRect(360, 10, 51, 81))
        self.i_chislo.setStyleSheet("font: 23pt \"Impact\";\n"
"")
        self.i_chislo.setAlignment(QtCore.Qt.AlignCenter)
        self.i_chislo.setObjectName("i_chislo")
        self.btn_nazad = QtWidgets.QPushButton(self.centralwidget)
        self.btn_nazad.setGeometry(QtCore.QRect(20, 590, 151, 51))
        self.btn_nazad.setStyleSheet("QPushButton {\n"
"font: 25pt \"Candara\";\n"
"background-color: rgb(70, 2, 115);\n"
"\n"
"color: rgb(85, 255, 255);\n"
"}\n"
"QPushButton:pressed { \n"
"    \n"
"    background-color: rgb(170, 85, 255);\n"
"    \n"
"    \n"
"}")
        self.btn_nazad.setObjectName("btn_nazad")
        self.btn_proverka = QtWidgets.QPushButton(self.centralwidget)
        self.btn_proverka.setGeometry(QtCore.QRect(70, 420, 301, 101))
        self.btn_proverka.setStyleSheet("QPushButton {\n"
"    \n"
"font: 36pt \"Matura MT Script Capitals\";\n"
"background-color: rgb(70, 2, 115);\n"
"border-radius: 30;\n"
"color: rgb(85, 255, 255);\n"
"}\n"
"QPushButton:pressed { \n"
"    \n"
"    \n"
"    background-color: rgb(85, 0, 255);\n"
"    \n"
"    \n"
"}")
        self.btn_proverka.setObjectName("btn_proverka")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(50, 290, 341, 61))
        self.lineEdit_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_3.setStyleSheet("font: 18pt \"Impact\";\n"
"background-color: rgb(85, 255, 255);")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 590, 211, 51))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"font: 25pt \"Candara\";\n"
"background-color: rgb(70, 2, 115);\n"
"\n"
"color: rgb(85, 255, 255);\n"
"}\n"
"QPushButton:pressed { \n"
"    \n"
"    background-color: rgb(170, 85, 255);\n"
"    \n"
"    \n"
"}")
        self.pushButton_3.setIconSize(QtCore.QSize(15, 20))
        self.pushButton_3.setAutoRepeatDelay(309)
        self.pushButton_3.setObjectName("pushButton_3")
        self.l_otvet = QtWidgets.QLabel(self.centralwidget)
        self.l_otvet.setGeometry(QtCore.QRect(20, 170, 391, 81))
        self.l_otvet.setStyleSheet("\n"
"font: 23pt \"Impact\";\n"
"color: rgb(70, 2, 115);")
        self.l_otvet.setText("")
        self.l_otvet.setAlignment(QtCore.Qt.AlignCenter)
        self.l_otvet.setObjectName("l_otvet")
        MainWindowmidle.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindowmidle)
        QtCore.QMetaObject.connectSlotsByName(MainWindowmidle)

    def retranslateUi(self, MainWindowmidle):
        _translate = QtCore.QCoreApplication.translate
        MainWindowmidle.setWindowTitle(_translate("MainWindowmidle", "Угадайка"))
        self.label_5.setText(_translate("MainWindowmidle", "<html><head/><body><p><span style=\" font-size:18pt;\">Введите число от 0 до 100 :</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindowmidle", "<html><head/><body><p><span style=\" font-size:24pt;\">Попыток:</span></p></body></html>"))
        self.i_chislo.setText(_translate("MainWindowmidle", "10"))
        self.btn_nazad.setText(_translate("MainWindowmidle", "Назад"))
        self.btn_proverka.setText(_translate("MainWindowmidle", "Проверка!"))
        self.lineEdit_3.setAccessibleName(_translate("MainWindowmidle", "<html><head/><body><p align=\"center\">ь</p></body></html>"))
        self.pushButton_3.setToolTip(_translate("MainWindowmidle", "<html><head/><body><p><span style=\" font-size:10pt;\">Новая </span></p><p><span style=\" font-size:10pt;\">игра</span></p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindowmidle", "Новая игра"))
        self.l_otvet.setWhatsThis(_translate("MainWindowmidle", "<html><head/><body><p>Вы проиграли! </p><p>Загаданное число </p></body></html>"))