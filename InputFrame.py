import sys
import os
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
        
        self.titleT = QLineEdit(self)
        self.titleT.setGeometry(70,40,233,20)
        self.titleT.textChanged.connect(self.updateCanvas)
        
        self.titleS = QSpinBox(self)
        self.titleS.setGeometry(70,69,40,20)
        self.titleS.setMinimum(1)
        self.titleS.setMaximum(999)
        self.titleS.setValue(8)
        self.titleS.valueChanged.connect(self.updateCanvas)
        
        self.titleX = QSpinBox(self)
        self.titleX.setGeometry(70,97,40,20)
        self.titleX.setMinimum(0)
        self.titleX.setMaximum(999)
        self.titleX.setValue(20)
        self.titleX.valueChanged.connect(self.updateCanvas)
        
        self.titleY = QSpinBox(self)
        self.titleY.setGeometry(70,126,40,20)
        self.titleY.setMinimum(0)
        self.titleY.setMaximum(999)
        self.titleY.setValue(20)
        self.titleY.valueChanged.connect(self.updateCanvas)
        
    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        br = QtGui.QBrush(QtGui.QColor(255,255,255,0),1)
        qp.setBrush(br)
        qp.setPen(QPen(QtGui.QColor(0,0,0), 1))
        qp.drawText(10,20,'Canvas')
        
        qp.drawText(10,53,'Title Text : ')
        qp.drawText(10,82,'Title Size : ')
        qp.drawText(10,111,'Title X : ')
        qp.drawText(10,140,'Title Y : ')
        
        
        qp.setPen(QPen(QtGui.QColor(140,140,140), 1))
        qp.drawRect(0,0,311,306)
        qp.drawRect(0,0,311,31)
        
    def saveValues(self):
        pass
        
    def loadValues(self):
        pass
        
    def updateCanvas(self):
        
        self.mainWindow.canvas.titleT = self.titleT.text()
        self.mainWindow.canvas.titleS = self.titleS.value()
        self.mainWindow.canvas.titleX = self.titleX.value()
        self.mainWindow.canvas.titleY = self.titleY.value()
        self.mainWindow.canvas.update()
        
        
#start
class start(QFrame):
    
    def __init__(self,window):
        super().__init__()
        self.mainWindow = window 
        
        self.toolName = QLineEdit(self)
        self.toolName.setGeometry(50,40,254,20)
        
    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        br = QtGui.QBrush(QtGui.QColor(255,255,255,0),1)
        qp.setBrush(br)
        qp.setPen(QPen(QtGui.QColor(0,0,0), 1))
        qp.drawText(10,20,'Starting Point of Execution Flow')
        
        qp.drawText(10,53,'Name : ')
        
        qp.setPen(QPen(QtGui.QColor(140,140,140), 1))
        qp.drawRect(0,0,311,306)
        qp.drawRect(0,0,311,31)
        
    def saveValues(self):
        if self.mainWindow.canvas.previousShape != -1:
            x = [self.toolName.text()]
            self.mainWindow.data.inputList[self.mainWindow.canvas.previousShape] = x
        
    def loadValues(self):
        x = self.mainWindow.data.inputList[self.mainWindow.canvas.currentShape]
        
        if len(x) > 0:
            self.toolName.setText(x[0])
        else:
            self.toolName.setText('')
            
            
#url
class url(QFrame):
    
    def __init__(self,window):
        super().__init__()
        self.mainWindow = window 
        
        self.toolName = QLineEdit(self)
        self.toolName.setGeometry(50,40,254,20)
        
        self.url = QTextEdit(self)
        self.url.setText('')
        self.url.setGeometry(50,70,254,86)
        
    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        br = QtGui.QBrush(QtGui.QColor(255,255,255,0),1)
        qp.setBrush(br)
        qp.setPen(QPen(QtGui.QColor(0,0,0), 1))
        qp.drawText(10,20,'Url Provider')
        
        qp.drawText(10,53,'Name : ')
        qp.drawText(10,80,'Url : *')
        qp.drawText(10,296,'* Use http:// or https://')
        
        qp.setPen(QPen(QtGui.QColor(140,140,140), 1))
        qp.drawRect(0,0,311,306)
        qp.drawRect(0,0,311,31)
        
    def saveValues(self):
        if self.mainWindow.canvas.previousShape != -1:
            x = [self.toolName.text(),self.url.toPlainText()]
            self.mainWindow.data.inputList[self.mainWindow.canvas.previousShape] = x
        
    def loadValues(self):
        x = self.mainWindow.data.inputList[self.mainWindow.canvas.currentShape]
        
        if len(x) > 0:
            self.toolName.setText(x[0])
            self.url.setText(x[1])
        else:
            self.toolName.setText('')
            self.url.setText('http://localhost/home.html')


#crawler
class crawler(QFrame):
    
    def __init__(self,window):
        super().__init__()
        self.mainWindow = window
        
        self.toolName = QLineEdit(self)
        self.toolName.setGeometry(50,40,254,20)
        
        self.levels = QSpinBox(self)
        self.levels.setGeometry(90,68,40,20)
        self.levels.setMinimum(0)
        
        self.external = QCheckBox(self)
        self.external.setGeometry(10,100,15,15)
        
    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        br = QtGui.QBrush(QtGui.QColor(255,255,255,0),1)
        qp.setBrush(br)
        qp.setPen(QPen(QtGui.QColor(0,0,0), 1))
        qp.drawText(10,20,'Web Crawler')
        
        qp.drawText(10,53,'Name : ')
        qp.drawText(10,82,'No. of Levels : ')
        qp.drawText(30,112,'Explore External Links')
        
        qp.setPen(QPen(QtGui.QColor(140,140,140), 1))
        qp.drawRect(0,0,311,306)
        qp.drawRect(0,0,311,31)
        
    def saveValues(self):
        if self.mainWindow.canvas.previousShape != -1:
            x = [self.toolName.text(),self.levels.value(),self.external.checkState()]
            self.mainWindow.data.inputList[self.mainWindow.canvas.previousShape] = x
        
    def loadValues(self):
        x = self.mainWindow.data.inputList[self.mainWindow.canvas.currentShape]
        if len(x) > 0:
            self.toolName.setText(x[0])
            self.levels.setValue(x[1])
            self.external.setCheckState(x[2])
        else:
            self.toolName.setText('')
            self.levels.setValue(0)
            self.external.setCheckState(False)

            
#media
class media(QFrame):
    
    def __init__(self,window):
        super().__init__()
        self.mainWindow = window
        
        self.toolName = QLineEdit(self)
        self.toolName.setGeometry(50,40,254,20)
        
        self.images = QCheckBox(self)
        self.images.setGeometry(10,70,15,15)
        
        self.documents = QCheckBox(self)
        self.documents.setGeometry(10,90,15,15)
        
        self.other = QCheckBox(self)
        self.other.setGeometry(10,110,15,15)
        
    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        br = QtGui.QBrush(QtGui.QColor(255,255,255,0),1)
        qp.setBrush(br)
        qp.setPen(QPen(QtGui.QColor(0,0,0), 1))
        qp.drawText(10,20,'Media Extractor')
        
        qp.drawText(10,53,'Name : ')
        qp.drawText(30,82,'Images')
        qp.drawText(30,102,'Documents')
        qp.drawText(30,122,'Other')
        
        qp.setPen(QPen(QtGui.QColor(140,140,140), 1))
        qp.drawRect(0,0,311,306)
        qp.drawRect(0,0,311,31)

    def saveValues(self):
        if self.mainWindow.canvas.previousShape != -1:
            x = [self.toolName.text(),self.images.checkState(),self.documents.checkState(),self.other.checkState()]
            self.mainWindow.data.inputList[self.mainWindow.canvas.previousShape] = x
        
    def loadValues(self):
        x = self.mainWindow.data.inputList[self.mainWindow.canvas.currentShape]
        
        if len(x) > 0:
            self.toolName.setText(x[0])
            self.images.setCheckState(x[1])
            self.documents.setCheckState(x[2])
            self.other.setCheckState(x[3])
        else:
            self.toolName.setText('')
            self.images.setCheckState(False)
            self.documents.setCheckState(False)
            self.other.setCheckState(False)


#rename
class rename(QFrame):
    
    def __init__(self,window):
        super().__init__()
        self.mainWindow = window
        
        self.toolName = QLineEdit(self)
        self.toolName.setGeometry(50,40,254,20)
        
        #Radio buttons 3
        self.extract = QRadioButton('Extract',self)
        self.extract.setGeometry(10,75,70,15)
        self.extract.setChecked(True)
        
        self.existing = QRadioButton('Existing',self)
        self.existing.setGeometry(10,95,70,15)
        
        self.custom = QRadioButton('Custom',self)
        self.custom.setGeometry(10,115,70,15)
        
        #Spin boxes 4
        self.link = QSpinBox(self)
        self.link.setGeometry(80,72,40,20)
        self.link.setMinimum(0)
        
        self.word = QSpinBox(self)
        self.word.setGeometry(125,72,40,20)
        self.word.setMinimum(0)
        
        self.subStringFrom = QSpinBox(self)
        self.subStringFrom.setGeometry(205,72,40,20)
        self.subStringFrom.setMinimum(0)
        
        self.subStringTo = QSpinBox(self)
        self.subStringTo.setGeometry(263,72,40,20)
        self.subStringTo.setMinimum(0)
        
        #Custom Word
        self.customWord = QLineEdit(self)
        self.customWord.setGeometry(80,112,225,20)
        
        #List
        self.wordList = QListWidget(self)
        self.wordList.setGeometry(6,141,270,110)
                
        #Buttons 4
        self.buttonAdd = QPushButton('', self)
        self.buttonAdd.setGeometry(281,140,25,25)
        self.buttonAdd.clicked.connect(self.itemAdd)
        self.buttonAdd.setIcon(QtGui.QIcon('Images/Icons/left.png'))
        self.buttonAdd.setIconSize(QtCore.QSize(20,20))
        self.buttonAdd.setToolTip('Add Record')
        
        self.buttonDelete = QPushButton('', self)
        self.buttonDelete.setGeometry(281,169,25,25)
        self.buttonDelete.clicked.connect(self.itemDelete)
        self.buttonDelete.setIcon(QtGui.QIcon('Images/Icons/right.png'))
        self.buttonDelete.setIconSize(QtCore.QSize(20,20))
        self.buttonDelete.setToolTip('Remove Record')
        
        self.buttonUp = QPushButton('', self)
        self.buttonUp.setGeometry(281,198,25,25)
        self.buttonUp.clicked.connect(self.itemUp)
        self.buttonUp.setIcon(QtGui.QIcon('Images/Icons/up.png'))
        self.buttonUp.setIconSize(QtCore.QSize(20,20))
        self.buttonUp.setToolTip('Move Record Up')
        
        self.buttonDown = QPushButton('', self)
        self.buttonDown.setGeometry(281,227,25,25)
        self.buttonDown.clicked.connect(self.itemDown)
        self.buttonDown.setIcon(QtGui.QIcon('Images/Icons/down.png'))
        self.buttonDown.setIconSize(QtCore.QSize(20,20))
        self.buttonDown.setToolTip('Move Record Down')
        
        #Combo box 2
        self.separator = QComboBox(self)
        self.separator.setGeometry(125,256,60,20)
        self.separator.addItem('Null')
        self.separator.addItem('Space')
        self.separator.addItem('-')
        
        self.notFound = QComboBox(self)
        self.notFound.setGeometry(125,281,60,20)
        self.notFound.addItem('Null')
        self.notFound.addItem('Space')
        self.notFound.addItem('*')
        
    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        br = QtGui.QBrush(QtGui.QColor(255,255,255,0),1)
        qp.setBrush(br)
        qp.setPen(QPen(QtGui.QColor(0,0,0), 1))
        qp.drawText(10,20,'Rename Media')
        qp.drawText(10,53,'Name : ')
        qp.drawText(180,86,'Sub')
        qp.drawText(250,86,'to')
        
        qp.drawText(10,270,'Select Separator Char: ')
        qp.drawText(10,295,'Not Found Character : ')
        
        qp.setPen(QPen(QtGui.QColor(140,140,140), 1))
        qp.drawRect(0,0,311,306)
        qp.drawRect(0,0,311,31)

    def saveValues(self):
        if self.mainWindow.canvas.previousShape != -1:
            x = [self.toolName.text()]
            x = x + [self.extract.isChecked(),self.existing.isChecked(),self.custom.isChecked()]
            x = x + [self.link.value(),self.word.value(),self.subStringFrom.value(),self.subStringTo.value()]
            x.append(self.customWord.text())
            
            items=[]
            for i in range(self.wordList.count()):
                items.append(self.wordList.item(i).text())
                
            x.append(items)
            x.append(self.separator.currentIndex())
            x.append(self.notFound.currentIndex())
            
            self.mainWindow.data.inputList[self.mainWindow.canvas.previousShape] = x
        
    def loadValues(self):
        x = self.mainWindow.data.inputList[self.mainWindow.canvas.currentShape]
        
        if len(x) > 0:
            self.toolName.setText(x[0])
            self.extract.setChecked(x[1])
            self.existing.setChecked(x[2])
            self.custom.setChecked(x[3])
            self.link.setValue(x[4])
            self.word.setValue(x[5])
            self.subStringFrom.setValue(x[6])
            self.subStringTo.setValue(x[7])
            self.customWord.setText(x[8])
            self.wordList.clear()
            self.wordList.addItems(x[9])
            self.separator.setCurrentIndex(x[10])
            self.notFound.setCurrentIndex(x[11])
        else:
            self.toolName.setText('')
            self.extract.setChecked(True)
            self.existing.setChecked(False)
            self.custom.setChecked(False)
            self.link.setValue(0)
            self.word.setValue(0)
            self.subStringFrom.setValue(0)
            self.subStringTo.setValue(0)
            self.customWord.setText('')
            self.wordList.clear()
            self.separator.setCurrentIndex(0)
            self.notFound.setCurrentIndex(0)
        
    def itemAdd(self):
        
        if self.extract.isChecked():
            self.wordList.addItem('Extracted from: '+str(self.link.value())+','
            +str(self.word.value())+','
            +str(self.subStringFrom.value())+','
            +str(self.subStringTo.value()))
        elif self.existing.isChecked():
            self.wordList.addItem('Existing')
        else:
            self.wordList.addItem('Custom: '+self.customWord.text())
        
    def itemDelete(self):
        self.wordList.takeItem(self.wordList.currentRow())
        
    def itemUp(self):
        r = self.wordList.currentRow()
        i = self.wordList.takeItem(r)
        self.wordList.insertItem(r-1,i)
        self.wordList.setCurrentRow(r-1)
        
    def itemDown(self):
        r = self.wordList.currentRow()
        i = self.wordList.takeItem(r)
        self.wordList.insertItem(r+1,i)
        self.wordList.setCurrentRow(r+1)

        
#sort
class sort(QFrame):
    
    def __init__(self,window):
        super().__init__()
        self.mainWindow = window
        
        self.toolName = QLineEdit(self)
        self.toolName.setGeometry(50,40,254,20)
        
        self.nameInc = QRadioButton(self)
        self.nameInc.setGeometry(101,83,25,25)
        
        self.nameDec = QRadioButton(self)
        self.nameDec.setGeometry(121,83,25,25)
        
        self.sizeInc = QRadioButton(self)
        self.sizeInc.setGeometry(101,103,25,25)
        
        self.sizeDec = QRadioButton(self)
        self.sizeDec.setGeometry(121,103,25,25)
        self.sizeDec.setChecked(True)
        
        self.group = QCheckBox('Group by level',self)
        self.group.setGeometry(10,140,150,25)
        
    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        br = QtGui.QBrush(QtGui.QColor(255,255,255,0),1)
        qp.setBrush(br)
        qp.setPen(QPen(QtGui.QColor(0,0,0), 1))
        qp.drawText(10,20,'Sort')
        
        qp.drawText(10,53,'Name : ')
        
        qp.drawText(10,100,'Sort by Name : ')
        qp.drawText(10,120,'Sort by Size : ')
        qp.drawText(100,80,'Inc')
        qp.drawText(120,80,'Dec')
        
        qp.setPen(QPen(QtGui.QColor(140,140,140), 1))
        qp.drawRect(0,0,311,306)
        qp.drawRect(0,0,311,31)
        
    def saveValues(self):
        if self.mainWindow.canvas.previousShape != -1:
            x = [self.toolName.text()]
            x.append(self.nameInc.isChecked())
            x.append(self.nameDec.isChecked())
            x.append(self.sizeInc.isChecked())
            x.append(self.sizeDec.isChecked())
            x.append(self.group.checkState())
            self.mainWindow.data.inputList[self.mainWindow.canvas.previousShape] = x
        
    def loadValues(self):
        x = self.mainWindow.data.inputList[self.mainWindow.canvas.currentShape]
        
        if len(x) > 0:
            self.toolName.setText(x[0])
            self.nameInc.setChecked(x[1])
            self.nameDec.setChecked(x[2])
            self.sizeInc.setChecked(x[3])
            self.sizeDec.setChecked(x[4])
            self.group.setCheckState(x[5])
        else:
            self.toolName.setText('')
            self.nameInc.setChecked(False)
            self.nameDec.setChecked(False)
            self.sizeInc.setChecked(False)
            self.sizeDec.setChecked(True)
            self.group.setCheckState(False)

            
#object
class object(QFrame):
    
    def __init__(self,window):
        super().__init__()
        self.mainWindow = window
        
        self.toolName = QLineEdit(self)
        self.toolName.setGeometry(50,40,254,20)
        
        self.xPath = QTextEdit(self)
        self.xPath.setText('')
        self.xPath.setGeometry(50,70,254,86)
        
    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        br = QtGui.QBrush(QtGui.QColor(255,255,255,0),1)
        qp.setBrush(br)
        qp.setPen(QPen(QtGui.QColor(0,0,0), 1))
        qp.drawText(10,20,'Object Detector')
        
        qp.drawText(10,53,'Name : ')
        qp.drawText(10,80,'XPath : ')
        
        qp.setPen(QPen(QtGui.QColor(140,140,140), 1))
        qp.drawRect(0,0,311,306)
        qp.drawRect(0,0,311,31)
        
    def saveValues(self):
        if self.mainWindow.canvas.previousShape != -1:
            x = [self.toolName.text(),self.xPath.toPlainText()]
            self.mainWindow.data.inputList[self.mainWindow.canvas.previousShape] = x
        
    def loadValues(self):
        x = self.mainWindow.data.inputList[self.mainWindow.canvas.currentShape]
        
        if len(x) > 0:
            self.toolName.setText(x[0])
            self.xPath.setText(x[1])
        else:
            self.toolName.setText('')
            self.xPath.setText('')
        
        
#keys
class keys(QFrame):
    
    def __init__(self,window):
        super().__init__()
        self.mainWindow = window
        
        self.toolName = QLineEdit(self)
        self.toolName.setGeometry(50,40,254,20)
        
        self.keySend = QTextEdit(self)
        self.keySend.setText('')
        self.keySend.setGeometry(50,70,254,86)
        
    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        br = QtGui.QBrush(QtGui.QColor(255,255,255,0),1)
        qp.setBrush(br)
        qp.setPen(QPen(QtGui.QColor(0,0,0), 1))
        qp.drawText(10,20,'Keyboard Events')
        
        qp.drawText(10,53,'Name : ')
        qp.drawText(10,80,'Keys : ')
        
        qp.setPen(QPen(QtGui.QColor(140,140,140), 1))
        qp.drawRect(0,0,311,306)
        qp.drawRect(0,0,311,31)
        
    def saveValues(self):
        if self.mainWindow.canvas.previousShape != -1:
            x = [self.toolName.text(),self.keySend.toPlainText()]
            self.mainWindow.data.inputList[self.mainWindow.canvas.previousShape] = x
        
    def loadValues(self):
        x = self.mainWindow.data.inputList[self.mainWindow.canvas.currentShape]
        
        if len(x) > 0:
            self.toolName.setText(x[0])
            self.keySend.setText(x[1])
        else:
            self.toolName.setText('')
            self.keySend.setText('')
        
        
#mouse
class mouse(QFrame):
    
    def __init__(self,window):
        super().__init__()
        self.mainWindow = window
        
        self.toolName = QLineEdit(self)
        self.toolName.setGeometry(50,40,254,20)
        
        #Radio buttons 4
        self.current = QRadioButton('Click at current position',self)
        self.current.setGeometry(10,75,150,15)
        self.current.setChecked(True)
        
        self.clickAt = QRadioButton('Click at ',self)
        self.clickAt.setGeometry(10,100,100,15)
        
        self.scrollUp = QRadioButton('Scroll up',self)
        self.scrollUp.setGeometry(10,125,100,15)
        
        self.scrollDown = QRadioButton('Scroll down',self)
        self.scrollDown.setGeometry(10,150,100,15)
        
        #Spin boxes 4
        self.x = QSpinBox(self)
        self.x.setGeometry(100,97,60,20)
        self.x.setMinimum(0)
        self.x.setMaximum(9999)
        
        self.y = QSpinBox(self)
        self.y.setGeometry(167,97,60,20)
        self.y.setMinimum(0)
        self.y.setMaximum(9999)
        
        self.u = QSpinBox(self)
        self.u.setGeometry(100,122,60,20)
        self.u.setMinimum(0)
        self.u.setMaximum(9999)
        
        self.d = QSpinBox(self)
        self.d.setGeometry(100,147,60,20)
        self.d.setMinimum(0)
        self.d.setMaximum(9999)
        
    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        br = QtGui.QBrush(QtGui.QColor(255,255,255,0),1)
        qp.setBrush(br)
        qp.setPen(QPen(QtGui.QColor(0,0,0), 1))
        qp.drawText(10,20,'Mouse Events')
        
        qp.drawText(10,53,'Name : ')
        
        qp.setPen(QPen(QtGui.QColor(140,140,140), 1))
        qp.drawRect(0,0,311,306)
        qp.drawRect(0,0,311,31)
        
    def saveValues(self):
        if self.mainWindow.canvas.previousShape != -1:
            x = list()
            
            x.append(self.toolName.text())
            x.append(self.current.isChecked())
            x.append(self.clickAt.isChecked())
            x.append(self.scrollUp.isChecked())
            x.append(self.scrollDown.isChecked())
            x.append(self.x.value())
            x.append(self.y.value())
            x.append(self.u.value())
            x.append(self.d.value())
            
            self.mainWindow.data.inputList[self.mainWindow.canvas.previousShape] = x
        
    def loadValues(self):
        x = self.mainWindow.data.inputList[self.mainWindow.canvas.currentShape]
        
        if len(x) > 0:
            self.toolName.setText(x[0])
            self.current.setChecked(x[1])
            self.clickAt.setChecked(x[2])
            self.scrollUp.setChecked(x[3])
            self.scrollDown.setChecked(x[4])
            self.x.setValue(x[5])
            self.y.setValue(x[6])
            self.u.setValue(x[7])
            self.d.setValue(x[8])
        else:
            self.toolName.setText('')
            self.current.setChecked(True)
            self.clickAt.setChecked(False)
            self.scrollUp.setChecked(False)
            self.scrollDown.setChecked(False)
            self.x.setValue(0)
            self.y.setValue(0)
            self.u.setValue(0)
            self.d.setValue(0)
        
        
#delay
class delay(QFrame):
    
    def __init__(self,window):
        super().__init__()
        self.mainWindow = window
        
        self.toolName = QLineEdit(self)
        self.toolName.setGeometry(50,40,254,20)
        
        self.wait = QDoubleSpinBox(self)
        self.wait.setMinimum(0)
        self.wait.setGeometry(50,70,50,20)
        
    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        br = QtGui.QBrush(QtGui.QColor(255,255,255,0),1)
        qp.setBrush(br)
        qp.setPen(QPen(QtGui.QColor(0,0,0), 1))
        qp.drawText(10,20,'Delay')
        
        qp.drawText(10,53,'Name : ')
        qp.drawText(10,85,'Wait : ')
        qp.drawText(105,85,'Second')
        
        qp.setPen(QPen(QtGui.QColor(140,140,140), 1))
        qp.drawRect(0,0,311,306)
        qp.drawRect(0,0,311,31)
        
    def saveValues(self):
        if self.mainWindow.canvas.previousShape != -1:
            x = [self.toolName.text(),self.wait.value()]
            self.mainWindow.data.inputList[self.mainWindow.canvas.previousShape] = x
        
    def loadValues(self):
        x = self.mainWindow.data.inputList[self.mainWindow.canvas.currentShape]
        
        if len(x) > 0:
            self.toolName.setText(x[0])
            self.wait.setValue(x[1])
        else:
            self.toolName.setText('')
            self.wait.setValue(0)
        

#filter
class filter(QFrame):
    
    def __init__(self,window):
        super().__init__()
        self.mainWindow = window 
        
        self.toolName = QLineEdit(self)
        self.toolName.setGeometry(50,40,254,20)
        
        #Radio buttons 2
        self.contains = QRadioButton('Contains : ',self)
        self.contains.setGeometry(10,70,100,25)
        self.contains.setChecked(True)
        
        self.regex = QRadioButton('RegEx : ',self)
        self.regex.setGeometry(10,96,100,25)
        
        #Line Edit 2
        self.containsKey = QLineEdit(self)
        self.containsKey.setGeometry(84,73,150,20)
        
        self.regexKey = QLineEdit(self)
        self.regexKey.setGeometry(84,100,150,20)
        
        #Spin boxes 2
        self.first = QSpinBox(self)
        self.first.setGeometry(60,127,40,20)
        self.first.setMinimum(0)
        self.first.setMaximum(999)
        
        self.last = QSpinBox(self)
        self.last.setGeometry(60,154,40,20)
        self.last.setMinimum(0)
        self.last.setMaximum(999)
        
        #Check Box 1
        self.group = QCheckBox('Group by level',self)
        self.group.setGeometry(10,180,150,25)
        
    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        br = QtGui.QBrush(QtGui.QColor(255,255,255,0),1)
        qp.setBrush(br)
        qp.setPen(QPen(QtGui.QColor(0,0,0), 1))
        qp.drawText(10,20,'Filter')
        
        qp.drawText(10,53,'Name : ')
        
        qp.drawText(10,141,'First n : ')
        qp.drawText(10,168,'Last n : ')
        qp.drawText(103,137,'*')
        qp.drawText(103,164,'*')
        qp.drawText(10,296,'* 0 means all from first/last')
        
        qp.setPen(QPen(QtGui.QColor(140,140,140), 1))
        qp.drawRect(0,0,311,306)
        qp.drawRect(0,0,311,31)
        
    def saveValues(self):
        if self.mainWindow.canvas.previousShape != -1:
            x = [self.toolName.text()]
            x = x + [self.contains.isChecked(),self.regex.isChecked()]
            x = x + [self.containsKey.text(),self.regexKey.text()]
            x = x + [self.first.value(),self.last.value()]
            x.append(self.group.checkState())
            self.mainWindow.data.inputList[self.mainWindow.canvas.previousShape] = x
        
    def loadValues(self):
        x = self.mainWindow.data.inputList[self.mainWindow.canvas.currentShape]
        
        if len(x) > 0:
            self.toolName.setText(x[0])
            self.contains.setChecked(x[1])
            self.regex.setChecked(x[2])
            self.containsKey.setText(x[3])
            self.regexKey.setText(x[4])
            self.first.setValue(x[5])
            self.last.setValue(x[6])
            self.group.setCheckState(x[7])
        else:
            self.toolName.setText('')
            self.contains.setChecked(True)
            self.regex.setChecked(False)
            self.containsKey.setText('')
            self.regexKey.setText('')
            self.first.setValue(0)
            self.last.setValue(0)
            self.group.setCheckState(False)


#dbcon
class dbcon(QFrame):
    
    def __init__(self,window):
        super().__init__()
        self.mainWindow = window
        
        self.toolName = QLineEdit(self)
        self.toolName.setGeometry(50,40,254,20)
        
        #Line Edit 4
        self.host = QLineEdit(self)
        self.host.setGeometry(70,75,214,20)
        
        self.name = QLineEdit(self)
        self.name.setGeometry(70,100,214,20)
        
        self.user = QLineEdit(self)
        self.user.setGeometry(70,125,214,20)
        
        self.password = QLineEdit(self)
        self.password.setGeometry(70,150,214,20)
        self.password.setEchoMode(QLineEdit.Password)
        
    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        br = QtGui.QBrush(QtGui.QColor(255,255,255,0),1)
        qp.setBrush(br)
        qp.setPen(QPen(QtGui.QColor(0,0,0), 1))
        qp.drawText(10,20,'DB Connection')
        
        qp.drawText(10,53,'Name : ')
        
        qp.drawText(10,89,'Host Path : ')
        qp.drawText(10,114,'DB Name : ')
        qp.drawText(10,139,'Login ID : ')
        qp.drawText(10,164,'Password : ')
        
        qp.setPen(QPen(QtGui.QColor(140,140,140), 1))
        qp.drawRect(0,0,311,306)
        qp.drawRect(0,0,311,31)
        
    def saveValues(self):
        if self.mainWindow.canvas.previousShape != -1:
            x = [self.toolName.text(),self.host.text(),self.name.text(),self.user.text(),self.password.text()]
            self.mainWindow.data.inputList[self.mainWindow.canvas.previousShape] = x
        
    def loadValues(self):
        x = self.mainWindow.data.inputList[self.mainWindow.canvas.currentShape]
        
        if len(x) > 0:
            self.toolName.setText(x[0])
            self.host.setText(x[1])
            self.name.setText(x[2])
            self.user.setText(x[3])
            self.password.setText(x[4])
        else:
            self.toolName.setText('')
            self.host.setText('')
            self.name.setText('')
            self.user.setText('')
            self.password.setText('')


#table
class table(QFrame):
    
    def __init__(self,window):
        super().__init__()
        self.mainWindow = window
        
        self.toolName = QLineEdit(self)
        self.toolName.setGeometry(50,40,254,20)
        
        self.tableName = QLineEdit(self)
        self.tableName.setGeometry(80,70,224,20)
        
        self.rowCode = QTextEdit(self)
        self.rowCode.setText('')
        self.rowCode.setGeometry(80,100,224,86)
        
    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        br = QtGui.QBrush(QtGui.QColor(255,255,255,0),1)
        qp.setBrush(br)
        qp.setPen(QPen(QtGui.QColor(0,0,0), 1))
        qp.drawText(10,20,'Table')
        
        qp.drawText(10,53,'Name : ')
        
        qp.drawText(10,84,'Table Name : ')
        qp.drawText(10,114,'Row Code : ')
        
        qp.setPen(QPen(QtGui.QColor(140,140,140), 1))
        qp.drawRect(0,0,311,306)
        qp.drawRect(0,0,311,31)
        
    def saveValues(self):
        if self.mainWindow.canvas.previousShape != -1:
            x = [self.toolName.text(),self.tableName.text(),self.rowCode.toPlainText()]
            self.mainWindow.data.inputList[self.mainWindow.canvas.previousShape] = x
        
    def loadValues(self):
        x = self.mainWindow.data.inputList[self.mainWindow.canvas.currentShape]
        
        if len(x) > 0:
            self.toolName.setText(x[0])
            self.tableName.setText(x[1])
            self.rowCode.setText(x[2])
        else:
            self.toolName.setText('')
            self.tableName.setText('')
            self.rowCode.setText('')
        
        
#column
class column(QFrame):
    
    def __init__(self,window):
        super().__init__()
        self.mainWindow = window
        
        self.toolName = QLineEdit(self)
        self.toolName.setGeometry(50,40,254,20)
        
        self.columnName = QLineEdit(self)
        self.columnName.setGeometry(80,70,224,20)
        
        self.cellCode = QTextEdit(self)
        self.cellCode.setText('')
        self.cellCode.setGeometry(80,100,224,86)
        
        self.pos = QSpinBox(self)
        self.pos.setGeometry(80,195,60,20)
        self.pos.setMinimum(1)
        self.pos.setMaximum(9999)
        
    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        br = QtGui.QBrush(QtGui.QColor(255,255,255,0),1)
        qp.setBrush(br)
        qp.setPen(QPen(QtGui.QColor(0,0,0), 1))
        qp.drawText(10,20,'Column')
        
        qp.drawText(10,53,'Name : ')
        
        qp.drawText(10,84,'Col\'n Name : ')
        qp.drawText(10,114,'Cell Code : ')
        qp.drawText(10,208,'Position : ')
        
        qp.setPen(QPen(QtGui.QColor(140,140,140), 1))
        qp.drawRect(0,0,311,306)
        qp.drawRect(0,0,311,31)
        
    def saveValues(self):
        if self.mainWindow.canvas.previousShape != -1:
            x = [self.toolName.text(),self.columnName.text(),self.cellCode.toPlainText(),self.pos.value()]
            self.mainWindow.data.inputList[self.mainWindow.canvas.previousShape] = x
        
    def loadValues(self):
        x = self.mainWindow.data.inputList[self.mainWindow.canvas.currentShape]
        
        if len(x) > 0:
            self.toolName.setText(x[0])
            self.columnName.setText(x[1])
            self.cellCode.setText(x[2])
            self.pos.setValue(x[3])
        else:
            self.toolName.setText('')
            self.columnName.setText('')
            self.cellCode.setText('')
            self.pos.setValue(1)
        
#Download
class download(QFrame):
    
    def __init__(self,window):
        super().__init__()
        self.mainWindow = window
        
        self.toolName = QLineEdit(self)
        self.toolName.setGeometry(50,40,254,20)
        
        self.fileDialog = QFileDialog()
        self.fileDialog.setFileMode(QFileDialog.Directory)
        
        self.buttonBrowse = QPushButton('Browse',self)
        self.buttonBrowse.setGeometry(255,156,50,25)
        self.buttonBrowse.clicked.connect(self.browseFile)
        
        self.temp = os.getcwd()
        self.temp = self.temp.replace('\\', '/')
        
        self.path = QTextEdit(self)
        self.path.setGeometry(50,70,254,80)
        self.path.setText(self.temp)
        self.path.setReadOnly(True)
        
        self.rename = QRadioButton('Rename files in inceasing order',self)
        self.rename.setGeometry(10,195,200,20)
        self.rename.setChecked(True)
        
        self.replace = QRadioButton('Replace files',self)
        self.replace.setGeometry(10,215,200,20)
        
        self.skip = QRadioButton('Skip files',self)
        self.skip.setGeometry(10,235,200,20)
        
    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        br = QtGui.QBrush(QtGui.QColor(255,255,255,0),1)
        qp.setBrush(br)
        qp.setPen(QPen(QtGui.QColor(0,0,0), 1))
        qp.drawText(10,20,'Download')
        
        qp.drawText(10,53,'Name : ')
        
        qp.drawText(10,85,'Path : ')
        qp.drawText(10,190,'Select action if files are existed : ')
        
        qp.setPen(QPen(QtGui.QColor(140,140,140), 1))
        qp.drawRect(0,0,311,306)
        qp.drawRect(0,0,311,31)
        
    def saveValues(self):
        if self.mainWindow.canvas.previousShape != -1:
            x = [self.toolName.text()]
            x.append(self.path.toPlainText())
            x = x + [self.rename.isChecked(),self.replace.isChecked(),self.skip.isChecked()]
            
            self.mainWindow.data.inputList[self.mainWindow.canvas.previousShape] = x
        
    def loadValues(self):
        x = self.mainWindow.data.inputList[self.mainWindow.canvas.currentShape]
        
        if len(x) > 0:
            self.toolName.setText(x[0])
            self.path.setText(x[1])
            self.rename.setChecked(x[2])
            self.replace.setChecked(x[3])
            self.skip.setChecked(x[4])
            self.fileDialog.setDirectory(x[1])
        else:
            self.toolName.setText('')
            self.path.setText(self.temp)
            self.rename.setChecked(True)
            self.replace.setChecked(False)
            self.skip.setChecked(False)
            self.fileDialog.setDirectory(str(os.getcwd))
        
    def browseFile(self):
        if self.fileDialog.exec_():
            self.path.setText(self.fileDialog.directory().absolutePath())
            
        self.update()


class Input(QtWidgets.QFrame):

    #330 x 325

    def __init__(self,window):
        super().__init__()
        self.mainWindow = window
        
        #Object of all 16 frames
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
        qp.drawRect(0,-1,329,325)

#========================================================================================================================