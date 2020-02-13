from PyQt5.Qt import *
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("例子")
        self.resize(600, 400)
        self.setup_ui()

    def setup_ui(self):
        # self.QObject信号与槽测试()
        # self.QObject信号与槽案例()
        # self.QObject类型判定()
        # self.QObject对象删除()
        self.QObject事件机制()

    def QObjectTest(self):
        label1 = QLabel(self)
        label1.setText("hhh")
        label1.setObjectName("notice")
        label1.setProperty("level", "error")

        label2 = QLabel(self)
        label2.setText("eee")
        label2.move(300, 200)
        label2.setObjectName("notice")
        label2.setProperty("level", "warning")

    def QObject信号与槽测试(self):
        self.obj = QObject()

        # destroyed会传入一个 参数给槽函数
        def printSign(obj):
            print("触发了", obj)

        # self.obj.destroyed.connect(printSign)
        # del self.obj

        self.obj.objectNameChanged.connect(printSign)

        # 返回信号连接的槽的个数
        print(self.obj.receivers(self.obj.objectNameChanged))

        self.obj.setObjectName("xxx")

        # self.obj.objectNameChanged.disconnect()

        # 临时阻断（非取消）信号与槽的连接
        self.obj.blockSignals(True)

        self.obj.setObjectName("ooo")

        self.obj.blockSignals(False)

        self.obj.setObjectName("xxoo")

    def QObject信号与槽案例(self):

        # Text1
        btn = QPushButton(self)
        btn.setText("点击我")

        def btn_cao():
            print("点我干哈？")

        btn.clicked.connect(btn_cao)

    def QObject类型判定(self):
        obj = QObject()
        w = QWidget()
        btn = QPushButton()

        for o in [obj, w, btn]:
            # 判断是否为控件类型
            print(o.isWidgetType())

            # 判断继承关系
            print(o.inherits("QWidget"))

    def QObject对象删除(self):
        obj1 = QObject()
        self.obj1 = obj1
        obj2 = QObject()
        obj3 = QObject()

        obj3.setParent(obj2)
        obj2.setParent(obj1)

        obj1.destroyed.connect(lambda : print("obj1 释放"))
        obj2.destroyed.connect(lambda : print("obj2 释放"))
        obj3.destroyed.connect(lambda : print("obj3 释放"))

        # del obj2
        obj2.deleteLater()
        print(obj1.children())

    def QObject事件机制(self):
        pass







if __name__ == '__main__':

    app = QApplication(sys.argv)
    with open("font.qss", "r") as font:
        app.setStyleSheet(font.read())
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
