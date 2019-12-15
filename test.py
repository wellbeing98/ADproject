
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class SeoulMetro(QWidget):

    def __init__(self, parent= None):
        super().__init__(parent)

        self.setup_ui()

    def setup_ui(self):

        # Find
        #strStart 출발지 입력
        self.strStart = QLineEdit()
        self.strStart.setMaxLength(15)

        #strEnd 도착지 입력
        self.strEnd = QLineEdit()
        self.strEnd.setMaxLength(15)

        #strStart, strEnd를 입력한 후 버튼 클릭
        self.findBtn = QToolButton()
        self.findBtn.setText("Find!")
        self.findBtn.clicked.connect(self.findevent)

        #없으니까 에러 남
        self.line= QLine()

        # End
        # timeLabel time표시
        self.timeLabel = QLabel("time")

        # strTime time표시
        self.strTime = QLineEdit()
        self.strTime.setReadOnly(True)
        self.strTime.setAlignment(Qt.AlignLeft)
        self.strTime.setMaxLength(10)

        # statusNull 빈공간
        self.statusNull= QLabel("")

        #statusLayout 오른쪽 레이아웃
        statusLayout = QGridLayout()
        statusLayout.addWidget(self.strStart, 0, 0, 1, 2)
        statusLayout.addWidget(self.strEnd, 1, 0, 1, 2)
        statusLayout.addWidget(self.findBtn, 2, 0)

        statusLayout.addWidget(self.statusNull, 3, 0)

        statusLayout.addWidget(self.timeLabel, 4, 0)
        statusLayout.addWidget(self.strTime, 4, 1)

        # show
        # metroLayout 역 구간 보이는 부분
        self.metroLayout = QGridLayout()

        self.fstBtn = QToolButton()
        self.fstBtn.setText("fst")

        self.endBtn = QToolButton()
        self.endBtn.setText("end")

        self.metroLayout.addWidget(self.fstBtn, 0, 0)
        self.metroLayout.addWidget(self.endBtn, 0, 4)

        # Display Window
        showLayout = QGridLayout()
        showLayout.addLayout(self.metroLayout, 0, 0)

        mainLayout = QGridLayout()

        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addLayout(statusLayout, 0, 1)
        mainLayout.addLayout(showLayout, 0, 0)

        self.setLayout(mainLayout)
        self.setWindowTitle("Seoul metro find")

    # FindClicked
    def findevent(self):
        self.fstBtn.setText("dongdamun history place")

        self.endBtn.setText("dongdamun")

        self.line = QLine(QPoint(self.fstBtn.x()+ 10, self.fstBtn.y()+ 10), QPoint(self.endBtn.x()+ 10, self.endBtn.y()+ 10))
        print(QPoint(self.fstBtn.x(), self.fstBtn.y()))
        print(QPoint(self.endBtn.x(), self.endBtn.y()))
        print(self.line)
        self.update()



    def paintEvent(self, event):
        if not self.line.isNull():
            painter = QPainter(self)
            pen = QPen(Qt.red, 3)
            painter.setPen(pen)
            painter.drawLine(self.line)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    subway = SeoulMetro()
    subway.show()
    sys.exit(app.exec_())