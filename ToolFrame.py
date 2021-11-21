import sys
import random
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPainter, QColor, QPen, QFont, QPixmap
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QFrame
from PyQt5.QtCore import Qt

from functools import partial
#========================================================================================================================


class Tools(QtWidgets.QFrame):

    def __init__(self, window):
        super().__init__()
        self.mainWindow = window
        
        self.color = (139,0,139)
        
        #Tool buttons
        self.buttonStart = QPushButton('',self)
        self.buttonStart.setGeometry(10,30,62,62)
        self.buttonStart.setIcon(QtGui.QIcon('Images/64/start.png'))
        self.buttonStart.setIconSize(QtCore.QSize(46,46))
        self.buttonStart.setToolTip('Start')
        self.buttonStart.setCheckable(True)
        self.buttonStart.clicked.connect(partial(self.setTool,1))
        
        self.buttonUrl = QPushButton('',self)
        self.buttonUrl.setGeometry(72,30,62,62)
        self.buttonUrl.setIcon(QtGui.QIcon('Images/64/url.png'))
        self.buttonUrl.setIconSize(QtCore.QSize(46,46))
        self.buttonUrl.setToolTip('URL')
        self.buttonUrl.setCheckable(True)
        self.buttonUrl.clicked.connect(partial(self.setTool,2))
        
        self.buttonCrawler = QPushButton('',self)
        self.buttonCrawler.setGeometry(134,30,62,62)
        self.buttonCrawler.setIcon(QtGui.QIcon('Images/64/crawler.png'))
        self.buttonCrawler.setIconSize(QtCore.QSize(46,46))
        self.buttonCrawler.setToolTip('Web Crawler')
        self.buttonCrawler.setCheckable(True)
        self.buttonCrawler.clicked.connect(partial(self.setTool,3))
        
        self.buttonMedia = QPushButton('',self)
        self.buttonMedia.setGeometry(196,30,62,62)
        self.buttonMedia.setIcon(QtGui.QIcon('Images/64/media.png'))
        self.buttonMedia.setIconSize(QtCore.QSize(46,46))
        self.buttonMedia.setToolTip('Media Extractor')
        self.buttonMedia.setCheckable(True)
        self.buttonMedia.clicked.connect(partial(self.setTool,4))
        
        self.buttonRename = QPushButton('',self)
        self.buttonRename.setGeometry(258,30,62,62)
        self.buttonRename.setIcon(QtGui.QIcon('Images/64/rename.png'))
        self.buttonRename.setIconSize(QtCore.QSize(46,46))
        self.buttonRename.setToolTip('Rename')
        self.buttonRename.setCheckable(True)
        self.buttonRename.clicked.connect(partial(self.setTool,5))
        
        self.buttonSort = QPushButton('',self)
        self.buttonSort.setGeometry(10,92,62,62)
        self.buttonSort.setIcon(QtGui.QIcon('Images/64/sort.png'))
        self.buttonSort.setIconSize(QtCore.QSize(46,46))
        self.buttonSort.setToolTip('Sort')
        self.buttonSort.setCheckable(True)
        self.buttonSort.clicked.connect(partial(self.setTool,6))
        
        self.buttonObject = QPushButton('',self)
        self.buttonObject.setGeometry(72,92,62,62)
        self.buttonObject.setIcon(QtGui.QIcon('Images/64/object.png'))
        self.buttonObject.setIconSize(QtCore.QSize(46,46))
        self.buttonObject.setToolTip('Object Detector')
        self.buttonObject.setCheckable(True)
        self.buttonObject.clicked.connect(partial(self.setTool,7))
        
        self.buttonKeys = QPushButton('',self)
        self.buttonKeys.setGeometry(134,92,62,62)
        self.buttonKeys.setIcon(QtGui.QIcon('Images/64/keys.png'))
        self.buttonKeys.setIconSize(QtCore.QSize(46,46))
        self.buttonKeys.setToolTip('Keyboard Events')
        self.buttonKeys.setCheckable(True)
        self.buttonKeys.clicked.connect(partial(self.setTool,8))
        
        self.buttonMouse = QPushButton('',self)
        self.buttonMouse.setGeometry(196,92,62,62)
        self.buttonMouse.setIcon(QtGui.QIcon('Images/64/mouse.png'))
        self.buttonMouse.setIconSize(QtCore.QSize(46,46))
        self.buttonMouse.setToolTip('Mouse Events')
        self.buttonMouse.setCheckable(True)
        self.buttonMouse.clicked.connect(partial(self.setTool,9))
        
        self.buttonDelay = QPushButton('',self)
        self.buttonDelay.setGeometry(258,92,62,62)
        self.buttonDelay.setIcon(QtGui.QIcon('Images/64/delay.png'))
        self.buttonDelay.setIconSize(QtCore.QSize(46,46))
        self.buttonDelay.setToolTip('Delay')
        self.buttonDelay.setCheckable(True)
        self.buttonDelay.clicked.connect(partial(self.setTool,10))
        
        self.buttonFilter = QPushButton('',self)
        self.buttonFilter.setGeometry(10,154,62,62)
        self.buttonFilter.setIcon(QtGui.QIcon('Images/64/filter.png'))
        self.buttonFilter.setIconSize(QtCore.QSize(46,46))
        self.buttonFilter.setToolTip('Filter')
        self.buttonFilter.setCheckable(True)
        self.buttonFilter.clicked.connect(partial(self.setTool,11))
        
        self.buttonDbcon = QPushButton('',self)
        self.buttonDbcon.setGeometry(72,154,62,62)
        self.buttonDbcon.setIcon(QtGui.QIcon('Images/64/dbcon.png'))
        self.buttonDbcon.setIconSize(QtCore.QSize(46,46))
        self.buttonDbcon.setToolTip('Database')
        self.buttonDbcon.setCheckable(True)
        self.buttonDbcon.clicked.connect(partial(self.setTool,12))
        
        self.buttonTable = QPushButton('',self)
        self.buttonTable.setGeometry(134,154,62,62)
        self.buttonTable.setIcon(QtGui.QIcon('Images/64/table.png'))
        self.buttonTable.setIconSize(QtCore.QSize(46,46))
        self.buttonTable.setToolTip('Table')
        self.buttonTable.setCheckable(True)
        self.buttonTable.clicked.connect(partial(self.setTool,13))
        
        self.buttonColumn = QPushButton('',self)
        self.buttonColumn.setGeometry(196,154,62,62)
        self.buttonColumn.setIcon(QtGui.QIcon('Images/64/column.png'))
        self.buttonColumn.setIconSize(QtCore.QSize(46,46))
        self.buttonColumn.setToolTip('Column')
        self.buttonColumn.setCheckable(True)
        self.buttonColumn.clicked.connect(partial(self.setTool,14))
        
        self.buttonDownload = QPushButton('',self)
        self.buttonDownload.setGeometry(258,154,62,62)
        self.buttonDownload.setIcon(QtGui.QIcon('Images/64/download.png'))
        self.buttonDownload.setIconSize(QtCore.QSize(46,46))
        self.buttonDownload.setToolTip('Download')
        self.buttonDownload.setCheckable(True)
        self.buttonDownload.clicked.connect(partial(self.setTool,15))
        
        self.btnTool = list()
        self.btnTool.append(self.buttonStart)
        self.btnTool.append(self.buttonStart)
        self.btnTool.append(self.buttonUrl)
        self.btnTool.append(self.buttonCrawler)
        self.btnTool.append(self.buttonMedia)
        self.btnTool.append(self.buttonRename)
        self.btnTool.append(self.buttonSort)
        self.btnTool.append(self.buttonObject)
        self.btnTool.append(self.buttonKeys)
        self.btnTool.append(self.buttonMouse)
        self.btnTool.append(self.buttonDelay)
        self.btnTool.append(self.buttonFilter)
        self.btnTool.append(self.buttonDbcon)
        self.btnTool.append(self.buttonTable)
        self.btnTool.append(self.buttonColumn)
        self.btnTool.append(self.buttonDownload)
        
        #Color buttons
        
        btn = list()
        
        for i in range(4):
            btn.append(list())
            for j in range(14):
                btn[i].append(QPushButton('',self))
                
        #get color data
        
        col = list()
        with open('Images/Color/colors.csv') as f:
            content = f.readlines()

        for i in content:
            col.append(i.split(',')[:2])
            
        for i in col:
            i[1] = i[1][1:]

        
        for i in range(4):
            for j in range(14):
                ci = i*14 + j
                btn[i][j].setGeometry(10+j*22,224+i*23,23,24)
                btn[i][j].setIcon(QtGui.QIcon('Images/Color/'+col[ci][0]+'.png'))
                btn[i][j].setIconSize(QtCore.QSize(15,16))
                btn[i][j].setToolTip(col[ci][0])
                btn[i][j].clicked.connect(self.drawRects)
                t = (int(col[ci][1][0:2],16),int(col[ci][1][2:4],16),int(col[ci][1][4:6],16))
                btn[i][j].clicked.connect(partial(self.setColor,t))
     
    def paintEvent(self, event):
    
        qp = QtGui.QPainter(self)
        br = QtGui.QBrush(QtGui.QColor(255,255,255),1)
        qp.setBrush(br)
        
        qp.setFont(QFont('Sans Serif', 9))
        
        qp.setPen(QPen(QtGui.QColor(140,140,140), 1))
        qp.drawRect(0,-1,329,326)
        
        qp.setPen(QPen(QtGui.QColor(171,171,171), 1))
        br = QtGui.QBrush(QtGui.QColor(171,171,171),1)
        qp.setBrush(br)
        
        #----
        qp.drawRect(9,29,311,187)
        qp.drawRect(12,230,300,85)
        qp.setPen(QPen(QtGui.QColor(0,0,0), 1))
        qp.drawText(10,18,'Tool box & Color palette : ')
        
        #---draw sample rect
        qp.setPen(QPen(QtGui.QColor(self.color[0],self.color[1],self.color[2],200), 1))
        br = QtGui.QBrush(QtGui.QColor(self.color[0],self.color[1],self.color[2],50),1)
        qp.setBrush(br)
        qp.drawRect(160,6,30,15)
        
    def mousePressEvent(self, event):
    
        if event.button() == Qt.RightButton:
            self.btnTool[self.mainWindow.tool].setChecked(False)
            self.mainWindow.tool = 12
            self.mainWindow.toolFlag=False
            self.mainWindow.canvas.update()
            self.update()
            return
        
        
    def setTool(self,t):
        self.mainWindow.tool = t
        self.mainWindow.toolFlag=True        
        self.mainWindow.canvas.update()
        self.update()
        
    def setColor(self,c):
        self.color  = c
        self.update()
        self.mainWindow.canvas.update()
        
    def drawRects(self):
        self.mainWindow.canvas.drawRects()
        
#========================================================================================================================