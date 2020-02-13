from PyQt5.Qt import *

import sys

# 当别人使用命令行启动程序时，可以设定一种功能（接受命令行输入的参数来执行不同的业务逻辑）
# args = sys.argv
# print(args)

class MyLabel(QLabel):


    def setSec(self, sec):
        self.setText(sec)


    def setstartTime(self, msec):
        self.time_id = self.startTimer(msec)

    def timerEvent(self, *args, **kwargs):
        text = int(self.text())
        text -= 100
        self.setText(str(text))

        if text == 0:
            self.killTimer(self.time_id)

class MyWidget(QWidget):

    def timerEvent(self, *args, **kwargs) -> None:
        current_h = self.height()
        print(current_h)
        current_w = self.width()
        print(current_w)

        self.resize(current_h + 10, current_w + 10)


# 1、创建一个应用程序对象
app = QApplication(sys.argv)

# 2、控件的操作
# 2.1 创建控件（没有父控件的控件可以成为一个"窗口"）
window = MyWidget()

# 2.2 设置控件
# 设置窗口标题
window.setWindowTitle("定时器的使用 ")
window.resize(500, 500)
# 设置窗口大小
window.startTimer(1000)

# label = MyLabel(window)
# label.move(100,100)
# label.setSec("20000")
# label.setstartTime(100)




# 2.3 展示控件(前提控件没有父控件)
window.show()

# 3、应用程序的执行，进入到消息循环(检测整个程序所接受到的用户的交互信息)
# app.exec_()
sys.exit(app.exec_())

