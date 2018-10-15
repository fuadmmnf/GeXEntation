# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Nombre:       QLabel_clickable.py
# Autor:        Miguel Andres Garcia Niño
# Creado:       11 de Abril 2018
# Modificado:   11 de Abril 2018
# Copyright:    (c) 2018 by Miguel Andres Garcia Niño, 2018
# License:      Apache License 2.0
# ----------------------------------------------------------------------------

__versión__ = "1.0"

"""
El módulo *QLabel_clickable* permite llamar a una función al hacer clic o doble clic sobre
un QLabel
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, pyqtSignal, QTimer
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QMessageBox


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
        self.setFixedSize(450,400)

        self.initUI()

    def initUI(self):

      # ==================== WIDGET QLABEL =======================
        
            

        self.button=QtWidgets.QPushButton('Start', self)
        self.button.setStyleSheet("QPushButton{ border: 1px "
                                       "#; border-radius: 4.5px;font-size:20px;}")
        self.button.setGeometry(320,100 ,80, 30)


        self.button1=QtWidgets.QPushButton('Manual', self)
        self.button1.setStyleSheet("QPushButton{ border: 1px "
                                       "#; border-radius: 4.5px;font-size:20px;}")
        self.button1.setGeometry(320,140 ,80, 30)

        self.button2=QtWidgets.QPushButton('Exit', self)
        self.button2.setStyleSheet("QPushButton{border: 1px "
                                       "#; border-radius: 4.5px;font-size:20px;}")
        
        self.button2.setGeometry(320,180 ,80, 30)
        self.button2.clicked.connect(self.close)


        self.labelImagen = QLabelClickable(self)
        self.labelImagen.setGeometry(50, 40, 120, 130)
        self.labelImagen.setToolTip("1st Gesture")
        self.labelImagen.setCursor(Qt.PointingHandCursor)

        self.labelImagen.setStyleSheet("QLabel {background-color: transparent; border: 1px "
                                       "; border-radius: 5px;transition-property: transform;}")

        self.labelImagen.setStyleSheet("QLabel:hover {background-color: white;}")
        self.pixmapImagen = QPixmap("1.png").scaled(112, 128, Qt.KeepAspectRatio,
                                                     Qt.SmoothTransformation)
        
        self.labelImagen.setPixmap(self.pixmapImagen)
        self.labelImagen.setAlignment(Qt.AlignCenter)
        



        self.label_2 = QLabelClickable(self)
        self.label_2.setGeometry(180, 40, 120, 130)
        self.label_2.setToolTip("2nd Gesture")
        self.label_2.setCursor(Qt.PointingHandCursor)
        self.label_2.setStyleSheet("QLabel {background-color: transparent; border: 1px  "
                                       "; border-radius: 5px;}")
        self.label_2.setStyleSheet("QLabel:hover {background-color: white;}")

        self.pixmapImagen2 = QPixmap("2.png").scaled(112, 128, Qt.KeepAspectRatio,
                                                     Qt.SmoothTransformation)
        self.label_2.setPixmap(self.pixmapImagen2)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.label_3 = QLabelClickable(self)
        self.label_3.setGeometry(50, 180, 120, 130)
        self.label_3.setToolTip("3rd Gesture")
        self.label_3.setCursor(Qt.PointingHandCursor)
        self.label_3.setStyleSheet("QLabel {background-color: transparent; border: 1px  "
                                       "; border-radius: 5px;}")

        self.label_3.setStyleSheet("QLabel:hover {background-color: white;}")
        self.pixmapImagen3 = QPixmap("3.png").scaled(112, 128, Qt.KeepAspectRatio,
                                                     Qt.SmoothTransformation)
        self.label_3.setPixmap(self.pixmapImagen3)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.label_4 = QLabelClickable(self)
        self.label_4.setGeometry(180, 180, 120, 130)
        self.label_4.setToolTip("3rd Gesture")
        self.label_4.setCursor(Qt.PointingHandCursor)
        self.label_4.setStyleSheet("QLabel {background-color: transparent; border: 1px  "
                                       "; border-radius: 5px;}")
        self.label_4.setStyleSheet("QLabel:hover {background-color: white;}")
        self.pixmapImagen4 = QPixmap("4.png").scaled(112, 128, Qt.KeepAspectRatio,
                                                     Qt.SmoothTransformation)
        self.label_4.setPixmap(self.pixmapImagen4)
        self.label_4.setAlignment(Qt.AlignCenter)









      # ===================== EVENTO QLABEL ======================

      # Llamar función al hacer clic o doble clic sobre el label
        self.labelImagen.clicked.connect(self.Clic)
        self.label_2.clicked.connect(self.secondClick)
        self.label_3.clicked.connect(self.thirdClick)
        self.label_4.clicked.connect(self.fourthClick)

  # ======================= FUNCIONES ============================

    def Clic(self):
        QMessageBox.information(self, "1st Gesture","1st Gesture was clicked")
    def secondClick(self):
        QMessageBox.information(self, "2nd Gesture","2nd Gesture was clicked")
    def thirdClick(self):
        QMessageBox.information(self, "3rd Gesture","3rd Gesture was clicked")
    def fourthClick(self):
        QMessageBox.information(self, "4th Gesture","4th Gesture was clicked") 
    def close(self):
        QApplication.quit()

# ================================================================

if __name__ == '__main__':
    
    import sys
    
    aplicacion = QApplication(sys.argv)
    
    ventana = labelClickable()
    ventana.show()
    
    sys.exit(aplicacion.exec_())
