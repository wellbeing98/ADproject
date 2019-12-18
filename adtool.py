from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from adproject import *

class SeoulMetro(QWidget):

    #용도 모름
    paintTrigger = pyqtSignal()

    def __init__(self, parent= None):
        super().__init__(parent)

        self.dict = {'1': Qt.darkBlue, '2': Qt.green, '3': Qt.darkYellow, '4': Qt.blue, '5': Qt.cyan, '6': Qt.gray,
                     '7': Qt.darkGray, '8': Qt.red, '9': Qt.gray, '분': Qt.yellow}

        # 없으니까 에러 남
        self.line1 = QLine()
        self.line2 = QLine()
        self.line3 = QLine()
        self.line4 = QLine()

        self.setup_ui()

    def setup_ui(self):

        # Find
        # 출발안내 라벨
        self.startLabel = QLabel("출발역을 입력해주세요!")

        # strStart 출발지 입력
        self.strStart = QLineEdit()
        self.strStart.setMaxLength(15)

        # 도착안내 라벨
        self.endLabel = QLabel("도착역을 입력해주세요!")

        # strEnd 도착지 입력
        self.strEnd = QLineEdit()
        self.strEnd.setMaxLength(15)

        # strStart, strEnd를 입력한 후 버튼 클릭
        self.findBtn = QToolButton()
        self.findBtn.setText("Find!")
        self.findBtn.clicked.connect(self.findEvent)

        # drawBtn 역 사이 호선을 그림
        self.drawBtn = QToolButton()
        self.drawBtn.setText("Function!")
        self.drawBtn.clicked.connect(self.drawEvent)

        self.resetBtn = QToolButton()
        self.resetBtn.setText("reset")
        self.resetBtn.clicked.connect(self.resetEvent)

        # statusNull 빈공간
        self.statusNull = QLabel("")

        # End
        # timeLabel time표시
        self.timeLabel = QLabel("time")

        # strTime time표시
        self.strTime = QLineEdit()
        self.strTime.setReadOnly(True)
        self.strTime.setAlignment(Qt.AlignLeft)
        self.strTime.setMaxLength(10)

        #statusLayout 오른쪽 레이아웃
        statusLayout = QGridLayout()
        statusLayout.addWidget(self.startLabel, 0, 0, 1, 3)
        statusLayout.addWidget(self.strStart, 1, 0, 1, 3)
        statusLayout.addWidget(self.endLabel, 2, 0, 1, 3)
        statusLayout.addWidget(self.strEnd, 3, 0, 1, 3)
        statusLayout.addWidget(self.findBtn, 4, 0)
        statusLayout.addWidget(self.drawBtn, 4, 1)
        statusLayout.addWidget(self.resetBtn, 4, 2)

        statusLayout.addWidget(self.statusNull, 5, 0)

        statusLayout.addWidget(self.timeLabel, 6, 0)
        statusLayout.addWidget(self.strTime, 6, 1, 1, 2)

        # show
        # metroLayout 역 구간 보이는 부분
        self.metroLayout = QHBoxLayout()

        # 시각적으로 나타내는 부분
        # fstBtn 시작역
        # endBtn 도착역
        # spaceNull 빈공간 및 환승역 나타내기용
        self.fstBtn = QToolButton()
        self.fstBtn.setText("fst")
        self.fstBtn.setFixedWidth(150)

        # ==========================================================
        self.finalBtn = QToolButton()
        self.finalBtn.setText("final")
        self.finalBtn.setFixedWidth(150)

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
        # =====================================================

        self.metroLayout.addWidget(self.fstBtn)

        self.metroLayout.addWidget(self.spaceNull1)
        self.metroLayout.addWidget(self.spaceNull2)
        self.metroLayout.addWidget(self.spaceNull3)
        self.metroLayout.addWidget(self.spaceNull4)
        self.metroLayout.addWidget(self.spaceNull5)
        self.metroLayout.addWidget(self.spaceNull6)
        self.metroLayout.addWidget(self.spaceNull7)

        self.metroLayout.addWidget(self.finalBtn)

        self.recentStatus = QTextEdit("결과")
        self.recentStatus.setReadOnly(True)
        self.recentStatus.setAlignment(Qt.AlignLeft)

        showLayout = QGridLayout()
        showLayout.addLayout(self.metroLayout, 0, 0)
        showLayout.addWidget(self.recentStatus, 1, 0)

        # Display Window
        # 왼쪽 레이아웃 = 환승구간 표시
        # 오른쪽 레이아웃 = 입력값 설정 및 시간 출력
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addLayout(showLayout, 0, 0)
        mainLayout.addLayout(statusLayout, 0, 1)

        self.setLayout(mainLayout)
        self.setWindowTitle("Seoul metro find")
        #=====================

    # FindClicked가 눌렸을 때 발생하는 이벤트
    # 입력한 역을 이용해 소요시간과 환승역을 구함
    def findEvent(self):
        self.fstString = self.strStart.text()
        self.finalString = self.strEnd.text()

        self.fstBtn.setText(self.fstString)
        self.finalBtn.setText(self.finalString)

        self.midlle = Gettime_station_history(self.fstString, self.finalString)

        self.strTime.setText(str(self.midlle.Gettime()))
        self.recentStatus.setText((str(self.midlle.Gethistory())))

        self.midlleStation= self.midlle.GetTransit_station()

        #환승역이 한 개인 경우
        if len(self.midlleStation) == 1:
            self.spaceNull4.setText(self.midlleStation[0])
            effect = QGraphicsOpacityEffect(self.spaceNull4)
            effect.setOpacity(100)
            self.spaceNull4.setGraphicsEffect(effect)

        elif len(self.midlleStation) == 2:
            self.spaceNull2.setText(self.midlleStation[0])
            effect = QGraphicsOpacityEffect(self.spaceNull2)
            effect.setOpacity(100)
            self.spaceNull2.setGraphicsEffect(effect)

            self.spaceNull6.setText(self.midlleStation[1])
            effect = QGraphicsOpacityEffect(self.spaceNull6)
            effect.setOpacity(100)
            self.spaceNull6.setGraphicsEffect(effect)

        elif len(self.midlleStation) == 3:
            self.spaceNull2.setText(self.midlleStation[0])
            effect = QGraphicsOpacityEffect(self.spaceNull2)
            effect.setOpacity(100)
            self.spaceNull2.setGraphicsEffect(effect)

            self.spaceNull4.setText(self.midlleStation[1])
            effect = QGraphicsOpacityEffect(self.spaceNull4)
            effect.setOpacity(100)
            self.spaceNull4.setGraphicsEffect(effect)

            self.spaceNull6.setText(self.midlleStation[2])
            effect = QGraphicsOpacityEffect(self.spaceNull6)
            effect.setOpacity(100)
            self.spaceNull6.setGraphicsEffect(effect)

    # 역에서 역 사이 구간의 좌표를 QLine으로 받음
    def drawEvent(self):
        # 환승역의 개수에 따라 선을 그려야할 구간 설정
        self.midlleLine = self.midlle.GetStation_line()

        if len(self.midlleLine) == 1:
            print("1")
            self.line1 = QLine(QPoint(self.fstBtn.x() + 10, self.fstBtn.y() + 10),
                               QPoint(self.finalBtn.x() + 10, self.finalBtn.y() + 10))
        elif len(self.midlleLine) == 2:
            print("2")
            self.line1 = QLine(QPoint(self.fstBtn.x()+ 10, self.fstBtn.y()+ 10),
                QPoint(self.spaceNull4.x()+ 10, self.spaceNull4.y()+ 10))
            self.line2 = QLine(QPoint(self.spaceNull4.x()+ 10, self.spaceNull4.y()+ 10),
                QPoint(self.finalBtn.x()+ 10, self.finalBtn.y()+ 10))

        elif len(self.midlleLine) == 3:
            print("3")
            self.line1 = QLine(QPoint(self.fstBtn.x()+ 10, self.fstBtn.y()+ 10),
                QPoint(self.spaceNull2.x()+ 10, self.spaceNull2.y()+ 10))
            self.line2 = QLine(QPoint(self.spaceNull2.x()+ 10, self.spaceNull2.y()+ 10),
                QPoint(self.spaceNull6.x()+ 10, self.spaceNull6.y()+ 10))
            self.line3 = QLine(QPoint(self.spaceNull6.x()+ 10, self.spaceNull6.y()+ 10),
                QPoint(self.finalBtn.x()+ 10, self.finalBtn.y()+ 10))

        elif len(self.midlleLine) == 4:
            print("4")
            self.line1 = QLine(QPoint(self.fstBtn.x()+ 10, self.fstBtn.y()+ 10),
                QPoint(self.spaceNull2.x()+ 10, self.spaceNull2.y()+ 10))
            self.line2 = QLine(QPoint(self.spaceNull2.x()+ 10, self.spaceNull2.y()+ 10),
                QPoint(self.spaceNull4.x()+ 10, self.spaceNull4.y()+ 10))
            self.line3 = QLine(QPoint(self.spaceNull4.x()+ 10, self.spaceNull4.y()+ 10),
                QPoint(self.spaceNull6.x()+ 10, self.spaceNull6.y()+ 10))
            self.line4 = QLine(QPoint(self.spaceNull6.x()+ 10, self.spaceNull6.y()+ 10),
                QPoint(self.finalBtn.x()+ 10, self.finalBtn.y()+ 10))

        print(self.midlleLine)
        self.update()

    # FunctionEvent가 눌렸을 때 QLine에 호선에 맞는 선을 그림

    def paintEvent(self, event):
        painter = QPainter(self)
        #painter.begin(self)
        self.draw_middleLine(painter)
        #painter.end()

    def draw_middleLine(self, painter):

        if not self.line1.isNull():
            pen = QPen(QColor(self.dict[str(self.midlleLine[0])]), 3)
            painter.setPen(pen)
            painter.drawLine(self.line1)

        if not self.line2.isNull():
            pen = QPen(QColor(self.dict[str(self.midlleLine[1])]), 3)
            painter.setPen(pen)
            painter.drawLine(self.line2)

        if not self.line3.isNull():
            pen = QPen(QColor(self.dict[str(self.midlleLine[2])]), 3)
            painter.setPen(pen)
            painter.drawLine(self.line3)

        if not self.line4.isNull():
            pen = QPen(QColor(self.dict[str(self.midlleLine[3])]), 3)
            painter.setPen(pen)
            painter.drawLine(self.line4)


        '''
        if len(self.midlleLine) == 1:
            pen = QPen(QColor(self.dict[str(self.midlleLine[0])]), 3)
            painter.setPen(pen)
            painter.drawLine(self.line1)
        elif len(self.midlleLine) == 2:
            pen = QPen(QColor(self.dict[str(self.midlleLine[0])]), 3)
            painter.setPen(pen)
            painter.drawLine(self.line1)
            pen = QPen(QColor(self.dict[str(self.midlleLine[1])]), 3)
            painter.setPen(pen)
            painter.drawLine(self.line1)
        '''




    '''
    def paintEvent(self, event):
        if len(self.midlleLine) == 1:
            if not self.line1.isNull():
                painter1 = QPainter(self)
                pen1 = QPen(QColor(self.dict[str(self.midlleLine[0])]), 3)
                painter1.setPen(pen1)
                painter1.drawLine(self.line1)
            if not self.line2.isNull():
                painter2 = QPainter(self)
                pen2 = QPen(QColor(self.dict[str(self.midlleLine[1])]), 3)
                painter2.setPen(pen2)
                painter2.drawLine(self.line2)
        elif len(self.midlleLine) == 2:
            if not self.line1.isNull():
                painter1 = QPainter(self)
                pen1 = QPen(QColor(), 3)
                painter1.setPen(pen1)
                painter1.drawLine(self.line1)
            if not self.line2.isNull():
                painter2 = QPainter(self)
                pen2 = QPen(Qt.red, 3)
                painter2.setPen(pen2)
                painter2.drawLine(self.line2)
            if not self.line3.isNull():
                painter3 = QPainter(self)
                pen3 = QPen(Qt.red, 3)
                painter3.setPen(pen3)
                painter3.drawLine(self.line3)
        elif len(self.midlleLine) == 3:
            if not self.line1.isNull():
                painter1 = QPainter(self)
                pen1 = QPen(QColor(), 3)
                painter1.setPen(pen1)
                painter1.drawLine(self.line1)
            if not self.line2.isNull():
                painter2 = QPainter(self)
                pen2 = QPen(Qt.red, 3)
                painter2.setPen(pen2)
                painter2.drawLine(self.line2)
            if not self.line3.isNull():
                painter3 = QPainter(self)
                pen3 = QPen(Qt.red, 3)
                painter3.setPen(pen3)
                painter3.drawLine(self.line3)
            if not self.line4.isNull():
                painter4 = QPainter(self)
                pen4 = QPen(Qt.red, 3)
                painter4.setPen(pen4)
                painter4.drawLine(self.line4)
    '''

    def resetEvent(self):
        self.line1 = QLine()
        self.line2 = QLine()
        self.line3 = QLine()
        self.line4 = QLine()

        self.fstBtn.setText("fst")
        self.fstBtn.setText("end")

        self.spaceNull2.setText("")
        self.spaceNull4.setText("")
        self.spaceNull6.setText("")

        effect = QGraphicsOpacityEffect(self.spaceNull1)
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

        pass


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    subway = SeoulMetro()
    subway.show()
    sys.exit(app.exec_())