from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QTimer, QPoint


class Prompter(QWidget):
    def __init__(self):
        super().__init__()

        # 设置窗口标题和大小
        self.setWindowTitle("Prompter")
        self.setGeometry(100, 100, 800, 600)

        # 创建文本输入框和滚动区域
        self.input_box = QTextEdit(self)

        # 创建滚动速度和字幕大小的滑块
        self.scroll_speed_slider = QSlider(Qt.Horizontal)
        self.scroll_speed_slider.setMinimum(1)
        self.scroll_speed_slider.setMaximum(10)
        self.scroll_speed_slider.setValue(5)
        self.font_size_slider = QSlider(Qt.Horizontal)
        self.font_size_slider.setMinimum(1)
        self.font_size_slider.setMaximum(100)
        self.font_size_slider.setValue(30)

        # 创建 QLabel 用于展示滚动文本，并将其添加到滚动区域中
        self.scroll_label = QLabel(self)
        self.scroll_label.setFont(QFont("Arial", self.font_size_slider.value()))
        self.scroll_label.setAlignment(Qt.AlignTop)
        self.scroll_label.setWordWrap(True)

        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.scroll_label)

        # 创建“开始”和“停止”按钮，并将它们连接到相应的槽函数
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.start_button.clicked.connect(self.start_scroll)
        self.stop_button.clicked.connect(self.stop_scroll)

        # 创建水平布局和垂直布局，并将所有控件添加到这些布局中
        hbox1 = QHBoxLayout()
        hbox1.addWidget(QLabel("Scroll Speed:"))
        hbox1.addWidget(self.scroll_speed_slider)
        hbox1.addWidget(QLabel("Font Size:"))
        hbox1.addWidget(self.font_size_slider)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.start_button)
        hbox2.addWidget(self.stop_button)

        vbox = QVBoxLayout()
        vbox.addWidget(self.input_box)
        vbox.addLayout(hbox1)
        vbox.addWidget(scroll_area)
        vbox.addLayout(hbox2)

        # 将垂直布局应用于窗口
        self.setLayout(vbox)

        # 创建定时器并将其连接到槽函数
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.scroll_text)

        # 初始化滚动文本
        self.scroll_text()

    def start_scroll(self):
        # 启动定时器
        self.timer.start(1000 // self.scroll_speed_slider.value())

    def stop_scroll(self):
        # 停止定时器
        self.timer.stop()

    def scroll_text(self):
        # 获取当前文本框中的文本，并将其设置为滚动标签的文本
        text = self.input_box.toPlainText()
        self.scroll_label.setText(text)

        # 获取滚动标签的高度
        label_height = self.scroll_label.height()

        # 获取滚动区域的高度
        scroll_area_height = self.scroll_label.parentWidget().height()

        # 如果滚动标签的高度大于滚动区域的高度，则将标签向上移动一个像素
        if label_height > scroll_area_height:
            scroll_pos = self.scroll_label.pos()
            new_pos = scroll_pos - QPoint(0, 1)
            if new_pos.y() + label_height < 0:
                new_pos.setY(scroll_area_height)
            self.scroll_label.move(new_pos)

        # 设置滚动标签的字体大小
        self.scroll_label.setFont(QFont("Arial", self.font_size_slider.value()))

if __name__ == "__main__":
    app = QApplication([])
    prompter = Prompter()
    prompter.show()
    app.exec_()