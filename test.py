import sys
import os
import threading
import requests
import time

from urllib.request import Request, urlopen
from selenium import webdriver
from pathlib import Path
from selenium.webdriver.common.keys import Keys


from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import *
from PyQt5 import QtGui
from PyQt5.QtWidgets import *

option = webdriver.ChromeOptions()
option.add_extension('Block-image_v1.1.crx')
driver = webdriver.Chrome(chrome_options=option)
driver.get('https://www.flipkart.com/search?q=laptop%20stand')


rows = driver.find_elements_by_css_selector('#container > div > div:nth-child(2) > div > div._1XdvSH._17zsTh > div > div._2xw3j- > div > div:nth-child(3) > div._2SxMvQ > div > div > div')
for i in rows:
    op = ''
    cell = i.find_elements_by_css_selector('a._1Vfi6u > div > div.VGWI6T')
        
    for j in cell:
        print(j.get_attribute('innerHTML'))
    
driver.close()