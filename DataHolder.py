#Python imports
import sys

#PyQt5 imports
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPainter, QColor, QPen, QPalette, QPixmap
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QFrame, QGridLayout
from PyQt5.QtCore import Qt

class NullFrame(QFrame):

    def __init__(self):
        super().__init__()
        
    def saveValues(self):
        pass
        
    def loadValues(self):
        pass

class Data():
    
    def __init__(self):
    
        #Current index of input and output frames
        self.ci = 0
        
        #input and output list
        self.inputList = list()
        self.outputList = list()
        
        #current frame from input and output frames
        self.currentInputFrame = NullFrame()
        self.currentOutputFrame = NullFrame()
        
        #Execution queue
        self.q = list()
        self.curentExecution = -1
        self.isQueueRunning = False
        self.background = False
        
        #File flags
        self.loadFile = False
        self.fileChanged = False
        self.fileName = ''