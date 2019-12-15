
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from testAD import *

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
        self.findBtn.clicked.connect(self.findEvent)

        #functionBtn
        self.functionBtn= QToolButton()
        self.functionBtn.setText("Function!")
        self.functionBtn.clicked.connect(self.functionEvent)

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
        statusLayout.addWidget(self.functionBtn, 2, 1)

        statusLayout.addWidget(self.statusNull, 3, 0)

        statusLayout.addWidget(self.timeLabel, 4, 0)
        statusLayout.addWidget(self.strTime, 4, 1)

        # show
        # metroLayout 역 구간 보이는 부분
        self.metroLayout = QVBoxLayout()

        self.nullSpace1 = QHBoxLayout()
        self.nullSpace2 = QHBoxLayout()
        self.nullSpace3 = QHBoxLayout()
        self.nullSpace4 = QHBoxLayout()
        self.nullSpace5 = QHBoxLayout()

        self.metroLayout.addLayout(self.nullSpace1)
        self.metroLayout.addLayout(self.nullSpace2)
        self.metroLayout.addLayout(self.nullSpace3)
        self.metroLayout.addLayout(self.nullSpace4)
        self.metroLayout.addLayout(self.nullSpace5)

        #
        self.fstBtn = QToolButton()
        self.fstBtn.setText("   fst   ")
        self.fstBtn.setFixedWidth(150)

        self.endBtn = QToolButton()
        self.endBtn.setText("   end   ")
        self.endBtn.setFixedWidth(150)

        self.spaceNull1 = QPushButton("")
        self.spaceNull1.setFixedWidth(50)

        self.spaceNull2 = QPushButton("")
        self.spaceNull2.setFixedWidth(150)

        self.spaceNull3 = QPushButton("")
        self.spaceNull3.setFixedWidth(50)

        self.spaceNull4 = QPushButton("")
        self.spaceNull4.setFixedWidth(150)

        self.spaceNull5 = QPushButton("")
        self.spaceNull5.setFixedWidth(50)

        # ============
        effect= QGraphicsOpacityEffect(self.spaceNull1)
        effect.setOpacity(0)
        self.spaceNull1.setGraphicsEffect(effect)

        effect = QGraphicsOpacityEffect(self.spaceNull2)
        effect.setOpacity(0)
        self.spaceNull2.setGraphicsEffect(effect)

        effect = QGraphicsOpacityEffect(self.spaceNull3)
        effect.setOpacity(0)
        self.spaceNull3.setGraphicsEffect(effect)

        effect = QGraphicsOpacityEffect(self.spaceNull4)
        effect.setOpacity(0)
        self.spaceNull4.setGraphicsEffect(effect)

        effect = QGraphicsOpacityEffect(self.spaceNull5)
        effect.setOpacity(0)
        self.spaceNull5.setGraphicsEffect(effect)
        # =============

        self.nullSpace3.addWidget(self.fstBtn)

        self.nullSpace3.addWidget(self.spaceNull1)
        self.nullSpace3.addWidget(self.spaceNull2)
        self.nullSpace3.addWidget(self.spaceNull3)
        self.nullSpace3.addWidget(self.spaceNull4)
        self.nullSpace3.addWidget(self.spaceNull5)

        self.nullSpace3.addWidget(self.endBtn)

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
    def findEvent(self):
        self.startString = self.strStart.text()
        self.endString = self.strEnd.text()

        self.fstBtn.setText(self.startString)
        self.endBtn.setText(self.endString)

        self.midlle= Gettime_station_history(self.startString, self.endString)

        self.strTime.setText(str(self.midlle.Gettime()))

    def functionEvent(self):
        self.line = QLine(QPoint(self.fstBtn.x() + 10, self.fstBtn.y() + 10),
                          QPoint(self.endBtn.x() + 10, self.endBtn.y() + 10))
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
