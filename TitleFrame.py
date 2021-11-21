import sys
import subprocess
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPainter, QColor, QPen, QFont
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QFrame

import Dialog
#========================================================================================================================

class Title(QtWidgets.QFrame):

    def __init__(self, window):
        super().__init__()
        self.mainWindow = window
        
        self.flag = False
        self.currentPath = 'Untitled.json'        
        self.mainLocation = QtCore.QPoint(18,10)
        self.oldLocation = QtCore.QPoint(18,10)
        
        buttonHelp = QPushButton('', self)
        buttonHelp.setToolTip('Get Help')
        buttonHelp.setGeometry(0, 0, 30, 30)
        buttonHelp.clicked.connect(self.getHelp)
        buttonHelp.setIcon(QtGui.QIcon('Images/Icons/help.png'))
        buttonHelp.setIconSize(QtCore.QSize(20,20))
        
        buttonMinimize = QPushButton('', self)
        buttonMinimize.setToolTip('Minimize')
        buttonMinimize.setGeometry(1251, 0, 30, 30)
        buttonMinimize.clicked.connect(self.minimizeWindow)
        buttonMinimize.setIcon(QtGui.QIcon('Images/Icons/minimize.png'))
        buttonMinimize.setIconSize(QtCore.QSize(20,20))
        
        buttonClose = QPushButton('', self)
        buttonClose.setToolTip('Close')
        buttonClose.setGeometry(1280, 0, 30, 30)
        buttonClose.clicked.connect(self.closeWindow)
        buttonClose.setIcon(QtGui.QIcon('Images/Icons/close.png'))
        buttonClose.setIconSize(QtCore.QSize(20,20))
        
    def paintEvent(self, event):
    
        qp = QtGui.QPainter(self)
        br = QtGui.QBrush(QtGui.QColor(255,255,255,10),1)
        qp.setBrush(br)
        
        qp.setPen(QPen(QtGui.QColor(140,140,140), 1))        
        qp.drawRect(0,0,1309,29)
        
        qp.setPen(QPen(QtGui.QColor(0,0,0), 1))
        qp.setFont(QFont('Sans Serif', 15))
        qp.drawText(40,23,'PyScrap - ')
        qp.setFont(QFont('Sans Serif', 10))
        qp.drawText(130,21,self.currentPath)
        
        
    def getHelp(self):
        subprocess.Popen('UserManual.pdf',shell=True)
    
    def minimizeWindow(self):
        self.mainWindow.showMinimized()
    
    def closeWindow(self):
        if self.mainWindow.data.fileChanged:
            d = Dialog.YesNoCancelDialog(self.mainWindow)
            d.setTitle('File not saved')
            d.setMessage('Save previous file?')
            
            stat = d.exec_()
            
            if stat == 1:
                self.mainWindow.bots.saveFile()
            elif stat == 0:
                return
        
        try:
            self.mainWindow.pycore.driver.close()
        except:
            pass
                
        self.mainWindow.close()
        
    
    def mousePressEvent(self, event):
        self.oldLocation = event.pos()
        self.flag = True
    
    def mouseMoveEvent(self, event):
    
        if self.flag:
            self.mainLocation.setX(self.mainLocation.x() - self.oldLocation.x() + event.pos().x())
            self.mainLocation.setY(self.mainLocation.y() - self.oldLocation.y() + event.pos().y())
            self.mainWindow.move(self.mainLocation)
        
    
    def mouseReleaseEvent(self, event):
        self.oldLocation = event.pos()
        self.flag = False

#========================================================================================================================