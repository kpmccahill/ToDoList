"""Handles the display and interaction of the UI
with the user.

Author: Kyle McCahill

"""

import sys
import logging
from manager.Entry import Entry
from manager.EntryManager import EntryManager
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QTableView, QPushButton, QListWidget, QInputDialog,
                             QListWidgetItem, QStatusBar)


# TODO: Clean up init and break into methods
# TODO: Add status and info messages with QLabels <------
class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.setWindowTitle('To Do List')
        self.setGeometry(500, 500, 325, 450)

        self.manager = EntryManager()
        self.manager.loadDB()

        vBox = QVBoxLayout()

        self.taskView = QListWidget()

        # this will make it so that when an item in the list is clicked it is removed immediately.
        # self.taskView.clicked.connect(self.__removeTask)

        hBox = QHBoxLayout()

        addButton = QPushButton("Add Task", self)
        addButton.clicked.connect(self.__addTask)

        removeButton = QPushButton("Remove Task", self)
        removeButton.clicked.connect(self.__removeTask)

        saveButton = QPushButton("Save")
        saveButton.clicked.connect(self.__saveList)

        self.statusBar = QStatusBar()

        self.__setStyling()

        vBox.addLayout(hBox)
        hBox.addWidget(saveButton)
        hBox.addWidget(addButton)
        hBox.addWidget(removeButton)

        vBox.addWidget(self.taskView)
        vBox.addWidget(self.statusBar)

        self.setLayout(vBox)

        self.taskView.show()
        self.__redrawTaskView()

        self.show()

    """Establishes the styling and formatting of mainly the tableView"""
    def __setStyling(self):
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.taskView.setFont(font)

        statusFont = font
        statusFont.setPointSize(9)
        self.statusBar.setFont(font)
        self.statusBar.setStyleSheet("color: red")
        self.statusBar.setSizeGripEnabled(False)

    """Adds a new entry to the entry manager"""
    def __addTask(self):
        item, ok = QInputDialog.getText(self, "Add Task", "Enter the task: ")
        if ok:
            date, ok = QInputDialog.getText(self, "Add Task", "Enter the due date: ")
            if ok:
                self.manager.addEntry(Entry(item, date))
                self.__redrawTaskView()
                self.statusBar.showMessage("Added", MESSAGE_TIME)

    """Removes the selected item from the list"""
    def __removeTask(self):
        try:
            self.manager.removeEntry(self.taskView.currentItem().text())
            self.__redrawTaskView()
            self.statusBar.showMessage("Removed", MESSAGE_TIME)
        except Exception:
            logging.error('Error nothing was selected')
            self.statusBar.showMessage("Error: Nothing was selected", MESSAGE_TIME)

    """Saves the list of tasks to the database"""
    def __saveList(self):
        self.manager.saveToDB()
        self.statusBar.showMessage("Saved", MESSAGE_TIME)

    """Redraws the taskView to keep it up to date"""
    def __redrawTaskView(self):
        self.taskView.clear()
        for entry in self.manager.entryList:
            entryString = entry.to_string()

            entryString = QListWidgetItem(entryString)
            entryString.setTextAlignment(QtCore.Qt.AlignHCenter)
            self.taskView.addItem(entryString)


# CONSTANTS #
MESSAGE_TIME = 2000

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())