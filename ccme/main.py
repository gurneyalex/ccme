from PyQt4 import QtGui
from PyQt4.QtCore import QObject, pyqtSlot
import sys
import jack

from .ui_mainwindow import Ui_MainWindow

class CCMe(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(CCMe, self).__init__()
        self.setupUi(self)
        self.setupJack()

    
    def on_btn0_clicked(self):
        self.midiCcValue.setValue(0)

    def on_btn128_clicked(self):
        self.midiCcValue.setValue(127)

    def on_btn64_clicked(self):
        self.midiCcValue.setValue(64)

    @pyqtSlot(int)
    def on_midiChannel_valueChanged(self, val):
        self.midiCcValue.setValue(0)

    @pyqtSlot(int)
    def on_midiController_valueChanged(self, val):
        self.midiCcValue.setValue(0)

    @pyqtSlot(int)
    def on_midiCcValue_valueChanged(self, val):
        self.sendMidiCc(self.midiChannel.getValue(),
                        self.midiController.getValue(),
                        val)

    def sendMidiCc(self, chan, cc, val):
        print(chan, cc, val)
        
    def setupJack(self):
        self.jackClient = jack.Client('CCMe')





def main():
    args = sys
    app = QtGui.QApplication(sys.argv)

    ccme = CCMe()
    ccme.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
