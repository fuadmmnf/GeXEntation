# Autor:  Saif Kamal Chowdhury



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, pyqtSignal, QTimer
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QMessageBox,QComboBox,QHBoxLayout,QActionGroup,QSystemTrayIcon,QStyle,QAction,qApp,QMenu
tray_icon = None
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
        newfile=open("../../rsc/appSelected.txt","w+")
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
        self.setStyleSheet("*{background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #2193b0, stop:1 #79f1fc);}")



    #minimize effort
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(self.style().standardIcon(QStyle.SP_ComputerIcon))
 
        
        show_action = QAction("Show", self)
        quit_action = QAction("Exit", self)
        hide_action = QAction("Hide", self)
        show_action.triggered.connect(self.show)
        hide_action.triggered.connect(self.hide)
        quit_action.triggered.connect(qApp.quit)
        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()






        
        self.initUI()

    def initUI(self):
       
        self.button = QtWidgets.QPushButton('Start', self)

        self.button.setStyleSheet("QPushButton{background:#4254f7;"
                                   "border-radius: 8px;font-size:13px;"
                                   "border-bottom-style: solid;border-width: 4px;border-color:#070f59;"
                                   "}::hover {  background-color: #070f59;color:white;  border-color:#070f59 ;border-width: 2px; top: 2px;}")
        self.button.setGeometry(320, 100, 90, 30)

        self.button1 = QtWidgets.QPushButton('Applications', self)
        #self.button1.setStyleSheet("QPushButton{ border: 1px "
        #                           "#; border-radius: 4.5px;font-size:20px;}")

        self.button1.setStyleSheet("QPushButton{background:#4254f7;"
                                   "border-radius: 8px;font-size:13px;"
                                   "border-bottom-style: solid;border-width: 4px;border-color:#070f59;"
                                   "}::hover {  background-color: #070f59;color:white;  border-color:#070f59 ;border-width: 2px; top: 2px;}")


        self.button1.setGeometry(320, 140, 90, 30)
        self.button1.clicked.connect(self.app_supported)



        self.button2 = QtWidgets.QPushButton('Exit', self)
#        self.button2.setStyleSheet("QPushButton{background:qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #c2e59c, stop:1 #64b3f4); "
#                                   "border-radius: 8px;font-size:13px;border:1 px solid black;}")
        self.button2.setStyleSheet("QPushButton{background:#4254f7;"
                                   "border-radius: 8px;font-size:13px;"
                                   "border-bottom-style: solid;border-width: 4px;border-color:#070f59;"
                                   "}::hover {  background-color: #070f59;color:white;  border-color:#070f59 ;border-width: 2px; top: 2px;}")

        self.button2.setGeometry(320, 180, 90, 30)
        self.button2.clicked.connect(self.close)


        self.hidden_button = QtWidgets.QPushButton('', self)
        self.hidden_button.setCursor(Qt.PointingHandCursor)
        self.hidden_button.setToolTip("1st Gesture")
        self.hidden_button.setIcon(QtGui.QIcon('palm.png'))
        self.hidden_button.setIconSize(QtCore.QSize(120, 130))
        self.hidden_button.setGeometry(50, 40, 120, 130)
        self.hidden_button.setStyleSheet(
            "QPushButton{background-color: transparent; border-style:outset; border-radius: 50px; border-width:0px;}::hover{"
            "background-color:white}::pressed{background-color: cyan}")        
        self.hidden_button.clicked.connect(self.manual)

        self.gest_1_label = QtWidgets.QLabel(fist_gesture, self)
        self.gest_1_label.setGeometry(73,155,120,50)

        self.gest_1_label.setStyleSheet("QLabel{background:transparent;font-size:14px;}")
        self.hidden_button2 = QtWidgets.QPushButton('', self)
        self.hidden_button2.setCursor(Qt.PointingHandCursor)
        self.hidden_button2.setIcon(QtGui.QIcon('fist.png'))
        self.hidden_button2.setIconSize(QtCore.QSize(120, 130))
        self.hidden_button2.setGeometry(180,40, 120, 130)
        self.hidden_button2.setStyleSheet(
            "QPushButton{background-color: transparent; border-style:outset;border-radius: 50px; border-width:0px;}::hover{"
            "background-color:white}::pressed{background-color: cyan}")
        self.hidden_button2.clicked.connect(self.manual_2)

        self.gest_2_label = QtWidgets.QLabel(palm_gesture, self)
        self.gest_2_label.setGeometry(203, 155, 120, 50)
        self.gest_2_label.setStyleSheet("QLabel{background:transparent;font-size:14px;}")


        self.hidden_button3 = QtWidgets.QPushButton('', self)
        self.hidden_button3.setCursor(Qt.PointingHandCursor)
        self.hidden_button3.setIcon(QtGui.QIcon('thumbs_down.png'))
        self.hidden_button3.setIconSize(QtCore.QSize(120, 130))
        self.hidden_button3.setGeometry(50, 200, 120, 130)
        self.hidden_button3.setStyleSheet(
            "QPushButton{background-color: transparent; border-style:outset;border-radius: 50px; border-width:0px;}::hover{"
            "background-color:white}::pressed{background-color: cyan}")
        self.hidden_button3.clicked.connect(self.manual_3)


        self.gest_3_label = QtWidgets.QLabel(point_gesture, self)
        self.gest_3_label.setGeometry(73,315, 120, 50)
        self.gest_3_label.setStyleSheet("QLabel{background:transparent;font-size:14px;}")



        self.hidden_button4 = QtWidgets.QPushButton('', self)
        self.hidden_button4.setCursor(Qt.PointingHandCursor)
        self.hidden_button4.setIcon(QtGui.QIcon('loser.png'))
        self.hidden_button4.setIconSize(QtCore.QSize(120, 130))
        self.hidden_button4.setGeometry(180, 200, 120, 130)
        self.hidden_button4.setStyleSheet(
            "QPushButton{background-color: transparent; border-style:outset;border-radius: 50px; border-width:0px;}::hover{"
            "background-color:white}::pressed{background-color: cyan}")

        self.hidden_button4.clicked.connect(self.manual_4)

        self.gest_4_label = QtWidgets.QLabel(thumbDown_gesture, self)
        self.gest_4_label.setGeometry(203,315, 120, 50)
     
        self.gest_4_label.setStyleSheet("QLabel{background:transparent;font-size:14px;}")
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
        
        menu.setStyleSheet("QMenu{background-color:#00FFF7;border-radius:5px;   }")

        # self.hidden_button.setStyleSheet(
        #     "QPushButton{border-style:inset; border-width:0px;}"
        #     "::hover{"
        #     "background-color:white}"
        #     "::menu-indicator{ image: none; }::pressed{background-color:cyan}")

        #panelPos = QtCore.QPoint(self.hidden_button.pos().x() - 120, self.hidden_button.pos().y())
        panelPos = QtCore.QPoint(self.hidden_button2.pos().x() - 120, self.hidden_button2.pos().y())
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

        panelPos = QtCore.QPoint(self.hidden_button3.pos().x() - 120, self.hidden_button3.pos().y())
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

        panelPos = QtCore.QPoint(self.hidden_button4.pos().x() - 120, self.hidden_button4.pos().y())
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
        self.ui.pushButton.clicked.connect(self.window.hide)


        # for i in range(3):
        #     checkBox = QtWidgets.QCheckBox(str(i), toolMenu)
        #     checkableAction = QtWidgets.QWidgetAction(toolMenu)
        #     checkableAction.setDefaultWidget(checkBox)
        #     toolMenu.addAction(checkableAction)

    def closeEvent(self, event):
        
            event.ignore()
            self.hide()
            self.tray_icon.showMessage(
                "Tray Program",
                "Application was minimized to Tray",
                QSystemTrayIcon.Information,
                2000
            )
 






if __name__ == '__main__':
    import sys


    fist_gesture = ""
    palm_gesture = ""
    point_gesture = ""
    thumbDown_gesture = ""

    aplicacion = QApplication(sys.argv)

    ventana = labelClickable()
    ventana.show()

    sys.exit(aplicacion.exec_())
