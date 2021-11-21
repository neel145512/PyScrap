import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import *
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class MessageDialog(QDialog):

    def __init__(self,window):
        super().__init__()
        self.mainWindow = window
        
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowModality(Qt.ApplicationModal)
        self.setGeometry(self.mainWindow.title.mainLocation.x()+1330/2-150,self.mainWindow.title.mainLocation.y()+720/2-75,300,150)
        
        self.title = 'Dialog Title'
        self.msg = 'This is dialog message'
        
        self.buttonOk = QPushButton('OK',self)
        self.buttonOk.setGeometry(240,110,40,20)
        self.buttonOk.clicked.connect(self.send1)
        
    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        br = QtGui.QBrush(QtGui.QColor(255,255,255,0),1)
        qp.setBrush(br)
        qp.setFont(QFont('Sans Serif', 9))
        
        qp.setPen(QPen(QtGui.QColor(150,150,150), 1))
        qp.drawLine(20,30,280,30)
        
        qp.setPen(QPen(QtGui.QColor(50,50,50), 1))
        qp.drawText(20,23,self.title)
        qp.drawText(20,48,self.msg)
        
        for i in range(5):
            qp.setPen(QPen(QtGui.QColor(250-i*10,250-i*20,255), 1))
            qp.drawRect(i,i,300-(i+1)*2,150-(i+1)*2)
        
    def send1(self):
        self.done(1)
        
    def setTitle(self,str):
        self.title = str
        
    def setMessage(self,str):
        self.msg = str
        
class YesNoDialog(QDialog):

    def __init__(self,window):
        super().__init__()
        self.mainWindow = window
        
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowModality(Qt.ApplicationModal)
        self.setGeometry(self.mainWindow.title.mainLocation.x()+1330/2-150,self.mainWindow.title.mainLocation.y()+720/2-75,300,150)
        
        self.title = 'Dialog Title'
        self.msg = 'This is dialog message'
        
        self.buttonNo = QPushButton('No',self)
        self.buttonNo.setGeometry(240,110,40,20)
        self.buttonNo.clicked.connect(self.send0)
        
        self.buttonYes = QPushButton('Yes',self)
        self.buttonYes.setGeometry(190,110,40,20)
        self.buttonYes.clicked.connect(self.send1)
        
    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        br = QtGui.QBrush(QtGui.QColor(255,255,255,0),1)
        qp.setBrush(br)
        qp.setFont(QFont('Sans Serif', 9))
        
        qp.setPen(QPen(QtGui.QColor(150,150,150), 1))
        qp.drawLine(20,30,280,30)
        
        qp.setPen(QPen(QtGui.QColor(50,50,50), 1))
        qp.drawText(20,23,self.title)
        qp.drawText(20,48,self.msg)
        
        for i in range(5):
            qp.setPen(QPen(QtGui.QColor(250-i*10,250-i*20,255), 1))
            qp.drawRect(i,i,300-(i+1)*2,150-(i+1)*2)
        
    def send0(self):
        self.done(0)
        
    def send1(self):
        self.done(1)
        
    def setTitle(self,str):
        self.title = str
        
    def setMessage(self,str):
        self.msg = str
        
class YesNoCancelDialog(QDialog):

    def __init__(self,window):
        super().__init__()
        self.mainWindow = window
        
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowModality(Qt.ApplicationModal)
        self.setGeometry(self.mainWindow.title.mainLocation.x()+1330/2-150,self.mainWindow.title.mainLocation.y()+720/2-75,300,150)
        
        self.title = 'Dialog Title'
        self.msg = 'This is dialog message'
        
        self.buttonCancel = QPushButton('Cancel',self)
        self.buttonCancel.setGeometry(240,110,40,20)
        self.buttonCancel.clicked.connect(self.send0)
        
        self.buttonNo = QPushButton('No',self)
        self.buttonNo.setGeometry(190,110,40,20)
        self.buttonNo.clicked.connect(self.send2)
        
        self.buttonYes = QPushButton('Yes',self)
        self.buttonYes.setGeometry(140,110,40,20)
        self.buttonYes.clicked.connect(self.send1)
        
    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        br = QtGui.QBrush(QtGui.QColor(255,255,255,0),1)
        qp.setBrush(br)
        qp.setFont(QFont('Sans Serif', 9))
        
        qp.setPen(QPen(QtGui.QColor(150,150,150), 1))
        qp.drawLine(20,30,280,30)
        
        qp.setPen(QPen(QtGui.QColor(50,50,50), 1))
        qp.drawText(20,23,self.title)
        qp.drawText(20,48,self.msg)
        
        for i in range(5):
            qp.setPen(QPen(QtGui.QColor(250-i*10,250-i*20,255), 1))
            qp.drawRect(i,i,300-(i+1)*2,150-(i+1)*2)
        
    def send0(self):
        self.done(0)
        
    def send1(self):
        self.done(1)
        
    def send2(self):
        self.done(2)
        
    def setTitle(self,str):
        self.title = str
        
    def setMessage(self,str):
        self.msg = str
        
class SaveDialog(QDialog):

    def __init__(self,window):
        super().__init__()
        self.mainWindow = window
        
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowModality(Qt.ApplicationModal)
        self.setGeometry(self.mainWindow.title.mainLocation.x()+1330/2-150,self.mainWindow.title.mainLocation.y()+720/2-75,300,150)
        
        self.title = 'Dialog Title'
        self.msg = 'This is dialog message'
        
        self.fileName = QLineEdit(self)
        self.fileName.setGeometry(20,55,260,20)
        
        self.buttonOk = QPushButton('Save',self)
        self.buttonOk.setGeometry(240,110,40,20)
        self.buttonOk.clicked.connect(self.send1)
        
    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        br = QtGui.QBrush(QtGui.QColor(255,255,255,0),1)
        qp.setBrush(br)
        qp.setFont(QFont('Sans Serif', 9))
        
        qp.setPen(QPen(QtGui.QColor(150,150,150), 1))
        qp.drawLine(20,30,280,30)
        
        qp.setPen(QPen(QtGui.QColor(50,50,50), 1))
        qp.drawText(20,23,self.title)
        qp.drawText(20,48,self.msg)
        
        for i in range(5):
            qp.setPen(QPen(QtGui.QColor(250-i*10,250-i*20,255), 1))
            qp.drawRect(i,i,300-(i+1)*2,150-(i+1)*2)
        
    def send1(self):
        if len(self.fileName.text()) == 0:
            d = MessageDialog(self.mainWindow)
            d.setTitle('Invalid file')
            d.setMessage('Enter atleast one character.')
            d.exec_()
            return
            
        self.mainWindow.data.fileName = self.fileName.text()
        self.done(1)
        
    def setTitle(self,str):
        self.title = str
        
    def setMessage(self,str):
        self.msg = str