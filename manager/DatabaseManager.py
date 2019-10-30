import os
import sqlite3
from manager.Entry import Entry
from manager.EntryManager import EntryManager




class DatabaseManager:

    def __init__(self, EntryManager):
        if os.path.exists(os.path.expanduser("~/ToDoManager/")):
            pass



if __name__ == "__main__":
    x = check_manager = EntryManager([Entry("Task1", "DateDue"),
                                      Entry("Task2", "DateDue")])

    print(x.to_string())