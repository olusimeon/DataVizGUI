# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

# this application allows user to input a csv filename, display data head, summary, adjust numbers of row, plot a line and bar chart
# before running this program the following libraries must be installed if not  pre-installed.
# pandas, matplotlib, seaborn and pyqt5

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as Navigation
from matplotlib.figure import Figure


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        # to connect load push button to dataset
        self.pushButton.clicked.connect(self.load_dataset)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        # to connect button to data summary
        self.pushButton_2.clicked.connect(self.describe)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        # to connect button to line graph
        self.pushButton_3.clicked.connect(self.line_graph)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        # to connect button to bar graph
        self.pushButton_4.clicked.connect(self.bar_graph)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # canvas for graph
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        # object for navigation toolbar
        self.toolbar = Navigation(self.canvas, self.centralwidget)

        # add navigation toolbar to horizontal layout
        self.horizontalLayout.addWidget(self.toolbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    # error function
    def error(self):
        # creating an object of a class Qmessagebox()
        message = QMessageBox()
        # instance of a class to set window name
        message.setWindowTitle("File name error")
        # setting error message
        message.setInformativeText("Please enter a filename")
        # setting icon of the error
        message.setIcon(QMessageBox.Warning)
        # to execute the Qmessage widget.
        message.exec_()

    def filenameerror(self):
        # creating an object of a class Qmessagebox()
        message = QMessageBox()
        # instance of a class to set window name
        message.setWindowTitle("File name error")
        # setting error message
        message.setInformativeText("Please enter the correct filename \n"
                                   "filename not found")
        # setting icon of the error
        message.setIcon(QMessageBox.Warning)
        # to execute the Qmessage widget.
        message.exec_()

    # to load dataset
    def load_dataset(self):

        # to get text from user
        covid = self.lineEdit.text()

        # setting limit for spinbox
        self.spinBox.setMaximum(50)

        if len(covid) != 0:
            # to handle errors
            try:
                # to load dataset with pandas
                covid = pd.read_csv(covid)

                # to read the first 50 datasets
                self.dataset = covid.head(50)

                # to set the number of column to the value in the spinbox.
                numcolomn = self.spinBox.value()

                # to get the numbers of column in the dataset
                if numcolomn == 0:
                    numrow = len(self.dataset.index)
                else:
                    numrow = numcolomn
                # to set column to length of columns in the dataset
                self.tableWidget.setColumnCount(len(self.dataset.columns))

                # to set row to length of rows in the dataset
                self.tableWidget.setRowCount(numrow)

                # to set column headers to column of the dataset
                self.tableWidget.setHorizontalHeaderLabels(self.dataset.columns)

                # to get the length of rows and columns in the dataset
                for i in range(numrow):
                    for j in range(len(self.dataset.columns)):
                        self.tableWidget.setItem(i, j, QTableWidgetItem(str(self.dataset.iat[i, j])))

                # to resize rows to length of rows in the dataset
                self.tableWidget.resizeRowsToContents()

                # to resize rows to length of columns in the dataset
                self.tableWidget.resizeColumnsToContents()

                # to set vertical header label
                header = ["0", "1", "2", "3", "4", "5", "6", "7", "8", ]
                self.tableWidget.setVerticalHeaderLabels(header)

            except FileNotFoundError:
                # set the error message if no filename is supplied
                self.filenameerror()
        else:
            # to set error message if incorrect filename is supplied
            self.error()

    def describe(self):
        # to get text from user
        covid = self.lineEdit.text()

        # sett limit for spinbox
        self.spinBox.setMaximum(8)

        if len(covid) != 0:
            # to handle errors
            try:
                # to load dataset with pandas
                covid = pd.read_csv(covid)

                # to read data summary
                self.dataset = covid.describe()

                # to set the number of column to the value in the spinbox.
                numcolomn = self.spinBox.value()

                # to get the numbers of column in the dataset
                if numcolomn == 0:
                    numrow = len(self.dataset.index)
                else:
                    numrow = numcolomn
                # to set column to length of columns in the dataset
                self.tableWidget.setColumnCount(len(self.dataset.columns))

                # to set row to length of rows in the dataset
                self.tableWidget.setRowCount(numrow)

                # to set column headers to column of the dataset
                self.tableWidget.setHorizontalHeaderLabels(self.dataset.columns)

                # to set vertical header label
                header = ["count", "mean", "std", "min", "25%", "50%", "75%", "max"]
                self.tableWidget.setVerticalHeaderLabels(header)

                # to get the length of rows and columns in the dataset
                for i in range(numrow):
                    for j in range(len(self.dataset.columns)):
                        self.tableWidget.setItem(i, j, QTableWidgetItem(str(self.dataset.iat[i, j])))

                # to resize rows to length of rows in the dataset
                self.tableWidget.resizeRowsToContents()
                # to resize rows to length of columns in the dataset
                self.tableWidget.resizeColumnsToContents()

            except FileNotFoundError:
                # set the error message if no filename is supplied
                self.filenameerror()
        else:
            # to set error message if incorrect filename is supplied
            self.error()

    # this function is to plot line chart
    def line_graph(self):

        # to get text from user
        covid = self.lineEdit.text()

        if len(covid) != 0:
            # to clear existing graph
            self.figure.clear()

            # to handle errors
            try:
                # to load dataset with pandas
                covid = pd.read_csv(covid)

                # to clear existing graph
                self.figure.clear()

                # to average total death , total cases and group by the continent
                line = covid.iloc[:, [1, 4, 7]].groupby(["continent"], as_index=False).mean()

                # to get the current polar axes on the current figure
                ax = plt.gca()

                # line graph for average of total cases
                line.plot(kind='line', x="continent", y="total_cases", ax=ax)

                # a line plot for average of total deaths
                line.plot(kind='line', x='continent', y="total_deaths", color="red", ax=ax)

                # set xlabel,ylabel and title of the graph
                ax.set(xlabel="continent", ylabel="total cases",
                       title="Relationship between Average total number of cases and total death recorded")

                # add grid to the chart
                plt.grid()

                # to add canvas to vertical layout
                self.verticalLayout.addWidget(self.canvas)

                # draw on canvas
                self.canvas.draw()

            except FileNotFoundError:
                # set the error message if no filename is supplied
                self.filenameerror()
        else:
            # to set error message if incorrect filename is supplied
            self.error()

    # this function is to plot bar chart
    def bar_graph(self):

        # to get text from user
        covid = self.lineEdit.text()

        if len(covid) != 0:
            # to clear existing graph
            self.figure.clear()

            # to handle errors
            try:
                # to load dataset with pandas
                covid = pd.read_csv(covid)
                # to clear existing graph
                self.figure.clear()

                # to plot a bar graph with seaborn
                plt = sns.barplot(x="continent", y='male_smokers', data=covid)

                # to set xlabel, ylabel and title for the graph
                plt.set(xlabel="Continent", ylabel="count of male smokers", title="Continents by smokers")

                # to add canvas to vertical layout
                self.verticalLayout.addWidget(self.canvas)

                # draw on canvas
                self.canvas.draw()

            except FileNotFoundError:
                # set the error message if no filename is supplied
                self.filenameerror()
        else:
            # to set error message if incorrect filename is supplied
            self.error()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Covid-19 Dashboard"))
        self.label_2.setText(_translate("MainWindow", "Filename"))
        self.label.setText(_translate("MainWindow", "Rows"))
        self.pushButton.setText(_translate("MainWindow", "Load"))
        self.pushButton_2.setText(_translate("MainWindow", "Summary"))
        self.pushButton_3.setText(_translate("MainWindow", "Line Chart"))
        self.pushButton_4.setText(_translate("MainWindow", "Bar Graph"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


