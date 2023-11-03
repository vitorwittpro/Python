from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget, QPushButton, QLabel
import re
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bin2Dec")

        self.title = QLabel("Bin2Dec")
        self.inputBin = QLineEdit()
        self.inputDec = QLineEdit()
        self.button = QPushButton("Convert")

        self.button.clicked.connect(self.convert)

        layout = QVBoxLayout()
        layout.addWidget(self.inputBin)
        layout.addWidget(self.inputDec)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(container)

    def convert(self):

        bin = self.inputBin.text()

        valid = re.search("[^0-1]", bin)

        if bool(valid):
            self.inputDec.setText("Invalid!")
            return
            
        bin = bin[::-1]

        decimal = 0

        for i, bit in enumerate(bin):
            decimal += ((2 ** i) * int(bit))

        self.inputDec.setText(str(decimal))


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()