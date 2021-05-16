from PyQt5 import QtCore, QtGui, QtWidgets
import summarizer as sm
import clipboard as cb

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowIcon(QtGui.QIcon("summarizer.ico"))
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(418, 454)
        MainWindow.setMinimumSize(QtCore.QSize(418, 454))
        MainWindow.setMaximumSize(QtCore.QSize(418, 454))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 398, 432))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.pastebt = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pastebt.setFont(font)
        self.pastebt.setObjectName("pastebt")
        self.verticalLayout_2.addWidget(self.pastebt)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.maintxt = QtWidgets.QTextEdit(self.layoutWidget)
        self.maintxt.setObjectName("maintxt")
        self.verticalLayout_4.addWidget(self.maintxt)
        self.sumtxt = QtWidgets.QTextEdit(self.layoutWidget)
        self.sumtxt.setObjectName("sumtxt")
        self.verticalLayout_4.addWidget(self.sumtxt)
        self.sumbt = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sumbt.setFont(font)
        self.sumbt.setObjectName("sumbt")
        self.verticalLayout_4.addWidget(self.sumbt)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 1, 2, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.copybt = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.copybt.setFont(font)
        self.copybt.setObjectName("copybt")
        self.verticalLayout_3.addWidget(self.copybt)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.copybt.setEnabled(False)
        self.sumbt.setEnabled(False)

        self.pastebt.clicked.connect(lambda: self.paster())
        self.sumbt.clicked.connect(lambda: self.summarize())
        self.copybt.clicked.connect(lambda: self.copier())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "King Summarizer"))
        self.label.setText(_translate("MainWindow", "Enter Your Text"))
        self.pastebt.setText(_translate("MainWindow", "Paste"))
        self.maintxt.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><br/></p></body></html>"))
        self.maintxt.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.sumtxt.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><br/></p></body></html>"))
        self.sumtxt.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.sumbt.setText(_translate("MainWindow", "Summarize"))
        self.label_2.setText(_translate("MainWindow", "Summarized Text"))
        self.copybt.setText(_translate("MainWindow", "Copy"))

    def paster(self):
        text = cb.paste()
        self.text = text
        self.maintxt.setText(self.text)
        self.sumbt.setEnabled(True)
        
    def summarize(self):
        text_sum = sm.text_summarizer(self.text)
        self.text_sum = text_sum
        self.sumtxt.setPlainText(self.text_sum)
        self.copybt.setEnabled(True)

    def copier(self):
        cb.copy(self.text_sum)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
