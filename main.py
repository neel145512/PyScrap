#Python imports
import sys

#PyQt5 imports
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPainter, QColor, QPen, QPalette, QPixmap
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QFrame, QGridLayout
from PyQt5.QtCore import Qt

#Frame imports
from TitleFrame import Title
from ToolFrame import Tools
from BotFrame import Bots
from CanvasFrame import Canvas
from InputFrame import Input
from OutputFrame import Output
from StatusFrame import Status


#Core imports
from DataHolder import Data
from CoreFunctions import PyCore
import Dialog

app = QtWidgets.QApplication(sys.argv)
app.setStyle('Fusion')

#========================================================================================================================


class MyWidget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        
        (self.tab,self.tool) = (0,12)
        #images for tool box
        self.toolsImages = list()
        
        self.toolsImagesTab0 = [
        QPixmap('images/50/notool.png'),
        QPixmap('images/50/start.png'),
        QPixmap('images/50/url.png'),
        QPixmap('images/50/crawler.png'),
        QPixmap('images/50/media.png'),
        QPixmap('images/50/rename.png'),
        QPixmap('images/50/sort.png'),
        QPixmap('images/50/object.png'),
        QPixmap('images/50/keys.png'),
        QPixmap('images/50/mouse.png'),
        QPixmap('images/50/delay.png'),
        QPixmap('images/50/filter.png'),
        QPixmap('images/50/dbcon.png'),
        QPixmap('images/50/table.png'),
        QPixmap('images/50/column.png'),
        QPixmap('images/50/download.png'),
        ]
        
        self.toolsImages.append(self.toolsImagesTab0)
        
        #Objects of core classes
        
        self.data = Data()
        self.title = Title(self)
        self.tools = Tools(self)
        self.bots = Bots(self)
        self.canvas = Canvas(self)
        self.input = Input(self)
        self.output = Output(self)
        self.status = Status(self)
        self.pycore = PyCore(self)
        
        layout = QGridLayout()
        layout.setSpacing(0)
        
        layout.addWidget(self.title  , 0, 0, 1, 3)
        layout.addWidget(self.bots   , 1, 0, 1, 1)
        layout.addWidget(self.tools  , 2, 0, 1, 1)
        layout.addWidget(self.canvas , 1, 1, 2, 1)
        layout.addWidget(self.input  , 1, 2, 1, 1)
        layout.addWidget(self.output , 2, 2, 1, 1)
        layout.addWidget(self.status , 3, 0, 1, 3)
        
        layout.setRowMinimumHeight(0, 30)
        layout.setRowMinimumHeight(1, 325)
        layout.setRowMinimumHeight(2, 325)
        layout.setRowMinimumHeight(3, 20)
        
        layout.setColumnMinimumWidth(0, 330)
        layout.setColumnMinimumWidth(1, 650)
        layout.setColumnMinimumWidth(2, 330)
        
        self.setLayout(layout)
        
        #Tool selector flag
        self.toolFlag = False
        
        #Sample status message
        self.status.setMessage('Welcome to the PyScrap.',0)
        
    def paintEvent(self, event):
        
        qp = QtGui.QPainter(self)
        br = QtGui.QBrush(QtGui.QColor(255,255,255,255),1)
        qp.setBrush(br)
        
        qp.setPen(QPen(QtGui.QColor(0,0,0), 1))
        
        #Draw outer border
        qp.drawRect(0,0,1331,721)
        qp.drawRect(11,11,1309,699)
        
        #Draw main border
        for i in range(10):
            qp.setPen(QPen(QtGui.QColor(50+i*10,50+i*20,255), 1))
            qp.drawRect(i+1,i+1,1331-(i+1)*2,721-(i+1)*2)


    def keyPressEvent(self, event):
        self.canvas.keyPressEvent(event)

#========================================================================================================================

window = MyWidget()
window.setGeometry(18,10,1330,720)
window.setWindowFlags(QtCore.Qt.FramelessWindowHint)
window.show()

app.aboutToQuit.connect(app.deleteLater)
sys.exit(app.exec_())