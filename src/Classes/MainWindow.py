from PyQt5 import QtCore, QtGui, QtWidgets


class NNIDChanger_GUI(object):
    def setupUi(self, NNIDChanger_GUI):
        NNIDChanger_GUI.setObjectName("NNIDChanger_GUI")
        NNIDChanger_GUI.resize(287, 415)
        NNIDChanger_GUI.setDocumentMode(False)
        NNIDChanger_GUI.setTabShape(QtWidgets.QTabWidget.Rounded)
        NNIDChanger_GUI.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(NNIDChanger_GUI)
        self.centralwidget.setObjectName("centralwidget")
        self.NNID_GroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.NNID_GroupBox.setGeometry(QtCore.QRect(10, 10, 261, 61))
        self.NNID_GroupBox.setObjectName("NNID_GroupBox")
        self.NNID_LineEdit = QtWidgets.QLineEdit(self.NNID_GroupBox)
        self.NNID_LineEdit.setGeometry(QtCore.QRect(10, 28, 241, 26))
        self.NNID_LineEdit.setObjectName("NNID_LineEdit")
        self.Code_GroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.Code_GroupBox.setGeometry(QtCore.QRect(10, 90, 261, 311))
        self.Code_GroupBox.setObjectName("Code_GroupBox")
        self.Code_TextEdit = QtWidgets.QPlainTextEdit(self.Code_GroupBox)
        self.Code_TextEdit.setGeometry(QtCore.QRect(10, 30, 241, 231))
        self.Code_TextEdit.setObjectName("Code_TextEdit")
        self.Copy_Button = QtWidgets.QPushButton(self.Code_GroupBox)
        self.Copy_Button.setGeometry(QtCore.QRect(10, 270, 241, 31))
        self.Copy_Button.setObjectName("Copy_Button")
        NNIDChanger_GUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(NNIDChanger_GUI)
        QtCore.QMetaObject.connectSlotsByName(NNIDChanger_GUI)

    def retranslateUi(self, NNIDChanger_GUI):
        _translate = QtCore.QCoreApplication.translate
        NNIDChanger_GUI.setWindowTitle(_translate("NNIDChanger_GUI", "NNIDChanger - KorOwOzin"))
        self.NNID_GroupBox.setTitle(_translate("NNIDChanger_GUI", "NNID"))
        self.Code_GroupBox.setTitle(_translate("NNIDChanger_GUI", "Code"))
        self.Copy_Button.setText(_translate("NNIDChanger_GUI", "COPY"))
