import sys
import os
import threading
import requests
import time

from urllib.request import Request, urlopen
from selenium import webdriver
from pathlib import Path
from selenium.webdriver.common.keys import Keys
import MySQLdb
import pyperclip


from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import *
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
#========================================================================================================================


class PyCore():

    def __init__(self,window):
        super().__init__()
        self.mainWindow = window
        
        self.xpath = ''
        
        #Threaded functions
        self.tfunctionSelect = list()
        
        self.tfunctionSet0 = [
        self.noFunction,
        self.noFunction,
        self.tcheckURL,
        self.tcrawl,
        self.tmedia,
        self.trename,
        self.tsort,
        self.tdetect,
        self.tkeys,
        self.tmouse,
        self.tdelay,
        self.tfilter,
        self.tdbconnect,
        self.ttable,
        self.noFunction,
        self.tdownload,
        ]
        
        self.tfunctionSelect.append(self.tfunctionSet0)
        
        #Functions without thread
        self.functionSelect = list()
        
        self.functionSet0 = [
        self.noFunction,
        self.noFunction,
        self.checkURL,
        self.crawl,
        self.media,
        self.rename,
        self.sort,
        self.detect,
        self.keys,
        self.mouse,
        self.delay,
        self.filter,
        self.dbconnect,
        self.table,
        self.noFunction,
        self.download,
        ]
        
        self.functionSelect.append(self.functionSet0)
        
        #Source rules
        
        self.rules = [
        [],
        [],
        [1],
        [2,3,11],
        [3,11],
        [4],
        [4,5],
        [2],
        [2],
        [2],
        [2],
        [3,4,5,6],
        [2,3,11],
        [12],
        [13],
        [4,5,11]
        ]
        
        
        
        
    #no function
    def noFunction(self):
        pass
     

    #URL check combo
    def tcheckURL(self):
        t = threading.Thread(target=self.checkURL)
        t.start()
        
    def checkURL(self):
        
        #Detect previous shape
        con = self.mainWindow.canvas.connections.copy()
        
        if self.mainWindow.data.isQueueRunning:
            cs = self.mainWindow.data.currentExecution
        else:
            cs = self.mainWindow.canvas.currentShape
        
        ps = -1
        
        for i in con:
            if i[1] == cs:
                ps = i[0]
                break
                
        if ps == -1:
            print('URL provider is not in a queue')
            return
            
        #Detect valid previous shape
        
        lim = len(con)*2
        
        while lim > 0:
        
            if self.mainWindow.canvas.shapes[ps][1] in self.rules[self.mainWindow.canvas.shapes[cs][1]]:
                break
            else:
                for i in con:
                    if i[1] == ps:
                        ps = i[0]
                        break
        
            lim -= 1
            
        if self.mainWindow.canvas.shapes[ps][1] not in self.rules[self.mainWindow.canvas.shapes[cs][1]]:
            print('URL is not in a queue')
            return
            
        #Save input data
        self.mainWindow.canvas.previousShape = self.mainWindow.canvas.currentShape
        self.mainWindow.data.currentInputFrame.saveValues()
        
        co = self.mainWindow.data.currentOutputFrame
        ip = self.mainWindow.data.inputList[cs]
        op = list()
        
        #Core Function
        
        self.option = webdriver.ChromeOptions()
        self.option.add_extension('Block-image_v1.1.crx')
        self.driver = webdriver.Chrome(chrome_options=self.option)
        self.driver.get(ip[1])
        
        try:
            request = requests.get(ip[1])
            code = request.status_code
        except:
            code = 0
        
        #Place data
        op.append(ip[1])
        op.append(str(code))
        
        #Update output data
        self.mainWindow.data.outputList[cs] = op
        co.loadValues()
        co.update()
        
        print('URL')
        
    
    #Web crawler combo
    def tcrawl(self):
        t = threading.Thread(target=self.crawl)
        t.start()
        
    def crawl(self):
    
        #Detect previous shape
        con = self.mainWindow.canvas.connections.copy()
        
        if self.mainWindow.data.isQueueRunning:
            cs = self.mainWindow.data.currentExecution
        else:
            cs = self.mainWindow.canvas.currentShape
            
        ps = -1
        
        for i in con:
            if i[1] == cs:
                ps = i[0]
                break
                
        if ps == -1:
            print('Crawler is not in a queue')
            return
            
        #Detect valid previous shape
        
        lim = len(con)*2
        
        while lim > 0:
        
            if self.mainWindow.canvas.shapes[ps][1] in self.rules[self.mainWindow.canvas.shapes[cs][1]]:
                break
            else:
                for i in con:
                    if i[1] == ps:
                        ps = i[0]
                        break
        
            lim -= 1
            
        if self.mainWindow.canvas.shapes[ps][1] not in self.rules[self.mainWindow.canvas.shapes[cs][1]]:
            print('Crawler is not in a queue')
            return
    
        #Save input data
        self.mainWindow.canvas.previousShape = self.mainWindow.canvas.currentShape
        self.mainWindow.data.currentInputFrame.saveValues()
        
        co = self.mainWindow.data.currentOutputFrame
        ip = self.mainWindow.data.inputList[cs]
        op = list()
        
        #Core Function
        
        u = self.mainWindow.data.outputList[ps][0]
        lvl = ip[1]

        #start browser
        try:
            driver = self.driver
        except:
            option = webdriver.ChromeOptions()
            option.add_extension('Block-image_v1.1.crx')
            driver = webdriver.Chrome(chrome_options=option)
            driver.get(u)

        #Get first list of links
        links = driver.find_elements_by_tag_name('a')
        href = list()
        old = list()
        new = list()
        temp = list()
        told = list()


        for i in links:
            href.append([i.get_attribute('href')])
            
        old = href
            
        #Get recursive links by level  
        for i in range(lvl):

            del new[:]

            for l in old:
                if len(l) != i+1:
                    continue
                    
                try:
                    driver.get(l[0])
                    links = driver.find_elements_by_tag_name('a')
                    
                    for j in links:
                        new.append([j.get_attribute('href')]+l)
                except:
                    pass
                    
            old += new
            
        #Insert home link
        old.insert(0,[u])
        #Remove duplicate links
        for i in old:
            temp.append(i[0])
            
        temp = set(temp)
        temp = list(temp)

        for i in temp:
            for j in old:
                if i == j[0]:
                    told.append(j)
                    break;
        
        driver.close()
        
        #Place data
        op = told.copy()
        
        #Update output data
        self.mainWindow.data.outputList[cs] = op
        co.loadValues()
        co.update()
        
        print('Crawler')
        
    #Media extractor combo
    def tmedia(self):
        t = threading.Thread(target=self.media)
        t.start()
        
    def media(self):
    
        #Detect previous shape
        con = self.mainWindow.canvas.connections.copy()
        
        if self.mainWindow.data.isQueueRunning:
            cs = self.mainWindow.data.currentExecution
        else:
            cs = self.mainWindow.canvas.currentShape
        
        ps = -1
        
        for i in con:
            if i[1] == cs:
                ps = i[0]
                break
                
        if ps == -1:
            print('Media extractor is not in a queue')
            return
            
        #Detect valid previous shape
        
        lim = len(con)*2
        
        while lim > 0:
        
            if self.mainWindow.canvas.shapes[ps][1] in self.rules[self.mainWindow.canvas.shapes[cs][1]]:
                break
            else:
                for i in con:
                    if i[1] == ps:
                        ps = i[0]
                        break
        
            lim -= 1
            
        if self.mainWindow.canvas.shapes[ps][1] not in self.rules[self.mainWindow.canvas.shapes[cs][1]]:
            print('Media extractor is not in a queue')
            return
            
        #Save input data
        self.mainWindow.canvas.previousShape = self.mainWindow.canvas.currentShape
        self.mainWindow.data.currentInputFrame.saveValues()
        
        co = self.mainWindow.data.currentOutputFrame
        ip = self.mainWindow.data.inputList[cs]
        op = list()
        
        #Core Function
        
        u = self.mainWindow.data.outputList[ps]
        
        #set options
        option = webdriver.ChromeOptions()
        option.add_extension('Block-image_v1.1.crx')
        driver = webdriver.Chrome(chrome_options=option)

        #Get list of images
        
        imgList = []
        
        for i in u:
            try:
                driver.get(i[0])
                links = driver.find_elements_by_tag_name('img')
                
                for j in links:
                    imgList.append([str(j.get_attribute('src')).split('/')[-1],j.get_attribute('src')] + i)
            except:
                pass
            
        driver.close()
        
        #Place data
        op = imgList.copy()
        
        #Update output data
        self.mainWindow.data.outputList[cs] = op
        co.loadValues()
        co.update()
        
        print('Media')
        
        
    #Rename combo
    def trename(self):
        t = threading.Thread(target=self.rename)
        t.start()
        
    def rename(self):
        
        #Detect previous shape
        con = self.mainWindow.canvas.connections.copy()
        
        if self.mainWindow.data.isQueueRunning:
            cs = self.mainWindow.data.currentExecution
        else:
            cs = self.mainWindow.canvas.currentShape
        
        ps = -1
        
        for i in con:
            if i[1] == cs:
                ps = i[0]
                break
                
        if ps == -1:
            print('Rename is not in a queue')
            return
            
        #Detect valid previous shape
        
        lim = len(con)*2
        
        while lim > 0:
        
            if self.mainWindow.canvas.shapes[ps][1] in self.rules[self.mainWindow.canvas.shapes[cs][1]]:
                break
            else:
                for i in con:
                    if i[1] == ps:
                        ps = i[0]
                        break
        
            lim -= 1
            
        if self.mainWindow.canvas.shapes[ps][1] not in self.rules[self.mainWindow.canvas.shapes[cs][1]]:
            print('Rename is not in a queue')
            return
            
        #Save input data
        self.mainWindow.canvas.previousShape = self.mainWindow.canvas.currentShape
        self.mainWindow.data.currentInputFrame.saveValues()
        
        co = self.mainWindow.data.currentOutputFrame
        ip = self.mainWindow.data.inputList[cs]
        op = list()
        
        #Core Function
        
        u = self.mainWindow.data.outputList[ps].copy()
        separator = ''
        notFound = ''
        ex = ''
        temp = []
        lword = []
        llink = []
        tlink = []
        tword = ''
        
        word = -1
        link = -1
        sfrom = -1
        sto = -1
        
        
        
        for i in u:
        
            temp = i[0].split('.')
            ext = temp.pop(-1)
            ex = ''.join(temp)
            
            newname = ''
            
            for cw in ip[9]:
                
                if cw[2] == 't':
                    
                    cw = cw[16:]
                    cw = cw.split(',')
                    
                    link  = int(cw[0])
                    word  = int(cw[1])
                    sfrom = int(cw[2])
                    sto   = int(cw[3])
                    
                    if link < len(i) -1:
                        
                        tlink = i[link+1].split('/')
                        
                        if word < len(tlink):
                            tword = tlink[-(word+1)]
                            
                            newname = newname + tword[sfrom:sto] + separator
                        else:
                            newname = newname + notFound + separator
                    else:
                        newname = newname + notFound + separator
                    
                elif cw[2] == 'i':
                    newname = newname + ex + separator
                else:
                    cw = cw[8:]
                    newname = newname + cw + separator
                    
            op.append([newname+'.'+ext] + i[1:])
        
        #Place data
        #Already placed in append mode
        
        #Update output data
        self.mainWindow.data.outputList[cs] = op
        co.loadValues()
        co.update()
        
        print('Rename')
        
    #object detector combo
    def tdetect(self):
        t = threading.Thread(target=self.detect)
        t.start()
        
    def detect(self):
    
        #Detect previous shape
        con = self.mainWindow.canvas.connections.copy()
        
        if self.mainWindow.data.isQueueRunning:
            cs = self.mainWindow.data.currentExecution
        else:
            cs = self.mainWindow.canvas.currentShape
        
        ps = -1
        
        for i in con:
            if i[1] == cs:
                ps = i[0]
                break
                
        if ps == -1:
            print('Object detector is not in a queue')
            return
            
        #Detect valid previous shape
        
        lim = len(con)*2
        
        while lim > 0:
        
            if self.mainWindow.canvas.shapes[ps][1] in self.rules[self.mainWindow.canvas.shapes[cs][1]]:
                break
            else:
                for i in con:
                    if i[1] == ps:
                        ps = i[0]
                        break
        
            lim -= 1
            
        if self.mainWindow.canvas.shapes[ps][1] not in self.rules[self.mainWindow.canvas.shapes[cs][1]]:
            print('Object detector is not in a queue')
            return
            
        #Save input data
        self.mainWindow.canvas.previousShape = self.mainWindow.canvas.currentShape
        self.mainWindow.data.currentInputFrame.saveValues()
        
        co = self.mainWindow.data.currentOutputFrame
        ip = self.mainWindow.data.inputList[cs]
        op = list()
        
        #Core Function
        self.xpath = ip[1]
        
        #Place data
        op.append(self.xpath)
        
        #Update output data
        self.mainWindow.data.outputList[cs] = op
        co.loadValues()
        co.update()
        
        print('Detect')
        
    #keys combo
    def tkeys(self):
        t = threading.Thread(target=self.keys)
        t.start()
        
    def keys(self):
        
        #Detect previous shape
        con = self.mainWindow.canvas.connections.copy()
        
        if self.mainWindow.data.isQueueRunning:
            cs = self.mainWindow.data.currentExecution
        else:
            cs = self.mainWindow.canvas.currentShape
        
        ps = -1
        
        for i in con:
            if i[1] == cs:
                ps = i[0]
                break
                
        if ps == -1:
            print('Keys is not in a queue')
            return
            
        #Detect valid previous shape
        
        lim = len(con)*2
        
        while lim > 0:
        
            if self.mainWindow.canvas.shapes[ps][1] in self.rules[self.mainWindow.canvas.shapes[cs][1]]:
                break
            else:
                for i in con:
                    if i[1] == ps:
                        ps = i[0]
                        break
        
            lim -= 1
            
        if self.mainWindow.canvas.shapes[ps][1] not in self.rules[self.mainWindow.canvas.shapes[cs][1]]:
            print('Keys is not in a queue')
            return
            
        #Save input data
        self.mainWindow.canvas.previousShape = self.mainWindow.canvas.currentShape
        self.mainWindow.data.currentInputFrame.saveValues()
        
        co = self.mainWindow.data.currentOutputFrame
        ip = self.mainWindow.data.inputList[cs]
        op = list()
        
        #Core Function
        obj = self.driver.find_element_by_xpath(self.xpath)
        obj.send_keys(ip[1])
        time.sleep(1)
        obj.send_keys(Keys.ESCAPE)
        
        #Place data
        
        
        #Update output data
        self.mainWindow.data.outputList[cs] = op
        co.loadValues()
        co.update()
        
        print('Keys')
        
        
    #mouse combo
    def tmouse(self):
        t = threading.Thread(target=self.mouse)
        t.start()
        
    def mouse(self):
        
        #Detect previous shape
        con = self.mainWindow.canvas.connections.copy()
        
        if self.mainWindow.data.isQueueRunning:
            cs = self.mainWindow.data.currentExecution
        else:
            cs = self.mainWindow.canvas.currentShape
        
        ps = -1
        
        for i in con:
            if i[1] == cs:
                ps = i[0]
                break
                
        if ps == -1:
            print('Mouse is not in a queue')
            return
            
        #Detect valid previous shape
        
        lim = len(con)*2
        
        while lim > 0:
        
            if self.mainWindow.canvas.shapes[ps][1] in self.rules[self.mainWindow.canvas.shapes[cs][1]]:
                break
            else:
                for i in con:
                    if i[1] == ps:
                        ps = i[0]
                        break
        
            lim -= 1
            
        if self.mainWindow.canvas.shapes[ps][1] not in self.rules[self.mainWindow.canvas.shapes[cs][1]]:
            print('Mouse is not in a queue')
            return
            
        #Save input data
        self.mainWindow.canvas.previousShape = self.mainWindow.canvas.currentShape
        self.mainWindow.data.currentInputFrame.saveValues()
        
        co = self.mainWindow.data.currentOutputFrame
        ip = self.mainWindow.data.inputList[cs]
        op = list()
        
        #Core Function
        obj = self.driver.find_element_by_xpath(self.xpath)
        obj.click()
        
        #Place data
        
        
        #Update output data
        self.mainWindow.data.outputList[cs] = op
        co.loadValues()
        co.update()
        
        print('Mouse')
        
        
    #Delay combo
    def tdelay(self):
        t = threading.Thread(target=self.delay)
        t.start()
        
    def delay(self):
    
        #Detect previous shape
        con = self.mainWindow.canvas.connections.copy()
        
        if self.mainWindow.data.isQueueRunning:
            cs = self.mainWindow.data.currentExecution
        else:
            cs = self.mainWindow.canvas.currentShape
        
        ps = -1
        
        for i in con:
            if i[1] == cs:
                ps = i[0]
                break
                
        if ps == -1:
            print('Delay is not in a queue')
            return
            
        #Detect valid previous shape
        
        lim = len(con)*2
        
        while lim > 0:
        
            if self.mainWindow.canvas.shapes[ps][1] in self.rules[self.mainWindow.canvas.shapes[cs][1]]:
                break
            else:
                for i in con:
                    if i[1] == ps:
                        ps = i[0]
                        break
        
            lim -= 1
            
        if self.mainWindow.canvas.shapes[ps][1] not in self.rules[self.mainWindow.canvas.shapes[cs][1]]:
            print('Delay is not in a queue')
            return
            
        #Save input data
        self.mainWindow.canvas.previousShape = self.mainWindow.canvas.currentShape
        self.mainWindow.data.currentInputFrame.saveValues()
        
        co = self.mainWindow.data.currentOutputFrame
        ip = self.mainWindow.data.inputList[cs]
        op = list()
        
        #Core Function
        time.sleep(int(ip[1]))
        
        #Place data
        
        
        #Update output data
        self.mainWindow.data.outputList[cs] = op
        co.loadValues()
        co.update()
        
        print('Delay')
        
    #Sort combo
    def tsort(self):
        t = threading.Thread(target=self.sort)
        t.start()
        
    def sort(self):
        
        #Detect previous shape
        con = self.mainWindow.canvas.connections.copy()
        
        if self.mainWindow.data.isQueueRunning:
            cs = self.mainWindow.data.currentExecution
        else:
            cs = self.mainWindow.canvas.currentShape
        
        ps = -1
        
        for i in con:
            if i[1] == cs:
                ps = i[0]
                break
                
        if ps == -1:
            print('Sort is not in a queue')
            return
            
        #Detect valid previous shape
        
        lim = len(con)*2
        
        while lim > 0:
        
            if self.mainWindow.canvas.shapes[ps][1] in self.rules[self.mainWindow.canvas.shapes[cs][1]]:
                break
            else:
                for i in con:
                    if i[1] == ps:
                        ps = i[0]
                        break
        
            lim -= 1
            
        if self.mainWindow.canvas.shapes[ps][1] not in self.rules[self.mainWindow.canvas.shapes[cs][1]]:
            print('Sort is not in a queue')
            return
            
        #Save input data
        self.mainWindow.canvas.previousShape = self.mainWindow.canvas.currentShape
        self.mainWindow.data.currentInputFrame.saveValues()
        
        co = self.mainWindow.data.currentOutputFrame
        ip = self.mainWindow.data.inputList[cs]
        op = list()
        
        #Core Function
        
        u = self.mainWindow.data.outputList[ps].copy()
        
        #Get image size
        for i in u:
        
            try:
                q = Request(i[1])
                q.add_header('User-Agent',
                             'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
                q.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
                q.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3')
                q.add_header('Accept-Encoding', 'none')
                q.add_header('Accept-Language', 'en-US,en;q=0.8')
                q.add_header('Connection', 'keep-alive')
                site = urlopen(q)
                size = int(site.info()['Content-Length'],10)
                site.close()
                
                op.append([size]+i)
            except:
                if i != None:
                    op.append([0]+i)
                
        #Sort
        l = len(op)
        i = 0
        f = -1
        t = -1

        while l > i:
                
            f = i
            cmp = op[i][3]
            flag = True
            
            while flag:
                if i != l-1:
                    
                    if cmp == op[i+1][3]:
                        i += 1
                    else:
                        flag = False
                        t = i
                        
                else:
                    flag = False
                    
            #sort
            
            for m in range(t-f):
                for n in range(f,t):
                    if op[n][0] < op[n+1][0]:
                        temp = op[n]
                        op[n] = op[n+1]
                        op[n+1] = temp
            
            i += 1
            
        t = i-1
        for m in range(t-f):
            for n in range(f,t):
                a = 0 + int(op[n][0])
                b = 0 + int(op[n+1][0])
                if a < b:
                    temp = op[n]
                    op[n] = op[n+1]
                    op[n+1] = temp
        
        #Place data
        for i in op:
            i.pop(0)
        
        #Update output data
        self.mainWindow.data.outputList[cs] = op
        co.loadValues()
        co.update()
        
        print('Sort')
        
        
    #Filter combo
    def tfilter(self):
        t = threading.Thread(target=self.filter)
        t.start()
        
    def filter(self):
        
        #Detect previous shape
        con = self.mainWindow.canvas.connections.copy()
        
        if self.mainWindow.data.isQueueRunning:
            cs = self.mainWindow.data.currentExecution
        else:
            cs = self.mainWindow.canvas.currentShape
        
        ps = -1
        
        for i in con:
            if i[1] == cs:
                ps = i[0]
                break
                
        if ps == -1:
            print('Filter is not in a queue')
            return
            
        #Detect valid previous shape
        
        lim = len(con)*2
        
        while lim > 0:
        
            if self.mainWindow.canvas.shapes[ps][1] in self.rules[self.mainWindow.canvas.shapes[cs][1]]:
                break
            else:
                for i in con:
                    if i[1] == ps:
                        ps = i[0]
                        break
        
            lim -= 1
            
        if self.mainWindow.canvas.shapes[ps][1] not in self.rules[self.mainWindow.canvas.shapes[cs][1]]:
            print('Filter is not in a queue')
            return
            
        #Save input data
        self.mainWindow.canvas.previousShape = self.mainWindow.canvas.currentShape
        self.mainWindow.data.currentInputFrame.saveValues()
        
        co = self.mainWindow.data.currentOutputFrame
        ip = self.mainWindow.data.inputList[cs]
        op = list()
        
        #Core Function
        
        u = self.mainWindow.data.outputList[ps].copy()
        n = ip[5]
        
                
        #Filter
        l = len(u)
        i = 0
        f = []
        t = []

        while l > i:
                
            f.append(i)
            cmp = u[i][2]
            flag = True
            
            while flag:
                if i != l-1:
                    
                    if cmp == u[i+1][2]:
                        i += 1
                    else:
                        flag = False
                        t.append(i)
                        
                else:
                    flag = False
                    
            i += 1
            
        t.append(i-1)

        for i in range(len(f)):

            if t[i]-f[i]+1 <= n:
                for k in range(f[i],t[i]+1):
                    op.append(u[k])
                    
            else:
                for k in range(f[i],f[i]+n):
                    op.append(u[k])
        
        #Place data
        #Append
        
        #Update output data
        self.mainWindow.data.outputList[cs] = op
        co.loadValues()
        co.update()
        
        print('Filter')
        
        
    #dbconnect combo
    def tdbconnect(self):
        t = threading.Thread(target=self.dbconnect)
        t.start()
        
    def dbconnect(self):
        
        #Detect previous shape
        con = self.mainWindow.canvas.connections.copy()
        
        if self.mainWindow.data.isQueueRunning:
            cs = self.mainWindow.data.currentExecution
        else:
            cs = self.mainWindow.canvas.currentShape
        
        ps = -1
        
        for i in con:
            if i[1] == cs:
                ps = i[0]
                break
                
                
        if ps == -1:
            print('Database is not in a queue')
            return
            
        #Detect valid previous shape
        
        lim = len(con)*2
        
        while lim > 0:
        
            if self.mainWindow.canvas.shapes[ps][1] in self.rules[self.mainWindow.canvas.shapes[cs][1]]:
                break
            else:
                for i in con:
                    if i[1] == ps:
                        ps = i[0]
                        break
        
            lim -= 1
            
        if self.mainWindow.canvas.shapes[ps][1] not in self.rules[self.mainWindow.canvas.shapes[cs][1]]:
            print('Database is not in a queue')
            return
            
        #Save input data
        self.mainWindow.canvas.previousShape = self.mainWindow.canvas.currentShape
        self.mainWindow.data.currentInputFrame.saveValues()
        
        co = self.mainWindow.data.currentOutputFrame
        ip = self.mainWindow.data.inputList[cs]
        op = list()
        
        #Core Function
        
        try:
            self.db = MySQLdb.connect(ip[1],ip[3],ip[4],ip[2],use_unicode=True,charset="utf8")
            msg = 'Connected with '+ip[2]
        except:
            self.db = MySQLdb.connect('localhost','root','','myscrap',use_unicode=True,charset="utf8")
            msg = 'Error in parameters. Please try again.'
        
        #Place data
        op.append(msg)
        
        #Update output data
        self.mainWindow.data.outputList[cs] = op
        co.loadValues()
        co.update()
        
        print('Database')
        
    
    #table combo
    def ttable(self):
        t = threading.Thread(target=self.table)
        t.start()
        
    def table(self):
        
        #Detect previous shape
        con = self.mainWindow.canvas.connections.copy()
        
        if self.mainWindow.data.isQueueRunning:
            cs = self.mainWindow.data.currentExecution
        else:
            cs = self.mainWindow.canvas.currentShape
        
        ps = -1
        
        for i in con:
            if i[1] == cs:
                ps = i[0]
                break
                
                
        if ps == -1:
            print('Table is not in a queue')
            return
            
        #Detect valid previous shape
        
        lim = len(con)*2
        
        while lim > 0:
        
            if self.mainWindow.canvas.shapes[ps][1] in self.rules[self.mainWindow.canvas.shapes[cs][1]]:
                break
            else:
                for i in con:
                    if i[1] == ps:
                        ps = i[0]
                        break
        
            lim -= 1
            
        if self.mainWindow.canvas.shapes[ps][1] not in self.rules[self.mainWindow.canvas.shapes[cs][1]]:
            print('Table is not in a queue')
            return
            
        #Save input data
        self.mainWindow.canvas.previousShape = self.mainWindow.canvas.currentShape
        self.mainWindow.data.currentInputFrame.saveValues()
        
        co = self.mainWindow.data.currentOutputFrame
        ip = self.mainWindow.data.inputList[cs]
        op = list()
        
        #Core Function
        
        try:
            db = self.db
            cursor = db.cursor()
        except:
            print('Database is not connected.')
            return
        
        tableName = ip[1]
        rowCode = ip[2]
        
        cols = list()
        colNames = list()
        con = self.mainWindow.canvas.connections.copy()
        
        for i in con:
            if i[0] == cs:
            
                if len(self.mainWindow.data.inputList[i[1]]) > 0:
                    cols.append([
                    self.mainWindow.data.inputList[i[1]][1],
                    self.mainWindow.data.inputList[i[1]][2],
                    self.mainWindow.data.inputList[i[1]][3]]
                    )
                    
                    colNames.append(self.mainWindow.data.inputList[i[1]][1])
                
        rows = self.driver.find_elements_by_css_selector(rowCode)
        

        for r in rows:
        
            i = 0
            dataList = list()
            colName = ''
            colData = ''
            
            for c in cols:
            
                cells = r.find_elements_by_css_selector(cols[i][1])
                
                try:
                    data = cells[cols[i][2]-1].get_attribute('innerHTML')
                    data = data.replace("'","")
                    data = data.replace('"',"")
                    data = data.replace('’',"")
                except:
                    data = ''
                    
                dataList.append(data)
            
                i += 1
                
            for c in colNames:
                colName += "`"+ c +"`,"
            colName = colName[:-1]
            
            for c in dataList:
                colData += "'"+ c +"',"
            colData = colData[:-1]
            
            sql = 'insert into '+tableName+'('+colName+')'+' values ('+colData+')'
            
            #insert data
            
            try:
                cursor.execute(sql)
                db.commit()
            except Exception as e:
                print(sql)
                pyperclip.copy(sql)
                print(str(e))
                print('----------------------------------------------------------')
            pass
            
        
        #Place data
        #op.append(msg)
        
        #Update output data
        self.mainWindow.data.outputList[cs] = op
        co.loadValues()
        co.update()
        
        print('Table')
    
    
    #Download combo
    def tdownload(self):
        t = threading.Thread(target=self.download)
        t.start()
        
    def download(self):
        
        #Detect previous shape
        con = self.mainWindow.canvas.connections.copy()
        
        if self.mainWindow.data.isQueueRunning:
            cs = self.mainWindow.data.currentExecution
        else:
            cs = self.mainWindow.canvas.currentShape
        
        ps = -1
        
        for i in con:
            if i[1] == cs:
                ps = i[0]
                break
                
                
        if ps == -1:
            print('Download is not in a queue')
            return
            
        #Detect valid previous shape
        
        lim = len(con)*2
        
        while lim > 0:
        
            if self.mainWindow.canvas.shapes[ps][1] in self.rules[self.mainWindow.canvas.shapes[cs][1]]:
                break
            else:
                for i in con:
                    if i[1] == ps:
                        ps = i[0]
                        break
        
            lim -= 1
            
        if self.mainWindow.canvas.shapes[ps][1] not in self.rules[self.mainWindow.canvas.shapes[cs][1]]:
            print('Download is not in a queue')
            return
            
        #Save input data
        self.mainWindow.canvas.previousShape = self.mainWindow.canvas.currentShape
        self.mainWindow.data.currentInputFrame.saveValues()
        
        co = self.mainWindow.data.currentOutputFrame
        ip = self.mainWindow.data.inputList[cs]
        op = list()
        
        #Core Function
        
        u = self.mainWindow.data.outputList[ps].copy()
        path = ip[1]
        downloaded = 0
        failed = 0
        total = len(u)
        skipped = 0
        
        for i in u:
        
            try:
            
                checkpath = Path(path + '/' + i[0])
                if checkpath.is_file():
                    skipped += 1
                    continue
                    
                f = open(path + '/' + i[0],'wb')

                q = Request(i[1])
                q.add_header('User-Agent',
                             'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
                q.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
                q.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3')
                q.add_header('Accept-Encoding', 'none')
                q.add_header('Accept-Language', 'en-US,en;q=0.8')
                q.add_header('Connection', 'keep-alive')

                site = urlopen(q)

                data = site.read()
                f.write(data)
                f.close()
                site.close()
                
                downloaded += 1
            except:
                failed += 1
        
        #Place data
        op.append(total)
        op.append(downloaded)
        op.append(skipped)
        op.append(failed)
        
        #Update output data
        self.mainWindow.data.outputList[cs] = op
        co.loadValues()
        co.update()
        
        print('Download')
        
        
    def execQueue(self):
        con = self.mainWindow.canvas.connections.copy()
        start = list()
        ilp = len(con) * 2
        #Find start
        
        t=0
        for i in con:
            if (self.mainWindow.canvas.shapes[i[0]][0],self.mainWindow.canvas.shapes[i[0]][1]) == (0,1):
                start = [t]
                break
            t += 1
        
            
        #Start making queue
        e = list()
        e.append(start)

        i=0
        while True:
            e.append(list())
            for j in con:
                if j[0] in start:
                    e[i+1].append(j[1])
            start = e[i+1]
            if len(start) == 0:
                e.pop(i+1)
                break
            i += 1
            ilp -= 1
            
            if ilp < 0:
                e = [[]]
                self.mainWindow.status.setMessage('Infinite execution queue detected. Restart the program and try again.',2)
                self.mainWindow.status.update()
                break
        
        #Queue generated
        self.mainWindow.data.q = e.copy()
        self.tstartQueue()
        
    #Start queue combo
    def tstartQueue(self):
        t = threading.Thread(target=self.startQueue)
        try:
            t.start()
        except:
            self.mainWindow.status.setMessage('Execution queue terminated. Please try again.',2)
            self.mainWindow.status.update()
            self.mainWindow.canvas.buttonPlay.setChecked(False)
        
    def startQueue(self):
    
        self.mainWindow.input.stackedView.setCurrentIndex(0)
        self.mainWindow.output.stackedView.setCurrentIndex(0)
        
        self.mainWindow.status.setMessage('Execution queue started.',1)
        self.mainWindow.status.update()
    
        t = -1
        s = -1
        q = self.mainWindow.data.q.copy()
        
        total = 0
        for i in q:
            total += len(i)
            
        self.mainWindow.output.t00.t = 0
        self.mainWindow.output.t00.update()
        
        self.mainWindow.data.isQueueRunning = True
        
        for j in q:
            for i in j:
                self.mainWindow.data.currentExecution = i
                t = self.mainWindow.canvas.shapes[i][0]
                s = self.mainWindow.canvas.shapes[i][1]
                try:
                    self.mainWindow.pycore.functionSelect[t][s]()
                except:
                    pass
                self.mainWindow.output.t00.t += 1/total*100
                self.mainWindow.output.t00.update()
            
        self.mainWindow.output.t00.t = 100
        self.mainWindow.output.t00.update()
        
        self.mainWindow.status.setMessage('Execution queue completed successfully.',1)
        self.mainWindow.status.update()
        
        self.mainWindow.data.isQueueRunning = False
        self.mainWindow.canvas.buttonPlay.setChecked(False)
    
#========================================================================================================================