"""
Class that handles adding all entries to the database for
permanent storage, and retrieving them from permanent storage.

:author: Kyle McCahill
"""

import os
import sqlite3
from manager.Entry import Entry


class DatabaseManager:

    def __init__(self):
        self.dbPath = os.path.expanduser("~/Documents/ToDoManager/")

        if not os.path.exists(self.dbPath):
            os.makedirs(self.dbPath)

        self.connection = sqlite3.connect(self.dbPath + "Manager.db")
        with self.connection:
            self.cursor = self.connection.cursor()
            self.cursor.execute("CREATE TABLE IF NOT EXISTS Manager (Item TEXT, Due TEXT)")

    """
    Saves the Entry List to the database
    
    :param entryList: the list from the Entry Manager to save
    """
    def saveManager(self, entryList):

        with self.connection:
            self.cursor = self.connection.cursor()
            self.cursor.execute("DROP TABLE IF EXISTS Manager")
            self.cursor.execute("CREATE TABLE Manager (Item TEXT, Due TEXT)")

            for i in range(len(entryList)):
                self.cursor.execute("INSERT INTO Manager VALUES (?, ?)", (entryList[i].item, entryList[i].dueDate))

    """
    Loads the database into list format, and formats it before returning to
    the EntryManager
    
    :returns: the entryList for an EntryManager object
    """
    def loadManager(self):
        with self.connection:
            self.cursor = self.connection.cursor()
            self.cursor.execute("SELECT * FROM Manager")
            prelimList = self.cursor.fetchall()         # preliminary list before formatting
                                                        # for new Entry objects

        entryList = []
        for item in prelimList:
            entryList.append(Entry(item[0], item[1]))

        return entryList
