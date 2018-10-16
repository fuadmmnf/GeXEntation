# Autor:  Saif Kamal Chowdhury XD
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, pyqtSignal, QTimer
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QMessageBox,QComboBox,QHBoxLayout,QActionGroup


# ===================== CLASE QLabelClickable ======================

class QLabelClickable(QLabel):
    clicked = pyqtSignal(str)

    def __init__(self, parent=None):
        super(QLabelClickable, self).__init__(parent)

    def mousePressEvent(self, event):
        self.ultimo = "Clic"

    def mouseReleaseEvent(self, event):
        if self.ultimo == "Clic":
            QTimer.singleShot(QApplication.instance().doubleClickInterval(),
                              self.performSingleClickAction)
        else:
            # Realizar acción de doble clic.
            self.clicked.emit(self.ultimo)

    def mouseDoubleClickEvent(self, event):
        self.ultimo = "Doble Clic"

    def performSingleClickAction(self):
        if self.ultimo == "Clic":
            self.clicked.emit(self.ultimo)


# ===================== CLASE labelClickable =======================

class labelClickable(QDialog):
    def __init__(self, parent=None):
        super(labelClickable, self).__init__(parent)

        self.setWindowTitle("GeXentation")
        self.setWindowIcon(QIcon("icon.png"))
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(500, 400)

        self.initUI()

    def initUI(self):
        # ==================== WIDGET QLABEL =======================
        layout=QHBoxLayout()
        self.button = QtWidgets.QPushButton('Start', self)
        self.button.setStyleSheet("QPushButton{ border: 1px "
                                  "#; border-radius: 4.5px;font-size:20px;}")
        self.button.setGeometry(320, 100, 80, 30)

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
        self.hidden_button.setIcon(QtGui.QIcon('1.png'))
        self.hidden_button.setIconSize(QtCore.QSize(120, 130))
        self.hidden_button.setGeometry(50, 40, 120, 130)
        self.hidden_button.setStyleSheet(
            "QPushButton{background-color: transparent; border-style:outset; border-radius: 4px; border-width:0px;}::hover{"
            "background-color:white}::pressed{background-color: cyan}")


        self.hidden_button.clicked.connect(self.actions)

        self.hidden_button2 = QtWidgets.QPushButton('', self)
        self.hidden_button2.setCursor(Qt.PointingHandCursor)
        self.hidden_button2.setIcon(QtGui.QIcon('2.png'))
        self.hidden_button2.setIconSize(QtCore.QSize(120, 130))
        self.hidden_button2.setGeometry(180,40, 120, 130)
        self.hidden_button2.setStyleSheet(
            "QPushButton{background-color: transparent; border-style:outset;border-radius: 4px; border-width:0px;}::hover{"
            "background-color:white}::pressed{background-color: cyan}")

        self.hidden_button2.clicked.connect(self.actions)

        self.hidden_button3 = QtWidgets.QPushButton('', self)
        self.hidden_button3.setCursor(Qt.PointingHandCursor)
        self.hidden_button3.setIcon(QtGui.QIcon('3.png'))
        self.hidden_button3.setIconSize(QtCore.QSize(120, 130))
        self.hidden_button3.setGeometry(50, 180, 120, 130)
        self.hidden_button3.setStyleSheet(
            "QPushButton{background-color: transparent; border-style:outset;border-radius: 4px; border-width:0px;}::hover{"
            "background-color:white}::pressed{background-color: cyan}")

        self.hidden_button3.clicked.connect(self.actions)

        self.hidden_button4 = QtWidgets.QPushButton('', self)
        self.hidden_button4.setCursor(Qt.PointingHandCursor)
        self.hidden_button4.setIcon(QtGui.QIcon('4.png'))
        self.hidden_button4.setIconSize(QtCore.QSize(120, 130))
        self.hidden_button4.setGeometry(180, 180, 120, 130)
        self.hidden_button4.setStyleSheet(
            "QPushButton{background-color: transparent; border-style:outset;border-radius: 4px; border-width:0px;}::hover{"
            "background-color:white}::pressed{background-color: cyan}")

        self.hidden_button4.clicked.connect(self.actions)


        #self.labelImagen.clicked.connect(self.Clic)
        #self.label_2.clicked.connect(self.secondClick)
        #self.label_3.clicked.connect(self.thirdClick)
        #self.label_4.clicked.connect(self.fourthClick)

    # ======================= FUNCTIONS ============================

    def Clic(self):
        QMessageBox.information(self, "1st Gesture","1st Gesture was clicked")
        print("1st gesture")

        #self.labelImagen.setContextMenuPolicy(menu)




    def secondClick(self):
        QMessageBox.information(self, "2nd Gesture", "2nd Gesture was clicked")

    def thirdClick(self):
        QMessageBox.information(self, "3rd Gesture", "3rd Gesture was clicked")

    def fourthClick(self):
        QMessageBox.information(self, "4th Gesture", "4th Gesture was clicked")

    def close(self):
        QApplication.quit()

    def actions(self):
        menu = QtWidgets.QMenu()
        with open('../../rsc/actions.txt') as fp:
            for line in fp:
                menu.addAction(line, self.Clic)


        # menu.addAction('hmmm',self.Clic)
        # menu.addAction('bitch',self.Clic)
        # menu.addAction('lasagna',self.Clic)

        # self.hidden_button.setStyleSheet(
        #     "QPushButton{border-style:inset; border-width:0px;}"
        #     "::hover{"
        #     "background-color:white}"
        #     "::menu-indicator{ image: none; }::pressed{background-color:cyan}")

        panelPos = QtCore.QPoint(self.hidden_button.pos().x() - 100, self.hidden_button.pos().y())
        menu.setStyleSheet("QMenu{background-color:#00FFF7;border-radius:5px; height:130px   }")
        action=menu.exec_(self.mapToGlobal(panelPos))
        #self.hidden_button.setMenu(menu)

    # def manual_2(self):
    #     menu = QtWidgets.QMenu()
    #     menu.addAction('hmmm2', self.Clic)
    #     menu.addAction('bitch2', self.Clic)
    #     menu.addAction('lasagna2', self.Clic)

    #     self.hidden_button2.setStyleSheet(
    #         "QPushButton{border-style:outset; border-width:0px;}::hover{"
    #         "background-color:white}"
    #         "::menu-indicator{ image: none; }::pressed{background-color:cyan}")

    #     panelPos = QtCore.QPoint(self.hidden_button2.pos().x() - 110, self.hidden_button2.pos().y())
    #     menu.setStyleSheet("QMenu{background-color:#00FFF7;border-radius:5px; height:130px }")

    #     action = menu.exec_(self.mapToGlobal(panelPos))



    # def manual_3(self):
    #     menu = QtWidgets.QMenu()
    #     menu.addAction('hmmm3', self.Clic)
    #     menu.addAction('bitch3', self.Clic)
    #     menu.addAction('lasagna3', self.Clic)

    #     self.hidden_button3.setStyleSheet(
    #         "QPushButton{border-style:outset; border-width:0px;}"
    #         "::hover{"
    #         "background-color:white}::menu-indicator{ image: none; }::pressed{background-color:cyan}")

    #     menu.setStyleSheet("QMenu{background-color:#00FFF7;border-radius:5px; height:130px }")
    #     panelPos = QtCore.QPoint(self.hidden_button3.pos().x() - 100, self.hidden_button3.pos().y())

    #     action = menu.exec_(self.mapToGlobal(panelPos))

    # def manual_4(self):
    #     menu = QtWidgets.QMenu()
    #     menu.addAction('hmmm4', self.Clic)
    #     menu.addAction('bitch4', self.Clic)
    #     menu.addAction('lasagna4', self.Clic)

    #     self.hidden_button4.setStyleSheet(
    #         "QPushButton{border-style:outset; border-width:0px;}::hover{"
    #         "background-color:white}"
    #         "::menu-indicator{ image: none; }::pressed{background-color:cyan}")

    #     menu.setStyleSheet("QMenu{background-color:#00FFF7;border-radius:5px; height:130px }")
    #     panelPos = QtCore.QPoint(self.hidden_button4.pos().x() - 100, self.hidden_button4.pos().y())

    #     action=menu.exec_(self.mapToGlobal(panelPos))





    def app_supported(self):
        file=open('app.txt','r+')
        x = str()
        x = file.read()
        lines = x.split("\n")

        toolMenu = QtWidgets.QMenu()
        for i in range(0,len(lines)):
            checkBox = QtWidgets.QCheckBox(lines[i], toolMenu)
            checkableAction = QtWidgets.QWidgetAction(toolMenu)
            checkableAction.setDefaultWidget(checkBox)
            toolMenu.addAction(checkableAction)
        # for i in range(3):
        #     checkBox = QtWidgets.QCheckBox(str(i), toolMenu)
        #     checkableAction = QtWidgets.QWidgetAction(toolMenu)
        #     checkableAction.setDefaultWidget(checkBox)
        #     toolMenu.addAction(checkableAction)
        self.button1.setMenu(toolMenu)


        #for i in range(0,len(lines)):
        #    menu2.addAction(QtWidgets.QAction(lines[i], menu2, checkable=True))
        #
        # #action=menu2.exec_(self.mapToGlobal(self.pos()))
        #self.button1.setMenu(menu2)





if __name__ == '__main__':
    import sys

    aplicacion = QApplication(sys.argv)

    ventana = labelClickable()
    ventana.show()

    sys.exit(aplicacion.exec_())
