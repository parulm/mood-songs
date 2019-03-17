# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Player.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import sys
import sentiment
import random
import time
from pygame import mixer
from PyQt4 import QtCore, QtGui
#from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(43, 43, 331, 161))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.commandLinkButton = QtGui.QCommandLinkButton(Dialog)
        self.commandLinkButton.setGeometry(QtCore.QRect(270, 240, 81, 41))
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.commandLinkButton.clicked.connect(self.send_message)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.commandLinkButton.setText(_translate("Dialog", "Send", None))

    def send_message(self):
        content = self.lineEdit.text()
        s = sentiment.analyze(content)
        print(s.score, s.magnitude)
        r = random.randint(1,4)
        print(r)
        if s.score<0:
            print('Its sad!')
            song = "songs/sad/"+str(r)+".mp3"
        else:
            print('Its happy!')
            song = "songs/happy/"+str(r)+".mp3"
        mixer.init()
        mixer.music.load(song)
        print('Playing music')
        mixer.music.play()
        time.sleep(120)
        print('Exiting...')



if __name__ == "__main__":

    import sys

    app = QtGui.QApplication(sys.argv)


    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)

    #Dialog.setWindowIcon(QtGui.QIcon('Tutor.jpg'))
    Dialog.show()

    sys.exit(app.exec_())