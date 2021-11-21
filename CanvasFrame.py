import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import *
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
#========================================================================================================================

class Canvas(QtWidgets.QFrame):

    def __init__(self,window):
        super().__init__()
        self.mainWindow = window
        
        self.canvasWidth = 650
        self.canvasHeight = 650
        self.xBias = 0
        self.yBias = 0
        
        self.currentLocation = QtCore.QPoint(-100,-100)
        self.setMouseTracking(True)
        
        self.shapes = list()
        self.connections = list()
        self.rects = list()
        
        self.previousShape = -1
        self.currentShape = -1
        self.currentRect = -1
        
        self.moveFlag = False
        self.connectFlag = False
        self.disconnectFlag = False
        self.rectFlag = False
        self.shiftFlag = False
        self.handFlag = False
        self.handScroll = False
        self.mapFlag = False
        
        self.conA = -1
        self.conB = -1
        
        self.label = QLabel()
        
        self.titleT = ''
        self.titleS = 8
        self.titleX = 20
        self.titleY = 20
        
        self.beginRect = QtCore.QPoint(-100,-100)
        self.endRect = QtCore.QPoint(-100,-100)
        
        #Scale factors
        self.f = 0
        
        #Color directory for MiniMap
        
        self.colDict = {
        0:(255,255,255),
        1:(216,0,39),
        2:(0,112,0),
        3:(0,112,0),
        4:(0,112,0),
        5:(0,112,0),
        6:(0,112,0),
        7:(0,63,140),
        8:(0,63,140),
        9:(0,63,140),
        10:(0,63,140),
        11:(0,112,0),
        12:(60,0,99),
        13:(60,0,99),
        14:(60,0,99),
        15:(60,0,99),
        }
        
        #Tool bar buttons
        
        self.buttonCollapse = QPushButton('',self)
        self.buttonCollapse.setGeometry(610,10,30,30)
        self.buttonCollapse.clicked.connect(self.collapse)
        self.buttonCollapse.setIcon(QtGui.QIcon('Images/Icons/collapse.png'))
        self.buttonCollapse.setIconSize(QtCore.QSize(20,20))
        self.buttonCollapse.setToolTip('Collapse Canvas')
        
        self.buttonExpand = QPushButton('',self)
        self.buttonExpand.setGeometry(581,10,30,30)
        self.buttonExpand.clicked.connect(self.expand)
        self.buttonExpand.setIcon(QtGui.QIcon('Images/Icons/expand.png'))
        self.buttonExpand.setIconSize(QtCore.QSize(20,20))
        self.buttonExpand.setToolTip('Expand Canvas')
        
        self.buttonPlay = QPushButton('',self)
        self.buttonPlay.setGeometry(552,10,30,30)
        self.buttonPlay.clicked.connect(self.playFunction)
        self.buttonPlay.setIcon(QtGui.QIcon('Images/Icons/play.png'))
        self.buttonPlay.setIconSize(QtCore.QSize(20,20))
        self.buttonPlay.setToolTip('Execute Queue')
        self.buttonPlay.setCheckable(True)
        
        self.buttonTest = QPushButton('',self)
        self.buttonTest.setGeometry(523,10,30,30)
        self.buttonTest.clicked.connect(self.coreFunction)
        self.buttonTest.setIcon(QtGui.QIcon('Images/Icons/test.png'))
        self.buttonTest.setIconSize(QtCore.QSize(20,20))
        self.buttonTest.setToolTip('Test Module')
        
        self.buttonDelete = QPushButton('',self)
        self.buttonDelete.setGeometry(494,10,30,30)
        self.buttonDelete.clicked.connect(self.deleteShape)
        self.buttonDelete.setIcon(QtGui.QIcon('Images/Icons/delete.png'))
        self.buttonDelete.setIconSize(QtCore.QSize(20,20))
        self.buttonDelete.setToolTip('Delete')
        
        self.buttonDisconnect = QPushButton('',self)
        self.buttonDisconnect.setGeometry(465,10,30,30)
        self.buttonDisconnect.clicked.connect(self.disconnectShapes)
        self.buttonDisconnect.setIcon(QtGui.QIcon('Images/Icons/disconnect.png'))
        self.buttonDisconnect.setIconSize(QtCore.QSize(20,20))
        self.buttonDisconnect.setToolTip('Disonnect')
        self.buttonDisconnect.setCheckable(True)
        
        self.buttonConnect = QPushButton('',self)
        self.buttonConnect.setGeometry(436,10,30,30)
        self.buttonConnect.clicked.connect(self.connectShapes)
        self.buttonConnect.setIcon(QtGui.QIcon('Images/Icons/connect.png'))
        self.buttonConnect.setIconSize(QtCore.QSize(20,20))
        self.buttonConnect.setToolTip('Connect')
        self.buttonConnect.setCheckable(True)
        
        self.buttonRect = QPushButton('',self)
        self.buttonRect.setGeometry(407,10,30,30)
        self.buttonRect.clicked.connect(self.drawRects)
        self.buttonRect.setIcon(QtGui.QIcon('Images/Icons/rect.png'))
        self.buttonRect.setIconSize(QtCore.QSize(20,20))
        self.buttonRect.setToolTip('Draw Rectangle')
        self.buttonRect.setCheckable(True)
        
        self.buttonHand = QPushButton('',self)
        self.buttonHand.setGeometry(378,10,30,30)
        self.buttonHand.clicked.connect(self.enableHand)
        self.buttonHand.setIcon(QtGui.QIcon('Images/Icons/handtool.png'))
        self.buttonHand.setIconSize(QtCore.QSize(20,20))
        self.buttonHand.setToolTip('Hand Tool')
        self.buttonHand.setCheckable(True)
        
        self.buttonMap = QPushButton('',self)
        self.buttonMap.setGeometry(611,611,30,30)
        self.buttonMap.clicked.connect(self.enableMap)
        self.buttonMap.setIcon(QtGui.QIcon('Images/Icons/map.png'))
        self.buttonMap.setIconSize(QtCore.QSize(20,20))
        self.buttonMap.setToolTip('Mini Map')
        
        #Sliders
        
        self.sh = QSlider(Qt.Horizontal,self)
        self.sh.setGeometry(49,617,550,20)
        self.sh.setValue(0)
        self.sh.valueChanged.connect(self.xValueChanged)
        
        self.sv = QSlider(Qt.Vertical,self)
        self.sv.setGeometry(617,49,20,550)
        self.sv.setValue(100)
        self.sv.valueChanged.connect(self.yValueChanged)
        
        #Connection rules
        
        self.rules = [
        [],
        [],
        [1],
        [2,3,11,7,8,9,10],
        [3,11],
        [4],
        [4,5],
        [2,7,8,9,10],
        [2,7,8,9,10],
        [2,7,8,9,10],
        [2,7,8,9,10],
        [3,4,5,6],
        [2,3,11,7,8,9,10],
        [12],
        [13],
        [4,5,11]
        ]


    def paintEvent(self, event):
    
        #650 x 650
        qp = QtGui.QPainter(self)
        
        br = QtGui.QBrush(QtGui.QColor(100,100,200,40),11)
        qp.setBrush(br)
        qp.setPen(QPen(QtGui.QColor(110,110,110), 2))
        
        #Background grid
        qp.drawRect(-1,-1,652,652)
        
        #Draw ongoing rectangle
        
        c = self.mainWindow.tools.color
        br = QtGui.QBrush(QtGui.QColor(c[0],c[1],c[2],50),1)
        qp.setBrush(br)
        qp.setPen(QPen(QtGui.QColor(c[0],c[1],c[2],200), 1))
        qp.setRenderHint(0x01)
        
        if self.rectFlag:
            qp.drawRect(self.beginRect.x(),self.beginRect.y(),self.endRect.x()-self.beginRect.x(),self.endRect.y()-self.beginRect.y())
            
        #draw existing rectangles
        
        for i in self.rects:
            
            br = QtGui.QBrush(QtGui.QColor(i[4],i[5],i[6],50),1)
            qp.setBrush(br)
            qp.setPen(QPen(QtGui.QColor(i[4],i[5],i[6],200),1))
            qp.drawRect(i[0]+self.xBias,i[1]+self.yBias,i[2]-i[0],i[3]-i[1])
            
            
        #Remove effect of rectangle
        br = QtGui.QBrush(QtGui.QColor(100,100,200,40),11)
        qp.setBrush(br)
        qp.setPen(QPen(QtGui.QColor(110,110,110), 2))
        
        #Draw connection lines
        for i in self.connections:
            qp.drawLine(
            self.shapes[i[0]][2] + self.shapes[i[0]][4]/2 + self.xBias,
            self.shapes[i[0]][3] + self.shapes[i[0]][5]/2 + self.yBias,
            self.shapes[i[1]][2] + self.shapes[i[1]][4]/2 + self.xBias,
            self.shapes[i[1]][3] + self.shapes[i[1]][5]/2 + self.yBias
            )
        
        #Draw ongoing connection
        if self.connectFlag and self.conA != -1:
            qp.drawLine(
            self.shapes[self.conA][2]+self.shapes[self.conA][4]/2 + self.xBias,
            self.shapes[self.conA][3]+self.shapes[self.conA][5]/2 + self.yBias,
            self.currentLocation.x(),
            self.currentLocation.y()
            )
            
        #Draw ongoing disconnection
        qp.setPen(QPen(QtGui.QColor(255,0,0), 2))
        if self.disconnectFlag and self.conA != -1:
            qp.drawLine(
            self.shapes[self.conA][2]+self.shapes[self.conA][4]/2 + self.xBias,
            self.shapes[self.conA][3]+self.shapes[self.conA][5]/2 + self.yBias,
            self.currentLocation.x(),
            self.currentLocation.y()
            )
        
        qp.setPen(QPen(QtGui.QColor(0,0,0), 1))
            
        #Draw shape and names
        qp.setFont(QFont('Sans Serif', 9))
        self.label.setFont(QFont('Sans Serif', 9))
        br = QtGui.QBrush(QtGui.QColor(255,255,255),1)
        qp.setBrush(br)
        k=0
        for i in self.shapes:
            qp.drawRect(i[2]-10 + self.xBias,i[3]-10 + self.yBias,70,70)
            qp.drawPixmap(i[2] + self.xBias,i[3] + self.yBias,self.mainWindow.toolsImages[i[0]][i[1]])
            if len(self.mainWindow.data.inputList[k]) > 0:
                self.label.setText(self.mainWindow.data.inputList[k][0])
                xbias=(50-self.label.fontMetrics().boundingRect(self.label.text()).width())/2
                qp.drawText(i[2]+xbias+self.xBias,i[3]+75+self.yBias,self.mainWindow.data.inputList[k][0])
            k=k+1
            
            
        #Draw selected tool
        if self.mainWindow.toolFlag:
            qp.drawPixmap(self.currentLocation,self.mainWindow.toolsImages[self.mainWindow.tab][self.mainWindow.tool])
        
        #Draw Title
        qp.setPen(QPen(QtGui.QColor(0,0,0), 1))
        qp.setFont(QFont('Sans Serif', self.titleS))
        qp.drawText(self.titleX+self.xBias,self.titleY+self.yBias,self.titleT)
        
        #Draw MiniMap
        qp.setPen(QPen(QtGui.QColor(70,70,70), 2))
        if self.mapFlag:
            qp.drawRect(395,395,210,210)
            
            qp.setPen(QPen(QtGui.QColor(110,110,110), 1))
                
            for i in self.connections:
            
                bx = self.shapes[i[0]][2] + 25
                by = self.shapes[i[0]][3] + 25
                ex = self.shapes[i[1]][2] + 25
                ey = self.shapes[i[1]][3] + 25
            
                bx = (bx/self.canvasWidth)*200
                by = (by/self.canvasWidth)*200
                ex = (ex/self.canvasWidth)*200
                ey = (ey/self.canvasWidth)*200
                
                qp.drawLine(bx+400,by+400,ex+400,ey+400)
            
            for i in self.shapes:
                x = i[2] + 25
                y = i[3] + 25
                c = self.colDict[i[1]]
                
                x = (x/self.canvasWidth)*200
                y = (y/self.canvasWidth)*200
                
                qpen = QPen(QtGui.QColor(c[0],c[1],c[2]), 10)
                qpen.setCapStyle(Qt.RoundCap)
                qp.setPen(qpen)
                
                qp.drawPoint(x+400,y+400)

        
    def mousePressEvent(self, event):
        
        self.mainWindow.data.fileChanged = True
        
        if self.handFlag:
            self.setCursor(QtGui.QCursor(QtGui.QPixmap('Images/Icons/punch.png')))
            self.handScroll = True
        
        #Release all if user press right click
        if event.button() == Qt.RightButton:
            self.mainWindow.tools.btnTool[self.mainWindow.tool].setChecked(False)
            self.mainWindow.tool = 0
            self.mainWindow.toolFlag=False
            self.connectFlag=False
            self.disconnectFlag=False
            self.rectFlag = False
            self.handFlag = False
            self.handScroll = False
            self.beginRect.setX(-100)
            self.beginRect.setY(-100)
            self.endRect.setX(-100)
            self.endRect.setY(-100)
            self.mainWindow.tools.update()
            
            self.unsetCursor()
            
            #Release buttons
            self.buttonHand.setChecked(False)
            self.buttonRect.setChecked(False)
            self.buttonConnect.setChecked(False)
            self.buttonDisconnect.setChecked(False)
            
        #Initialize rectangle
        if self.rectFlag:
            self.beginRect = event.pos()
            self.endRect = event.pos()
        
        #Add shape to the list
        if self.mainWindow.toolFlag:
        
            isStartPlaced = False
        
            '''for i in self.shapes:
                if (self.mainWindow.tab,self.mainWindow.tool) == (0,1):
                    isStartPlaced = True
                    self.mainWindow.status.setMessage('Only one start is allowed.',2)
                    self.mainWindow.status.update()
                    break'''
                    
            if not isStartPlaced:
                self.shapes.append([self.mainWindow.tab,self.mainWindow.tool,event.pos().x()-self.xBias,event.pos().y()-self.yBias,50,50])
                self.mainWindow.tools.btnTool[self.mainWindow.tool].setChecked(False)
                self.mainWindow.toolFlag = False
                self.mainWindow.tool = 0
                self.mainWindow.tools.update()
                #add input and output
                self.mainWindow.data.inputList.append(list())
                self.mainWindow.data.outputList.append(list())
            else:
                self.mainWindow.tools.btnTool[self.mainWindow.tool].setChecked(False)
        
        #Detect Shape
        self.previousShape = self.currentShape
        self.currentShape = self.detectShape(event.pos())
        self.currentRect = self.detectRect(event.pos())
        
        #Set input and output frames
        if self.currentShape != -1:
            self.mainWindow.input.stackedView.setCurrentIndex(self.shapes[self.currentShape][0]*12+self.shapes[self.currentShape][1])
            self.mainWindow.output.stackedView.setCurrentIndex(self.shapes[self.currentShape][0]*12+self.shapes[self.currentShape][1])
        else:
            self.mainWindow.input.stackedView.setCurrentIndex(0)
            self.mainWindow.output.stackedView.setCurrentIndex(0)
        
        #save data from previous shape
        if self.mainWindow.data.loadFile:
            self.mainWindow.data.currentInputFrame = self.mainWindow.input.t00
            self.mainWindow.data.loadFile = False
            
        self.mainWindow.data.currentInputFrame.saveValues()
        #set new frames
        self.mainWindow.data.currentInputFrame = self.mainWindow.input.stackedView.currentWidget()
        self.mainWindow.data.currentOutputFrame = self.mainWindow.output.stackedView.currentWidget()
        #load data to new frames
        self.mainWindow.data.currentInputFrame.loadValues()
        self.mainWindow.data.currentInputFrame.update()
        self.mainWindow.data.currentOutputFrame.loadValues()
        self.mainWindow.data.currentOutputFrame.update()
        
        #Move shape enable
        if self.currentShape != -1:
            if not (self.connectFlag or self.disconnectFlag):
                self.moveFlag = True
        
        #set conA
        if (self.connectFlag or self.disconnectFlag) and self.conA == -1:
            self.conA = self.currentShape
            if self.conA == -1:
                self.mainWindow.toolFlag=False
                self.mainWindow.tool = 0
                self.mainWindow.tools.update()
                
        #Update after every click
        self.update()
        
    def mouseMoveEvent(self,event):
        
        #Move shape
        if self.moveFlag and self.currentShape != -1 and self.mainWindow.toolFlag != True:
            self.shapes[self.currentShape][2] = self.shapes[self.currentShape][2] + event.pos().x() - self.currentLocation.x()
            self.shapes[self.currentShape][3] = self.shapes[self.currentShape][3] + event.pos().y() - self.currentLocation.y()
        
        #Scroll with hand
        if self.handScroll and self.currentShape == -1:
            newX = self.xBias + event.pos().x() - self.currentLocation.x()
            newY = self.yBias + event.pos().y() - self.currentLocation.y()
            extra = self.canvasWidth - 650
            
            if newX <= 0 and newX >= -(self.canvasWidth - 650):
                self.xBias = newX
                if extra != 0:
                    self.sh.setValue((-self.xBias/extra)*100)
            if newY <= 0 and newY >= -(self.canvasWidth - 650):
                self.yBias = newY
                if extra != 0:
                    self.sv.setValue(100 - (-self.yBias/extra)*100)
        
        #update current location
        self.currentLocation = event.pos()
        
        #Initialize rectangle   
        if self.rectFlag and self.beginRect.x() != -100:
            self.endRect = event.pos()
        
        #update after every move
        self.update()
        
    def mouseReleaseEvent(self, event):
    
        if self.handFlag:
            self.setCursor(QtGui.QCursor(QtGui.QPixmap('Images/Icons/hand.png')))
            self.handScroll = False
    
        #set conB and add connection
        if self.connectFlag and self.conA != -1:
        
            self.conB = self.detectShape(event.pos())
            if self.conB != -1 and self.conB != self.conA:
            
                isExists = False
                multipleSource = False
                isValid = True
            
                for i in self.connections:
                    if (self.conA == i[0] and self.conB == i[1]) or (self.conA == i[1] and self.conB == i[0]):
                        isExists = True
                        self.mainWindow.status.setMessage('Connection already exists.',2)
                        self.mainWindow.status.update()
                        break
                        
                for i in self.connections:
                    if self.conB == i[1]:
                        multipleSource = True
                        self.mainWindow.status.setMessage('Can\'t have multiple source.',2)
                        self.mainWindow.status.update()
                        break
                
                if (not isExists) and (not multipleSource):
                    if self.shapes[self.conA][1] not in self.rules[self.shapes[self.conB][1]]:
                        isValid = False
                        self.mainWindow.status.setMessage('Invalid connection. Refer user manual for more information.',2)
                        self.mainWindow.status.update()
            
                if (not isExists) and (not multipleSource) and (isValid):
                    self.connections.append([self.conA,self.conB])
                    self.mainWindow.status.setMessage('Connection established.',1)
                    self.mainWindow.status.update()
                
        #set conB and remove connection
        if self.disconnectFlag and self.conA != -1:
            self.conB = self.detectShape(event.pos())
            if self.conB != -1:
                found = False
                c = 0
                for i in self.connections:
                    if i[0] == self.conA and i[1] == self.conB:
                        found = True
                        break
                    c += 1
                if found:
                    self.connections.pop(c)
                    
        #Reset Flags
        
        self.conA = -1
        self.conB = -1
        self.mainWindow.toolFlag = False
        self.mainWindow.tool = 0
        self.mainWindow.tools.update()
        
        #Save rectangle
        if self.rectFlag:
            c = self.mainWindow.tools.color
            self.rects.append([
            self.beginRect.x() - self.xBias,
            self.beginRect.y() - self.yBias,
            self.endRect.x() - self.xBias,
            self.endRect.y() - self.yBias,
            c[0],c[1],c[2]])
            
            self.beginRect.setX(-100)
            self.beginRect.setY(-100)
            self.endRect.setX(-100)
            self.endRect.setY(-100)
            self.rectFlag = False
            self.buttonRect.setChecked(False)
            
    
        #Release move flag
        self.moveFlag = False
        
        #Update screen
        self.update()
        
    def keyPressEvent(self,event):
        
        if self.currentRect != -1 and event.key() == Qt.Key_Delete:
            self.rects.pop(self.currentRect)
            self.update()
            self.currentRect = -1
            self.mainWindow.output.update()
            
        if event.key() == Qt.Key_Shift:
            self.shiftFlag = True
            
    def keyReleaseEvent(self,event):
        if event.key() == Qt.Key_Shift:
            self.shiftFlag = False
    
    def isIn(self,id,pos):
    
        bx = self.shapes[id][2]-10 + self.xBias
        by = self.shapes[id][3]-10 + self.yBias
        ex = self.shapes[id][2]+self.shapes[id][4]+10 + self.xBias
        ey = self.shapes[id][3]+self.shapes[id][5]+10 + self.yBias
    
        if pos.x() >= bx and pos.x() <= ex and pos.y() >= by and pos.y() <= ey:
            return True
        else:
            return False
            
    def isInRect(self,id,pos):
    
        bx = min(self.rects[id][0],self.rects[id][2]) + self.xBias
        by = min(self.rects[id][1],self.rects[id][3]) + self.yBias
        ex = max(self.rects[id][0],self.rects[id][2]) + self.xBias
        ey = max(self.rects[id][1],self.rects[id][3]) + self.yBias
    
        if pos.x() >= bx and pos.x() <= ex and pos.y() >= by and pos.y() <= ey:
            return True
        else:
            return False
        
    def detectShape(self,pos):
        for i in reversed(range(len(self.shapes))):
            if self.isIn(i,pos):
                return i
        return -1
        
    def coreFunction(self):
        if self.currentShape != -1:
            tab = self.shapes[self.currentShape][0]
            tool = self.shapes[self.currentShape][1]
            self.mainWindow.pycore.tfunctionSelect[tab][tool]()
            
    def playFunction(self):
        self.mainWindow.pycore.execQueue()
        
    def connectShapes(self):
        self.connectFlag = True
        self.disconnectFlag = False
        self.moveFlag = False
        
    def drawRects(self):
        self.rectFlag = True
        
    def detectRect(self,pos):
    
        if self.currentShape != -1:
            return -1
    
        for i in reversed(range(len(self.rects))):
            if self.isInRect(i,pos):
                return i
        return -1
        
    def wheelEvent(self,event):
        
        step = event.angleDelta().y() / 120
        
        if self.shiftFlag:
            self.sh.setValue(self.sh.value() - step * self.f)
            
            if step > 0 :
                self.xBias = min(self.xBias + 50,0)
            elif step < 0 :
                self.xBias = max(self.xBias - 50,-(self.canvasWidth - 650))
                
        else:
            self.sv.setValue(self.sv.value() + step * self.f)
            
            if step > 0 :
                self.yBias = min(self.yBias + 50,0)
            elif step < 0 :
                self.yBias = max(self.yBias - 50,-(self.canvasWidth - 650))
        
        self.update()
            
    def deleteShape(self):
        
        if self.currentShape != -1:
            self.shapes.pop(self.currentShape)
            self.mainWindow.data.inputList.pop(self.currentShape)
            self.mainWindow.data.outputList.pop(self.currentShape)
            
            temp = list()
            
            for i in self.connections:
                if i[0] != self.currentShape and i[1] != self.currentShape:
                    temp.append(i)
            
            for i in temp:
                if i[0] > self.currentShape:
                    i[0] -= 1
                if i[1] > self.currentShape:
                    i[1] -= 1
            
            self.connections = temp.copy()
            
            temp = list()
            
            for i in self.connections:
                if i[0] != i[1]:
                    temp.append(i)
                    
            self.connections = temp.copy()
            
            self.currentShape = -1
                
            self.mainWindow.input.stackedView.setCurrentIndex(0)
            self.mainWindow.output.stackedView.setCurrentIndex(0)
            
            self.update()
            
    def expand(self):
        self.canvasWidth += 50
        self.canvasHeight += 50
        self.mainWindow.status.update()
        
        self.scaleFactor()
        self.update()
        
    def collapse(self):
    
        if self.canvasWidth != 650:
            self.canvasWidth -= 50
            self.canvasHeight -= 50
            self.mainWindow.status.update()
            self.scaleFactor()
            
            if self.xBias < -(self.canvasWidth - 650):
                self.xBias = -(self.canvasWidth - 650)
            if self.yBias < -(self.canvasWidth - 650):
                self.yBias = -(self.canvasWidth - 650)
            self.update()
            
    def disconnectShapes(self):
        self.disconnectFlag = True
        self.connectFlag = False
        self.moveFlag = False
        
    def scaleFactor(self):
        extra = self.canvasWidth - 650
        slice = extra / 50
        if slice == 0:
            self.f = 0
            return
            
        self.f = 100 / slice
        
    def enableHand(self):
        self.handFlag = True
        self.setCursor(QtGui.QCursor(QtGui.QPixmap('Images/Icons/hand.png')))
        
    def xValueChanged(self):
        self.xBias = -(self.canvasWidth - 650) * self.sh.value() / 100
        self.update()
        
    def yValueChanged(self):
        self.yBias = -(self.canvasWidth - 650) * (100 - self.sv.value()) / 100
        self.update()
        
    def enableMap(self):
        self.mapFlag = not self.mapFlag
        self.update()
        
#========================================================================================================================