import sys
import math
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import *
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
#========================================================================================================================

#notool
class notool(QFrame):
    
    def __init__(self,window):
        super().__init__()
        self.mainWindow = window
        
        self.c = 0
        self.t = 0
        
    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        qp.setRenderHint(0x08)
        
        br = QtGui.QBrush(QtGui.QColor(255,255,255,0),1)
        qp.setBrush(br)
        qp.setPen(QPen(QtGui.QColor(0,0,0), 1))
        
        qp.drawText(10,20,'Canvas')
        qp.drawText(10,53,'Selected Rectangle : ')
        
        if self.mainWindow.canvas.currentRect == -1:
            qp.drawText(114,53,'None')
        else:
            if len(self.mainWindow.canvas.rects) > 0:
                c = self.mainWindow.canvas.rects[self.mainWindow.canvas.currentRect]
                qp.setPen(QPen(QtGui.QColor(c[4],c[5],c[6],200), 1))
                br = QtGui.QBrush(QtGui.QColor(c[4],c[5],c[6],50),1)
                qp.setBrush(br)
                qp.drawRect(114,42,30,15)
            else:
                qp.drawText(114,53,'None')
        
        br = QtGui.QBrush(QtGui.QColor(255,255,255,0),1)
        qp.setBrush(br)
        qp.setPen(QPen(QtGui.QColor(140,140,140), 1))
        qp.drawRect(0,0,311,306)
        qp.drawRect(0,0,311,31)
        
        #Draw progress meter total
        
        x = 18
        y = 290
        r = 200
        
        qpen = QPen(QtGui.QColor(89,172,255), 4)
        qpen.setCapStyle(Qt.RoundCap)
        qp.setPen(qpen)
        
        for i in range(21):
            qp.drawPoint(x+r*math.cos(math.radians(270+i*4.5)),y+r*math.sin(math.radians(270+i*4.5)))
        
        for i in range(11):
        
            if i==0 or i==5 or i==10:
                qpen = QPen(QtGui.QColor(0,0,0), 14)
                qpen.setCapStyle(Qt.RoundCap)
                qp.setPen(qpen)
            else:
                qpen = QPen(QtGui.QColor(0,0,0), 8)
                qpen.setCapStyle(Qt.RoundCap)
                qp.setPen(qpen)
            
            qp.drawPoint(x+r*math.cos(math.radians(270+i*9)),y+r*math.sin(math.radians(270+i*9)))
            
            if i==0 or i==5 or i==10:
                qpen = QPen(QtGui.QColor(89,172,255), 12)
                qpen.setCapStyle(Qt.RoundCap)
                qp.setPen(qpen)
            else:
                qpen = QPen(QtGui.QColor(89,172,255), 6)
                qpen.setCapStyle(Qt.RoundCap)
                qp.setPen(qpen)
            
            qp.drawPoint(x+r*math.cos(math.radians(270+i*9)),y+r*math.sin(math.radians(270+i*9)))
            
        
        qpen = QPen(QtGui.QColor(0,0,0), 7)
        qpen.setCapStyle(Qt.RoundCap)
        qp.setPen(qpen)
        r *= 0.90
        qp.drawLine(x,y,x+r*math.cos(math.radians(270+(self.t/100*90))),y+r*math.sin(math.radians(270+(self.t/100*90))))
        
        qpen = QPen(QtGui.QColor(140,140,140), 5)
        qpen.setCapStyle(Qt.RoundCap)
        qp.setPen(qpen)
        qp.drawLine(x,y,x+r*math.cos(math.radians(270+(self.t/100*90))),y+r*math.sin(math.radians(270+(self.t/100*90))))
        
        qpen = QPen(QtGui.QColor(0,0,0), 22)
        qpen.setCapStyle(Qt.RoundCap)
        qp.setPen(qpen)
        qp.drawPoint(x,y)
        
        qpen = QPen(QtGui.QColor(89,172,255), 20)
        qpen.setCapStyle(Qt.RoundCap)
        qp.setPen(qpen)
        qp.drawPoint(x,y)
        
        
        
        #Draw progress meter current
        
        '''x = 295
        y = 50
        r = 100
        
        for i in range(11):
        
            if i==0 or i==5 or i==10:
                qpen = QPen(QtGui.QColor(0,0,0), 10)
                qpen.setCapStyle(Qt.RoundCap)
                qp.setPen(qpen)
            else:
                qpen = QPen(QtGui.QColor(0,0,0), 7)
                qpen.setCapStyle(Qt.RoundCap)
                qp.setPen(qpen)
                
            qp.drawPoint(x+r*math.cos(math.radians(90+i*9)),y+r*math.sin(math.radians(90+i*9)))
            
            if i==0 or i==5 or i==10:
                qpen = QPen(QtGui.QColor(89,172,255), 8)
                qpen.setCapStyle(Qt.RoundCap)
                qp.setPen(qpen)
            else:
                qpen = QPen(QtGui.QColor(89,172,255), 5)
                qpen.setCapStyle(Qt.RoundCap)
                qp.setPen(qpen)
            
            qp.drawPoint(x+r*math.cos(math.radians(90+i*9)),y+r*math.sin(math.radians(90+i*9)))
            
        qpen = QPen(QtGui.QColor(0,0,0), 5)
        qpen.setCapStyle(Qt.RoundCap)
        qp.setPen(qpen)
        r *= 0.85
        qp.drawLine(x,y,x+r*math.cos(math.radians(90+(self.c/100*90))),y+r*math.sin(math.radians(90+(self.c/100*90))))
        
        qpen = QPen(QtGui.QColor(140,140,140), 3)
        qpen.setCapStyle(Qt.RoundCap)
        qp.setPen(qpen)
        qp.drawLine(x,y,x+r*math.cos(math.radians(90+(self.c/100*90))),y+r*math.sin(math.radians(90+(self.c/100*90))))
            
        qpen = QPen(QtGui.QColor(0,0,0), 17)
        qpen.setCapStyle(Qt.RoundCap)
        qp.setPen(qpen)
        qp.drawPoint(x,y)
        
        qpen = QPen(QtGui.QColor(89,172,255), 15)
        qpen.setCapStyle(Qt.RoundCap)
        qp.setPen(qpen)
        qp.drawPoint(x,y)
        
        qpen = QPen(QtGui.QColor(140,140,140), 15)
        qpen.setCapStyle(Qt.RoundCap)
        qp.setPen(qpen)
        qp.drawLine(x,y,x,y)'''
        
        #Draw percentages
        
        qp.setPen(QPen(QtGui.QColor(140,140,140), 1))
        qp.setFont(QFont('Sans Serif', 25))
        qp.drawText(215,130,str(round(self.t,1))+'%')
        '''qp.setFont(QFont('Sans Serif', 15))
        qp.drawText(225,190,str(round(self.c,1))+'%')'''
        
    def loadValues(self):
        pass


#start
class start(QFrame):
    
    def __init__(self,window):
        super().__init__()
        self.mainWindow = window
        
    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        br = QtGui.QBrush(QtGui.QColor(255,255,255,0),1)
        qp.setBrush(br)
        qp.setPen(QPen(QtGui.QColor(0,0,0),1))
        qp.drawText(10,20,'No Output Needed')

        qp.setPen(QPen(QtGui.QColor(140,140,140),1))
        qp.drawRect(0,0,311,306)
        qp.drawRect(0,0,311,31)
        
    def loadValues(self):
        pass


#url
class url(QFrame):
    
    def __init__(self,window):
        super().__init__()
        self.mainWindow = window
        
        self.urlStatus = 'Url Status'
        
        self.httpCodes = {
            '0':'Invalid URL (or check your Internet connection)',
            '200': 'HTTP Request Successful',
            '401': 'Unauthorised Access',
            '403': 'Forbidden',
            '404': 'Not Found'
        }
        
    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        br = QtGui.QBrush(QtGui.QColor(255,255,255,0),1)
        qp.setBrush(br)
        qp.setPen(QPen(QtGui.QColor(0,0,0), 1))
        qp.drawText(10,20,'Url Provider Output')
        
        qp.drawText(10,53,self.urlStatus)
        
        qp.setPen(QPen(QtGui.QColor(140,140,140), 1))
        qp.drawRect(0,0,311,306)
        qp.drawRect(0,0,311,31)
        
    def loadValues(self):
    
        x = self.mainWindow.data.outputList[self.mainWindow.canvas.currentShape]
        
        if len(x) > 0:
            self.urlStatus = str(x[1]) + ' - '
            if str(x[1]) in self.urlStatus:
                try:
                    self.urlStatus = self.urlStatus + self.httpCodes.get(str(x[1]))
                except:
                    pass
            else:
                self.urlStatus = self.urlStatus + 'Something is wrong, Try againg please.'
        else:
            self.urlStatus = ''
            
        self.update()
        

#crawler
class crawler(QFrame):

    level,link,parent = range(3)
    
    def __init__(self,window):
        super().__init__()
        self.mainWindow = window
        
        layout = QGridLayout()
        layout.setContentsMargins(0,0,0,0)
        
        #--------------
        self.model = QStandardItemModel(0, 3, self)
        self.model.setHeaderData(self.level, Qt.Horizontal, 'lvl')
        self.model.setHeaderData(self.link, Qt.Horizontal, 'Link')
        self.model.setHeaderData(self.parent, Qt.Horizontal, 'Parent Links')

        #QTreeView for links
        view = QTreeView(self)
        view.header().setSectionsClickable(True)
        view.setRootIsDecorated(False)
        view.setAlternatingRowColors(True)

        view.setModel(self.model)
        view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        view.setSelectionMode(0)
        view.setColumnWidth(0,1)
        view.setColumnWidth(1,270)
        view.setColumnWidth(2,400)

        f = QFrame()
        layout.setRowMinimumHeight(0, 25)
        
        layout.addWidget(f,0,0)
        layout.addWidget(view,1,0)
        #--------------
        
        self.setLayout(layout)
        
    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        br = QtGui.QBrush(QtGui.QColor(255,255,255,0),1)
        qp.setBrush(br)
        qp.setPen(QPen(QtGui.QColor(0,0,0), 1))
        qp.drawText(10,20,'Links')
        
        qp.setPen(QPen(QtGui.QColor(140,140,140), 1))
        qp.drawRect(0,0,311,306)
        qp.drawRect(0,0,311,31)
        
    def loadValues(self):
        x = self.mainWindow.data.outputList[self.mainWindow.canvas.currentShape]
        
        if len(x) > 0:
            
            for i in range(self.model.rowCount()):
                self.model.takeRow(i)
            self.model.setRowCount(0)
            
            for i in x:        
                self.model.insertRow(0)
                self.model.setData(self.model.index(0, self.level), len(i)-1)
                self.model.setData(self.model.index(0, self.link), i[0])
                self.model.setData(self.model.index(0, self.parent), '|'.join(i[1:]))
        else:
            for i in range(self.model.rowCount()):
                self.model.takeRow(i)
            self.model.setRowCount(0)
            
        self.update()


#media
class media(QFrame):
    
    file,link = range(2)
    
    def __init__(self,window):
        super().__init__()
        self.mainWindow = window
        
        layout = QGridLayout()
        layout.setContentsMargins(0,0,0,0)
        
        #--------------
        self.model = QStandardItemModel(0, 2, self)
        self.model.setHeaderData(self.file, Qt.Horizontal, 'File')
        self.model.setHeaderData(self.link, Qt.Horizontal, 'Link')

        #QTreeView for links
        view = QTreeView(self)
        view.header().setSectionsClickable(True)
        view.setRootIsDecorated(False)
        view.setAlternatingRowColors(True)

        view.setModel(self.model)
        view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        view.setSelectionMode(0)
        view.setColumnWidth(0,150)
        view.setColumnWidth(1,400)

        f = QFrame()
        layout.setRowMinimumHeight(0, 25)
        
        layout.addWidget(f,0,0)
        layout.addWidget(view,1,0)
        #--------------
        
        self.setLayout(layout)
        
    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        br = QtGui.QBrush(QtGui.QColor(255,255,255,0),1)
        qp.setBrush(br)
        qp.setPen(QPen(QtGui.QColor(0,0,0), 1))
        qp.drawText(10,20,'Files')
        
        qp.setPen(QPen(QtGui.QColor(140,140,140), 1))
        qp.drawRect(0,0,311,306)
        qp.drawRect(0,0,311,31)
        
    def loadValues(self):
        x = self.mainWindow.data.outputList[self.mainWindow.canvas.currentShape]
        
        if len(x) > 0:
            
            for i in range(self.model.rowCount()):
                self.model.takeRow(i)
            self.model.setRowCount(0)
            
            for i in x:        
                self.model.insertRow(0)
                self.model.setData(self.model.index(0, self.file), ''.join(i[0:1]))
                self.model.setData(self.model.index(0, self.link), '|'.join(i[1:]))
        else:
            for i in range(self.model.rowCount()):
                self.model.takeRow(i)
            self.model.setRowCount(0)
            
        self.update()


#rename
class rename(QFrame):
    
    file,link = range(2)
    
    def __init__(self,window):
        super().__init__()
        self.mainWindow = window
        
        layout = QGridLayout()
        layout.setContentsMargins(0,0,0,0)
        
        #--------------
        self.model = QStandardItemModel(0, 2, self)
        self.model.setHeaderData(self.file, Qt.Horizontal, 'File')
        self.model.setHeaderData(self.link, Qt.Horizontal, 'Link')

        #QTreeView for links
        view = QTreeView(self)
        view.header().setSectionsClickable(True)
        view.setRootIsDecorated(False)
        view.setAlternatingRowColors(True)

        view.setModel(self.model)
        view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        view.setSelectionMode(0)
        view.setColumnWidth(0,150)
        view.setColumnWidth(1,400)

        f = QFrame()
        layout.setRowMinimumHeight(0, 25)
        
        layout.addWidget(f,0,0)
        layout.addWidget(view,1,0)
        #--------------
        
        self.setLayout(layout)
        
    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        br = QtGui.QBrush(QtGui.QColor(255,255,255,0),1)
        qp.setBrush(br)
        qp.setPen(QPen(QtGui.QColor(0,0,0), 1))
        qp.drawText(10,20,'Files')
        
        qp.setPen(QPen(QtGui.QColor(140,140,140), 1))
        qp.drawRect(0,0,311,306)
        qp.drawRect(0,0,311,31)
        
    def loadValues(self):
        x = self.mainWindow.data.outputList[self.mainWindow.canvas.currentShape]
        
        if len(x) > 0:
            
            for i in range(self.model.rowCount()):
                self.model.takeRow(i)
            self.model.setRowCount(0)
            
            for i in x:        
                self.model.insertRow(0)
                self.model.setData(self.model.index(0, self.file), ''.join(i[0:1]))
                self.model.setData(self.model.index(0, self.link), '|'.join(i[1:]))
        else:
            for i in range(self.model.rowCount()):
                self.model.takeRow(i)
            self.model.setRowCount(0)
            
        self.update()


#sort
class sort(QFrame):
    
    file,link = range(2)
    
    def __init__(self,window):
        super().__init__()
        self.mainWindow = window
        
        layout = QGridLayout()
        layout.setContentsMargins(0,0,0,0)
        
        #--------------
        self.model = QStandardItemModel(0, 2, self)
        self.model.setHeaderData(self.file, Qt.Horizontal, 'File')
        self.model.setHeaderData(self.link, Qt.Horizontal, 'Link')

        #QTreeView for links
        view = QTreeView(self)
        view.header().setSectionsClickable(True)
        view.setRootIsDecorated(False)
        view.setAlternatingRowColors(True)

        view.setModel(self.model)
        view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        view.setSelectionMode(0)
        view.setColumnWidth(0,150)
        view.setColumnWidth(1,400)

        f = QFrame()
        layout.setRowMinimumHeight(0, 25)
        
        layout.addWidget(f,0,0)
        layout.addWidget(view,1,0)
        #--------------
        
        self.setLayout(layout)
        
    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        br = QtGui.QBrush(QtGui.QColor(255,255,255,0),1)
        qp.setBrush(br)
        qp.setPen(QPen(QtGui.QColor(0,0,0), 1))
        qp.drawText(10,20,'Files')
        
        qp.setPen(QPen(QtGui.QColor(140,140,140), 1))
        qp.drawRect(0,0,311,306)
        qp.drawRect(0,0,311,31)
        
    def loadValues(self):
        x = self.mainWindow.data.outputList[self.mainWindow.canvas.currentShape]
        
        if len(x) > 0:
            
            for i in range(self.model.rowCount()):
                self.model.takeRow(i)
            self.model.setRowCount(0)
            
            for i in x:        
                self.model.insertRow(0)
                self.model.setData(self.model.index(0, self.file), ''.join(i[0:1]))
                self.model.setData(self.model.index(0, self.link), '|'.join(i[1:]))
        else:
            for i in range(self.model.rowCount()):
                self.model.takeRow(i)
            self.model.setRowCount(0)
            
        self.update()


#object detector
class object(QFrame):
    
    def __init__(self,window):
        super().__init__()
        self.mainWindow = window
        
        self.xp = ''
        
    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        br = QtGui.QBrush(QtGui.QColor(255,255,255,0),1)
        qp.setBrush(br)
        qp.setPen(QPen(QtGui.QColor(0,0,0), 1))
        qp.drawText(10,20,'Object XPath')
        
        qp.drawText(10,53,self.xp)
        
        qp.setPen(QPen(QtGui.QColor(140,140,140), 1))
        qp.drawRect(0,0,311,306)
        qp.drawRect(0,0,311,31)
        
    def loadValues(self):
    
        x = self.mainWindow.data.outputList[self.mainWindow.canvas.currentShape]
        
        if len(x) > 0:
            self.xp = x[0]
        else:
            self.xp = ''
            
        self.update()


#keys
class keys(QFrame):
    
    def __init__(self,window):
        super().__init__()
        self.mainWindow = window
        
    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        br = QtGui.QBrush(QtGui.QColor(255,255,255,0),1)
        qp.setBrush(br)
        qp.setPen(QPen(QtGui.QColor(0,0,0), 1))
        qp.drawText(10,20,'Keys')

        qp.setPen(QPen(QtGui.QColor(140,140,140), 1))
        qp.drawRect(0,0,311,306)
        qp.drawRect(0,0,311,31)
        
    def loadValues(self):
        pass


#mouse
class mouse(QFrame):
    
    def __init__(self,window):
        super().__init__()
        self.mainWindow = window
        
    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        br = QtGui.QBrush(QtGui.QColor(255,255,255,0),1)
        qp.setBrush(br)
        qp.setPen(QPen(QtGui.QColor(0,0,0), 1))
        qp.drawText(10,20,'Mouse')

        qp.setPen(QPen(QtGui.QColor(140,140,140), 1))
        qp.drawRect(0,0,311,306)
        qp.drawRect(0,0,311,31)
        
    def loadValues(self):
        pass


#delay
class delay(QFrame):
    
    def __init__(self,window):
        super().__init__()
        self.mainWindow = window
        
    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        br = QtGui.QBrush(QtGui.QColor(255,255,255,0),1)
        qp.setBrush(br)
        qp.setPen(QPen(QtGui.QColor(0,0,0), 1))
        qp.drawText(10,20,'Delay')

        qp.setPen(QPen(QtGui.QColor(140,140,140), 1))
        qp.drawRect(0,0,311,306)
        qp.drawRect(0,0,311,31)
        
    def loadValues(self):
        pass


#filter
class filter(QFrame):
    
    file,link = range(2)
    
    def __init__(self,window):
        super().__init__()
        self.mainWindow = window
        
        layout = QGridLayout()
        layout.setContentsMargins(0,0,0,0)
        
        #--------------
        self.model = QStandardItemModel(0, 2, self)
        self.model.setHeaderData(self.file, Qt.Horizontal, 'File')
        self.model.setHeaderData(self.link, Qt.Horizontal, 'Link')

        #QTreeView for links
        view = QTreeView(self)
        view.header().setSectionsClickable(True)
        view.setRootIsDecorated(False)
        view.setAlternatingRowColors(True)

        view.setModel(self.model)
        view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        view.setSelectionMode(0)
        view.setColumnWidth(0,150)
        view.setColumnWidth(1,400)

        f = QFrame()
        layout.setRowMinimumHeight(0, 25)
        
        layout.addWidget(f,0,0)
        layout.addWidget(view,1,0)
        #--------------
        
        self.setLayout(layout)
        
    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        br = QtGui.QBrush(QtGui.QColor(255,255,255,0),1)
        qp.setBrush(br)
        qp.setPen(QPen(QtGui.QColor(0,0,0), 1))
        qp.drawText(10,20,'Files')
        
        qp.setPen(QPen(QtGui.QColor(140,140,140), 1))
        qp.drawRect(0,0,311,306)
        qp.drawRect(0,0,311,31)
        
    def loadValues(self):
        x = self.mainWindow.data.outputList[self.mainWindow.canvas.currentShape]
        
        if len(x) > 0:
            
            for i in range(self.model.rowCount()):
                self.model.takeRow(i)
            self.model.setRowCount(0)
            
            for i in x:        
                self.model.insertRow(0)
                self.model.setData(self.model.index(0, self.file), ''.join(i[0:1]))
                self.model.setData(self.model.index(0, self.link), '|'.join(i[1:]))
        else:
            for i in range(self.model.rowCount()):
                self.model.takeRow(i)
            self.model.setRowCount(0)
            
        self.update()


#dbcon
class dbcon(QFrame):
    
    def __init__(self,window):
        super().__init__()
        self.mainWindow = window
        
        self.xp = ''
        
    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        br = QtGui.QBrush(QtGui.QColor(255,255,255,0),1)
        qp.setBrush(br)
        qp.setPen(QPen(QtGui.QColor(0,0,0), 1))
        qp.drawText(10,20,'DB Con')
        
        qp.drawText(10,53,self.xp)
        
        qp.setPen(QPen(QtGui.QColor(140,140,140), 1))
        qp.drawRect(0,0,311,306)
        qp.drawRect(0,0,311,31)
        
    def loadValues(self):
    
        x = self.mainWindow.data.outputList[self.mainWindow.canvas.currentShape]
        
        if len(x) > 0:
            self.xp = x[0]
        else:
            self.xp = ''
            
        self.update()


#table
class table(QFrame):
    
    def __init__(self,window):
        super().__init__()
        self.mainWindow = window
        
    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        br = QtGui.QBrush(QtGui.QColor(255,255,255,0),1)
        qp.setBrush(br)
        qp.setPen(QPen(QtGui.QColor(0,0,0), 1))
        qp.drawText(10,20,'Table')

        qp.setPen(QPen(QtGui.QColor(140,140,140), 1))
        qp.drawRect(0,0,311,306)
        qp.drawRect(0,0,311,31)
        
    def loadValues(self):
        pass


#column
class column(QFrame):
    
    def __init__(self,window):
        super().__init__()
        self.mainWindow = window
        
    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        br = QtGui.QBrush(QtGui.QColor(255,255,255,0),1)
        qp.setBrush(br)
        qp.setPen(QPen(QtGui.QColor(0,0,0), 1))
        qp.drawText(10,20,'Column')

        qp.setPen(QPen(QtGui.QColor(140,140,140), 1))
        qp.drawRect(0,0,311,306)
        qp.drawRect(0,0,311,31)
        
    def loadValues(self):
        pass


#download
class download(QFrame):
    
    def __init__(self,window):
        super().__init__()
        self.mainWindow = window
        
        self.total = 0
        self.downloaded = 0
        self.skipped = 0
        self.failed = 0
        
    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        br = QtGui.QBrush(QtGui.QColor(255,255,255,0),1)
        qp.setBrush(br)
        qp.setPen(QPen(QtGui.QColor(0,0,0), 1))
        qp.drawText(10,20,'Download status')
        
        qp.drawText(10,53,'Total files')
        qp.drawText(10,73,'Downloaded')
        qp.drawText(10,93,'Skipped')
        qp.drawText(10,113,'Failed')
        
        qp.drawText(80,53,': '+str(self.total))
        qp.drawText(80,73,': '+str(self.downloaded))
        qp.drawText(80,93,': '+str(self.skipped))
        qp.drawText(80,113,': '+str(self.failed))
        
        qp.setPen(QPen(QtGui.QColor(140,140,140), 1))
        qp.drawRect(0,0,311,306)
        qp.drawRect(0,0,311,31)
        
    def loadValues(self):
    
        x = self.mainWindow.data.outputList[self.mainWindow.canvas.currentShape]
        
        if len(x) > 0:
            self.total = x[0]
            self.downloaded = x[1]
            self.skipped = x[2]
            self.failed = x[3]
        else:
            self.total = 0
            self.downloaded = 0
            self.skipped = 0
            self.failed = 0
            
        self.update()


class Output(QtWidgets.QFrame):

    def __init__(self,window):
        super().__init__()
        self.mainWindow = window

        #Object of all 48 frames
        self.t00 = notool(self.mainWindow)
        t01 = start(self.mainWindow)
        t02 = url(self.mainWindow)
        t03 = crawler(self.mainWindow)
        t04 = media(self.mainWindow)
        t05 = rename(self.mainWindow)
        t06 = sort(self.mainWindow)
        t07 = object(self.mainWindow)
        t08 = keys(self.mainWindow)
        t09 = mouse(self.mainWindow)
        t10 = delay(self.mainWindow)
        t11 = filter(self.mainWindow)
        t12 = dbcon(self.mainWindow)
        t13 = table(self.mainWindow)
        t14 = column(self.mainWindow)
        t15 = download(self.mainWindow)
        
        #Create stacked-view and add all the frames into stacked-view
        self.stackedView = QStackedWidget(self)        
        self.stackedView.addWidget(self.t00)
        self.stackedView.addWidget(t01)
        self.stackedView.addWidget(t02)
        self.stackedView.addWidget(t03)
        self.stackedView.addWidget(t04)
        self.stackedView.addWidget(t05)
        self.stackedView.addWidget(t06)
        self.stackedView.addWidget(t07)
        self.stackedView.addWidget(t08)
        self.stackedView.addWidget(t09)
        self.stackedView.addWidget(t10)
        self.stackedView.addWidget(t11)
        self.stackedView.addWidget(t12)
        self.stackedView.addWidget(t13)
        self.stackedView.addWidget(t14)
        self.stackedView.addWidget(t15)
		
        layout = QGridLayout(self)
        layout.addWidget(self.stackedView)
        
        self.setLayout(layout)
        self.stackedView.setCurrentIndex(self.mainWindow.data.ci)
        
        
    def paintEvent(self, event):
    
        qp = QtGui.QPainter(self)
        br = QtGui.QBrush(QtGui.QColor(255,255,255,0),1)
        qp.setBrush(br)
        qp.setPen(QPen(QtGui.QColor(140,140,140), 1))
        qp.drawRect(0,-1,329,326)

#========================================================================================================================