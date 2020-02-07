from PyQt5.Qt import *
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("例子")
        self.resize(600, 400)
        self.setup_ui()

    def setup_ui(self):
        

if __name__ == '__main__':

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
