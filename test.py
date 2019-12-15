
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

        # 시각적으로 나타내는 부분
        # fstBtn 시작역
        # endBtn 도착역
        # spaceNull 빈공간 및 환승역 나타내기용
        self.fstBtn = QToolButton()
        self.fstBtn.setText("   fst   ")
        self.fstBtn.setFixedWidth(150)

        self.endBtn = QToolButton()
        self.endBtn.setText("   end   ")
        self.endBtn.setFixedWidth(150)

        self.spaceNull1 = QPushButton("")
        self.spaceNull1.setFixedWidth(15)

        self.spaceNull2 = QPushButton("")
        self.spaceNull2.setFixedWidth(150)

        self.spaceNull3 = QPushButton("")
        self.spaceNull3.setFixedWidth(15)

        self.spaceNull4 = QPushButton("")
        self.spaceNull4.setFixedWidth(150)

        self.spaceNull5 = QPushButton("")
        self.spaceNull5.setFixedWidth(15)

        self.spaceNull6 = QPushButton("")
        self.spaceNull6.setFixedWidth(150)

        self.spaceNull7 = QPushButton("")
        self.spaceNull7.setFixedWidth(15)

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

        effect = QGraphicsOpacityEffect(self.spaceNull6)
        effect.setOpacity(0)
        self.spaceNull6.setGraphicsEffect(effect)

        effect = QGraphicsOpacityEffect(self.spaceNull7)
        effect.setOpacity(0)
        self.spaceNull7.setGraphicsEffect(effect)
        # =============

        self.nullSpace3.addWidget(self.fstBtn)

        self.nullSpace3.addWidget(self.spaceNull1)
        self.nullSpace3.addWidget(self.spaceNull2)
        self.nullSpace3.addWidget(self.spaceNull3)
        self.nullSpace3.addWidget(self.spaceNull4)
        self.nullSpace3.addWidget(self.spaceNull5)
        self.nullSpace3.addWidget(self.spaceNull6)
        self.nullSpace3.addWidget(self.spaceNull7)

        self.nullSpace3.addWidget(self.endBtn)

        showLayout = QGridLayout()
        showLayout.addLayout(self.metroLayout, 0, 0)

        # Display Window
        # 왼쪽 레이아웃 = 환승구간 표시
        # 오른쪽 레이아웃 = 입력값 설정 및 시간 출력
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addLayout(statusLayout, 0, 1)
        mainLayout.addLayout(showLayout, 0, 0)

        self.setLayout(mainLayout)
        self.setWindowTitle("Seoul metro find")

    # FindClicked가 눌렸을 때 발생하는 이벤트
    # 입력한 역을 이용해 소요시간과 환승역을 구함 
    def findEvent(self):
        self.startString = self.strStart.text()
        self.endString = self.strEnd.text()

        self.fstBtn.setText(self.startString)
        self.endBtn.setText(self.endString)

        self.midlle= Gettime_station_history(self.startString, self.endString)

        self.strTime.setText(str(self.midlle.Gettime()))

        self.midlleStation= self.midlle.GetTransit_station()

        if len(midlleStation) == 1:
            self.spaceNull4.setText(midlleStation[0])
        elif len(midlleStation) == 2:
            self.spaceNull2.setText(midlleStation[0])
            self.spaceNull6.setText(midlleStation[1])
        elif len(midlleStation) == 3:
            self.spaceNull2.setText(midlleStation[0])
            self.spaceNull4.setText(midlleStation[1])
            self.spaceNull6.setText(midlleStation[2])

    # 역에서 역 사이 구간의 좌표를 QLine으로 받음
    def functionEvent(self):
        # 환승역의 개수에 따라 선을 그려야할 구간 설정
        self.midlleLine = self.midlle.GetStation_line()

        if len(midlleLine) == 1:
            self.line1 = QLine(QPoint(self.fstBtn.x()+ 10, self.fstBtn.y()+ 10),
                QPoint(self.spaceNull4.x()+ 10, self.spaceNull4.y()+ 10))
            self.line2 = QLine(QPoint(self.spaceNull4.x()+ 10, self.spaceNull4.y()+ 10),
                QPoint(self.endBtn.x()+ 10, self.endBtn.y()+ 10))

        elif len(midlleLine) == 2:
            self.line1 = QLine(QPoint(self.fstBtn.x()+ 10, self.fstBtn.y()+ 10),
                QPoint(self.spaceNull2.x()+ 10, self.spaceNull2.y()+ 10))
            self.line2 = QLine(QPoint(self.spaceNull2.x()+ 10, self.spaceNull2.y()+ 10),
                QPoint(self.spaceNull6.x()+ 10, self.spaceNull6.y()+ 10))
            self.line3 = QLine(QPoint(self.spaceNull6.x()+ 10, self.spaceNull6.y()+ 10),
                QPoint(self.endBtn.x()+ 10, self.endBtn.y()+ 10))

        elif len(midlleLine) == 3:
            self.line1 = QLine(QPoint(self.fstBtn.x()+ 10, self.fstBtn.y()+ 10),
                QPoint(self.spaceNull2.x()+ 10, self.spaceNull2.y()+ 10))
            self.line2 = QLine(QPoint(self.spaceNull2.x()+ 10, self.spaceNull2.y()+ 10),
                QPoint(self.spaceNull4.x()+ 10, self.spaceNull4.y()+ 10))
            self.line3 = QLine(QPoint(self.spaceNull4.x()+ 10, self.spaceNull4.y()+ 10),
                QPoint(self.spaceNull6.x()+ 10, self.spaceNull6.y()+ 10))
            self.line4 = QLine(QPoint(self.spaceNull6.x()+ 10, self.spaceNull6.y()+ 10),
                QPoint(self.endBtn.x()+ 10, self.endBtn.y()+ 10))

        self.update()

    # FunctionEvent가 눌렸을 때 QLine에 호선에 맞는 선을 그림
    def paintEvent(self, event):
        if not self.line1.isNull():
            painter = QPainter(self)
            pen = QPen(Qt.red, 3)
            painter.setPen(pen)
            painter.drawLine(self.line1)

        if not self.line2.isNull():
            painter = QPainter(self)
            pen = QPen(Qt.red, 3)
            painter.setPen(pen)
            painter.drawLine(self.line2)

        if not self.line3.isNull():
            painter = QPainter(self)
            pen = QPen(Qt.red, 3)
            painter.setPen(pen)
            painter.drawLine(self.line3)

        if not self.line4.isNull():
            painter = QPainter(self)
            pen = QPen(Qt.red, 3)
            painter.setPen(pen)
            painter.drawLine(self.line4)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    subway = SeoulMetro()
    subway.show()
    sys.exit(app.exec_())
