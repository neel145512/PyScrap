import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QFrame, QProgressBar
#========================================================================================================================


class Status(QtWidgets.QFrame):

    def __init__(self,window):
        super().__init__()
        self.mainWindow = window
        
        self.msg = ''
        self.color = (0,0,0)
        
    def paintEvent(self, event):
    
        qp = QtGui.QPainter(self)
        br = QtGui.QBrush(QtGui.QColor(255,255,255,10),1)
        qp.setBrush(br)
        qp.setPen(QPen(QtGui.QColor(140,140,140), 1))
        qp.drawRect(0,0,1309,19)

        qp.setPen(QPen(QtGui.QColor(self.color[0],self.color[1],self.color[2]),1))
        qp.drawText(9,14,self.msg)
        
        qp.setPen(QPen(QtGui.QColor(0,0,0), 1))
        qp.drawText(850,14,'Canvas size : ' + str(self.mainWindow.canvas.canvasWidth)+' X '+str(self.mainWindow.canvas.canvasHeight))
        
        qp.drawText(1050,14,'Windows')
        qp.drawText(1150,14,'UTF-8')
        qp.drawText(1250,14,'English')
        
    def setMessage(self,s,c):
        
        self.msg = s
        
        if c==1:
            self.color = (0,170,0)
        elif c==2:
            self.color = (255,0,0)
        else:
            self.color = (0,0,0)
#========================================================================================================================