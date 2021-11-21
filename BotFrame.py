import sys
import os
import json
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import *
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

import Dialog
#========================================================================================================================
    
class Bots(QtWidgets.QFrame):

    botName,period,nextRun = range(3)

    def __init__(self, window):
        super().__init__()
        self.mainWindow = window
        
        self.setMouseTracking(True)
        layout = QGridLayout()
        
        #--------------
        self.model = QStandardItemModel(0, 3, self)
        self.model.setHeaderData(self.botName, Qt.Horizontal, 'Bot Name')
        self.model.setHeaderData(self.period, Qt.Horizontal, 'Con\'s')
        self.model.setHeaderData(self.nextRun, Qt.Horizontal, 'Tools')
        
        self.path = os.getcwd().replace('\\','/') + '/Bots'
        self.fileName = ''
        
        #filter json files
        self.validBots = list()
        
        for i in os.listdir(self.path):
            if i.split('.')[-1] == 'json':
            
                try:
                    f = open(self.path + '\\' +i)
                    l = f.readlines()
                    if len(l) > 0:
                        if len(l[0]) > 28:
                            if l[0][2:11] == 'PyScrapNZ':
                                self.validBots.append(i)
                except:
                    pass
        
        for i in reversed(self.validBots):
        
            f = open(self.path + '\\' + i)
            jdata = f.readlines()[0]
            f.close()
            data = json.loads(jdata)
        
            self.model.insertRow(0)
            self.model.setData(self.model.index(0, self.botName), i)
            self.model.setData(self.model.index(0, self.period), str(len(data[2])))
            self.model.setData(self.model.index(0, self.nextRun), str(len(data[1])))
        
        #QTreeView for bots
        self.view = QTreeView(self)
        self.view.header().setSectionsClickable(True)
        self.view.setRootIsDecorated(False)
        self.view.setAlternatingRowColors(True)

        self.view.setModel(self.model)
        self.view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.view.setSelectionMode(1)
        self.view.setColumnWidth(0,190)
        self.view.setColumnWidth(1,60)
        self.view.setColumnWidth(2,60)
        
        #Tree-view events
        self.view.doubleClicked.connect(self.openFile)

        f = QFrame()
        layout.setRowMinimumHeight(0, 20)
        layout.setRowMinimumHeight(2, 32)
        
        layout.addWidget(self.view,1,0)
        layout.addWidget(f,2,0)
        #--------------
        
        self.setLayout(layout)
        
        self.buttonNew = QPushButton('',self)
        self.buttonNew.setGeometry(9,286,30,30)
        self.buttonNew.clicked.connect(self.newFile)
        self.buttonNew.setIcon(QtGui.QIcon('Images/Icons/new.png'))
        self.buttonNew.setIconSize(QtCore.QSize(20,20))
        self.buttonNew.setToolTip('New Bot')
        
        self.buttonSave = QPushButton('',self)
        self.buttonSave.setGeometry(38,286,30,30)
        self.buttonSave.clicked.connect(self.saveFile)
        self.buttonSave.setIcon(QtGui.QIcon('Images/Icons/save.png'))
        self.buttonSave.setIconSize(QtCore.QSize(20,20))
        self.buttonSave.setToolTip('Save Bot')
        
        self.buttonOpen = QPushButton('',self)
        self.buttonOpen.setGeometry(67,286,30,30)
        self.buttonOpen.clicked.connect(self.openFile)
        self.buttonOpen.setIcon(QtGui.QIcon('Images/Icons/open.png'))
        self.buttonOpen.setIconSize(QtCore.QSize(20,20))
        self.buttonOpen.setToolTip('Open Bot')
        
        self.buttonRefresh = QPushButton('',self)
        self.buttonRefresh.setGeometry(96,286,30,30)
        self.buttonRefresh.clicked.connect(self.refresh)
        self.buttonRefresh.setIcon(QtGui.QIcon('Images/Icons/refresh.png'))
        self.buttonRefresh.setIconSize(QtCore.QSize(20,20))
        self.buttonRefresh.setToolTip('Refresh Bot-List')
        
        self.buttonBrowse = QPushButton('',self)
        self.buttonBrowse.setGeometry(125,286,30,30)
        self.buttonBrowse.clicked.connect(self.browse)
        self.buttonBrowse.setIcon(QtGui.QIcon('Images/Icons/browse.png'))
        self.buttonBrowse.setIconSize(QtCore.QSize(20,20))
        self.buttonBrowse.setToolTip('Browse')
        
        self.lbl = self.path + ' '
        
        self.fileDialog = QFileDialog()
        self.fileDialog.setFileMode(QFileDialog.Directory)
        
        
    def paintEvent(self, event):
    
        qp = QtGui.QPainter(self)
        br = QtGui.QBrush(QtGui.QColor(255,255,255,0),1)
        qp.setBrush(br)
        qp.setFont(QFont('Sans Serif', 9))
        
        qp.drawText(170,306,'...'+self.lbl[-20:-1])
        qp.drawText(12,20,'Existing Bots : ')
        
        qp.setPen(QPen(QtGui.QColor(140,140,140), 1))
        qp.drawRect(0,-1,329,326)
        
        qp.drawRect(163,287,156,27)
        
        
    def newFile(self):
    
        if self.mainWindow.data.fileChanged:
            d = Dialog.YesNoDialog(self.mainWindow)
            d.setTitle('File not saved')
            d.setMessage('Save previous file?')
            
            if d.exec_() == 1:
                self.saveFile()
            
        self.mainWindow.canvas.previousShape = 0
        self.mainWindow.canvas.currentShape = 0
        self.mainWindow.input.stackedView.setCurrentIndex(0)
        self.mainWindow.output.stackedView.setCurrentIndex(0)
        self.mainWindow.tool = 0
        self.mainWindow.data.loadFile = True
        self.fileName = ''
        
        self.mainWindow.title.currentPath = 'Untitled.json'
        self.mainWindow.title.currentPath = self.mainWindow.title.currentPath.replace('\\', '/')
        self.mainWindow.title.update()
        
        self.mainWindow.canvas.shapes = list()
        self.mainWindow.canvas.rects = list()
        self.mainWindow.canvas.connections = list()
        self.mainWindow.data.inputList = list()
        self.mainWindow.data.outputList = list()
        
        self.mainWindow.canvas.titleT = ''
        self.mainWindow.canvas.titleS = 8
        self.mainWindow.canvas.titleX = 20
        self.mainWindow.canvas.titleY = 20
        
        self.mainWindow.input.t00.titleT.setText('')
        self.mainWindow.input.t00.titleS.setValue(8)
        self.mainWindow.input.t00.titleX.setValue(20)
        self.mainWindow.input.t00.titleY.setValue(20)
        
        self.mainWindow.canvas.canvasWidth = 650
        self.mainWindow.canvas.canvasHeight = 650
        self.mainWindow.canvas.sh.setValue(0)
        self.mainWindow.canvas.sv.setValue(100)
        self.mainWindow.canvas.xBias = 0
        self.mainWindow.canvas.yBias = 0
        self.mainWindow.canvas.f = 0
        self.mainWindow.output.t00.t = 0
        self.mainWindow.output.t00.c = 0
        
        self.mainWindow.canvas.update()
        self.mainWindow.status.update()
        self.mainWindow.output.t00.update()
        
    def saveFile(self):
    
        if self.fileName == '':
            d = Dialog.SaveDialog(self.mainWindow)
            d.setTitle('Save bot')
            d.setMessage('Enter bot-name : ')
            if d.exec_() == 1:
                self.fileName = self.mainWindow.data.fileName + '.json'
                
                if self.fileName in self.validBots:
                    d = Dialog.YesNoDialog(self.mainWindow)
                    d.setTitle('Bot already exists')
                    d.setMessage('Overwrite bot?')
                    if d.exec_() == 0:
                        self.fileName = ''
                        return
            else:
                return
            
        data = ['PyScrapNZ',self.mainWindow.canvas.shapes,self.mainWindow.canvas.connections,self.mainWindow.canvas.rects]
        data.append(self.mainWindow.data.inputList)
        data.append(self.mainWindow.data.outputList)
        
        x = list()
        x.append(self.mainWindow.canvas.titleT)
        x.append(self.mainWindow.canvas.titleS)
        x.append(self.mainWindow.canvas.titleX)
        x.append(self.mainWindow.canvas.titleY)
        x.append(self.mainWindow.canvas.canvasWidth)
        x.append(self.mainWindow.canvas.canvasHeight)
        x.append(self.mainWindow.canvas.sh.value())
        x.append(self.mainWindow.canvas.sv.value())
        x.append(self.mainWindow.canvas.xBias)
        x.append(self.mainWindow.canvas.yBias)
        x.append(self.mainWindow.canvas.f)
        data.append(x)
        
        jdata = json.dumps(data)
        f = open(self.path + '\\' +self.fileName,'w')
        f.write(jdata)
        f.close()
        self.mainWindow.data.fileChanged = False
        
        self.mainWindow.title.currentPath = self.path + '\\' + self.fileName
        self.mainWindow.title.currentPath = self.mainWindow.title.currentPath.replace('\\', '/')
        
        self.mainWindow.title.update()
        self.mainWindow.status.setMessage('File saved successfully.',0)
        self.mainWindow.status.update()
        
    def openFile(self):
    
        if len(self.view.selectedIndexes()) == 0:
            d = Dialog.MessageDialog(self.mainWindow)
            d.setTitle('Bot not found')
            d.setMessage('Choose bot from bot-list.')
            d.exec_()
            return
        else:
            if self.mainWindow.data.fileChanged:
                d = Dialog.YesNoDialog(self.mainWindow)
                d.setTitle('File not saved')
                d.setMessage('Save previous file?')
                
                if d.exec_() == 1:
                    self.saveFile()
            self.fileName = self.validBots[self.view.selectedIndexes()[0].row()]

        self.mainWindow.canvas.previousShape = 0
        self.mainWindow.canvas.currentShape = 0
        self.mainWindow.input.stackedView.setCurrentIndex(0)
        self.mainWindow.output.stackedView.setCurrentIndex(0)
        self.mainWindow.tool = 0
        self.mainWindow.data.loadFile = True
        self.mainWindow.data.fileChanged = False
        
        self.mainWindow.title.currentPath = self.path + '\\' + self.fileName
        self.mainWindow.title.currentPath = self.mainWindow.title.currentPath.replace('\\', '/')
        self.mainWindow.title.update()

        f = open(self.path + '\\' + self.fileName)
        jdata = f.readlines()[0]
        f.close()
        data = json.loads(jdata)
        
        self.mainWindow.canvas.shapes = data[1]
        self.mainWindow.canvas.connections = data[2]
        self.mainWindow.canvas.rects = data[3]
        self.mainWindow.data.inputList = data[4]
        self.mainWindow.data.outputList = data[5]
        
        self.mainWindow.canvas.titleT = data[6][0]
        self.mainWindow.canvas.titleS = data[6][1]
        self.mainWindow.canvas.titleX = data[6][2]
        self.mainWindow.canvas.titleY = data[6][3]
        
        self.mainWindow.input.t00.titleT.setText(data[6][0])
        self.mainWindow.input.t00.titleS.setValue(data[6][1])
        self.mainWindow.input.t00.titleX.setValue(data[6][2])
        self.mainWindow.input.t00.titleY.setValue(data[6][3])
        
        self.mainWindow.canvas.canvasWidth = data[6][4]
        self.mainWindow.canvas.canvasHeight = data[6][5]
        self.mainWindow.canvas.sh.setValue(data[6][6])
        self.mainWindow.canvas.sv.setValue(data[6][7])
        self.mainWindow.canvas.xBias = data[6][8]
        self.mainWindow.canvas.yBias = data[6][9]
        self.mainWindow.canvas.f = data[6][10]
        
        self.mainWindow.output.t00.t = 0
        self.mainWindow.output.t00.c = 0
        
        self.mainWindow.canvas.update()
        self.mainWindow.status.update()
        self.mainWindow.output.t00.update()
        
        self.mainWindow.status.setMessage('File loaded successfully.',0)
        self.mainWindow.status.update()
        
    def refresh(self):
        self.model.setRowCount(0)
        
        self.validBots = list()
        
        for i in os.listdir(self.path):
            if i.split('.')[-1] == 'json':
            
                try:
                    f = open(self.path + '\\' +i)
                    l = f.readlines()
                    if len(l) > 0:
                        if len(l[0]) > 28:
                            if l[0][2:11] == 'PyScrapNZ':
                                self.validBots.append(i)
                except:
                    pass
        
        for i in reversed(self.validBots):
        
            f = open(self.path + '\\' + i)
            jdata = f.readlines()[0]
            f.close()
            data = json.loads(jdata)
        
            self.model.insertRow(0)
            self.model.setData(self.model.index(0, self.botName), i)
            self.model.setData(self.model.index(0, self.period), str(len(data[2])))
            self.model.setData(self.model.index(0, self.nextRun), str(len(data[1])))
            
    def browse(self):
        if self.fileDialog.exec_():
            self.path = (self.fileDialog.directory().absolutePath())
            self.lbl = self.path + ' '
        self.refresh()
        self.update()
#========================================================================================================================