import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Digital Clock 2026 Lite Pro")
        self.setGeometry(600, 400, 500, 300)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setText("00:00:00")
        self.time_label.setStyleSheet("font-size: 100px;"
                                      "font-family: Arial;"
                                      "color: #00ff00;")
        self.setStyleSheet("background-color: #000000")
        self.time_label.adjustSize()
        self.adjustSize()
        self.time_label.setAlignment(Qt.AlignCenter)

        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)
        self.updateTime()

    def updateTime(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)

def main():
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
