# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'message_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from sending_end import sending



class Ui_Message_To_Be_send(object):
    def setupUi(self, Message_To_Be_send):
        Message_To_Be_send.setObjectName("Message_To_Be_send")
        Message_To_Be_send.resize(630, 584)
        Message_To_Be_send.setStyleSheet("\n" "background-color: rgb(241, 241, 241);")
        self.centralwidget = QtWidgets.QWidget(Message_To_Be_send)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.From = QtWidgets.QTextEdit(self.centralwidget)
        self.From.setGeometry(QtCore.QRect(120, 70, 181, 31))
        self.From.setObjectName("From")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.send_To = QtWidgets.QTextEdit(self.centralwidget)
        self.send_To.setGeometry(QtCore.QRect(120, 160, 241, 51))
        self.send_To.setObjectName("send_To")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 230, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.message = QtWidgets.QTextEdit(self.centralwidget)
        self.message.setGeometry(QtCore.QRect(120, 290, 471, 181))
        self.message.setObjectName("message")
        self.Send_Button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.Send_Window())
        self.Send_Button.setGeometry(QtCore.QRect(450, 490, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Send_Button.setFont(font)
        self.Send_Button.setObjectName("Send_Button")
        Message_To_Be_send.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Message_To_Be_send)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 630, 26))
        self.menubar.setObjectName("menubar")
        Message_To_Be_send.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Message_To_Be_send)
        self.statusbar.setObjectName("statusbar")
        Message_To_Be_send.setStatusBar(self.statusbar)

        self.retranslateUi(Message_To_Be_send)
        QtCore.QMetaObject.connectSlotsByName(Message_To_Be_send)


    def conversion(self,li):
        answer=""
        answer_list=[]
        for k in li:
            if k==":":
                answer_list.append(answer)
                answer=""
            else:
                answer=answer+k
        if answer_list==[]:
            answer_list.append(li)
        return (answer_list)

    def Send_Window(self):
        from_addr=self.From.toPlainText()
        print(from_addr)
        to_addrs=self.conversion(self.send_To.toPlainText())
        print(to_addrs)
        messagee=self.message.toPlainText()
        print(messagee)
        print(sending(from_addr, to_addrs, messagee))
        Message_To_Be_send.close()

    def retranslateUi(self, Message_To_Be_send):
        _translate = QtCore.QCoreApplication.translate
        Message_To_Be_send.setWindowTitle(_translate("Message_To_Be_send", "MainWindow"))
        self.label.setText(_translate("Message_To_Be_send", "From:"))
        self.From.setText("artificali.project@gmail.com")
        self.label_2.setText(_translate("Message_To_Be_send", "To:"))
        self.send_To.setText("multiple emails should be separated with ':'")
        self.label_3.setText(_translate("Message_To_Be_send", "To:"))
        self.message.setHtml("Enter the the message")
        self.Send_Button.setText(_translate("Message_To_Be_send", "Send"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Message_To_Be_send = QtWidgets.QMainWindow()
    ui = Ui_Message_To_Be_send()
    ui.setupUi(Message_To_Be_send)
    Message_To_Be_send.show()
    sys.exit(app.exec_())
