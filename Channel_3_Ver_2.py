# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mute.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import json
import pyaudio
import sounddevice as sd
import osascript
from pygame import mixer
mixer.init()


mac_input_vol = 50
jabra_input_vol = 71


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(630, 381)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 630, 381))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("z-3.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(0, 30, 630, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        #Scroll Area
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(25, 70, 420, 291))
        self.scrollArea.setStyleSheet("background-color: transparent;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QLabel(Form)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 469, 289))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        self.scrollAreaWidgetContents.setFont(font)

        data = ""
        self.p = pyaudio.PyAudio()
        for i in range(self.p.get_device_count()):
            data += "\t" + self.p.get_device_info_by_index(i).get("name") +";\n" +json.dumps([self.p.get_device_info_by_index(i)], sort_keys=False, indent=4) + "\n"

        data = "DETECTED AUDIO DEVICES\n" + str(sd.query_devices()) + "\n\n" + data

        self.scrollAreaWidgetContents.setText(data)
        self.scrollAreaWidgetContents.setWordWrap(True)
        self.scrollAreaWidgetContents.setScaledContents(True)
        self.scrollAreaWidgetContents.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.Mute = QtWidgets.QPushButton(Form)
        self.Mute.setGeometry(QtCore.QRect(448, 66, 151, 30))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.Mute.setFont(font)
        self.Mute.setStyleSheet("background-color: transparent; text-align:left;")
        self.Mute.setObjectName("Mute")


        self.Refresh = QtWidgets.QPushButton(Form)
        self.Refresh.setGeometry(QtCore.QRect(448, 90, 151, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.Refresh.setFont(font)
        self.Refresh.setStyleSheet("background-color: transparent; color: rgb(255, 255, 255); text-align:left;")
        self.Refresh.setObjectName("Refresh")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


        self.Mute.clicked.connect(self.mute)
        self.Refresh.clicked.connect(self.refresh)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Sound_Channel_3_Ver_2"))
        self.label_3.setText(_translate("Form", "SOUND CHANNEL"))
        self.Mute.setText(_translate("Form", "PAUSE AUDIO STREAM"))
        self.Refresh.setText(_translate("Form", "REFRESH"))

    def mute(self):
        mac_input_vol = 50
        jabra_input_vol = 71

        origional_input_volume = osascript.osascript('input volume of (get volume settings)')[1]
        print(origional_input_volume)

        if int(origional_input_volume) == 0:
            osascript.osascript(f"set volume input volume {jabra_input_vol}")
            mixer.music.load(f"SoundEffects/StartAudio.mp3")
            mixer.music.play()

            self.Mute.setStyleSheet("background-color: transparent; text-align:left;\n"
    "\n"
    "color : rgb(0, 255, 0);")


        else:
            osascript.osascript("set volume input volume 0")
            mixer.music.load(f"SoundEffects/StopAudio.mp3")
            mixer.music.play()

            self.Mute.setStyleSheet("background-color: transparent; text-align:left;\n"
    "\n"
    "color : rgb(255, 0, 0);")

    def refresh(self):

        data = ""
        self.p.terminate()
        sd._terminate()
        sd._initialize()
        self.p = pyaudio.PyAudio()
        for i in range(self.p.get_device_count()):
            data += "\t" + self.p.get_device_info_by_index(i).get("name") +";\n" +json.dumps([self.p.get_device_info_by_index(i)], sort_keys=False, indent=4) + "\n"

        data = data = "DETECTED AUDIO DEVICES\n" + str(sd.query_devices()) + "\n\n" + data
        print(sd.query_devices())
        mixer.music.load(f"SoundEffects/Refresh3.mp3")
        mixer.music.play()

        self.scrollAreaWidgetContents.setText(data)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
