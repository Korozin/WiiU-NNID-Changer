from PyQt5 import QtWidgets
from Classes import MainWindow, InfoWindow, ErrorWindow


class NNIDChanger_Main(QtWidgets.QMainWindow, MainWindow.NNIDChanger_GUI):
    def __init__(self):
        super(NNIDChanger_Main, self).__init__()

        # Set up base GUI parameters
        self.setupUi(self)
        self.Set_Functions()
        self.Code_TextEdit.setReadOnly(True)

        # Initialize Error / Info windows
        self.ErrorWindow = ErrorWindow.ErrorWindow()
        self.InfoWindow = InfoWindow.InfoWindow()


    def Set_Functions(self):
        self.NNID_LineEdit.textChanged.connect(self.Output_Code)
        self.Copy_Button.clicked.connect(self.Copy_Form_Contents)


    def format_code(self, code):
        input_string = code.replace(" ", "").replace("\n", "")
        output_list = []
        i = 0
        for i in range(0, len(input_string), 17):
                output_list.append(input_string[i:i+17])
    
        output_string = "".join(output_list)
    
        new_output_list = []
        for i in range(0, len(output_string), 16):
                new_output_list.append(output_string[i:i+8] + " " + output_string[i+8:i+16])
    
        new_output_string = "\n".join(new_output_list)
    
        return new_output_string.upper()


    def encode_text(self, text):
        hexm = text.encode('utf-16be', 'replace').hex().upper()
        offset = 0x00
        code = '30000000109CED1810000000500000003100000000000050'
        hexc = len(hexm)
        if (len(text) % 2) != 0:
            hexc = len(hexm) + 8
        x = 0
        while x < hexc // 8:
            code += '0012' + format(offset + x * 4, '04X') + hexm[x * 8:x * 8 + 4]
            code += hexm[x * 8 + 4:x * 8 + 8]
            x += 1
        if (len(text) % 2) != 0:
            code += '0000'
        code += '0012' + format(offset + x * 4, '04X') + '00000000' + 'D0000000DEADCAFE'
        return self.format_code(code)


    def Output_Code(self):
        Code_Text = self.NNID_LineEdit.text()

        if Code_Text == "":
            self.Code_TextEdit.clear()
        else:
            self.Code_TextEdit.clear()
            Result = self.encode_text(Code_Text)
            self.Code_TextEdit.insertPlainText(Result)


    def Copy_Form_Contents(self):
        Text_To_Copy = self.Code_TextEdit.toPlainText()
        if Text_To_Copy == "":
            self.ErrorWindow.CreateWindow("Clipboard Manager",
                                         f"Code Text Box is empty!",
                                         500, 200)
            self.ErrorWindow.show()
        else:
            Lines = len(Text_To_Copy.split("\n"))
            Clipboard = QtWidgets.QApplication.clipboard()
            Clipboard.setText(Text_To_Copy)
            self.InfoWindow.CreateWindow("Clipboard Manager",
                                         f"Successfully copied {Lines} line(s)!",
                                         500, 200)
            self.InfoWindow.show()


if __name__ == "__main__":
    import sys
    NNIDChanger_App = QtWidgets.QApplication(sys.argv)
    NNIDChanger_Var = NNIDChanger_Main()
    NNIDChanger_Var.show()
    sys.exit(NNIDChanger_App.exec_())
