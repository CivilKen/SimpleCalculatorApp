import sys, operator
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon
from Calculator import *

# Calculator state.
READY = 0
INPUT = 1


class CalculatorMainWindow(QMainWindow, Ui_CalculatorMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Setup flags
        self.state = None
        self.stack = [0]
        self.current_operation = None
        self.last_operation = None
        self.decimal = False
        self.decimal_point = 0

        # Setup number
        for i in range(10):
            # 利用 getattr 來得到 pushButton 的物件
            getattr(self, 'pushButton_%s' % i).pressed.connect(lambda v=i: self.input_number(v))

        # Setup operation
        self.pushButton_plus.pressed.connect(lambda: self.operation(operator.add))  # pressed == clicked
        self.pushButton_minus.pressed.connect(lambda: self.operation(operator.sub))
        self.pushButton_multiply.pressed.connect(lambda: self.operation(operator.mul))
        self.pushButton_divide.pressed.connect(lambda: self.operation(operator.truediv))
        self.pushButton_equal.pressed.connect(self.equals)
        self.pushButton_dot.clicked.connect(self.dot_operation)

        # Setup actions
        self.pushButton_c.pressed.connect(self.reset)

        self.setWindowIcon(QIcon('anyicon.png'))
        self.reset()
        self.show()

    def operation(self, op):
        if self.current_operation:
            self.equals()

        self.stack.append(0)
        self.state = INPUT
        self.current_operation = op
        self.decimal = False
        self.decimal_point = 0

        self.display(op)

    def dot_operation(self):
        self.decimal = True
        self.decimal_point += 1

    def input_number(self, v):
        if self.state == READY:
            self.state = INPUT
            self.stack[-1] = v
        else:
            if not self.decimal:
                self.stack[-1] = self.stack[-1] * 10 + v
                # 每輸入一個數字就代表再進位一次
            if self.decimal:
                self.stack[-1] = self.stack[-1] + v * pow(10, -self.decimal_point)
                self.decimal_point += 1

        self.display()

    def equals(self):
        # equals 會讓目前的 operation 先得到結果
        # last_operation 會儲存最後的結果和上一步的 operation
        if self.state == READY and self.last_operation:
            s, self.current_operation = self.last_operation
            self.stack.append(s)

        if self.current_operation:
            self.last_operation = self.stack[-1], self.current_operation

            try:
                self.stack = [self.current_operation(*self.stack)]  # '*'的用意是將stack內的 element 全部進行 operation
            except Exception:
                self.lineEdit_output.setText('Err')
                self.stack = [0]
            else:
                self.current_operation = None
                self.state = READY
                self.display()

    def reset(self):
        self.state = READY
        self.stack = [0]
        self.decimal = False
        self.decimal_point = 0
        self.current_operation = None
        self.last_operation = None
        self.display()

    def display(self, display_type=None):
        if display_type is None:
            self.lineEdit_output.setText(str(self.stack[-1]))
        elif display_type == operator.add:
            self.lineEdit_output.setText('+')
        elif display_type == operator.sub:
            self.lineEdit_output.setText('-')
        elif display_type == operator.mul:
            self.lineEdit_output.setText('x')
        elif display_type == operator.truediv:
            self.lineEdit_output.setText('÷')
        self.lineEdit_output.setAlignment(QtCore.Qt.AlignHCenter)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = CalculatorMainWindow()
    myWin.show()
    sys.exit(app.exec_())
