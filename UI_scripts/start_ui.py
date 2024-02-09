import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
import webbrowser
import requests
import folium
import sqlite3

conn = sqlite3.connect('../database/bd.db')
cursor = conn.cursor()

class Monitoringiop(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)

        self.totalData = {}
        self.data = []
        self.liststations = set()
        self.sef = None
        self.flag = True
        self.time_start = []
        self.time_end = []

        self.navTab = {
            'Загрузка данных': [self.btnDownloadTab.clicked.connect(self.navigate), 1],
            'Визуализация данных': [self.btnVisualTab.clicked.connect(self.navigate), 2],
            'Анализ данных': [self.btnAnalizeTab.clicked.connect(self.navigate), 3],
            'Прогноз': [self.btnPredictTab.clicked.connect(self.navigate), 4],
            'Мониторинг': [self.btnMonitoringTab.clicked.connect(self.navigate), 5],
            'Экспорт': [self.btnExportTab.clicked.connect(self.navigate), 6]
        }

        self.downloadFileData.clicked.connect(self.loadTable)
        self.clearBtnTableWidget.clicked.connect(self.clearTableWidget)

        self.homeBtnDowloadTab.clicked.connect(self.homeGo)
        self.homeBtnVisualTab.clicked.connect(self.homeGo)
        self.homeBtnAnalisTab.clicked.connect(self.homeGo)
        self.homeBtnPredictTab.clicked.connect(self.homeGo)
        self.homeBtnMonitoringtab.clicked.connect(self.homeGo)

        # self.QPushButton.clicked.connect(self.ip_a)
        self.pushBtnCheckboxesClear.clicked.connect(self.clear_button)
        self.clearBtnGraphView.clicked.connect(self.clear_graph)

        self.visualizationBtn.clicked.connect(self.get_time)
        self.visualizationBtn.clicked.connect(self.visualization)
        self.downloadFileData.clicked.connect(self.download)


    # Загрузка
    def download(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('bd13.sqlite')
        db.open()
        model = QSqlTableModel(self)
        model.setTable('stations')
        model.select()

        self.tableWidget.setModel(model)


    # Получение временного отрезка
    def get_time(self):
        # Время начала
        self.time_start = list(map(int, str(self.dateTimeEdit_2.dateTime())[23:len(str(self.dateTimeEdit_2.dateTime())) - 1].split(", ")))
        self.time_start.reverse()
        del self.time_start[0]

        # Время конца
        self.time_end = list(map(int, str(self.dateTimeEdit.dateTime())[23:len(str(self.dateTimeEdit.dateTime())) - 1].split(", ")))
        self.time_end.reverse()
        del self.time_end[0]

        print(self.time_start)
        print(self.time_end)


    # Визуализация
    def visualization(self):
        self.graphicsView.clear()
        querry = ((self.time_end[3] - self.time_start[3]) * 365 +
                  (self.time_end[2] - self.time_start[2]) * 30 +
                  (self.time_end[1] - self.time_start[1])) * 24 + (self.time_end[0] - self.time_start[0])

        querries = 0
        for i in range(0, querry + 1, 3):
            querries += 1

        if self.checkBoxHumidity.isChecked():
            cursor.execute(f"SELECT humidity FROM stations WHERE year >= {self.time_start[3]} and month >= {self.time_start[2]} and day >= {self.time_start[1]}")

            y_t = [x[0] for x in cursor.fetchmany(querries)]
            x_t = [i for i in range(querries)]

            self.graphicsView.plot(x_t, y_t, pen={"color":"g"})
            self.graphicsView_2.plot(x_t, y_t)

        if self.checkBoxPrecipitation.isChecked():
            cursor.execute(f"SELECT precipit FROM stations WHERE year >= {self.time_start[3]} and month >= {self.time_start[2]} and day >= {self.time_start[1]}")

            y_t = [x[0] for x in cursor.fetchmany(querries)]
            x_t = [i for i in range(querries)]

            self.graphicsView.plot(x_t, y_t, pen={"color":"b"})
            self.graphicsView_3.plot(x_t, y_t)

        if self.checkBoxDirectionWind.isChecked():
            cursor.execute(f"SELECT dirwind FROM stations WHERE year >= {self.time_start[3]} and month >= {self.time_start[2]} and day >= {self.time_start[1]}")

            y_t = [x[0] for x in cursor.fetchmany(querries)]
            x_t = [i for i in range(querries)]

            self.graphicsView.plot(x_t, y_t,  pen={"color":"y"})

        if self.checkBoxTemperature.isChecked():
            cursor.execute(f"SELECT temperature FROM stations WHERE year >= {self.time_start[3]} and month >= {self.time_start[2]} and day >= {self.time_start[1]}")

            y_t = [x[0] for x in cursor.fetchmany(querries)]
            x_t = [i for i in range(querries)]

            self.graphicsView.plot(x_t, y_t, pen={"color":"r"})
            self.graphicsView_4.plot(x_t, y_t)


    # Очистка чекбоксов
    def clear_button(self):
        self.checkBoxHumidity.setChecked(False)
        self.checkBoxPrecipitation.setChecked(False)
        self.checkBoxDirectionWind.setChecked(False)
        self.checkBoxTemperature.setChecked(False)


    def clear_graph(self):
        self.graphicsView.clear()


    # Навигация
    def navigate(self):
        self.tabWidget.setCurrentIndex(self.navTab[self.sender().text()][1])


    # На главную
    def homeGo(self):
        self.tabWidget.setCurrentIndex(0)


    def clearTableWidget(self):
        pass

    def loadTable(self):
        pass


    # Местоположение
    def ip_a(self):
        def get_ip():
            response = requests.get('https://api64.ipify.org?format=json').json()
            return response["ip"]

        def get_location():
            ip_address = get_ip()
            location_data = {
                "ip": ip_address}
            n = ''.join([j for i, j in location_data.items()])
            return n

        def main_1():
            try:
                 url = requests.get('https://api64.ipify.org?format=json')
                 if url:
                     ip = get_location()
                     n = []
                     response = requests.get(f'http://ip-api.com/json/{ip}').json()
                     for i, j in response.items():
                         if i == 'lat' or i == 'lon':
                             n.append(j)
                     m = folium.Map(location=[n[0], n[1]], zoom_start=15)
                     folium.Marker([n[0], n[1]], poput='Место 1', tooltip=None).add_to(m)
                     m.save('weather.html')
                     webbrowser.open('weather.html')


            except requests.ConnectionError as e:
                print(e)


        if __name__ == '__main__':
            main_1()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Monitoringiop()
    ex.show()
    sys.exit(app.exec_())
