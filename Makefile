all: ccme/ui_mainwindow.py

ccme/ui_mainwindow.py: res/ccmidi.ui
	pyuic4 res/ccmidi.ui -o ccme/ui_mainwindow.py
