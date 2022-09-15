#-*- encoding = utf-8 -*-
import hashlib                             #先引入哈希模块和sys 常用的模块
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileDialog

from Windows.MainWindow import Ui_MainWindow

class MyWindow(QMainWindow,Ui_MainWindow):  #定义一个Mywindow的函数 去继承ui界面中的QMainWindow,Ui_MainWindow的俩个父类
    def __init__(self):
        super(MyWindow,self).__init__()    # 当执行这句话的时候 它会初始化这俩个父类本身的位置  要不然父类的属性是不能访问的

        self.setupUi(self)                 #实例窗口对象

        #给四个按钮绑定事件   lambda函数    按钮名都在MainWindow里面创建了

        self.exit_btn.clicked.connect(lambda :sys.exit())     #
        self.encry_btn.clicked.connect(self.encry)
        self.file_btn.clicked.connect(self.file_choose)
        self.clear_btn.clicked.connect(lambda :self.original_text.setText(''))
    def encry(self):                           #编写
        text=self.original_text.toPlainText()  #通过组件对象的toPlainText方法获取了组件的文本
                                                #多行简单文本框用 toPlainText()
        textArr = text.split('\n')

        for i in range(0, len(textArr)):
            textArr[i] = hashlib.md5(textArr[i].encode()).hexdigest()

        r = '\n'.join(textArr)

        print(r)

        # result=hashlib.md5(text.encode()).hexdigest()

        self.res_shower.setText(r)         #然后将结果展示框的内容设置为加密后的结果，同时控制台输出内容
        print("[==>加密成功<==]\n|{%s}==>{%s}|"%(text,r))

    def file_choose(self):
        filename,filetype=QFileDialog.getOpenFileName(self,"打开文件","/","文本文件(*.txt);全部文件(*.*)")
        if filename!="":
            f=open(filename,'r',encoding='utf-8')
            text=f.read()
            self.original_text.setText(text)
            self.encry()

if __name__ == '__main__':
    app=QtWidgets.QApplication(sys.argv)                # 实例化，传参
    ui=MyWindow()                            # 创建ui，引用MainWindow.ui文件中的Mywindow类
    ui.show()                                # 调用MainWindow类的setupUi，创建初始组件
    sys.exit(app.exec_())
