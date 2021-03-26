#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @ Time      :2020/12/3 22:55
# @ Author    :CP 10260824
# @ File      :QtGui.py
# @ Fuction   : 绘制三个频段的频谱，和发射的镜像，发射的LO±2*IF、LO±3*IF，观察结果，选择合适的本振

from LO_Selection import Ui_MainWindow
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QTextEdit
from functools import partial
import matplotlib.pyplot as plt
from PyQt5.QtGui import QIcon


def convert_LO(ui):
    Tx1_Freq1 = int(ui.lineEdit.text() ) #获取文本框内输入信息
    Tx1_Freq2 = int(ui.lineEdit_2.text())
    Tx2_Freq1 = int(ui.lineEdit_3.text())
    Tx2_Freq2 = int(ui.lineEdit_4.text())
    Tx3_Freq1 = int(ui.lineEdit_5.text())
    Tx3_Freq2 = int(ui.lineEdit_6.text())
    Rx1_Freq1 = int(ui.lineEdit_10.text())
    Rx1_Freq2 = int(ui.lineEdit_11.text())
    Rx2_Freq1 = int(ui.lineEdit_12.text())
    Rx2_Freq2 = int(ui.lineEdit_7.text())
    Rx3_Freq1 = int(ui.lineEdit_8.text())
    Rx3_Freq2 = int(ui.lineEdit_9.text())

    Tx_LO = int(ui.lineEdit_13.text())
    Rx_LO = int(ui.lineEdit_14.text())
    Tx1_Freq1_Data = []
    Tx2_Freq1_Data = []
    Tx3_Freq1_Data = []
    Rx1_Freq1_Data = []
    Rx2_Freq1_Data = []
    Rx3_Freq1_Data = []
    Tx_LO_Data = []
    Rx_LO_Data = []
    Tx1_Freq1_Img_Data = []
    Tx2_Freq1_Img_Data = []
    Tx3_Freq1_Img_Data = []
    Tx1_Freq1_LOp2IF_Data = []
    Tx1_Freq1_LOn2IF_Data = []
    Tx1_Freq1_LOp3IF_Data = []
    Tx1_Freq1_LOn3IF_Data = []
    Tx2_Freq1_LOp2IF_Data = []
    Tx2_Freq1_LOn2IF_Data = []
    Tx2_Freq1_LOp3IF_Data = []
    Tx2_Freq1_LOn3IF_Data = []
    Tx3_Freq1_LOp2IF_Data = []
    Tx3_Freq1_LOn2IF_Data = []
    Tx3_Freq1_LOp3IF_Data = []
    Tx3_Freq1_LOn3IF_Data = []

    ###x_line1 = int(ui.lineEdit_15.text())
    ###x_line2 = int(ui.lineEdit_16.text())

    line = [Tx1_Freq1, Tx2_Freq1, Tx3_Freq1, Rx1_Freq1, Rx2_Freq1, Rx3_Freq1]
    for i in line:
        if (i != 0):
            x_line = i
            x_line = min(x_line, i)
    x_line1 = x_line - 500

    #x_line1 = min(3*Tx1_Freq1-2*Tx_LO,4*Tx_LO-3*Tx1_Freq2,3*Tx2_Freq1-2*Tx_LO,4*Tx_LO-3*Tx2_Freq2,3*Tx3_Freq1-2*Tx_LO,4*Tx_LO-3*Tx3_Freq2)-100
    x_line2 = max(Tx1_Freq2,Tx2_Freq2,Tx3_Freq2)+500
    #print(x_line1)
    #print(x_line2)
    Freq = []

    for n in range(x_line1,x_line2) :
        Freq.append(n)

        if (n >= Tx1_Freq1) & (n <= Tx1_Freq2):
            Tx1_Freq1_Data.append(1)            ###发射频率1
        else :
            Tx1_Freq1_Data.append(0)

        if (n >= Tx2_Freq1) & (n <= Tx2_Freq2):
            Tx2_Freq1_Data.append(1)            ###发射频率2
        else :
            Tx2_Freq1_Data.append(0)

        if (n >= Tx3_Freq1) & (n <= Tx3_Freq2):
            Tx3_Freq1_Data.append(1)            ###发射频率3
        else :
            Tx3_Freq1_Data.append(0)

        if (n >= Rx1_Freq1) & (n <= Rx1_Freq2):
            Rx1_Freq1_Data.append(0.8)          ###接收频率1
        else :
            Rx1_Freq1_Data.append(0)

        if (n >= Rx2_Freq1) & (n <= Rx2_Freq2):
            Rx2_Freq1_Data.append(0.8)          ###接收频率2
        else :
            Rx2_Freq1_Data.append(0)

        if (n >= Rx3_Freq1) & (n <= Rx3_Freq2):
            Rx3_Freq1_Data.append(0.8)          ###接收频率3
        else :
            Rx3_Freq1_Data.append(0)

        if (n >= Tx_LO) & (n <= Tx_LO):
            Tx_LO_Data.append(1.2)              ###发射本振
        else :
            Tx_LO_Data.append(0)

        if (n >= Rx_LO) & (n <= Rx_LO):
            Rx_LO_Data.append(1.2)              ###接收本振
        else :
            Rx_LO_Data.append(0)

        if (n >= 2*Tx_LO-Tx1_Freq2) & (n <= 2*Tx_LO-Tx1_Freq1):
            Tx1_Freq1_Img_Data.append(0.7)              ###Tx1镜像
        else :
            Tx1_Freq1_Img_Data.append(0)

        if (n >= 2*Tx_LO-Tx2_Freq2) & (n <= 2*Tx_LO-Tx2_Freq1):
            Tx2_Freq1_Img_Data.append(0.7)              ###Tx2镜像
        else :
            Tx2_Freq1_Img_Data.append(0)

        if (n >= 2*Tx_LO-Tx3_Freq2) & (n <= 2*Tx_LO-Tx3_Freq1):
            Tx3_Freq1_Img_Data.append(0.7)              ###Tx3镜像
        else :
            Tx3_Freq1_Img_Data.append(0)

        if (n >= 2*Tx1_Freq1-Tx_LO) & (n <= 2*Tx1_Freq2-Tx_LO):
            Tx1_Freq1_LOp2IF_Data.append(0.55)              ###发射Tx1 ：LO+2*IF
        else:
            Tx1_Freq1_LOp2IF_Data.append(0)

        if (n >= 3*Tx_LO-2*Tx1_Freq2) & (n <= 3*Tx_LO-2*Tx1_Freq1):
            Tx1_Freq1_LOn2IF_Data.append(0.55)              ###发射Tx1 ：LO-2*IF
        else:
            Tx1_Freq1_LOn2IF_Data.append(0)

        if (n >= 2*Tx2_Freq1-Tx_LO) & (n <= 2*Tx2_Freq2-Tx_LO):
            Tx2_Freq1_LOp2IF_Data.append(0.55)              ###发射Tx2 ：LO+2*IF
        else:
            Tx2_Freq1_LOp2IF_Data.append(0)

        if (n >= 3*Tx_LO-2*Tx2_Freq2) & (n <= 3*Tx_LO-2*Tx2_Freq1):
            Tx2_Freq1_LOn2IF_Data.append(0.55)              ###发射Tx2 ：LO-2*IF
        else:
            Tx2_Freq1_LOn2IF_Data.append(0)

        if (n >= 2*Tx3_Freq1-Tx_LO) & (n <= 2*Tx3_Freq2-Tx_LO):
            Tx3_Freq1_LOp2IF_Data.append(0.55)              ###发射Tx3 ：LO+2*IF
        else:
            Tx3_Freq1_LOp2IF_Data.append(0)

        if (n >= 3*Tx_LO-2*Tx3_Freq2) & (n <= 3*Tx_LO-2*Tx3_Freq1):
            Tx3_Freq1_LOn2IF_Data.append(0.55)              ###发射Tx3 ：LO-2*IF
        else:
            Tx3_Freq1_LOn2IF_Data.append(0)

        if (n >= 3*Tx1_Freq1-2*Tx_LO) & (n <= 3*Tx1_Freq2-2*Tx_LO):
            Tx1_Freq1_LOp3IF_Data.append(0.45)  ###发射Tx1 ：LO+3*IF
        else:
            Tx1_Freq1_LOp3IF_Data.append(0)

        if (n >= 4*Tx_LO-3*Tx1_Freq2) & (n <= 4*Tx_LO-3*Tx1_Freq1):
            Tx1_Freq1_LOn3IF_Data.append(0.45)  ###发射Tx1 ：LO-3*IF
        else:
            Tx1_Freq1_LOn3IF_Data.append(0)

        if (n >= 3*Tx2_Freq1-2*Tx_LO) & (n <= 3*Tx2_Freq2-2*Tx_LO):
            Tx2_Freq1_LOp3IF_Data.append(0.45)  ###发射Tx2 ：LO+3*IF
        else:
            Tx2_Freq1_LOp3IF_Data.append(0)

        if (n >= 4*Tx_LO-3*Tx2_Freq2) & (n <= 4*Tx_LO-3*Tx2_Freq1):
            Tx2_Freq1_LOn3IF_Data.append(0.45)  ###发射Tx2 ：LO-3*IF
        else:
            Tx2_Freq1_LOn3IF_Data.append(0)

        if (n >= 3*Tx3_Freq1-2*Tx_LO) & (n <= 3*Tx3_Freq2-2*Tx_LO):
            Tx3_Freq1_LOp3IF_Data.append(0.45)  ###发射Tx3 ：LO+3*IF
        else:
            Tx3_Freq1_LOp3IF_Data.append(0)

        if (n >= 4*Tx_LO-3*Tx3_Freq2) & (n <= 4*Tx_LO-3*Tx3_Freq1):
            Tx3_Freq1_LOn3IF_Data.append(0.45)  ###发射Tx3 ：LO-3*IF
        else:
            Tx3_Freq1_LOn3IF_Data.append(0)


###绘制曲线
    plt.figure(figsize=(15, 10))
    plt.plot(Freq, Tx1_Freq1_Data,label = 'Tx1',linewidth=2)
    plt.plot(Freq, Tx2_Freq1_Data,label = 'Tx2',linewidth=2)
    plt.plot(Freq, Tx3_Freq1_Data,label = 'Tx3',linewidth=2)
    plt.plot(Freq, Rx1_Freq1_Data,label = 'Rx1',linewidth=2)
    plt.plot(Freq, Rx2_Freq1_Data,label = 'Rx2',linewidth=2)
    plt.plot(Freq, Rx3_Freq1_Data,label = 'Rx3',linewidth=2)
###绘制本振
    plt.plot(Freq, Tx_LO_Data,label = "Tx_LO")  ###没有显示Label？？？ 需要plt.legend(loc="upper right")
    plt.plot(Freq, Rx_LO_Data,label = "Rx_LO")
###绘制镜像信号
    plt.plot(Freq, Tx1_Freq1_Img_Data,linewidth=1,label = 'Tx1_Img')
    plt.plot(Freq, Tx2_Freq1_Img_Data,linewidth=1,label = 'Tx2_Img')
    plt.plot(Freq, Tx3_Freq1_Img_Data,linewidth=1,label = 'Tx3_Img')
###绘制LO±2*IF
    plt.plot(Freq, Tx1_Freq1_LOp2IF_Data,linewidth=1,label = 'Tx1_LO+2*IF')
    plt.plot(Freq, Tx1_Freq1_LOn2IF_Data,linewidth=1,label = 'Tx1_LO-2*IF')
    plt.plot(Freq, Tx2_Freq1_LOp2IF_Data,linewidth=1,label = 'Tx2_LO+2*IF')
    plt.plot(Freq, Tx2_Freq1_LOn2IF_Data,linewidth=1,label = 'Tx2_LO-2*IF')
    plt.plot(Freq, Tx3_Freq1_LOp2IF_Data,linewidth=1,label = 'Tx3_LO+2*IF')
    plt.plot(Freq, Tx3_Freq1_LOn2IF_Data,linewidth=1,label = 'Tx3_LO-2*IF')
###绘制LO±3*IF
    plt.plot(Freq, Tx1_Freq1_LOp3IF_Data,linewidth=1,label = 'Tx1_LO+3*IF')
    plt.plot(Freq, Tx1_Freq1_LOn3IF_Data,linewidth=1,label = 'Tx1_LO-3*IF')
    plt.plot(Freq, Tx2_Freq1_LOp3IF_Data,linewidth=1,label = 'Tx2_LO+3*IF')
    plt.plot(Freq, Tx2_Freq1_LOn3IF_Data,linewidth=1,label = 'Tx2_LO-3*IF')
    plt.plot(Freq, Tx3_Freq1_LOp3IF_Data,linewidth=1,label = 'Tx3_LO+3*IF')
    plt.plot(Freq, Tx3_Freq1_LOn3IF_Data,linewidth=1,label = 'Tx3_LO-3*IF')

    plt.title('LO Selection ')
    plt.xlabel(" Frequency ")
    plt.ylabel(" Amplitude ")
    plt.grid(linestyle='-.')

    plt.legend(bbox_to_anchor=(1.12, 1), loc=1, borderaxespad=0)
    ###bbox_to_anchor=(Num1, num2);Num1 水平位置，num2 垂直位置;loc =1 位于右上角；

    plt.show()


def convert_IF(ui):
    Tx1_Freq1 = int(ui.lineEdit.text())  # 获取文本框内输入信息
    Tx1_Freq2 = int(ui.lineEdit_2.text())
    Tx2_Freq1 = int(ui.lineEdit_3.text())
    Tx2_Freq2 = int(ui.lineEdit_4.text())
    Tx3_Freq1 = int(ui.lineEdit_5.text())
    Tx3_Freq2 = int(ui.lineEdit_6.text())
    Rx1_Freq1 = int(ui.lineEdit_10.text())
    Rx1_Freq2 = int(ui.lineEdit_11.text())
    Rx2_Freq1 = int(ui.lineEdit_12.text())
    Rx2_Freq2 = int(ui.lineEdit_7.text())
    Rx3_Freq1 = int(ui.lineEdit_8.text())
    Rx3_Freq2 = int(ui.lineEdit_9.text())

    Tx_LO = int(ui.lineEdit_13.text())
    Rx_LO = int(ui.lineEdit_14.text())
    Tx1_IF = []
    Tx2_IF = []
    Tx3_IF = []
    Tx1_IF_3rd = []
    Tx2_IF_3rd = []
    Tx3_IF_3rd = []
    freq = []
    IF0 = []
    for i in range(-300,300) :
        freq.append(i)
        if i == 0 :
            IF0.append(1)
        else :
            IF0.append(0)

        if (i>=Tx1_Freq1-Tx_LO) & (i<=Tx1_Freq2-Tx_LO) :
            Tx1_IF.append(0.8)
        else :
            Tx1_IF.append(0)

        if (i>=(Tx1_Freq1-Tx_LO)-(Tx1_Freq2-Tx1_Freq1)) & (i<=(Tx1_Freq2-Tx_LO)+(Tx1_Freq2-Tx1_Freq1)) :
            Tx1_IF_3rd.append(0.3)
        else :
            Tx1_IF_3rd.append(0)


        if (i>=Tx2_Freq1-Tx_LO) & (i<=Tx2_Freq2-Tx_LO) :
            Tx2_IF.append(0.8)
        else :
            Tx2_IF.append(0)

        if (i>=(Tx2_Freq1-Tx_LO)-(Tx2_Freq2-Tx2_Freq1)) & (i<=(Tx2_Freq2-Tx_LO)+(Tx2_Freq2-Tx2_Freq1)) :
            Tx2_IF_3rd.append(0.3)
        else :
            Tx2_IF_3rd.append(0)

        if (i >= Tx3_Freq1 - Tx_LO) & (i <= Tx3_Freq2 - Tx_LO):
            Tx3_IF.append(0.8)
        else:
            Tx3_IF.append(0)
        if (i>=(Tx3_Freq1-Tx_LO)-(Tx3_Freq2-Tx3_Freq1)) & (i<=(Tx3_Freq2-Tx_LO)+(Tx3_Freq2-Tx3_Freq1)) :
            Tx3_IF_3rd.append(0.3)
        else :
            Tx3_IF_3rd.append(0)

    plt.figure(figsize=(15, 10))
    plt.plot(freq, Tx1_IF,linewidth=1,label = 'Tx1_IF')
    plt.plot(freq, Tx2_IF, linewidth=1, label='Tx2_IF')
    plt.plot(freq, Tx3_IF, linewidth=1, label='Tx3_IF')
    plt.plot(freq, IF0, linewidth=1, label='IF0')
    plt.plot(freq, Tx1_IF_3rd, linewidth=1, label='Tx1_IF_3rd')
    plt.plot(freq, Tx2_IF_3rd, linewidth=1, label='Tx2_IF_3rd')
    plt.plot(freq, Tx3_IF_3rd, linewidth=1, label='Tx3_IF_3rd')
    plt.title('IF ')
    plt.xlabel(" Frequency ")
    plt.ylabel(" Amplitude ")
    plt.grid(linestyle='-.')

    plt.legend(bbox_to_anchor=(1.12, 1), loc=1, borderaxespad=0)
    ###bbox_to_anchor=(Num1, num2);Num1 水平位置，num2 垂直位置;loc =1 位于右上角；

    plt.show()



def shuoming():
    print('弹出说明文档')

class CamShow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(CamShow, self).__init__(parent)
        self.setupUi(self)
        self.setGeometry (200, 425, 750, 450)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = CamShow()
    ui.show()
    ui.pushButton.clicked.connect(partial(convert_LO, ui))
    ui.pushButton_2.clicked.connect(partial(convert_IF, ui))
    ui.actionshuoming.triggered.connect(shuoming)       ## 点击 说明 菜单执行函数
    ui.actionQuit.triggered.connect(exit)               ## 点击 退出 退出窗口
    sys.exit(app.exec_())