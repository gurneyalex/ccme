#!/usr/bin/env python3
from PyQt4 import QtGui
from PyQt4.QtCore import QObject, pyqtSlot
import sys
import jack
import struct
import queue

from .ui_mainwindow import Ui_MainWindow
from .midi_cc import definitions

class CCMe(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(CCMe, self).__init__()
        self.setupUi(self)
        self.out_queue = queue.Queue()
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
        name = definitions['%d'%val]
        self.controllerName.setText(name)
        self.midiCcValue.setValue(0)

    @pyqtSlot(int)
    def on_midiCcValue_valueChanged(self, val):
        self.sendMidiCc(self.midiChannel.value(),
                        self.midiController.value(),
                        val)

    def sendMidiCc(self, chan, cc, val):
        print(chan, cc, val)
        event = struct.pack('>BBB', 0xb0 + chan - 1, cc, val)
        print('put')
        self.out_queue.put(event)

    def setupJack(self):
        self.jackClient = jack.Client('CCMe')
        self.midi_out = self.jackClient.midi_outports.register('midi_out')
        self.jackClient.set_process_callback(self.jack_cb)
        self.jackClient.activate()

    def on_mainwindow_destroyed(self):
        self.jackClient.deactivate()
        self.jackClient.close()

    def jack_cb(self, frames):
        time = 0
        self.midi_out.clear_buffer()
        try:
            while True:
                time += 1
                event = self.out_queue.get_nowait()
                print(time, event)
                try:
                    self.midi_out.write_midi_event(time, event)
                except jack.JackError as exc:
                    print (exc)
        except queue.Empty:
            pass





def main():
    args = sys
    app = QtGui.QApplication(sys.argv)

    ccme = CCMe()
    ccme.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
