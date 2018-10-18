# Autor:  Saif Kamal Chowdhury
import cv2
import numpy as np
import math
import os
import time
import pyautogui


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, pyqtSignal, QTimer
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QMessageBox,QComboBox,QHBoxLayout,QActionGroup

class Ui_Form(object):



    









    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(240, 270, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 270, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 401, 261))
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setStyleSheet("QListWidget{border: 0px;padding-left: 10px;}")
        #self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidget.itemSelectionChanged.connect(self.on_change)
        self.retranslateUi(Form)

        self.pushButton.clicked.connect(self.print_info)



        QtCore.QMetaObject.connectSlotsByName(Form)
    def on_change(self):
        self.x=[]
        for item in self.listWidget.selectedItems():
            self.x.append(item.text())
#        print([x.append(item.text()) for item in self.listWidget.selectedItems()])
       # print(self.x)

    def print_info(self):
        #print("OK pressed")
        newfile=open("appSelected.txt","w+")
        for i in range(0,len(self.x)):
            newfile.write(self.x[i])
            newfile.write("\n")




    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Ok"))
        self.pushButton_2.setText(_translate("Form", "Cancel"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        file = open('../../rsc/applications.txt', 'r+')
        temp = file.read()
        lines = temp.split("\n")

        #self.listWidget.addItems(lines)
        for i in range (0,len(lines)):

            item = QtWidgets.QListWidgetItem()
            item.setText(lines[i].replace('.desktop', ''))
            #item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            #item.setCheckState(QtCore.Qt.Unchecked)
            self.listWidget.addItem(item)




















class labelClickable(QDialog):
    def __init__(self, parent=None):
        super(labelClickable, self).__init__(parent)

        self.file=open('../../rsc/actions.txt','r+')
        self.temp= self.file.read()
        self.lines= self.temp.split("\n")

        self.gestureNum  = -1

        self.setWindowTitle("GeXentation")
        self.setWindowIcon(QIcon("icon.png"))
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(500, 400)

        self.initUI()

    def initUI(self):
       
        self.button = QtWidgets.QPushButton('Start', self)
        self.button.setStyleSheet("QPushButton{ border: 1px "
                                  "#; border-radius: 4.5px;font-size:20px;}")
        self.button.setGeometry(320, 100, 80, 30)
        self.button.clicked.connect(self.startWeb)


        self.button1 = QtWidgets.QPushButton('Applications', self)
        self.button1.setStyleSheet("QPushButton{ border: 1px "
                                   "#; border-radius: 4.5px;font-size:20px;}")
        self.button1.setGeometry(320, 140, 80, 30)
        self.button1.clicked.connect(self.app_supported)



        self.button2 = QtWidgets.QPushButton('Exit', self)
        self.button2.setStyleSheet("QPushButton{border: 1px "
                                   "#; border-radius: 4.5px;font-size:20px;}")

        self.button2.setGeometry(320, 180, 80, 30)
        self.button2.clicked.connect(self.close)


        self.hidden_button = QtWidgets.QPushButton('', self)
        self.hidden_button.setCursor(Qt.PointingHandCursor)
        self.hidden_button.setToolTip("1st Gesture")
        self.hidden_button.setIcon(QtGui.QIcon('hand.jpg'))
        self.hidden_button.setIconSize(QtCore.QSize(120, 130))
        self.hidden_button.setGeometry(50, 40, 120, 130)
        self.hidden_button.setStyleSheet(
            "QPushButton{background-color: transparent; border-style:outset; border-radius: 4px; border-width:0px;}::hover{"
            "background-color:white}::pressed{background-color: cyan}")        
        self.hidden_button.clicked.connect(self.manual)

        self.gest_1_label = QtWidgets.QLabel(fist_gesture, self)
        self.gest_1_label.setGeometry(73,155,100,50)


        self.hidden_button2 = QtWidgets.QPushButton('', self)
        self.hidden_button2.setCursor(Qt.PointingHandCursor)
        self.hidden_button2.setIcon(QtGui.QIcon('fist.jpg'))
        self.hidden_button2.setIconSize(QtCore.QSize(120, 130))
        self.hidden_button2.setGeometry(180,40, 120, 130)
        self.hidden_button2.setStyleSheet(
            "QPushButton{background-color: transparent; border-style:outset;border-radius: 4px; border-width:0px;}::hover{"
            "background-color:white}::pressed{background-color: cyan}")
        self.hidden_button2.clicked.connect(self.manual_2)

        self.gest_2_label = QtWidgets.QLabel(palm_gesture, self)
        self.gest_2_label.setGeometry(203, 155, 100, 50)



        self.hidden_button3 = QtWidgets.QPushButton('', self)
        self.hidden_button3.setCursor(Qt.PointingHandCursor)
        self.hidden_button3.setIcon(QtGui.QIcon('thumbDown.jpg'))
        self.hidden_button3.setIconSize(QtCore.QSize(120, 130))
        self.hidden_button3.setGeometry(50, 200, 120, 130)
        self.hidden_button3.setStyleSheet(
            "QPushButton{background-color: transparent; border-style:outset;border-radius: 4px; border-width:0px;}::hover{"
            "background-color:white}::pressed{background-color: cyan}")
        self.hidden_button3.clicked.connect(self.manual_3)


        self.gest_3_label = QtWidgets.QLabel(point_gesture, self)
        self.gest_3_label.setGeometry(73,315, 100, 50)




        self.hidden_button4 = QtWidgets.QPushButton('', self)
        self.hidden_button4.setCursor(Qt.PointingHandCursor)
        self.hidden_button4.setIcon(QtGui.QIcon('loser1.jpg'))
        self.hidden_button4.setIconSize(QtCore.QSize(120, 130))
        self.hidden_button4.setGeometry(180, 200, 120, 130)
        self.hidden_button4.setStyleSheet(
            "QPushButton{background-color: transparent; border-style:outset;border-radius: 4px; border-width:0px;}::hover{"
            "background-color:white}::pressed{background-color: cyan}")

        self.hidden_button4.clicked.connect(self.manual_4)

        self.gest_4_label = QtWidgets.QLabel(thumbDown_gesture, self)
        self.gest_4_label.setGeometry(203,315, 100, 50)
     
        
        #self.labelImagen.clicked.connect(self.Clic)
        #self.label_2.clicked.connect(self.secondClick)
        #self.label_3.clicked.connect(self.thirdClick)
        #self.label_4.clicked.connect(self.fourthClick)

    # ======================= FUNCTIONS ============================

    def Clic(self,action):
        #QMessageBox.information(self, "1st Gesture","1st Gesture was clicked")
        
        if self.gestureNum == 1:
            fist_gesture = action.text()
            self.gest_1_label.setText(fist_gesture)
        elif self.gestureNum == 2:
            palm_gesture = action.text()
            self.gest_2_label.setText(palm_gesture)
        elif self.gestureNum == 3:
            point_gesture = action.text()
            self.gest_3_label.setText(point_gesture)
        elif self.gestureNum == 4:
            thumbDown_gesture = action.text()
            self.gest_4_label.setText(thumbDown_gesture)
        




    # def secondClick(self):
    #     QMessageBox.information(self, "2nd Gesture", "2nd Gesture was clicked")

    # def thirdClick(self):
    #     QMessageBox.information(self, "3rd Gesture", "3rd Gesture was clicked")

    # def fourthClick(self):
    #     QMessageBox.information(self, "4th Gesture", "4th Gesture was clicked")

    # def close(self):
    #     QApplication.quit()

    def manual(self):

        menu = QtWidgets.QMenu()
        menu.setStyleSheet("QMenu{menu-scrollable: 1;background-color:#00FFF7;border-radius:5px; "
                           "width:140px}")

        
        for line in self.lines:
            menu.addAction(line)

        self.gestureNum = 1

        menu.triggered.connect(self.Clic)
        # panelPos = QtCore.QPoint(self.hidden_button.pos().x() - 100, self.hidden_button.pos().y())
        # menu.setStyleSheet("QMenu{background-color:#00FFF7;border-radius:5px;   }")

        # self.hidden_button.setStyleSheet(
        #     "QPushButton{border-style:inset; border-width:0px;}"
        #     "::hover{"
        #     "background-color:white}"
        #     "::menu-indicator{ image: none; }::pressed{background-color:cyan}")

        panelPos = QtCore.QPoint(self.hidden_button.pos().x() - 120, self.hidden_button.pos().y())
        action=menu.exec_(self.mapToGlobal(panelPos))


        #self.hidden_button.setMenu(menu)

    def manual_2(self):

        menu = QtWidgets.QMenu()
        menu.setStyleSheet("QMenu{menu-scrollable: 1;background-color:#00FFF7;border-radius:5px; "
                           "width:140px}")

      
        for line in self.lines:
            menu.addAction(line)

        self.gestureNum = 2

        menu.triggered.connect(self.Clic)
        # panelPos = QtCore.QPoint(self.hidden_button.pos().x() - 100, self.hidden_button.pos().y())
        # menu.setStyleSheet("QMenu{background-color:#00FFF7;border-radius:5px;   }")

        # self.hidden_button.setStyleSheet(
        #     "QPushButton{border-style:inset; border-width:0px;}"
        #     "::hover{"
        #     "background-color:white}"
        #     "::menu-indicator{ image: none; }::pressed{background-color:cyan}")

        panelPos = QtCore.QPoint(self.hidden_button.pos().x() - 120, self.hidden_button.pos().y())
        action=menu.exec_(self.mapToGlobal(panelPos))


        #self.hidden_button.setMenu(menu)


    def manual_3(self):

        menu = QtWidgets.QMenu()
        menu.setStyleSheet("QMenu{menu-scrollable: 1;background-color:#00FFF7;border-radius:5px; "
                           "width:140px}")

        
        for line in self.lines:
            menu.addAction(line)

        self.gestureNum = 3

        menu.triggered.connect(self.Clic)
        # panelPos = QtCore.QPoint(self.hidden_button.pos().x() - 100, self.hidden_button.pos().y())
        # menu.setStyleSheet("QMenu{background-color:#00FFF7;border-radius:5px;   }")

        # self.hidden_button.setStyleSheet(
        #     "QPushButton{border-style:inset; border-width:0px;}"
        #     "::hover{"
        #     "background-color:white}"
        #     "::menu-indicator{ image: none; }::pressed{background-color:cyan}")

        panelPos = QtCore.QPoint(self.hidden_button.pos().x() - 120, self.hidden_button.pos().y())
        action=menu.exec_(self.mapToGlobal(panelPos))


        #self.hidden_button.setMenu(menu)


    def manual_4(self):

        menu = QtWidgets.QMenu()
        menu.setStyleSheet("QMenu{menu-scrollable: 1;background-color:#00FFF7;border-radius:5px; "
                           "width:140px}")

        
        for line in self.lines:
            menu.addAction(line)

        self.gestureNum = 4

        menu.triggered.connect(self.Clic)
        # panelPos = QtCore.QPoint(self.hidden_button.pos().x() - 100, self.hidden_button.pos().y())
        # menu.setStyleSheet("QMenu{background-color:#00FFF7;border-radius:5px;   }")

        # self.hidden_button.setStyleSheet(
        #     "QPushButton{border-style:inset; border-width:0px;}"
        #     "::hover{"
        #     "background-color:white}"
        #     "::menu-indicator{ image: none; }::pressed{background-color:cyan}")

        panelPos = QtCore.QPoint(self.hidden_button.pos().x() - 120, self.hidden_button.pos().y())
        action=menu.exec_(self.mapToGlobal(panelPos))


        #self.hidden_button.setMenu(menu)


    def app_supported(self):
        # file=open('../../rsc/applications.txt','r+')
        # x = str()
        # x = file.read()
        # lines = x.split("\n")

        # toolMenu = QtWidgets.QMenu()
        # toolMenu.setStyleSheet("QMenu { menu-scrollable: 1; }")
        # for i in range(0,len(lines)):
        #     checkBox = QtWidgets.QCheckBox(lines[i], toolMenu)
        #     checkableAction = QtWidgets.QWidgetAction(toolMenu)
        #     checkableAction.setDefaultWidget(checkBox)
        #     toolMenu.addAction(checkableAction)

        self.window=QtWidgets.QWidget()
        self.ui =Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()


        # for i in range(3):
        #     checkBox = QtWidgets.QCheckBox(str(i), toolMenu)
        #     checkableAction = QtWidgets.QWidgetAction(toolMenu)
        #     checkableAction.setDefaultWidget(checkBox)
        #     toolMenu.addAction(checkableAction)




    def execute(self, str):
        print(str,'left_mouse click')
        if str == 'left_mouse click':
            pyautogui.click( button = 'left' )
            print('kam hoise')
        elif str == 'right_mouse click':
            pyautogui.click( button = 'right' )
        elif str == 'middle_mouse click':
            pyautogui.click( button = 'middle' )
        elif str == 'scroll_up':
            pyautogui.scroll(10)
        elif str == 'scroll_down':
            pyautogui.scroll(-10)
        elif str == 'scroll_right':
            pyautogui.hscroll(10)
        elif str == 'scroll_left':
            pyautogui.hscroll(-10)
        elif str == 'page_up':
            pyautogui.press('pgup')
        elif str == 'page_down':
            pyautogui.press('pgdn')
        elif str == 'zoom_out':
            pyautogui.keydown('shift')
            pyautogui.press('+')
            pyautogui.keyup('shift')
        elif str == 'zoom_in':
            pyautogui.keydown('shift')
            pyautogui.press('-')
            pyautogui.keyup('shift')
        elif str == 'refresh':
            pyautogui.press('f5')
        elif str == 'screenshot':
            pyautogui.screenshot()
        elif str == 'volume_up':
            pyautogui.press('volumeup')
        elif str == 'volume_down':
            pyautogui.press('volumedown')
        elif str == 'next_track':
            pyautogui.press('nexttrack')
        elif str == 'prev_track':
            pyautogui.press('prevtrack')
        elif str == 'play/pause':
            pyautogui.press('playpause')


















    def startWeb(self):

        # gesture detection code
        cap = cv2.VideoCapture(0)
        start_time = -1 
        finish_time = 0
        while(1):   
                isValid = False;

                _,img=cap.read()
                #cv2.imshow('Webcam',img)
                        
                k=cv2.waitKey(10)
                if k==27:
                        break


                finish_time = time.time()
                if(start_time==-1 or finish_time-start_time>=1):
                
                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        
                        #point = point_cascade.detectMultiScale(gray,1.1,5)
                        #fin=fin_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5,flags=0, minSize=(100,80))
                        right_palm = right_h1_cascade.detectMultiScale(gray,1.1, 5)
                        point=point_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3,flags=0, minSize=(100,80))
                        #hand = hand_cascade.detectMultiScale(gray,1.1, 5)
                        #LtoR=hand_left_to_right_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3,flags=0, minSize=(100,150))
                        #RtoL=hand_right_to_left_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3,flags=0, minSize=(100,150))
                        #finger_count = finger_count_cascade.detectMultiScale(gray,1.1,5)
                        #left_palm = left_h1_cascade.detectMultiScale(gray,1.1, 5)
                        #right_dir = right_cascade.detectMultiScale(gray,1.1, 5)
                        #left_dir = left_cascade.detectMultiScale(gray,1.1, 5)
                        fist=fist_cascade.detectMultiScale(gray,1.1, 5)
                        #fist=fist_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3,flags=0, minSize=(100,150))

                        thumbdown=thumbdown_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3,flags=0, minSize=(100,80))





                        for (x,y,w,h) in fist:
                                print(self.gest_1_label.text())
                                self.execute(self.gest_1_label.text())
                                print('fist')
                                start_time = time.time()
                               

                        for (x,y,w,h) in right_palm:
                                self.execute(self.gest_2_label.text())
                                print('palm')
                                start_time = time.time()




                        for (x,y,w,h) in point:
                                self.execute(self.gest_3_label.text())
                                print('point')
                                start_time = time.time()
                        

                        for (x,y,w,h) in thumbdown:   
                            print('thumbdown')
                            self.execute(self.gest_4_label.text())
                            start_time = time.time()


                        
        cap.release()    
        cv2.destroyAllWindows()









if __name__ == '__main__':
    import sys


    fist_gesture = ""
    palm_gesture = ""
    point_gesture = ""
    thumbDown_gesture = ""


    #haar cascades initializatoin
    right_h1_cascade=cv2.CascadeClassifier('../../rsc/haar_cascades/rpalm.xml') # right palm
    #hand_cascade = cv2.CascadeClassifier('heppu_handa.xml')
    #left_h1_cascade=cv2.CascadeClassifier('./haarCascades/lpalm.xml') #left palm
    #right_cascade=cv2.CascadeClassifier('./haarCascades/right.xml') #right direction
    #left_cascade=cv2.CascadeClassifier('left.xml') #left direction
    #finger_count_cascade = cv2.CascadeClassifier('finger_count.xml')
    #okay_cascade = cv2.CascadeClassifier('./haarCascades/ok.xml') # okay sign
    point_cascade = cv2.CascadeClassifier('../../rsc/haar_cascades/point1.xml')
    #fin_cascade=cv2.CascadeClassifier('./haarCascades/fin_2.xml') 
    #hand_left_to_right_cascade = cv2.CascadeClassifier('./haarCascades/heppu_handb.xml')
    #hand_right_to_left_cascade = cv2.CascadeClassifier('./haarCascades/heppu_hands.xml')
    fist_cascade=cv2.CascadeClassifier('../../rsc/haar_cascades/fist.xml') # fist
    thumbdown_cascade = cv2.CascadeClassifier('../../rsc/haar_cascades/thumbdown.xml')

    #--------------------------------------------



    aplicacion = QApplication(sys.argv)

    ventana = labelClickable()
    ventana.show()

    sys.exit(aplicacion.exec_())
