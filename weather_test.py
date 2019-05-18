import requests
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from mianLayoutUI import *

class Example(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Example, self).__init__(parent)
        self.setupUi(self)
        self.addAction()
        self.setWindowIcon(QIcon('icon.png'))

    def addAction(self):
        self.pushButton_query.clicked.connect(self.queryWeahter)
        self.pushButton_clear.clicked.connect(self.clearQueryResult)

    def queryWeahter(self):
        cityCode = self.transCityName(self.comboBox_city.currentText())

        rep = requests.get('http://www.weather.com.cn/data/sk/'+cityCode+'.html')
        rep.encoding = 'utf-8'
        print(rep.json())
        msg1 = '城市：%s' % rep.json()['weatherinfo']['city']+'\n'
        msg2 = '风向：%s' % rep.json()['weatherinfo']['WD']+'\n'
        msg3 = '温度：%s' % rep.json()['weatherinfo']['temp']+'摄氏度'+'\n'
        msg4 = '湿度：%s' % rep.json()['weatherinfo']['SD'] + '\n'
        msg5 = '风力：%s' % rep.json()['weatherinfo']['WS'] + '\n'
        result = msg1+ msg2+ msg3+ msg4+ msg5
        self.textEdit_result.setText(result)

    def transCityName(self, city):
        if city == '北京':
            return '101010100'
        elif city == '上海':
            return '101020100'
        elif city == "天津":
            return '101030100'
        elif city == "广州":
            return '101280101'

    def clearQueryResult(self):
        self.textEdit_result.setText('')


if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = Example()
        ex.show()
        sys.exit(app.exec_())